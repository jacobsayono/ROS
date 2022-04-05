#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def parse_vision_data(vision_data): # data is of type int
    if vision_data.data > 5:
        fix = vision_data.data - 5
        print("go down by", fix)
    elif vision_data.data < 5:
        fix = vision_data.data - 5
        print("go up by", -1 * fix)
    else:
        fix = 0
        print("right on track!", fix)

    pub.publish(fix) # publish data type string

rospy.init_node('plan', anonymous = True)

sub = rospy.Subscriber('vision_to_plan', Int32, parse_vision_data)
pub = rospy.Publisher('plan_backto_vision', Int32, queue_size = 10)

rospy.spin()