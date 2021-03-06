#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('duangjai_topic', String, queue_size=10)
    rospy.init_node('duangjai', anonymous=True)
    rate = rospy.Rate(5) # 5hz
    while not rospy.is_shutdown():
        name_str = "My name is Duangjai %s" % rospy.get_time()
        rospy.loginfo(name_str)
        pub.publish(name_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
