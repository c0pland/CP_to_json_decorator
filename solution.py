import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = json.dumps(func(*args, **kwargs))
        return res

    return wrapped
