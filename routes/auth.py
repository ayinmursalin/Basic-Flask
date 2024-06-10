from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__, url_prefix='/api')

@auth.route('/auth/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login Success'})

@auth.route('/auth/profile', methods=['GET'])
def get_profile():
    return jsonify({'message': 'Success get Profile'})

@auth.route('/auth/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logout Success'})