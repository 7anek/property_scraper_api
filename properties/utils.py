from urllib.parse import urljoin, urlencode, urlparse, urlunparse, unquote, parse_qs
import unicodedata
from bs4 import BeautifulSoup

def url_encode(url):
    return unquote(url)

def dict_filter_none(d):
    return {key: value for key, value in d.items() if value}

def remove_accents(str):
    return ''.join(c for c in unicodedata.normalize('NFD', str) if unicodedata.category(c) != 'Mn')

def lowercase_with_hyphen_str(str):
    return '-'.join(str.lower().split())

def slugify(str):
    """używane do wygenerowania lokalizacji jako parametr urla"""
    return lowercase_with_hyphen_str(remove_accents(str))

def flatten_dict(d):
    """
    input:{'search[filter_float_price:from]': ['300000'], 'search[filter_float_price:to]': ['400000'], 'page': ['1']}
    output:{'search[filter_float_price:from]': '300000', 'search[filter_float_price:to]': '400000', 'page': '1'}
    """
    return {k: v[0] for k, v in d.items()}

def url_to_params_dict(url):
    """
    input:https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki/?search%5Bfilter_float_price%3Afrom%5D=300000&search%5Bfilter_float_price%3Ato%5D=400000&page=1
    output:{'search[filter_float_price:from]': '300000', 'search[filter_float_price:to]': '400000', 'page': '1'}
    """
    d=parse_qs(urlparse(url).query)
    fd=flatten_dict(d)
    return fd

def get_url_path(url):
    """
    input:https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki/?search%5Bfilter_float_price%3Afrom%5D=300000&search%5Bfilter_float_price%3Ato%5D=400000&page=1
    output:/nieruchomosci/mieszkania/sprzedaz/grodzisk-mazowiecki
    """
    return urlparse(url).path


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

def soup_from_file(path):
    page=open(path)
    return BeautifulSoup(page.read(), "html.parser")

def safe_execute(default, exception, function, *args):
    """
    safe_execute(
        "Divsion by zero is invalid.",
        ZeroDivisionError,
        div, 1, 0
    )
    # Returns "Divsion by zero is invalid."
    """
    try:
        return function(*args)
    except exception:
        return default

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
