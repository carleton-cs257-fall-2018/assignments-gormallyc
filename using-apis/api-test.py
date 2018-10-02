'''
    api-test.py
    Conor Gormally
'''

import sys, argparse, json, urllib.request, requests

def get_list_of_places(query):
    '''

    '''
    query =query.replace(' ', '+')
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key=AIzaSyDC7uCch4XQ8yYVizaXDJHKspfwIFpKqHw'
    url = base_url.format(query)
    print(url)
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    places_from_key = json.loads(string_from_server)
    result_list = []
    for place in result_list:
        name_of_place = place['name']
        type_of_place = place['type']
        location_of_place = place['formatted_address']
        place_id = place['place_id']
        if type(name_of_place) != type(''):
            raise Exception('name has wrong type: "{0}"'.format(name_of_place))
        if type(location_of_place) != type(''):
            raise Exception('location of place has wrong type: "{0}"'.format(location_of_place))
        result_list.append({'name':name_of_place, 'location':location_of_place})
    return result_list

def get_more_information(name_query):
    '''

    '''
    name_query = name_query.replace(' ', '%20')
    base_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?&input={0}&inputtype=textquery&fields=name,formatted_address,rating,opening_hours,types&key=AIzaSyDC7uCch4XQ8yYVizaXDJHKspfwIFpKqHw'
    url = base_url.format(name_query)
    print(url)
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    place_information = json.loads(string_from_server)
    return_information_list = []
    for info_chunk in place_information:
        place_name = info_chunk['name']
        place_location = info_chunk['formatted_address']
        place_rating = info_chunk['rating']
        place_hours = info_chunk['opening_hours']
        place_types = info_chunk['types']
        if type(place_name) != type(''):
            raise Exception('name has wrong type: "{0}"'.format(place_name))
        if type(place_location) != type(''):
            raise Exception('location of place has wrong type: "{0}"'.format(place_location))
        if type(place_rating) != type(''):
            raise Exception('rating of place has wrong type: "{0}"'.format(place_rating))
        if type(place_hours) != type(''):
            raise Exception('hours of place has wrong type: "{0}"'.format(place_hours))
        if type(place_types) != type([]):
            raise Exception('type of places has wrong type: "{0}"'.format(place_types))
        information_list.append({'name':place_name, 'location':place_location, 'rating':place_rating, 'hours':place_hours, 'types':place_types})
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
            hours = info_chunk['opening_hours']
            types = info_chunk['types']
            print('{0} [{1} {2} {3} {4}]'.format(name, location, rating, hours, types))

if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
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
