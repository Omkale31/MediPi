from flask import Flask, render_template, request, redirect, Response
from sensors import get_sensor_data, lcd_string
from camera import generate_frames
from database import insert_patient, insert_health_data

app = Flask(__name__)
patient_id = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_patient_info', methods=['POST'])
def submit_patient_info():
    global patient_id
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    blood_group = request.form.get("blood_group")
    mobile = request.form.get("mobile")
    insert_patient(name, age, gender, blood_group, mobile)
    patient_id = 1  # TODO: fetch inserted patient ID dynamically
    return redirect('/')

@app.route('/sensor_data')
def sensor_data():
    global patient_id
    ambient_temp, object_temp, bpm = get_sensor_data()
    lcd_string(f"Temp: {object_temp:.2f}C", 0x00)
    lcd_string(f"Heart: {bpm:.0f} BPM", 0x40)
    if patient_id:
        insert_health_data(patient_id, ambient_temp, object_temp, bpm)
    return {
        "ambient_temp": f"{ambient_temp:.2f}C",
        "object_temp": f"{object_temp:.2f}C",
        "bpm": f"{bpm:.0f} BPM"
    }

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
