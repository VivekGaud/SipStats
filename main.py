from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to simulate a database
dummy_data = []

# Route to handle GET requests
@app.route('/get_sip_stats', methods=['GET'])
def get_sip_stats():
    return jsonify(dummy_data)

# Route to handle POST requests
@app.route('/get_sip_stats', methods=['POST'])
def set_sip_stats():
    data = request.json  # Assuming JSON data is sent in the request body
    dummy_data.append(data)
    return jsonify({"message": "Data added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
