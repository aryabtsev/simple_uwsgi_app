from routing import route
import views


def application(env, start_response):

    url = env.get('PATH_INFO')
    view_path, is_404 = route(url)
    data_to_return = views.generate_view(view_path)

    if is_404:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    else:
        start_response('200 OK', [('Content-Type', 'text/html')])

    return data_to_return




