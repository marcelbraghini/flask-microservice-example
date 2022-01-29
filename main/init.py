from flask import Flask
import json

app = Flask(__name__)


@app.route('/example', methods=['GET'])
def init():

    person = '{"first_name": "Marcel", "last_name": "Braghini"}'

    response = app.response_class(
        response=json.dumps(person),
        mimetype='application/json',
        status=200
    )

    return response


if __name__ == '__main__':
    port = int(5000)
    app.run(debug=True, host='0.0.0.0', port=port)
