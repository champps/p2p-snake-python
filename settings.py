#!/usr/bin/env python

num_of_calls = {}

connection_dict ={
                "my_ip": None,
                 "start_port": 6000,
                 "end_port": 6005,
                 "listening_peers": 1,
                "ip_range": 24,
                "max_num_of_peers": 30,
                "max client search socket": 500,
                "print_value_form_get_value": 0

                 }


# count num of return value
def get_value_setting(key):
    val = connection_dict[key]

    if val not in num_of_calls:
        num_of_calls[val] = 1
    else:
        num_of_calls[val] += 1

    if connection_dict["print_value_form_get_value"]:
        print ("{} :  {}".format(key, val, num_of_calls[val]))
    return val
