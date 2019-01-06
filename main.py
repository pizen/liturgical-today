from datetime import date
from flask import abort, Flask, Response
import json
from pyliturgical import calendar

app = Flask(__name__)


@app.route('/reformed/<date_str>')
def reformed(date_str):
    try:
        d = date.fromisoformat(date_str)
    except Exception:
        abort(400)

    resp = Response(
        json.dumps(calendar.lookup(d)),
        status=200,
        mimetype='application/json'
    )
    resp.cache_control.public = True
    resp.cache_control.max_age = 86400
    return resp


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
