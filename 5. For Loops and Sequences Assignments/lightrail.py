"""
Jin Young Park
CS5001 Fall 2021
HW05 lightrail.py
The program tells a direction of the user's destination and the number of
stops from departure station to destination.

Contains five functions: is_valid_station, get_direction, get_num_stops,
                         get_index_from_tuple, invalid_condition
"""

LINK_STATIONS = ("Northgate", "Roosevelt", "U District",
                 "University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(string):
    '''
        Function -- is_valid_station
            Checks if a given string is a valid Seattle light rail station.
            Provided station must match a station name exactly. For example,
            "mount baker" would not be valid because the case doesn't match.
        Parameter:
            station -- The string to check
        Returns:
            True if a given string is a valid Seattle light rail station
            name, False otherwise.
    '''
    if string in LINK_STATIONS:
        return True
    return False


def get_direction(start, end):
    '''
        Function -- get_direction
            Given start and end station names, determines if the direction is
            Northbound or Southbound.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            "Northbound" if the end station is north of the start station, or
            "Southbound" if the end station is south of the start station. If
            either station is invalid, or start and end stations are the same,
            return "No destination found".
    '''
    # if start or end is invalid or they are the same, return invalid statement
    # by using invalid_condition function
    if invalid_condition(start, end):
        return "No destination found"

    # get the index of start and end stations in the tuple using
    # get_index_from_tuple function
    start_index = get_index_from_tuple(start, LINK_STATIONS)
    end_index = get_index_from_tuple(end, LINK_STATIONS)

    # use if statement to get the direction
    if start_index > end_index:
        return "Northbound"
    else:
        return "Southbound"


def get_num_stops(start, end):
    '''
        Function -- get_num_stops
            Calculates the number of stops from start to end.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            The number of stops from start to end. If either station is invalid
            or both stations are the same, return 0.
    '''
    # if start or end is invalid or they are the same, return invalid statement
    # by using invalid_condition function
    if invalid_condition(start, end):
        return 0

    # get the index of start and end stations in the tuple using
    # get_index_from_tuple function
    start_index = get_index_from_tuple(start, LINK_STATIONS)
    end_index = get_index_from_tuple(end, LINK_STATIONS)

    # calculate the number of stations from start to end.
    num_stops = abs(start_index - end_index)
    return num_stops


def invalid_condition(start, end):
    '''
        Function -- invalid_condition
            Check if there is any invalid condition for start and end stations
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            Returns True if the start station or end station is not among the
            tuple of Link stations or if the start and end station are the
            same. Returns False otherwise.
    '''
    if not is_valid_station(start) or not is_valid_station(end)\
       or start == end:
        return True
    return False


def get_index_from_tuple(string, tuple):
    '''
        Function -- get_index_from_tuple
            Get the index of string in the tuple.
        Parameters:
            string -- an element in a tuple
            tuple -- a given tuple
        Returns:
            Returns an index number of where the string is located in the tuple
            as an element.
    '''
    index = tuple.index(string)
    return index
