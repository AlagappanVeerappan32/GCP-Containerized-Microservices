from google.cloud import firestore
from flask import Flask, request, jsonify

app = Flask(__name__)

key = '/Users/alagappanveerappan/Downloads/Serverless/Assignment2/code/backend/key.json'

# DB Initialization
database_connection = firestore.Client.from_service_account_json(key)

@app.route("/update_data", methods =['POST'])
def update_db():
    payload = request.get_json()

    email = payload['email']
    get_collection = database_connection.collection('state').document(email)
    document = get_collection.get()

    if document.exists:
        state = document.to_dict().get('state')
        if state == "online":
            get_collection.update({
                'state': "offline",
                'timestamp': firestore.SERVER_TIMESTAMP
            })
            print("updated offline")
            response = {'status': 'success', 'message': 'password matches'}
            return jsonify(response), 200
        else:
            print("user is in active mode")
            return jsonify(response), 403 
    else:
        print("email id does not match")
        response = {'status': 'error', 'message': 'email doesn\'t exist!'}
        return jsonify(response), 404 



if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=6000)

    


