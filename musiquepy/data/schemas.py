from marshmallow import Schema, fields


class GenericRecordSchema(Schema):
    id = fields.Str()
    description = fields.Str()


class AlbumSchema(GenericRecordSchema):
    artist = fields.Nested(GenericRecordSchema)

class MusicTrackSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    order = fields.Number()
    album = fields.Nested(AlbumSchema)
    artist = fields.Nested(GenericRecordSchema)
    duration = fields.TimeDelta()
