from flask import Flask, request, jsonify, render_template
import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return render_template('real_estate.html')


@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    if request.method == 'POST':
        area = float(request.form.get('area'))

        rooms = int(request.form.get('rooms'))
        suites = int(request.form.get('suites'))
        bathrooms = int(request.form.get('bathrooms'))
        parkings = int(request.form.get('parkings'))
        neighborhood = request.form.get('neighborhood')

        response = utils.get_estimated_price(
            neighborhood, area, rooms, suites, bathrooms, parkings)
        if response < 0:
            return render_template('real_estate.html', prediction_texts="The price is below zero", prediction_text_dollar="The price is below zero")
        else:
            return render_template('real_estate.html', prediction_text="{:.2f}R$".format(response), prediction_text_dollar="{:.2f}$".format(response/5.12))
    else:
        return render_template('real_estate.html')


if __name__ == "__main__":
    print('Starting python Flask Server for Real estate Prediction')
    utils.load_saved_model()
    app.run()
