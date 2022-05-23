from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
<<<<<<< HEAD
    response_body = '\n\n'.join(response_body)
=======
    response_body = '\r \n'.join(response_body)
>>>>>>> 19e037123c22d1d117ddea6cf8b6be07a02f9a52
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
    return [response_body]

httpd = make_server(
    '',
    8051,
    application
)

httpd.handle_request()

