def sample_get():
    return b"Hello World, this is a GET endpoint."


def route_request(path, method):
    print(ROUTER, path, method)
    if path not in ROUTER:
        return 404, b"Not found"
    if method not in ROUTER[path]:
        return 405, b"Method not allowed"
    return 200, "OK"


ROUTER = {b"/path": {b"GET": sample_get}}
