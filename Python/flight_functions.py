"""Starter code for CSC108 Assignment 3"""

from typing import List, Set, Tuple#, Dict
from flight_reader import AirportDict, AIRPORT_DATA_INDEXES, RouteDict
#from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES

def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """

    return airports[iata][AIRPORT_DATA_INDEXES[info]]

def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    return iata_dst in routes[iata_src]

#helper function
def is_valid_iata(iata: str, routes: RouteDict) -> bool:
    """Return whether the iata is valid(either in keys or values of routes).
    
    >>> is_valid_iata('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_iata('AA5', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    l = []
    answer = False
    if iata in routes:
        return True
    elif iata not in routes:
        for keys in routes:
            l.append(routes[keys])
            for sets in l:
                if iata in sets:
                    return True
                else:
                    answer = False
    return answer    
    
def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    >>> is_valid_flight_sequence(['AA1', 'AA2'], {'AA1': {'AA2', 'AA3'}})
    True
    """
    answer = True
    if len(iata_list) == 1:
        return True
    #for i in range(len(iata_list) - 1):
        #if iata_list[i] in routes and iata_list[i + 1] not in routes:
            #if iata_list[i + 2:] != []:
                #answer = False
            #elif iata_list[i + 2:] == []:
                #answer = iata_list[i + 1] in routes[iata_list[i]]
    #return answer
    for iata in iata_list:
        if len(iata_list) >= 1 and not is_valid_iata(iata, routes):    
            return False
        elif len(iata_list) >= 1 and is_valid_iata(iata, routes):
            for i in range(len(iata_list) - 1):
                if iata_list[i] in routes and iata_list[i + 1] in routes and \
                   not is_direct_flight(iata_list[i], iata_list[i + 1], routes):
                    return False
                elif iata_list[i] in routes and iata_list[i + 1] in routes and \
                     is_direct_flight(iata_list[i], iata_list[i + 1], routes):
                    answer = True
                else: 
                    if iata_list[i] not in routes and iata_list[i + 1:] != []:
                        return False
                    elif iata_list[i + 1] not in routes and iata_list[i + 2:] != []:
                        return False
                    else:
                        if iata_list[i + 1] in routes[iata_list[i]]:
                            return True
                        return False
    return answer
    
def count_outgoing_flights(iata: str, routes: RouteDict) -> int:
    """Return the number of outgoing flights for the airport with the iata in \
    the given routes information.
    
    
    >>> count_outgoing_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_outgoing_flights('AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    """
    
    return len(routes[iata])

def count_incoming_flights(iata: str, routes: RouteDict) -> int:
    """Return the number of incoming flights for the airport with the iata in\
    the given routes information.
    
    >>> count_incoming_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_incoming_flights('AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    """
    num = 0
    for i in routes:
        if iata in routes[i]:
            num += 1
    return num

#helper function which returns all the possible destinations \
#under the restriction of the maximum number of hops.
def get_destination(iata: str, num: int, routes: RouteDict) -> List[Set[str]]:
    """Return a set of all IATA reachable from the iata in num hop(s)
    
    #TEST_ROUTES_DICT_FOUR_CITIES = {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1'}}
    
    >>> get_destination('AA1', 2, TEST_ROUTES_DICT_FOUR_CITIES)
    [{'AA1'}, {'AA2', 'AA4'}, {'AA3', 'AA1'}]
    
    >>> get_destination('AA3', 1, TEST_ROUTES_DICT_FOUR_CITIES)
    [{'AA3'}, {'AA4', 'AA1'}]
    """
    if num == 0:
        return [{iata}]
    elif num == 1:
        return [{iata}, routes[iata]]
    else:
        
        for i in range(2):
            dst_lst = [{iata}, routes[iata]]
            dst_set = set()
            for iata_1 in dst_lst[i]:
                for iata_2 in routes[iata_1]:
                    dst_set.add(iata_2)
        dst_lst.append(dst_set)
        return dst_lst

def reachable_destinations(iata_src: str, n: int, routes: RouteDict) -> \
    List[Set[str]]:                  #maximum number of direct flights allowed
    
    """Return a list of the sets of IATA reachable from the iata in steps from\
    0 up to (and including) the nth hop.
    
    #TEST_ROUTES_DICT_FOUR_CITIES = {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1'}}
    
    >>> reachable_destinations('AA1', 2, TEST_ROUTES_DICT_FOUR_CITIES)
    [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}]
    
    """

    if n == 0:
        return [{iata_src}]
    elif n == 1:
        return get_destination(iata_src, 1, routes)
    else:
        reachable_list = [{iata_src}]
        get_list = get_destination(iata_src, n, routes)
        # [{'AA1'}, {'AA2', 'AA4'}, {'AA3', 'AA1'}]
        for i_2 in range(1, len(get_list)):
            for i_3 in reachable_list[:i_2]:
                a = get_list[i_2] - i_3
                b = a
                get_list[i_2] = b
                if b != set() and b not in reachable_list:
                    reachable_list.append(b)
                
        return reachable_list

#helper function
def count_flights(iata: str, routes: RouteDict) -> int:
    """Return the sum of inbound and outbound flights from an\
    airport with iata accoring to the routes.
    
    >>> count_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    4
    
    >>> count_flights('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    3
    """
    base_val = len(routes[iata])
    for iata_1 in routes:
        if is_direct_flight(iata_1, iata, routes):
            base_val += 1    
    
    return base_val

#helper_function
def get_larger_tuple(t1: Tuple[str, int], t2: Tuple[str, int]) -> List[Tuple[str, int]]:
    """Return a list of the larger tuple between t1 and t2.The \
    larger the int, the larger the tuple.
    
    >>> get_larger_tuple(('AA3', 3), ('AA4', 1))
    [('AA3', 3)]
    
    >>> get_larger_tuple(('AA5', 3), ('AA2', 3))
    [('AA5', 3), ('AA2', 3)]
    """
    if t1[1] > t2[1]:
        return [t1]
    elif t1[1] < t2[1]:
        return [t2]
    else:
        return [t1, t2]


#helper function
def get_busy_list(routes: RouteDict) -> List[Tuple[str, int]]:
    """Return a list of the tuple of iata of airport and the traffic volume of \
    the iata by using information from routes.The busier the airport(i.e.higher\
    traffic volume), the smaller the index of the tuple in the list
    
    >>> get_busy_list(TEST_ROUTES_DICT_FOUR_CITIES)
    [('AA1', 4), ('AA3', 3), ('AA4', 3), ('AA2', 2)]
    
    """
    #Return all tuples in a list with the form (str, int)
    initial_list = []
    j = 0
    for i in routes:
        initial_list.append((i, count_flights(i, routes))) #list of tuples
    
    for i in range(len(initial_list)):
        j = i + 1
        if j < len(initial_list):
            if get_larger_tuple(initial_list[i], initial_list[j]) == [initial_list[j]]:
                smaller = initial_list[i]
                initial_list[i] = initial_list[j]
                initial_list[j] = smaller
    
    return initial_list

def find_busiest_airports(routes: RouteDict, n: int) -> List[Tuple[str, int]]:
    """Find the n busiest airports in terms of air traffic volume.\
    Use the total number of inbound and outbound flights from an airport \
    according to routes as the traffic volume for that airport.
    
    #Your output should include at most n airports, meaning that if the nth \
    #busiest airport and the n+1th busiest airports have the same traffic, \
    #then all airports at that traffic volume must be excluded from the output.
    #Your output should include the IATA code and traffic volume, with tuples \
    #sorted by traffic volume in descending order and alphabetically in case of ties.
    
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 3)
    [('AA1', 4), ('AA3', 3), ('AA4', 3)]
    
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 2)
    [('AA1', 4)]
    
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 1)
    [('AA1', 4)]
    """
    busy_list = get_busy_list(routes)[:n + 1]
    #[('AA1', 4), ('AA3', 3), ('AA4', 3), ('AA2', 2)] n = 1, i = 0
    # n  1*             2          3          4
    # i  0*             1          2          3
    if busy_list[n - 1][1] == busy_list[n][1]:
        num = busy_list[n - 1][1]
        busy_list[n:] = []
        for info in busy_list:
            if info[1] == num:
                busy_list.remove(info)
        return busy_list
    else:
        return busy_list[:n]




if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    #from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    #from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    #import doctest
    #doctest.testmod()
