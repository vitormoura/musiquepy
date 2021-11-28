from marshmallow import Schema, fields


class GenericRecordSchema(Schema):
    id = fields.Str()
    description = fields.Str()


class AlbumSchema(GenericRecordSchema):
    artist = fields.Nested(GenericRecordSchema)


class MusicTrackSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    order = fields.Int()
    album = fields.Nested(AlbumSchema)
    artist = fields.Nested(GenericRecordSchema)
    duration = fields.TimeDelta()


class ArtistSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    web_site = fields.Str()
    code = fields.Str()
    historique = fields.Str()
    