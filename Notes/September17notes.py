
"""
If I leave my house at 6:52 AM, and run 1 km at
an easy pace (8:15min/km), then 3 km at a hard
pace (7:12min/km) and 1 km at easy pace again,
what time do I get home for breakfast?
"""

# Welcome! This is how we comment in Python!

"""We can also comment using three double quotes
and this can last a couple of lines"""

# we will take our runner assignment, and make it into
# a set of instructions

initial_time = 6*60 + 4 # when i left the house

# these tell me the speeds of runner
slow_speed = 8 + (15/60)
fast_speed = 7 + (12/60)

#distance of runners
slow_distance = 3 
fast_distance = 4

#these tell me the times of the runner
slow_time = slow_distance*slow_speed
fast_time = fast_distance*fast_speed

#these tell me total time and time at home.
total_time = slow_time + fast_time
time_at_home = initial_time + total_time

#output the actual answers!
print('The total time elapsed was:', total_time)
print('The total time after midnight:', time_at_home)


    
