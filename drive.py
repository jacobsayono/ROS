#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def parse_plan_data(plan_data): # data is of type String

    if plan_data.data == "even":
        print("turn left")
    else:
        print("turn right")

rospy.init_node('drive', anonymous = True)

sub = rospy.Subscriber('plan_to_drive', String, parse_plan_data)

rospy.spin()