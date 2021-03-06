# ------------------------------------------#
# !/usr/bin/env python3
# Title: strformat_lab.py
# Desc: In this exercise we will reinforce the important concepts of string formatting, so that these start to become second nature!
# Tian Xie, 2020-04-10, Created File
# ------------------------------------------#

# Task 1
print('------Task 1------')
my_tuple = ( 2, 123.4567, 10000, 12345.67)
print(f'file_00{my_tuple[0]} :','   {:.2f},'.format(my_tuple[1]), '{:.2e},'.format(my_tuple[2]),'{:.2e}'.format(my_tuple[3]))

# Task 2
print('------Task 2------')
print(f"file_00{my_tuple[0]} :    {round(my_tuple[1],2)}, {'%.2e' % my_tuple[2]}, {'%.2e' % my_tuple[3]}")

# Task 3
print('------Task 3------')


def formatter(in_tuple):
    form_string = "the {} numbers are: {}" + (", {}" * (len(in_tuple) - 1))
    return form_string.format(len(in_tuple), *in_tuple[:])


print(formatter((1,2,3,4,5,6)))


# Task 4
print('------Task 4------')
t = ( 4, 30, 2017, 2, 27)
print(f'\'0{t[3]} {t[4]} {t[2]} 0{t[0]}{t[1]}\'')

# Task 5
print('------Task 5------')
list_task5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {list_task5[0][:-1]} is {list_task5[1]} and the weight of a {list_task5[2][:-1]} is {list_task5[3]}")
print(f"The weight of an {list_task5[0][:-1].upper()} is {list_task5[1]*1.2} and the weight of a {list_task5[2][:-1].upper()} is {list_task5[3]*1.2}")

# Task 6
print('------Task 6------')
task6_tuple = (('Name', 'Age', 'Cost'), ('turtle000000000', '500', '$1000000'), ('cat', '1', '$5'))


def task6(a_tuple):
    form_string = '{:<20} {:<20} {:<20}'
    for row in a_tuple:
        print(form_string.format(*row))


# Extra Task
print('------Extra Task------')
extra_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def extra(a_tuple):
    for i in a_tuple:
        print("{:=5d}".format(i), end=" ")


if __name__ == '__main__':
    task6(task6_tuple)
    extra(extra_tuple)
