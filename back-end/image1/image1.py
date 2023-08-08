from google.cloud import firestore
from flask import Flask, request
import os



app = Flask(__name__)

# key = '/Users/alagappanveerappan/Downloads/Serverless/Assignment2/code/backend/key.json'

# DB Initialization
# database_connection = firestore.Client.from_service_account_json(key)
database_connection = firestore.Client(project="glowing-reserve-390522")

@app.route("/insert_data", methods=['POST'])
def insert_data():
    payload = request.get_json()
    
    # Creating collection Registration and storing the User Payload
    collection_name = 'Reg'
    collection_ref = database_connection.collection(collection_name)
    document_name = payload['email']
    doc_ref = database_connection.collection(collection_name).document(document_name)
    # Store the payload data in the specified document
    doc_ref.set(payload)
    
    # Creating collection State and storing the User state with timestamp
    collection_state_name = 'state'
    collection_state_refernece = database_connection.collection(collection_state_name)
    state = {
            'state': "offline",
            'timestamp': firestore.SERVER_TIMESTAMP
        }
    insert_state = database_connection.collection(collection_state_name).document(document_name)
    insert_state.set(state)

    return 'Data inserted successfully'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    


