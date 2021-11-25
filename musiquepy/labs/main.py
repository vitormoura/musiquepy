import os
import logging
import logging.config
from typing_extensions import Required, TypeAlias
from dataclasses_json.api import DataClassJsonMixin

import orjson
import json
from pprint import pprint

from dataclasses import asdict, astuple, dataclass, field, is_dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import TypeVar
from types import GenericAlias, new_class

from marshmallow import Schema, fields
from marshmallow.decorators import post_load
from marshmallow.utils import EXCLUDE

PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# dataclasses-json
# https://pypi.org/project/dataclasses-json/

# Marshmallow
# https://marshmallow.readthedocs.io/en/stable/index.html


@dataclass
class MyClass():
    message: str
    date: datetime
    parent: 'MyClass'


class MyClass2Schema(Schema):
    message = fields.Str()
    date = fields.DateTime()
    parent = fields.Nested(lambda: MyClass2Schema, unknown=EXCLUDE,
                           include="message,date", required=False, allow_none=True)

    @post_load
    def make_object(self, data, **kwargs):
        return MyClass(**data)


def package_path(*paths, package_directory=PACKAGE_ROOT_DIR):
    return os.path.join(package_directory, *paths)


def asdataclass(klass, d):
    if not is_dataclass(klass):
        return d
    values = {}
    for f in fields(klass):
        if isinstance(f.type, GenericAlias) and f.type.__origin__ == list:
            values[f.name] = [asdataclass(f.type.__args__[0], d2)
                              for d2 in d[f.name]]
        else:
            values[f.name] = asdataclass(f.type, d[f.name])

    return klass(**values)


def dataclass_from_dict(klass, d):
    try:
        fieldtypes = {f.name: f.type for f in fields(klass)}
        return klass(**{f: dataclass_from_dict(fieldtypes[f], d[f]) for f in d})
    except:
        return d  # Not a dataclass field


def explore_json_tools():
    m = MyClass('root', datetime.now(), None)
    m2 = MyClass('child', datetime.now(), m)

    orig_dict = asdict(m2)

    # dataclasses_json
    #json_text = m2.to_json()
    #new_obj = MyClass.from_dict(orig_dict)

    # orjson
    #json_text = orjson.dumps(orig_dict)
    #new_obj = orjson.loads(json_text)

    # pure dataclasses
    #json_text = json.dumps(orig_dict)
    #new_obj = asdataclass(MyClass, orig_dict)

    # marshmallow
    #m1_asdict = { 'message': 'hello', 'date': datetime.now(), 'parent': None }

    schema = MyClass2Schema()
    
    dump_text = schema.dump(m2)
    json_text = schema.dumps(m2)
    
    print('DUMP TEXT')
    pprint(dump_text)

    print('JSON TEXT')
    pprint(json_text)

    new_obj_as_dict = schema.load(dump_text)
    new_obj = schema.loads(json_text)

    print('LOAD FROM DUMP')
    pprint(new_obj_as_dict)

    print('LOAD FROM JSON')
    pprint(new_obj)


def explore_path_info():
    print(PACKAGE_ROOT_DIR)
    print(__file__)


def explore_logging():

    #logging.basicConfig(format="%(levelname)s %(asctime)s -- %(message)s", level=logging.INFO)
    """
    Pour en savoir plus: 
    https://docs.python.org/3/library/logging.html
    https://docs.python.org/3/howto/logging.html

    """

    logging.config.fileConfig(package_path('logging.conf'))

    """
    ch = logging.StreamHandler()
    #ch = logging.NullHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)

    log.setLevel(logging.DEBUG)
    log.addHandler(ch)
    """

    log = logging.getLogger('simpleExample')
    log.info('hello %s', '[error error error]')


if __name__ == '__main__':
    # explore_logging()
    # explore_path_info()
    explore_json_tools()
