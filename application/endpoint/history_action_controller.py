import json

from flask import Blueprint, Response, request

from application.service.findHistoryByTicker import find_history_by_ticker

blueprint = Blueprint("history-action", __name__)


@blueprint.route("/history-action", methods=["POST"])
def history_action():
    response = []
    target = json.loads(request.data)

    history = find_history_by_ticker(target)

    for h in history:
        model = {
            str(h): {
                'open': history[h]['Open'],
                'high': history[h]['High'],
                'low': history[h]['Low'],
                'close': history[h]['Close'],
                'volume': history[h]['Volume'],
                'dividends': history[h]['Dividends'],
                'stock_splits': history[h]['Stock Splits']
            }
        }
        response.append(model)

    return Response(
        json.dumps(response),
        mimetype="application/json",
        status=200,
    )
