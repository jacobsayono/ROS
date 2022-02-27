#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

def parse_vision_data(vision_data): # data is of type int
    
    if vision_data.data % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(even_or_odd)

    pub.publish(even_or_odd) # publish data type string

rospy.init_node('plan', anonymous = True)

sub = rospy.Subscriber('vision_to_plan', Int32, parse_vision_data)
pub = rospy.Publisher('plan_to_drive', String, queue_size = 10)

rospy.spin()
