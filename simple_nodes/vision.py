#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('vision', anonymous = True)
    
pub = rospy.Publisher('vision_to_plan', Int32, queue_size = 10)
    
rate = rospy.Rate(1) # publish once per second

count = 0
while not rospy.is_shutdown():
    print(count)
    pub.publish(count) # publish data type int
    count += 1
    rate.sleep()
