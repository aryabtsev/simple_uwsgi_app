def application (environ, start_response):
    '''
    copy-pasted simple application that show you environ dict on every your request
    just for undestanding
    '''

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]