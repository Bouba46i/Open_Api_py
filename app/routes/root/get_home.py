from flask import jsonify

def get_home():
    return jsonify({"message": "Welcome to the CRUD API with Flask - Go to /apidocs to see the documentation or /persons to see the persons list"})
