🚗 DailyCom – Smart Ride Sharing Platform

A web-based ride-sharing platform designed to help daily commuters create, find, and share rides efficiently.

📌 Overview

DailyCom focuses on solving a real-world problem:
daily commuters struggle to find reliable, recurring ride-sharing options.

Unlike traditional ride apps, this platform is built specifically for:

Students 🎓
Office workers 🧑‍💼
Regular commuters 🚶

It enables users to coordinate daily travel, reduce costs, and improve vehicle utilization.

❗ Problem Statement

Most ride-sharing platforms:

Focus on one-time bookings
Lack community-based commuting
Don’t support daily recurring travel

This leads to:

Increased travel costs 💸
Traffic congestion 🚦
Underutilized vehicles 🚗
🎯 Objectives
Enable users to create and join rides
Reduce commuting costs
Provide a simple and reliable platform
Improve vehicle utilization
Support daily commute coordination
⚙️ Tech Stack

Frontend

HTML
CSS

Backend

Django (Python)

Database

SQLite

Maps & Location

MapLibre (Open-source, no API key)
OpenStreetMap (Nominatim for reverse geocoding)
🚀 Features (Current - MVP)
🔐 User Authentication (Signup/Login)
🚗 Create a Ride
🔍 Search & View Available Rides
📅 Filter by source, destination, and date
🪑 Seat availability system
📖 Book a Ride
📂 View My Bookings
❌ Cancel Booking
🗺️ Map-based source & destination selection
🧠 How It Works
User signs up or logs in
User creates or searches for rides
User books a seat
Booking is stored in the system
User manages bookings
🏗️ System Architecture
User → Web Interface → Django Backend → Database (SQLite)
📂 Project Structure
DailyCom/
│
├── Dailycom/          # Main Django project
├── rides/             # App (core logic)
├── templates/         # HTML templates
├── static/css/        # Styles
├── db.sqlite3         # Database
├── manage.py
🛠️ Installation & Setup
# Clone the repository
git clone https://github.com/your-username/dailycom.git

# Navigate to project
cd dailycom

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
🌐 Usage
Visit: http://127.0.0.1:8000/
Create an account
Start creating or booking rides
⚠️ Current Limitations
No real-time updates
No chat between users
No payment integration
Basic UI/UX
🔮 Future Enhancements
💬 Real-time chat system
⭐ Rating & review system
💳 Payment gateway integration
📍 Live location tracking
🤖 AI-based ride matching (research scope)
📈 Current Progress
Django setup completed
Core features implemented
Authentication system working
Basic UI developed
🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a PR.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Abhi
Engineering Student | Web Developer

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
