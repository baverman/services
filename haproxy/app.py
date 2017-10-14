import uwsgi

def application(env, start_response):
    if env['REQUEST_METHOD'] == 'OPTIONS':
        content = b'Ok'
    else:
        uwsgi.async_sleep(1)
        content = b"Hello World"

    start_response('200 OK', [('Content-Type', 'text/plain'),
                              ('Content-Length', str(len(content)))])
    return [content]
