from routing import route
import views


def application(env, start_response):

    url = env.get('PATH_INFO')
    view_info = route(url)
    data_to_return = views.generate_view(view_info[0])
    start_response(view_info[1], [(view_info[2], view_info[3])])
    return data_to_return




