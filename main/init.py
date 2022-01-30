from flask import Flask
import json
from main.settings import HOST, PORT

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
    app.run(debug=True, host=HOST, port=int(PORT))
