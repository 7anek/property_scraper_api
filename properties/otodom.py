import unicodedata
from properties.utils import *

offer_type_mapping = {
    'sell': 'sprzedaz',
    'rent': 'wynajem',
    # 'wszystko': 'wszystko'
}
property_type_mapping = {
    'flat': 'mieszkanie',
    'house': 'dom',
    'plot': 'dzialka',
    'garage': 'garaz'
}

def get_url_path(search_params, lang='pl'):
    url_path = []
    if 'offer_type' in search_params:
        url_path.append(offer_type_mapping[search_params['offer_type']])
    if 'property_type' in search_params:
        url_path.append(property_type_mapping[search_params['property_type']])
    url_path.append(slugify(search_params['localization']))
    return f"{lang}/oferty/{'/'.join(url_path)}"


def url_query(search_params,page=1,limit=24):
    url_query = {
        'distanceRadius': 0,
        'market': 'ALL',
        'viewType': 'listing',
        'lang': 'pl',
        'searchingCriteria': offer_type_mapping[search_params['offer_type']],
    }

    if 'price_min' in search_params:
        url_query['priceMin'] = search_params['price_min']
    if 'price_max' in search_params:
        url_query['priceMax'] = search_params['price_max']
    if 'area_min' in search_params:
        url_query['areaMin'] = search_params['area_min']
    if 'area_max' in search_params:
        url_query['areaMax'] = search_params['area_max']

    print('url_query', url_query)
    return url_query