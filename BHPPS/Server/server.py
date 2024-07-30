from flask import Flask, request, jsonify
import use
app = Flask(__name__)

@app.route('/get_loc_names', methods=['GET'])
def get_loc_names():
    response = jsonify({
        'locations': use.get_loc_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_price',methods=['GET', 'POST'])

def predict_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': use.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Python flask server for house price prediction")
    use.get_saved_artifacts()
    app.run()