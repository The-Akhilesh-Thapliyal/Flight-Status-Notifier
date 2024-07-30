
<h2 align="center">Flight Status Notifier</h2>

## Overview

This web application allows users to search for flight information, view lists of upcoming and outgoing flights, and receive status updates via SMS. It utilizes a microservices architecture and modern web technologies.

## Features

- **Flight Search**: Users can find specific flight details using flight numbers.
- **Arrivals & Departures**: Displays real-time lists of arriving and departing flights.
- **Detailed Flight Information**: Provides comprehensive details about each flight.
- **Notifications**: Users can subscribe to receive SMS updates on flight status, gate numbers, and baggage carousel information.
- **User Authentication**: Secure login and signup processes to ensure data privacy and access control.

## Tech Stack

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

## Usage

1. **Flight Search**:
   - Enter the flight number to retrieve flight information.
2. **Viewing Flights**:
   - Access lists of upcoming arrivals and departures.
3. **Notifications**:
   - Subscribe to receive updates on your mobile device.

## Visual Overview

### User Interfaces

- **Landing Page**: Includes animation and a search bar.
- **Authentication**: Screens for user login and signup.
- **Main Dashboard**: Displays flight lists and details.
- **Notification Service**: Allows users to sign up for SMS notifications.

### SMS Notifications

- **Arrival & Departure Updates**: Notifications sent to users' mobile phones.

<h2 align="center">🚀 About Me</h2>

Hello, I'm Akhilesh Thapliyal! 👋
<h2 align="center">Contact</h2>

- **Email:** akhilesh.thedev@gmail.com
- **LinkedIn:** www.linkedin.com/in/akhilesh-thapliyal
- **GitHub:** https://github.com/The-Akhilesh-Thapliyal