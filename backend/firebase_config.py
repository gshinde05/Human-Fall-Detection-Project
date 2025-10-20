
import firebase_admin
from firebase_admin import credentials

def init_firebase():
    cred = credentials.Certificate("firebase-adminsdk.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://your-database.firebaseio.com/'
    })
