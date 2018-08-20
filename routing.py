from yaml import load

url_dict = load(open('urls.yaml'))


def route(url, url_dict = url_dict):
    
    url_to_return = url_dict.get(url)
    
    if url_to_return is None:
        return url_dict.get('404_error_page'), True
    
    return url_to_return, False
