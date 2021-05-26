# I always hit a wall once I spend few hours with Python.
# Then I jump to something sexy but complex and get lost in the shit.
#
# Comments
#

# Comments on its own line

import sys
import keyword
print("Hello, world!")  # Inline comments

#
# Variables
#

#
# Keywords
#

key_words = keyword.kwlist
print(key_words)

#
# Data types
#

integer_variable = 5
float_variable = 5.5
complex_variable = complex(1, 2)  # represents 1+2i

print(sys.float_info)

# arithmentic operators

addition = 3 + 7
substraction = 8 - 2
multiplication = 3 * 7
division = 87/9
floor_division = 87 // 9
modulus = 87 % 9
power = 2 ** 2

float_from_integer = float(98)  # float() is built-in function
float_from_string = float("654.76")

integer_from_float = int(3.14)
integer_from_string = int("33")  # can not be "33.3"

boolean_variable = True

# comparison operators

lower_than = 3 < 6  # True
greater_or_equal_than = 5 >= 7  # False
equal = 7 == 7  # True
not_equal = 8 != 9  # True

boolean_from_number = bool(1)  # 1 is True, 0 is False
boolean_from_string = bool("a")  # empty string is False
# empty list is False, something in list means True
boolean_from_list = bool([])

integer_from_boolean = int(False)  # False is 0, True is 1

#
# Strings
#

single_quotes_string = 'single quote'
double_quote_string = "double quote"
escaped_quote = 'escaped \' quote'
not_escaped_quote = "not escaped ' quote"

concatenation = "one" + "two"  # onetwo, spaces need to be added
length_of_string = len("of string")
upper_string = concatenation.upper()  # lower, title, etc.

# f-string

name = "Radek"
surname = "Zitek"
full_name = "My full name is {0} {1}".format(name, surname)
full_name = f"My full name is {name} {surname}"

sub_string = full_name[7]
long_sub_string = full_name[1:5]

#
# Lists
#

empty_list = []
number_list = [1, 2, 3, 4]
string_list = ["one", "two", "three"]
print(string_list.count("two"))
print(string_list.index("two"))
mixed_list = [1, "two", 3.0, False]

addition_list = number_list + string_list  # second list follows the first

list_slice = mixed_list[2:3]

first_item = mixed_list[0]
last_item = mixed_list[-1]
counting_from_end_item = mixed_list[-2]

nested_list = [1, 2, 3, ["one", "two", "three"], ["alfa", "beta", "gama"]]
item_two = nested_list[1]  # counting from 0
item_two_in_sublist = nested_list[3][1]

count_of_items = len(number_list)
number_list.append(5)  # adding object to the end of the list
string_list.sort()  # sorting list
# returns new sorted list, does not change original
sorted_string_list = sorted(string_list)
third_item = string_list.pop(2)  # returns and removes item

#
# Tuples
#

names_tuple = ("adam", "eva", "evil")  # can not change and the () are optional
name = names_tuple[0]  # accessible as list

list_from_tuple = list(names_tuple)

#
# Dictionaries
#

simple_dict = {"key": "value", "next_key": "another value"}
print(simple_dict["key"])
print(simple_dict.keys())
print(simple_dict.values())
print(simple_dict.items())

#
# Sets ... collection of UNIQUE items
#
simple_set = {"red", "green", "blue"}
set_from_list = set(string_list)
empty_set = set()

rgb_set = {"red", "green", "blue"}
some_color_set = {"blue", "white"}
union_set = rgb_set | some_color_set
print(union_set)
intersection_set = rgb_set & some_color_set
print(intersection_set)
some_color_set.add("magenta")
some_color_set.remove("magenta")
difference_set = rgb_set - some_color_set
print(difference_set)

#
# Conditionals
#

a, b = 5

if a < b:
    print("if branch")
elif a == b:
    print("first elif")
elif a > b:
    print("second elif")
else:
    print("else branch")

#
# Loops
#

for color in some_color_set:
    print(color)
    if color:
        #next iterration
        continue
    if len(color)=1:
        #stop itterations
        break
else: 
    # run this at the end if there was no break
    print("no break")

while True:
    print("whiling")
    if a==b:
        break
    if a<b:
        continue
    print("no break no continue")
else:
    print("at the end with no break")
    
