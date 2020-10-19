"""Functions for CSC108 Assignment 3 to read in the airport and route data.
"""

from typing import TextIO
#from typing import Dict, List, Set, Tuple

# Note about "from io import StringIO" in the docstrings:
# We can use StringIO to pretend that a string is the contents of a file.
# We are only using it for the examples below, to help you understand what
# the functions will do. 
# You do NOT have to use it yourself.

from flight_types_constants_and_test_data import AIRPORT_DATA_INDEXES, \
     ROUTE_DATA_INDEXES, AirportDict, RouteDict#, TEST_AIRPORTS_SRC, \
          #TEST_AIRPORTS_DICT, TEST_ROUTES_SRC, TEST_ROUTES_DICT_FOUR_CITIES

def get_airports_information(information_list: str, index: int) -> str:
    """Return the airports' information in the information_list corresponding to the\
    index. 
    
    >>> get_airports_information('1,"Apt1","Cty1","Cntry1","AA1","AAA1",-1,1,1,1,"1","D1","Typ1","Src1"', 0)
    '1'
    
    >>> get_airports_information('3,"Apt3","Cty3","Cntry3","AA3","AAA3",-3,3,3,3,"3","D3","Type3","Src3"', 2)
    'Cty3'
    """
    comma_index = 0
    num_comma = 0
    if index == AIRPORT_DATA_INDEXES['Airport ID']:
        s_to_return = information_list[:information_list.find(',')]
        return s_to_return
        
    elif index == AIRPORT_DATA_INDEXES['Latitude'] or \
         index == AIRPORT_DATA_INDEXES['Longitude'] or \
        index == AIRPORT_DATA_INDEXES['Altitude'] or \
        index == AIRPORT_DATA_INDEXES['Timezone']:
        while num_comma < index:#index is the input
            comma_index = information_list.find(',', comma_index)
            num_comma += 1
            comma_index += 1
        s_to_return = information_list[comma_index:information_list.\
                                                 find(',', comma_index)]                     
        return s_to_return        
             
    else:
        while num_comma < index:#index is the input
            comma_index = information_list.find(',', comma_index)
        
            num_comma += 1
            comma_index += 1
        s_to_return = information_list[comma_index + 1:information_list.\
                                         find(',', comma_index) - 1]        
        return s_to_return

def read_airports(airports_source: TextIO) -> AirportDict:
                                          #AirportDict = Dict[str, List[str]]
    """Return a dictionary containing the information in airports_source.
    Skip entries that have no IATA code.

    >>> from io import StringIO
    >>> airports_src = StringIO(TEST_AIRPORTS_SRC)
    >>> airports_res = read_airports(airports_src)
    >>> airports_res['AA1'][0], airports_res['AA1'][1]
    ('1', 'Apt1')
    >>> airports_res['AA4'][0], airports_res['AA4'][1]
    ('4', 'Apt4')
    >>> len(airports_res)
    4
    >>> airports_res == TEST_AIRPORTS_DICT
    True
    """
    
    airports_list = airports_source.readlines()
    d = {}
    iata_index = AIRPORT_DATA_INDEXES['IATA']
    
    i = 0
    while i < len(airports_list):
        num_comma = 0
        comma_index = 0        
        while num_comma < iata_index:
            comma_index = airports_list[i].find(',', comma_index)
            num_comma += 1
            comma_index += 1
        iata = airports_list[i][comma_index + 1: \
                                airports_list[i].find(',', comma_index) - 1]
        
        if iata != '""' and iata != "\\N":
            d[iata] = [get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Airport ID']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Name']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['City']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Country']), get_airports_information(airports_list[i],\
    AIRPORT_DATA_INDEXES['IATA']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['ICAO']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Latitude']), get_airports_information(airports_list[i],\
    AIRPORT_DATA_INDEXES['Longitude']), get_airports_information(airports_list[i],\
    AIRPORT_DATA_INDEXES['Altitude']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Timezone']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['DST']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Tz']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Type']), get_airports_information(airports_list[i], \
    AIRPORT_DATA_INDEXES['Source'])]
        
        i += 1
        
    return d
    
def get_routes_information(information_list: str, index: int) -> str:
    """Return the information of the routes in the information_list corresponding to the\
    index. 
    
    >>> get_routes_information('A1,1111,AA1,1,AA2,2,,0,EQ1', 0)
    'A1'
    >>> get_routes_information('A3,3333,AA3,3,AA4,4,,0,EQ1', 2)
    'AA3'
    """
    comma_index = 0
    num_comma = 0
    while num_comma < index:#index is the input
        comma_index = information_list.find(',', comma_index)
        
        num_comma += 1
        comma_index += 1
    s_to_return = information_list[comma_index:information_list.\
                                         find(',', comma_index)]
    return s_to_return 


def read_routes(routes_source: TextIO, airports: AirportDict) -> RouteDict:
                                              #RouteDict = Dict[str, Set[str]]
    """Return the flight routes from routes_source, including only the ones
    that have an entry in airports. If there are multiple routes between
    routes_source and a destination (on different airlines for example),
    include the destination only once. Routes that include null airport IDs
    should still be included, but routes that have empty IATA should be
    excluded.

    >>> from io import StringIO
    >>> routes_src = StringIO(TEST_ROUTES_SRC)
    >>> actual = read_routes(routes_src, TEST_AIRPORTS_DICT)
    >>> actual == TEST_ROUTES_DICT_FOUR_CITIES
    True
    """
    routes_list = routes_source.readlines()
    d = {}
    src_index = ROUTE_DATA_INDEXES['Source airport']
    dst_index = ROUTE_DATA_INDEXES['Destination airport']
    
    for i in range(len(routes_list)):
        source_airport = get_routes_information(routes_list[i], src_index)
        destination_airport = get_routes_information(routes_list[i], dst_index)
        
        if source_airport in airports and destination_airport in airports\
           and source_airport not in d:
            
            routes = set() # it's a set
            routes.add(destination_airport)
            d[source_airport] = routes
        
        elif source_airport in airports and destination_airport in \
             airports and source_airport in d:
            d[source_airport].add(destination_airport)
    return d


    
                

if __name__ == '__main__':
    """Uncommment the following as needed to run the doctests"""
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    #from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    #from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    #import doctest
    #doctest.testmod()