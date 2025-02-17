import os
from flask import Flask, request, jsonify , g
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import pika
from dotenv import load_dotenv
from db import create_user, find_user_by_email, create_flight, get_all_flights, get_flight_by_number, log_notification ,create_user_flight_data
from auth import encode_auth_token, decode_auth_token
from functools import wraps
from twilio.rest import Client

# Load the environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Twilio Configuration
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')


def convert_to_serializable(flight):
    flight['_id'] = str(flight['_id'])
    return flight

@app.route('/')
def home():
    return "Jinda hu bhai"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    
    
    if not data or not 'email' in data or not 'password' in data or not 'name' in data:
        return jsonify({'message': 'Invalid data'}), 400

    # Print the data
    # Print(data)

    user = find_user_by_email(data['email'])
    # Print(user)
    if user:
        return jsonify({'message': 'User already exists'}), 409
    
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    user_data = {
        'name': data['name'],
        'email': data['email'],
        'password': hashed_password
    }
    # Return jsonify({"user_data" : user_data}), 201
    create_user(user_data)
    user = find_user_by_email(data['email'])
    token = encode_auth_token(str(user['_id']))
    return jsonify({"jwt" : token}),201


@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'message': 'Invalid data'}), 400
    
    user = find_user_by_email(data['email'])
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401
    
    token = encode_auth_token(str(user['_id']))
    return jsonify({'token': token}), 200

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            token = auth_header.split(" ")[1]
            user_id = decode_auth_token(token)
            print("Decoded user_id:", user_id)
            if isinstance(user_id, str):
                g.user_id = user_id
            else:
                print("Error message:", user_id)
                return jsonify({'message': user_id}), 401
        except Exception as e:
            print("Exception:", str(e))
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return _verify

@app.route('/flights', methods=['GET'])
@token_required
def get_flights():
    flights = get_all_flights()
    # Print
    flights = [convert_to_serializable(flight) for flight in flights]
    return jsonify(flights), 200

@app.route('/flights/<flight_number>', methods=['GET'])
@token_required
def get_flight(flight_number):
    flight = get_flight_by_number(flight_number)
    return jsonify(convert_to_serializable(flight)) if flight else ('Not Found', 404)

def send_sms_notification(flight_data, user_contact , user_name):
    if flight_data['flightType'] == 'Departure':
       
        message_body = (
            f"Dear {user_name},\n"
            f"Your Flight Details are as follows:\n"
            f"Flight Number: {flight_data['flightNumber']}\n"
            f"Airline: {flight_data['airline']}\n"
            f"Source: {flight_data['source']}\n"
            f"Destination: {flight_data['destination']}\n"
            f"Departure Time: {flight_data['departureTime']}\n"
            f"Status: {flight_data['status']}\n"
            f"Gate Number: {flight_data.get('gateNumber', 'N/A')}\n"
            f"Baggage Carousel: N/A\n"
        )
    else:
        
        message_body = (
            f"Dear {user_name},\n"
            f"Your Flight Details are as follows:\n"
            f"Flight Number: {flight_data['flightNumber']}\n"
            f"Airline: {flight_data['airline']}\n"
            f"Source: {flight_data['source']}\n"
            f"Destination: {flight_data['destination']}\n"
            f"Arrival Time: {flight_data['arrivalTime']}\n"
            f"Status: {flight_data['status']}\n"
            f"Gate Number: N/A\n"
            f"Baggage Carousel: {flight_data.get('baggageCarousel', 'N/A')}\n"
        )

    try:
        message = twilio_client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=user_contact
        )
        return message.sid
    except Exception as e:
        print(f"Failed to send SMS notification: {e}")
        return None

@app.route('/search', methods=['POST'])
@token_required
def search_flight():
    data = request.json
    required_fields = ['departure_airport', 'arrival_airport', 'departure_date', 'flight_number', 'name', 'contact']
    
    # Check if all required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing data'}), 400
    
    # Validate flight information
    flight = get_flight_by_number(data['flight_number'])
    if not flight:
        return jsonify({'message': 'Flight not found'}), 404

    # Store user data along with user_id
    user_data = {
        'user_id': g.user_id,
        'departure_airport': data['departure_airport'],
        'arrival_airport': data['arrival_airport'],
        'departure_date': data['departure_date'],
        'flight_number': data['flight_number'],
        'name': data['name'],
        'contact': data['contact']
    }

    # Print(user_data)
    create_user_flight_data(user_data)


    # Send Notification
    sms_sid = send_sms_notification(flight, data['contact'],data['name'])
    if not sms_sid:
        return jsonify({'message': 'Flight data stored successfully, but failed to send notification'}), 500

    
    return jsonify({'message': 'Flight data stored successfully and notification sent', 'flightData': convert_to_serializable(flight)}), 201

