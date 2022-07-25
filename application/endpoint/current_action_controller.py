import json

from flask import Blueprint, Response, request

from application.service.findTicker import find_ticker
from application.service.findTickers import find_tickers

blueprint = Blueprint("current-action", __name__)


@blueprint.route("/current-action", methods=["POST"])
def current_action():
    response = []
    actionsToFind = json.loads(request.data)

    if (len(actionsToFind)) < 2:
        response = find_ticker(actionsToFind[0])
    else:
        response = find_tickers(actionsToFind)

    return Response(
        json.dumps(response),
        mimetype="application/json",
        status=200,
    )
