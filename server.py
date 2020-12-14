from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'HI'


@app.route('/predict_price', methods=['POST'])
def predict_price():
    area = float(request.form['area'])
    rooms = int(request.form['rooms'])
    suites = int(request.form['suites'])
    bathrooms = int(request.form['bathrooms'])
    parkings = int(request.form['parkings'])
    neighborhood = request.form['neighborhood']

    response = jsonify({
        'estimated_price': utils.get_estimated_price(neighborhood, area, rooms, suites, bathrooms, parkings)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print('Starting python Flask Server for Real estate Prediction')
    utils.load_saved_model()
    app.run()
