import json
from os import error
from flask import Response

def _json_response(json_dump: str, is_success=True, error_status_code=400):

    message_envelope = f"""
    {{
        "status": 100,
        "is_success": {json.dumps(is_success)},
        "result" : {json_dump if is_success else 'null'},
        "error" : {json_dump if not is_success else 'null'}
    }}
    """

    return Response(
        response=message_envelope,
        status=200 if is_success else error_status_code,
        mimetype='application/json'
    )

def json_ok(json_dump: str):
    return _json_response(json_dump, is_success=True, error_status_code=400)

def json_badrequest(details: str):
    return _json_response(json.dumps(details), is_success=False, error_status_code=400)

def json_error(details: str):
    return _json_response(json.dumps(details), is_success=False, error_status_code=500)
