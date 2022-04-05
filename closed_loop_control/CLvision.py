#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('vision', anonymous = True)

def parse_planback_data(planback_data):
    fix = planback_data.data
    correct = number - fix
    pub1.publish(correct)

pub = rospy.Publisher('vision_to_plan', Int32, queue_size = 10)
pub1 = rospy.Publisher('vision_to_drive', Int32, queue_size = 10)
sub = rospy.Subscriber('plan_backto_vision', Int32, parse_planback_data)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    number = random.randint(1,9)
    print(number)
    pub.publish(number)
    rate.sleep()