import math

def average(items_list):
    total_num_of_items = len(items_list)
    average = sum(items_list) / total_num_of_items
    print(average)


def find_percentage_of_total(total_number, portion_of_total):
    percent = (portion_of_total / total_number) * 100
    print(percent, '%')


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

# average(items_list=[27,25,24,32])

########################################################################################################
# find_percentage_of_total(total_number=200, portion_of_total=35)

# new_value_after_percent_increase(original_value=16, percent_increase=20)
# new_value_after_percent_decrease(original_value=30, percent_decrease=15)

# find_total_value_given_x_units_are_a_percentage_of(x_units=468, x_units_make_up_what_percentage_of_total=40)

# find_percentage_increase_from_2_values(original_value=24, new_higher_value=32)
# find_percentage_decrease_from_2_values(original_value=30, new_lower_value=24)

# percentage_difference_of_2_numbers_with_no_start_point(value_1=240, value_2=200)  #  order doesn't matter

# find_original_value_after_percentage_increase(new_value_after_increase=18, percentage_increase=40)
# find_original_value_after_percentage_decrease(new_value_after_decrease=45, percentage_decrease=20)
#########################################################################################################

# find_amount_given_ratio(ratio='2:15', total_amount=3600000)
# find_ratio_given_amounts(first_amount=67.9, second_amount=147)

find_speed(distance=450, time_minutes=90)
# find_distance(speed=100, time_minutes=30)
# find_time(distance=450, speed=310)
