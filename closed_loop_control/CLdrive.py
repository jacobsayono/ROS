#!/usr/bin/env python

from numpy import fix
import rospy
from std_msgs.msg import Int32

def parse_fixvision_data(fixvision_data):
    fixvision = fixvision_data.data
    print(fixvision)

rospy.init_node('drive', anonymous = True)

sub = rospy.Subscriber('vision_to_drive', Int32, parse_fixvision_data)

rospy.spin()