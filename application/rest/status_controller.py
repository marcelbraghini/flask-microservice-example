import json

from flask import Blueprint, Response

blueprint = Blueprint("status", __name__)


@blueprint.route("/status", methods=["GET"])
def save_person():
    status = {
        'status': 'OK'
    }

    return Response(
        json.dumps(status),
        mimetype="application/json",
        status=200,
    )
