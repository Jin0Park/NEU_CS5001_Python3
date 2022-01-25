"""
Jin Young Park
CS5001 Fall 2021
HW05 test_lightrail.py
Test functions in lightrail.py
"""


from lightrail import is_valid_station, get_direction, get_num_stops,\
                      invalid_condition, get_index_from_tuple


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))
    assert(is_valid_station("Northgate"))


def test_get_direction():
    assert(get_direction("Northgate", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "Northgate")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("Northgate", "Angle Lake") == 18)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)


def test_invalid_condition():
    # invalid cases
    assert(invalid_condition("Northgate", "Northgate") is True)
    assert(invalid_condition("angle lake", "University of Washington") is True)
    assert(invalid_condition("University Street", "university street") is True)
    # valid cases
    assert(invalid_condition("University Street", "Northgate") is False)


def test_get_index_from_tuple():
    LINK_STATIONS = ("Northgate", "Roosevelt", "U District",
                     "University of Washington", "Capitol Hill", "Westlake",
                     "University Street", "Pioneer Square",
                     "International District/Chinatown", "Stadium", "SODO",
                     "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                     "Rainier Beach", "Tukwila International Boulevard",
                     "SeaTac/Airport", "Angle Lake")
    assert(get_index_from_tuple("Northgate", LINK_STATIONS) == 0)
    assert(get_index_from_tuple("Angle Lake", LINK_STATIONS) == 18)
    assert(get_index_from_tuple("Pioneer Square", LINK_STATIONS) == 7)
