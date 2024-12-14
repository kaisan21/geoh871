from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will serve the index.html from templates folder

# Route to handle location data upload
@app.route('/upload-location', methods=['POST'])
def upload_location():
    try:
        # Get the JSON data from the request
        location_data = request.get_json()

        # Extract latitude and longitude
        latitude = location_data.get('latitude')
        longitude = location_data.get('longitude')

        if latitude is not None and longitude is not None:
            # Process the location data (you can store it, log it, etc.)
            print(f"Received location: Latitude = {latitude}, Longitude = {longitude}")

            # Respond back with a success message
            return jsonify({'message': 'Location successfully received and uploaded!'})
        else:
            return jsonify({'message': 'Invalid location data'}), 400

    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app on all available interfaces (0.0.0.0) and on port 8000
    app.run(debug=True, host='0.0.0.0', port=8000)
