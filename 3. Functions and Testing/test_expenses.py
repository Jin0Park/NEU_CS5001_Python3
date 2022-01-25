"""

Jin Young Park
CS5001 Fall 2021
HW3 test_expenses.py
The program contains test functions for every function in expenses.py
besides main function.

"""


from expenses import calculate_mileage, get_reimbursement_amount, \
                     get_actual_mileage_rate, get_actual_trip_cost


def test_calculate_mileage():
    assert(calculate_mileage(0, 10) == 10)
    assert(calculate_mileage(98000, 98805) == 805)
    assert(calculate_mileage(8, 2) == 0)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(8) == 4.60)
    assert(get_reimbursement_amount(1000) == 575.00)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(32, 3.11) == 0.0972)
    assert(get_actual_mileage_rate(48, 2.74) == 0.0571)
    assert(get_actual_mileage_rate(22, 4.89) == 0.2223)
    assert(get_actual_mileage_rate(30, -1) == 0.0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(1000, 1010, 36, 3.09) == 0.86)
    assert(get_actual_trip_cost(25, 86, 32, 3.11) == 5.93)
    assert(get_actual_trip_cost(98703, 110012, 22, 4.89) == 2513.99)
    assert(get_actual_trip_cost(1000, 1010, 0, -20) == 0.0)
