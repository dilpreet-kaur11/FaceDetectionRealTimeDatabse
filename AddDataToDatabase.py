import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendencerealtime-b3eea-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name" : "Aditi",
            "major":"Information Technology",
            "Starting_Year":"2020",
            "total_attendance":6,
            "Gender" : "F",
            "year":4,
            "last_attendance_time":"2023-7-10 00:54:34"
        },
"852741":
        {
            "name" : "Emily Blunt",
            "major":"Economics",
            "Starting_Year":"2018",
            "total_attendance":6,
            "Gender" : "F",
            "year":4,
            "last_attendance_time":"2023-7-10 00:54:34"
        },
"963852":
        {
            "name" : "Elon Musk",
            "major":"Robotics",
            "Starting_Year":"2014",
            "total_attendance":6,
            "Gender" : "M ",
            "year":4,
            "last_attendance_time":"2023-7-10 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)