import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

path = os.path.dirname(os.path.realpath(__file__))
cred = credentials.Certificate(os.path.join(path ,"sistema-caixa-firebase-adminsdk-o6faa-77b6d40db9.json"))
firebase_admin.initialize_app(cred)


def docDB():
    db = firestore.client()
    ac = db.collection('senha')
    doc = ac.get()
    lis = []
    for i in doc:
        lis.append(i.to_dict())
    return lis
        




    
    
