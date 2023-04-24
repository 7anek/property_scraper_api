from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote
import unicodedata

def url_encode(url):
    return unquote(url)

def dict_filter_none(d):
    return {key: value for key, value in d.items() if value is not None}

def remove_accents(str):
    return ''.join(c for c in unicodedata.normalize('NFD', str) if unicodedata.category(c) != 'Mn')

def lowercase_with_hyphen_str(str):
    return '-'.join(str.lower().split())

def slugify(str):
    """używane do wygenerowania lokalizacji jako parametr urla"""
    return lowercase_with_hyphen_str(remove_accents(str))

def generate_url(scheme='https', netloc='', path='', url='', query='', fragment=''):
    """
    scheme - protokół, 
    netloc - adres hosta, 
    path - reszta ścieżki, 
    query - niewiem coto, dożuca średnik, zostawiać puste, 
    params - parametry http get, 
    fragment - html id
    https://stackoverflow.com/questions/15799696/how-to-build-urls-in-python
    https://docs.python.org/3/library/urllib.parse.html
    """
    return urlunparse((
            scheme,
            netloc,
            path,
            url,
            urlencode(query),
            fragment
        )
    )

class DictAutoVivification(dict):
    """
    Implementation of perl's autovivification feature.
    >>> d = DictAutoVivification()
    >>> d['b']['s']['f']=4
    >>> d
    {'b': {'s': {'f': 4}}}
    >>> d['b']['r']['d']=7
    >>> d
    {'b': {'s': {'f': 4}, 'r': {'d': 7}}}
    """

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
