import operator as op
from functools import reduce

def average(items_list):
    total_num_of_items = len(items_list)
    average = sum(items_list) / total_num_of_items
    print(average)

def find_percentage_of_total(total_number, portion_of_total):
    percent = (portion_of_total / total_number) * 100
    print(percent, '%')

def find_total_number_given_smaller_percent_is_x_amount_less_than_larger_percent(larger_percent, units_less_than):
    remaining_percentage = 100 - larger_percent
    percent_reduced_to_one = larger_percent - remaining_percentage
    total = units_less_than / (percent_reduced_to_one / 100)
    print(total)

def find_total_number_given_larger_percent_is_x_amount_more_than_smaller_percent(smaller_percent, units_more_than):
    remaining_percentage = 100 - smaller_percent
    percent_reduced_to_one = remaining_percentage - smaller_percent
    total = units_more_than / (percent_reduced_to_one / 100)
    print(total)

def new_value_after_percent_increase(original_value, percent_increase):
    new_value = ((100 + percent_increase) / 100) * original_value
    print("new value", new_value)


def new_value_after_percent_decrease(original_value, percent_decrease):
    new_value = ((100 - percent_decrease) / 100) * original_value
    print("new value", new_value)


def find_percentage_increase_from_2_values(original_value, new_higher_value):
    percent_increase = ((new_higher_value - original_value) / original_value) * 100
    print(percent_increase, "% increase")


def find_percentage_decrease_from_2_values(original_value, new_lower_value):
    percent_decrease = ((original_value - new_lower_value) / original_value) * 100
    print(percent_decrease, "% decrease")


def percentage_difference_of_2_numbers_with_no_start_point(value_1, value_2):
    percentage_diff = abs(((value_1 - value_2) / ((value_1 + value_2) / 2)) * 100)
    print(percentage_diff)


def find_original_value_after_percentage_increase(new_value_after_increase, percentage_increase):
    original_value = (new_value_after_increase / (100 + percentage_increase)) * 100
    print(original_value)


def find_original_value_after_percentage_decrease(new_value_after_decrease, percentage_decrease):
    original_value = (new_value_after_decrease / (100 - percentage_decrease)) * 100
    print(original_value)

def find_total_value_given_x_units_are_a_percentage_of(x_units, x_units_make_up_what_percentage_of_total):
    total_value = x_units * (100/x_units_make_up_what_percentage_of_total)
    print(total_value)

def find_amount_given_ratio(ratio, total_amount):
    ratio_a = int(ratio[0])
    ratio_b = int(ratio[-1])
    amount_for_first_part_ratio = (ratio_a / (ratio_a + ratio_b)) * total_amount
    print(amount_for_first_part_ratio, "units for the FIRST part of ratio")
    amount_for_second_part_ratio = (ratio_b / (ratio_a + ratio_b)) * total_amount
    print(amount_for_second_part_ratio, "units for the SECOND part of ratio")

def find_ratio_given_amounts(first_amount, second_amount):
    lowest_num = min(first_amount, second_amount)
    highest_num = max(first_amount, second_amount)
    divided = round((highest_num / lowest_num), 2)
    ratio = ['1', ':', '1']
    if highest_num == first_amount:
        ratio[0] = str(divided)
    else:
        ratio[-1] = str(divided)
    ratio = ''.join(ratio)
    print(ratio)


def find_speed(distance, time_minutes):
    speed = (distance / time_minutes) * 60
    print(speed, 'kp/h')


def find_distance(speed, time_minutes):
    distance = (speed * time_minutes) / 60
    print(distance, 'km')


def find_time(distance, speed):
    time = distance / speed * 60
    print(time, 'minutes,\nor', int(time / 60), 'hours and', time % 60, 'minutes')


def number_of_combinations_not_repeated(larger_num, smaller_num):
    r = min(smaller_num, larger_num-smaller_num)
    numer = reduce(op.mul, range(larger_num, larger_num-smaller_num, -1), 1)
    denom = reduce(op.mul, range(1, smaller_num+1), 1)
    print(numer // denom)

# average(items_list=[11500,20000,12500,12000])
########################################################################################################
# find_percentage_of_total(total_number=2374000, portion_of_total=95000)

# new_value_after_percent_increase(original_value=20, percent_increase=26)
# new_value_after_percent_decrease(original_value=14, percent_decrease=33.33)

# find_total_value_given_x_units_are_a_percentage_of(x_units=468, x_units_make_up_what_percentage_of_total=40)

# find_percentage_increase_from_2_values(original_value=80, new_higher_value=84)
# find_percentage_decrease_from_2_values(original_value=24, new_lower_value=32)

# percentage_difference_of_2_numbers_with_no_start_point(value_1=2374000, value_2=95000)  #  order doesn't matter

# find_original_value_after_percentage_increase(new_value_after_increase=18, percentage_increase=40)
# find_original_value_after_percentage_decrease(new_value_after_decrease=12, percentage_decrease=20)

# find_total_number_given_smaller_percent_is_x_amount_less_than_larger_percent(larger_percent=70, units_less_than=120)
# find_total_number_given_larger_percent_is_x_amount_more_than_smaller_percent(smaller_percent=30, units_more_than=120)

# number_of_combinations_not_repeated(larger_num=7, smaller_num=4)

#########################################################################################################
# find_amount_given_ratio(ratio='2:15', total_amount=3600000)
# find_ratio_given_amounts(first_amount=60, second_amount=30)

# find_speed(distance=450, time_minutes=90)
# find_distance(speed=100, time_minutes=30)
# find_time(distance=450, speed=310)
