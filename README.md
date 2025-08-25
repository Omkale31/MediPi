Medipi is an IoT-based health monitoring system developed using Raspberry Pi 3 B+. It is designed to measure and track key health parameters such as body temperature, heart rate, and environmental conditions in real-time. In addition, the project integrates the PiCamera2 module to capture patient images, making health records more detailed and reliable.

The main goal of this project is to create a portable, affordable, and smart health monitoring device that can be used in rural areas, clinics, hospitals, or even at home. It helps doctors and patients to monitor vital signs remotely through a Flask-based web interface, while automatically saving all readings into a local SQLite3 database for future reference.


⚙️ Key Features

🌡️ Body Temperature Measurement: Uses MLX90614 infrared sensor for accurate non-contact temperature readings.

❤️ Heart Rate Monitoring: Tracks patient pulse using a heart rate sensor.

🌤️ Environment Monitoring: Collects surrounding temperature and humidity to check environmental conditions.

📷 Patient Image Capture: Integrates PiCamera2 with Raspberry Pi to capture real-time patient images.

💾 Data Storage: Stores all health records in SQLite3 database for analysis and reporting.

🌐 Web Interface: Flask-based web application provides a user-friendly dashboard to display health parameters and images.

📊 Visualization: Data is shown in both text and graphical format for better understanding



>Hardware Components:

-Raspberry Pi 3 B+

-MLX90614 Infrared Temperature Sensor

-Heart Rate Sensor

-PiCamera2 Module

-Breadboard, jumper wires, resistors

>Software & Tools:

-Python

-Flask (for web application)

-SQLite3 (for database)

-Picamera2 library

-SMBus2 library (for I2C communication)

-HTML, CSS (for frontend templates)


>System Workflow

Data Collection – Sensors (MLX90614 and Heart Rate Sensor) collect patient health data.

Image Capture – PiCamera2 captures the patient’s image.

Data Processing – Raspberry Pi processes sensor values using Python scripts.

Storage – All data (sensor values + image path) is stored in an SQLite database.

Visualization – Flask web app displays real-time data and images on a clean dashboard.

Remote Access – Doctors or patients can access the dashboard from any device connected to the same
