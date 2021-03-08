from repositories.DataRepository import DataRepository
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Custom endpoint
endpoint = '/api/v1'


@app.route('/')
def index():
    return redirect("/api/v1/klanten", code=302)

#########  Klanten  #########


@app.route(endpoint + '/klanten', methods=['GET', 'POST'])
def klanten():
    if request.method == 'GET':
        data = DataRepository.read_klanten()
        if data is not None:
            return jsonify(klanten=data), 200
        else:
            return jsonify(message='error'), 404
    elif request.method == 'POST':
        gegevens = DataRepository.json_or_formdata(request)
        data = DataRepository.create_klant(gegevens['FNaam'], gegevens['VNaam'], gegevens['Straat'],
                                           gegevens['Nummer'], gegevens['Postcode'], gegevens['Gemeente'])
        return jsonify(KlantID=data), 201


@app.route(endpoint + '/klanten/<id>', methods=['GET', 'PUT', 'DELETE'])
def klant(id):
    if request.method == 'GET':
        data = DataRepository.read_klant(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message='error'), 404

    elif request.method == 'PUT':  # update
        gegevens = DataRepository.json_or_formdata(request)
        data = DataRepository.update_klant(gegevens['FNaam'], gegevens['VNaam'], gegevens['Straat'],
                                           gegevens['Nummer'], gegevens['Postcode'], gegevens['Gemeente'], id)
        if data is not None:
            if data > 0:
                return jsonify(KlantID=id), 200
            else:
                return jsonify(status=data), 200
        else:
            return jsonify(message='error'), 404

    elif request.method == 'DELETE':
        data = DataRepository.delete_klant(id)
        print(data)
        return jsonify(status=data), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
