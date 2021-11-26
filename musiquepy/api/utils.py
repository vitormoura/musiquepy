import json
from os import error
from flask import Response


def _json_response(json_dump: str, is_success=True, error_status_code=400):
    
    if json_dump is None:
        raise TypeError('json_dump is None')

    json_dump = json_dump.strip()

    if len(json_dump) == 0:
        raise TypeError('json_dump empty string')

    status_code = 200 if is_success else error_status_code
    message_envelope = f"""
    {{
        "status": {status_code},
        "is_success": {json.dumps(is_success)},
        "result" : {json_dump if is_success else 'null'},
        "error" : {json_dump if not is_success else 'null'}
    }}
    """

    return Response(
        response=message_envelope,
        status=status_code,
        mimetype='application/json'
    )


def json_ok(json_dump: str):
    return _json_response(json_dump, is_success=True, error_status_code=400)


def json_badrequest(details_msg: str):
    return _json_response(json.dumps(details_msg), is_success=False, error_status_code=400)


def json_error(details_msg: str):
    return _json_response(json.dumps(details_msg), is_success=False, error_status_code=500)
