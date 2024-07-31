
<h1 align="center">Flight Status Notifier</h1>
<p align="center">
<img src="http://drive.google.com/uc?export=view&id=1ncf9-pnPyTXAty6sM0OpXU8mYn_3owuP">
</p>


<h2 align="center">Overview</h2>

This web application allows users to search for flight information, view lists of upcoming and outgoing flights, and receive status updates via SMS. It utilizes a microservices architecture and modern web technologies.


<h2 align="center">Features</h2>

- **Flight Search**: Users can find specific flight details using flight numbers.
- **Arrivals & Departures**: Displays real-time lists of arriving and departing flights.
- **Detailed Flight Information**: Provides comprehensive details about each flight.
- **Notifications**: Users can subscribe to receive SMS updates on flight status, gate numbers, and baggage carousel information.
- **User Authentication**: Secure login and signup processes to ensure data privacy and access control.


<h2 align="center">Tech Stack</h2>

### Frontend


- **Frameworks & Libraries**:
  - React
  - Vite
  - Tailwind CSS
- **Dependencies**:
  - `axios`: API requests
  - `react-router-dom`: Routing
  - `react-icons`: UI components
  - `react-loading-skeleton`: Loading placeholders
  - `react-responsive-carousel`: Carousel component


### Backend

- **Framework**:
  - Flask (Python)
- **Messaging**:
  - Twilio for SMS notifications
- **Dependencies**:
  - `bcrypt`: Password hashing
  - `Flask-Cors`: CORS handling
  - `Flask-PyMongo`: MongoDB integration
  - `pyjwt`: JWT management
  - `pymongo`: MongoDB driver
  - `requests`: HTTP requests
  - `twilio`: SMS services
  - `werkzeug`: WSGI utilities
  - Other utility libraries: `dnspython`, `yarl`, `click`, `python-dotenv`, `urllib3`, `aiohttp`, `aiosignal`, `attrs`


### Database

- **MongoDB**: NoSQL database for storing flight and user data.


<h2 align="center">Usage</h2>

1. **Flight Search**:
   - Enter the flight number to retrieve flight information.
2. **Viewing Flights**:
   - Access lists of upcoming arrivals and departures.
3. **Notifications**:
   - Subscribe to receive updates on your mobile device.


<h2 align="center">Visual Overview</h2>

### User Interfaces

- **Landing Page**: Includes animation.<br/><br/>
![image](http://drive.google.com/uc?export=view&id=1ZT6un2d_aFGasspTgA-oYEGWPZy0_dc6) <br/>

- **Authentication**: Screens for user login and signup.<br/><br/>
![image](http://drive.google.com/uc?export=view&id=1h43wyW2vG3xKnJ43W_9PXyek4hKCdk5A) <br/>

- **Main Dashboard**: Displays flight lists and details.<br/><br/>
![image](http://drive.google.com/uc?export=view&id=1al-m2yLNBMHyJ0ZSjOtEN6aF5GeoAayQ) <br/><br/>
![image](http://drive.google.com/uc?export=view&id=1E-nVIfPcazeAgJURM96ePr02cA6pJZFw) <br/>

- **Notification Service**: Allows users to sign up for SMS notifications.<br/><br/>
![image](http://drive.google.com/uc?export=view&id=1IU1bA2aeodxb1DHwN-37K11rsph9g-YV) <br/>


### SMS Notifications of Arrival & Departure Updates: Notifications sent to users' mobile phones

- **Mobile SMS Received By Passengers (For Arrival )**: <br/><br/>
![image](http://drive.google.com/uc?export=view&id=1snN6fiOyYDEVBiqqb_DDuJxr13N3jg9L) <br/>

- **Mobile SMS Received By Passengers (For Departure )**: <br/><br/>
![image](http://drive.google.com/uc?export=view&id=1j03XoLvPPSPLLRALXLwX25lCL3_KlVhH) <br/>

<h2 align="center">🚀 About Me</h2>

Hello, I'm Akhilesh Thapliyal! 👋
<h2 align="center">Contact</h2>

- **Email:** akhilesh.thedev@gmail.com
- **LinkedIn:** www.linkedin.com/in/akhilesh-thapliyal
- **GitHub:** https://github.com/The-Akhilesh-Thapliyal
