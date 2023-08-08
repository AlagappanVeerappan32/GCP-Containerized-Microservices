from google.cloud import firestore
from flask import Flask, request, jsonify



app = Flask(__name__)

key = '/Users/alagappanveerappan/Downloads/Serverless/Assignment2/code/backend/key.json'

# DB Initialization
database_connection = firestore.Client.from_service_account_json(key)


@app.route("/get_data", methods=['POST'])
def validate_login():
    payload = request.get_json()

    email = payload['email']
    password = payload['password']

    get_collection = database_connection.collection('Reg').document(email)
    document = get_collection.get()

    if document.exists:
        email_to_check = document.to_dict().get('email')
        password_to_check = document.to_dict().get('password')
        
        if password_to_check == password:
            response = {'status': 'success', 'message': 'password matches'}
            if update_user_state(email):
                return jsonify(response), 200
            else:
                return jsonify({'status': 'error', 'message': 'Failed to update user state'}), 401
        else:
            response = {'status': 'error', 'message': 'password doesn\'t match'}
            return jsonify(response), 401
    else:
        response = {'status': 'error', 'message': 'email doesn\'t exist!'}
        print("error here")
        return jsonify(response), 404


def update_user_state(email):
    get_collection = database_connection.collection('state').document(email)
    document = get_collection.get()

    if document.exists:
        state = document.to_dict().get('state')
        if state == "offline":
            get_collection.update({
                'state': "online",
                'timestamp': firestore.SERVER_TIMESTAMP
            })
            print("updated to online")
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
    app.run(host='0.0.0.0', port=3000)

    


