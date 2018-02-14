#!/home/eboss/anaconda3/envs/py27/bin/python

# coding=<utf-8> 

import rospy 
import roslib
import numpy
import json
import message_filters
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ModelStates

mpu6500_0_twist = []
mpu6500_1_twist = []
mpu6500_2_twist = []
mpu6500_3_twist = []
mpu6500_4_twist = []
mpu6500_5_twist = []
mpu6500_6_twist = []
mpu6500_7_twist = []
mpu6500_8_twist = []
mpu6500_9_twist = []
mpu6500_10_twist = []
mpu6500_11_twist = []
mpu6500_12_twist = []
mpu6500_13_twist = []
mpu6500_14_twist = []
mpu6500_15_twist = []

counter = 1080000 # 24*60*60*1000/10   100HZ about 6hours

last = 0



def ts6500_callback(mpu6500_0, mpu6500_1,mpu6500_2,mpu6500_3,mpu6500_4,mpu6500_5,mpu6500_6,mpu6500_7,mpu6500_8,mpu6500_9,mpu6500_10,mpu6500_11,mpu6500_12,mpu6500_13,mpu6500_14,mpu6500_15):
    rospy.loginfo("ts2 success!")
    global last, counter
    if mpu6500_0.header.stamp.nsecs - last != 10000000:
        print "2", mpu6500_0.header.stamp.nsecs - last
    last = mpu6500_0.header.stamp.nsecs

    mpu6500_0_twist.append([mpu6500_0.header.stamp.secs,mpu6500_0.header.stamp.nsecs,mpu6500_0.angular_velocity.x,mpu6500_0.angular_velocity.y,mpu6500_0.angular_velocity.z,mpu6500_0.linear_acceleration.x,mpu6500_0.linear_acceleration.y,mpu6500_0.linear_acceleration.z])
    mpu6500_1_twist.append([mpu6500_1.header.stamp.secs,mpu6500_1.header.stamp.nsecs,mpu6500_1.angular_velocity.x,mpu6500_1.angular_velocity.y,mpu6500_1.angular_velocity.z,mpu6500_1.linear_acceleration.x,mpu6500_1.linear_acceleration.y,mpu6500_1.linear_acceleration.z])
    mpu6500_2_twist.append([mpu6500_2.header.stamp.secs,mpu6500_2.header.stamp.nsecs,mpu6500_2.angular_velocity.x,mpu6500_2.angular_velocity.y,mpu6500_2.angular_velocity.z,mpu6500_2.linear_acceleration.x,mpu6500_2.linear_acceleration.y,mpu6500_2.linear_acceleration.z])
    mpu6500_3_twist.append([mpu6500_3.header.stamp.secs,mpu6500_3.header.stamp.nsecs,mpu6500_3.angular_velocity.x,mpu6500_3.angular_velocity.y,mpu6500_3.angular_velocity.z,mpu6500_3.linear_acceleration.x,mpu6500_3.linear_acceleration.y,mpu6500_3.linear_acceleration.z])
    mpu6500_4_twist.append([mpu6500_4.header.stamp.secs,mpu6500_4.header.stamp.nsecs,mpu6500_4.angular_velocity.x,mpu6500_4.angular_velocity.y,mpu6500_4.angular_velocity.z,mpu6500_4.linear_acceleration.x,mpu6500_4.linear_acceleration.y,mpu6500_4.linear_acceleration.z])
    mpu6500_5_twist.append([mpu6500_5.header.stamp.secs,mpu6500_5.header.stamp.nsecs,mpu6500_5.angular_velocity.x,mpu6500_5.angular_velocity.y,mpu6500_5.angular_velocity.z,mpu6500_5.linear_acceleration.x,mpu6500_5.linear_acceleration.y,mpu6500_5.linear_acceleration.z])
    mpu6500_6_twist.append([mpu6500_6.header.stamp.secs,mpu6500_6.header.stamp.nsecs,mpu6500_6.angular_velocity.x,mpu6500_6.angular_velocity.y,mpu6500_6.angular_velocity.z,mpu6500_6.linear_acceleration.x,mpu6500_6.linear_acceleration.y,mpu6500_6.linear_acceleration.z])
    mpu6500_7_twist.append([mpu6500_7.header.stamp.secs,mpu6500_7.header.stamp.nsecs,mpu6500_7.angular_velocity.x,mpu6500_7.angular_velocity.y,mpu6500_7.angular_velocity.z,mpu6500_7.linear_acceleration.x,mpu6500_7.linear_acceleration.y,mpu6500_7.linear_acceleration.z])
    mpu6500_8_twist.append([mpu6500_8.header.stamp.secs,mpu6500_8.header.stamp.nsecs,mpu6500_8.angular_velocity.x,mpu6500_8.angular_velocity.y,mpu6500_8.angular_velocity.z,mpu6500_8.linear_acceleration.x,mpu6500_8.linear_acceleration.y,mpu6500_8.linear_acceleration.z])
    mpu6500_9_twist.append([mpu6500_9.header.stamp.secs,mpu6500_9.header.stamp.nsecs,mpu6500_9.angular_velocity.x,mpu6500_9.angular_velocity.y,mpu6500_9.angular_velocity.z,mpu6500_9.linear_acceleration.x,mpu6500_9.linear_acceleration.y,mpu6500_9.linear_acceleration.z])
    mpu6500_10_twist.append([mpu6500_10.header.stamp.secs,mpu6500_10.header.stamp.nsecs,mpu6500_10.angular_velocity.x,mpu6500_10.angular_velocity.y,mpu6500_10.angular_velocity.z,mpu6500_10.linear_acceleration.x,mpu6500_10.linear_acceleration.y,mpu6500_10.linear_acceleration.z])
    mpu6500_11_twist.append([mpu6500_11.header.stamp.secs,mpu6500_11.header.stamp.nsecs,mpu6500_11.angular_velocity.x,mpu6500_11.angular_velocity.y,mpu6500_11.angular_velocity.z,mpu6500_11.linear_acceleration.x,mpu6500_11.linear_acceleration.y,mpu6500_11.linear_acceleration.z])
    mpu6500_12_twist.append([mpu6500_12.header.stamp.secs,mpu6500_12.header.stamp.nsecs,mpu6500_12.angular_velocity.x,mpu6500_12.angular_velocity.y,mpu6500_12.angular_velocity.z,mpu6500_12.linear_acceleration.x,mpu6500_12.linear_acceleration.y,mpu6500_12.linear_acceleration.z])
    mpu6500_13_twist.append([mpu6500_13.header.stamp.secs,mpu6500_13.header.stamp.nsecs,mpu6500_13.angular_velocity.x,mpu6500_13.angular_velocity.y,mpu6500_13.angular_velocity.z,mpu6500_13.linear_acceleration.x,mpu6500_13.linear_acceleration.y,mpu6500_13.linear_acceleration.z])
    mpu6500_14_twist.append([mpu6500_14.header.stamp.secs,mpu6500_14.header.stamp.nsecs,mpu6500_14.angular_velocity.x,mpu6500_14.angular_velocity.y,mpu6500_14.angular_velocity.z,mpu6500_14.linear_acceleration.x,mpu6500_14.linear_acceleration.y,mpu6500_14.linear_acceleration.z])
    mpu6500_15_twist.append([mpu6500_15.header.stamp.secs,mpu6500_15.header.stamp.nsecs,mpu6500_15.angular_velocity.x,mpu6500_15.angular_velocity.y,mpu6500_15.angular_velocity.z,mpu6500_15.linear_acceleration.x,mpu6500_15.linear_acceleration.y,mpu6500_15.linear_acceleration.z])

    if counter == 0:
        json.dump(mpu6500_0_twist, open('./data/mpu6500_0_twist.txt','w'))
        json.dump(mpu6500_1_twist, open('./data/mpu6500_1_twist.txt','w'))
        json.dump(mpu6500_2_twist, open('./data/mpu6500_2_twist.txt','w'))
        json.dump(mpu6500_3_twist, open('./data/mpu6500_3_twist.txt','w')) 
        json.dump(mpu6500_4_twist, open('./data/mpu6500_4_twist.txt','w'))
        json.dump(mpu6500_5_twist, open('./data/mpu6500_5_twist.txt','w'))
        json.dump(mpu6500_6_twist, open('./data/mpu6500_6_twist.txt','w'))
        json.dump(mpu6500_7_twist, open('./data/mpu6500_7_twist.txt','w'))
        json.dump(mpu6500_8_twist, open('./data/mpu6500_8_twist.txt','w'))
        json.dump(mpu6500_9_twist, open('./data/mpu6500_9_twist.txt','w'))
        json.dump(mpu6500_10_twist, open('./data/mpu6500_10_twist.txt','w'))
        json.dump(mpu6500_11_twist, open('./data/mpu6500_11_twist.txt','w'))
        json.dump(mpu6500_12_twist, open('./data/mpu6500_12_twist.txt','w'))
        json.dump(mpu6500_13_twist, open('./data/mpu6500_13_twist.txt','w'))
        json.dump(mpu6500_14_twist, open('./data/mpu6500_14_twist.txt','w'))
        json.dump(mpu6500_15_twist, open('./data/mpu6500_15_twist.txt','w'))
    counter = counter -1



rospy.init_node('logger1')

mpu6500_0_sub = message_filters.Subscriber('mpu6500_0', Imu)
mpu6500_1_sub = message_filters.Subscriber('mpu6500_1', Imu)
mpu6500_2_sub = message_filters.Subscriber('mpu6500_2', Imu)
mpu6500_3_sub = message_filters.Subscriber('mpu6500_3', Imu)
mpu6500_4_sub = message_filters.Subscriber('mpu6500_4', Imu)
mpu6500_5_sub = message_filters.Subscriber('mpu6500_5', Imu)
mpu6500_6_sub = message_filters.Subscriber('mpu6500_6', Imu)
mpu6500_7_sub = message_filters.Subscriber('mpu6500_7', Imu)
mpu6500_8_sub = message_filters.Subscriber('mpu6500_8', Imu)
mpu6500_9_sub = message_filters.Subscriber('mpu6500_9', Imu)
mpu6500_10_sub = message_filters.Subscriber('mpu6500_10', Imu)
mpu6500_11_sub = message_filters.Subscriber('mpu6500_11', Imu)
mpu6500_12_sub = message_filters.Subscriber('mpu6500_12', Imu)
mpu6500_13_sub = message_filters.Subscriber('mpu6500_13', Imu)
mpu6500_14_sub = message_filters.Subscriber('mpu6500_14', Imu)
mpu6500_15_sub = message_filters.Subscriber('mpu6500_15', Imu)

ts6500 = message_filters.TimeSynchronizer([mpu6500_0_sub, mpu6500_1_sub,mpu6500_2_sub,mpu6500_3_sub,mpu6500_4_sub,mpu6500_5_sub,mpu6500_6_sub,mpu6500_7_sub,mpu6500_8_sub,mpu6500_9_sub,mpu6500_10_sub,mpu6500_11_sub,mpu6500_12_sub,mpu6500_13_sub,mpu6500_14_sub,mpu6500_15_sub], 10)
ts6500.registerCallback(ts6500_callback)

rospy.spin()

