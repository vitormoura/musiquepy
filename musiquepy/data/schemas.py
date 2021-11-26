from marshmallow import Schema, fields
from musiquepy.data.model import GenericRecord

class GenericRecordSchema(Schema):
    id = fields.Str()
    description = fields.Str()
