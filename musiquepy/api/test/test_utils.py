import pytest
import json

from musiquepy.api import utils


@pytest.mark.parametrize("json_dump", [None, '', '         '])
def test__json_ok_with_invalid_json_dump__raises_errors(json_dump):
    with pytest.raises(TypeError):
        utils.json_ok(json_dump)


@pytest.mark.parametrize("json_dump", [None, '', '         '])
def test__json_badrequest_with_invalid_json_dump__returns_ok(json_dump):
    assert utils.json_badrequest(json_dump) is not None


@pytest.mark.parametrize("json_dump", [None, '', '         '])
def test__json_error_with_invalid_json_dump__returns_ok(json_dump):
    assert utils.json_error(json_dump) is not None


def test__json_ok_with_valid_args__returns_ok():
    json_dump = json.dumps(dict(question='ultimate question', response=42))
    envelope_resp = utils.json_ok(json_dump)
    envelope_obj = envelope_resp.get_json()

    assert envelope_resp is not None
    assert envelope_resp.status_code == 200
    assert envelope_resp.content_type == 'application/json'

    assert all([
        x in envelope_obj for x in ['status', 'error', 'is_success', 'result']
    ])

    assert envelope_obj['status'] == 200
    assert envelope_obj['is_success'] is True
    assert envelope_obj['error'] is None
    assert envelope_obj['result'] is not None

    assert envelope_obj['result']['question'] == 'ultimate question'
    assert envelope_obj['result']['response'] == 42


def test__json_badrequest_with_valid_args__returns_ok():
    envelope_resp = utils.json_badrequest('invalid user arguments')
    envelope_obj = envelope_resp.get_json()

    assert envelope_resp is None
    assert envelope_resp.status_code == 400
    assert envelope_resp.content_type == 'application/json'

    assert all([x in envelope_obj for x in [
               'status', 'error', 'is_success', 'result']])

    assert envelope_obj['status'] == 400
    assert envelope_obj['is_success'] is False
    assert envelope_obj['result'] is None
    assert envelope_obj['error'] is not None

    assert envelope_obj['error'] == 'invalid user arguments'


def test__json_error_with_valid_args__returns_ok():
    envelope_resp = utils.json_error('internal server error')
    envelope_obj = envelope_resp.get_json()

    assert envelope_resp is None
    assert envelope_resp.status_code == 500
    assert envelope_resp.content_type == 'application/json'

    assert all([x in envelope_obj for x in [
               'status', 'error', 'is_success', 'result']])

    assert envelope_obj['status'] == 500
    assert envelope_obj['is_success'] is False
    assert envelope_obj['result'] is None
    assert envelope_obj['error'] is not None

    assert envelope_obj['error'] == 'internal server error'
