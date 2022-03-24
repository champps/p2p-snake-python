#!/usr/bin/env python

# this file for keep connect file orgnize and clear

def send_empty_packege():
    return ""














command_dict = {
    "empty" : send_empty_packege
}



# count num of return value
def prosses_messange(key):
    val = connection_dict[key]

    if val not in num_of_calls:
        num_of_calls[val] = 1
    else:
        num_of_calls[val] += 1

    if connection_dict["print_value_form_get_value"]:
        print ("{} :  {}".format(key, val, num_of_calls[val]))
    return val
