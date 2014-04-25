import json


class MalformedJSON(ValueError):
    """JSON string is not valid."""
    pass


def read_json(stream, content_length):
    try:
        return json.loads(stream.read(content_length))

    except ValueError as ex:
        raise MalformedJSON(ex)