'''
    Conor Gormally
    9/30/18
    A program that uses the Google Places api to get information about places based on user input
'''

import sys, argparse, json, urllib.request

def get_list_of_places(query):
    '''
    Gets a list of places based on user-inputted search text
    '''
    query =query.replace(' ', '+')
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key=AIzaSyC8juvEv-Mws-Ei7RWCGD_ABLXLsmy2Su4'
    url = base_url.format(query)
    #gets and decodes json data from the API
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    places_from_key = json.loads(string_from_server)
    result_list = []
    for place in result_list:
        name_of_place = place['name']
        type_of_place = place['type']
        location_of_place = place['formatted_address']
        place_id = place['place_id']
        result_list.append({'name':name_of_place, 'location':location_of_place})
    return result_list

def get_more_information(name_query):
    '''
    Gets information about a specific place
    '''
    name_query = name_query.replace(' ', '%20')
    base_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?&input={0}&inputtype=textquery&fields=name,formatted_address,rating,opening_hours,types&key=AIzaSyC8juvEv-Mws-Ei7RWCGD_ABLXLsmy2Su4'
    url = base_url.format(name_query)
    #gets and decodes json data from the API
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    place_information = json.loads(string_from_server)
    return_information_list = []
    for info_chunk in place_information['candidates']:
        place_name = info_chunk['name']
        place_location = info_chunk['formatted_address']
        place_rating = info_chunk['rating']
        place_types = info_chunk['types']
        return_information_list.append({'name':place_name, 'location':place_location, 'rating':place_rating, 'types':place_types})
    return return_information_list

def main(args):
    if args.action == 'query':
        list_of_places = get_list_of_places(args.querytext)
        for place in list_of_places:
            name_of_place = place['name']
            location_of_place = place['formatted_address']
            print('{0} [{1}]'.format(name_of_place, location_of_place))

    elif args.action == 'info':
        place_information = get_more_information(args.querytext)
        for info_chunk in place_information:
            name = info_chunk['name']
            location = info_chunk['formatted_address']
            rating = info_chunk['rating']
            types = info_chunk['types']
            print('{0} [{1} {2} {3} {4}]'.format(name, location, rating, types))

if _name_ == '_main_':
    parser = argparse.ArgumentParser(description='Get places and place information from Google Places API')

    parser.add_argument('querytext',
                        metavar='querytext',
                        help='The name or descriptive text used to search for a place or list of places')

    parser.add_argument('action',
                        metavar='action',
                        help='returns a list of places or more information about a single place',
                        choices=['query', 'info'])

    args = parser.parse_args()
    main(args)
