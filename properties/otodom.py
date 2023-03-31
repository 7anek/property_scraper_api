import unicodedata

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

def url_path(search_params, lang='pl'):
    url_path = []
    if 'offer_type' in search_params:
        url_path.append(offer_type_mapping[search_params['offer_type']])
    if 'property_type' in search_params:
        url_path.append(property_type_mapping[search_params['property_type']])
    url_path.append(parse_localization(search_params['localization']))
    return f"{lang}/oferty/{'/'.join(url_path)}"

def parse_localization(str):
    return lowercase_with_hyphen_str(remove_accents(str))

def lowercase_with_hyphen_str(str):
    return '-'.join(str.lower().split())

def remove_accents(str):
    return ''.join(c for c in unicodedata.normalize('NFD', str) if unicodedata.category(c) != 'Mn')

def url_query(search_params):
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
    if 'page' in search_params:
        url_query['page'] = search_params['page']
    if 'limit' in search_params:
        url_query['limit'] = search_params['limit']
    print('url_query', url_query)
    return url_query