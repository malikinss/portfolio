'''
TODO:   
        Implement a normalize_url() function that performs data normalization.
        It takes a website address and returns it with https:// at the beginning.

        The function accepts addresses in the form ADDRESS or http://ADDRESS, but always returns an address in the form https://ADDRESS. 
        
        The function input can also receive an address in the already normalized form https://ADDRESS; in this case, nothing needs to be changed.

'''
NORMAL_PROTOCOL = 'https://'
OLD_PROTOCOL = 'http://'

def remove_old_protocol(given_url):
    return given_url[len(OLD_PROTOCOL):]

def get_normalized_url(given_url):
    return NORMAL_PROTOCOL + given_url

def normalize_url(given_url): 
    if given_url.startswith(NORMAL_PROTOCOL):
        return given_url
    elif given_url.startswith(OLD_PROTOCOL):
        given_url = remove_old_protocol(given_url)    
    return get_normalized_url(given_url)

print(normalize_url('ya.ru'))