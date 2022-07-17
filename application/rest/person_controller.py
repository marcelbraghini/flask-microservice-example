import json

from flask import Blueprint, Response, request

blueprint = Blueprint("person", __name__)


@blueprint.route("/person", methods=["POST"])
def save_person():
    person = json.loads(request.data)

    print(person)

    return Response(
        json.dumps(person),
        mimetype="application/json",
        status=200,
    )
