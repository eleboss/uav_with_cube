#!/home/eboss/anaconda3/envs/py27/bin/python

# coding=<utf-8> 

import rospy 
import roslib
import numpy
import json
import message_filters
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ModelStates

mpu9150_0_twist = []
mpu9150_1_twist = []
mpu9150_2_twist = []
mpu9150_3_twist = []
mpu9150_4_twist = []
mpu9150_5_twist = []
mpu9150_6_twist = []
mpu9150_7_twist = []
mpu9150_8_twist = []
mpu9150_9_twist = []
mpu9150_10_twist = []
mpu9150_11_twist = []
mpu9150_12_twist = []
mpu9150_13_twist = []
mpu9150_14_twist = []
mpu9150_15_twist = []

counter = 1080000 # 24*60*60*1000/10   100HZ about 6hours

last = 0


def ts9150_callback(mpu9150_0, mpu9150_1,mpu9150_2,mpu9150_3,mpu9150_4,mpu9150_5,mpu9150_6,mpu9150_7,mpu9150_8,mpu9150_9,mpu9150_10,mpu9150_11,mpu9150_12,mpu9150_13,mpu9150_14,mpu9150_15):
    rospy.loginfo("ts3 success!")
    global last, counter
    # if mpu9150_0.header.stamp.nsecs - last != 10000000:
    #     print "3", mpu9150_0.header.stamp.nsecs - last
    # last = mpu9150_0.header.stamp.nsecs
    if counter % 1000 == 0
        print counter

    mpu9150_0_twist.append([mpu9150_0.header.stamp.secs,mpu9150_0.header.stamp.nsecs,mpu9150_0.angular_velocity.x,mpu9150_0.angular_velocity.y,mpu9150_0.angular_velocity.z,mpu9150_0.linear_acceleration.x,mpu9150_0.linear_acceleration.y,mpu9150_0.linear_acceleration.z])
    mpu9150_1_twist.append([mpu9150_1.header.stamp.secs,mpu9150_1.header.stamp.nsecs,mpu9150_1.angular_velocity.x,mpu9150_1.angular_velocity.y,mpu9150_1.angular_velocity.z,mpu9150_1.linear_acceleration.x,mpu9150_1.linear_acceleration.y,mpu9150_1.linear_acceleration.z])
    mpu9150_2_twist.append([mpu9150_2.header.stamp.secs,mpu9150_2.header.stamp.nsecs,mpu9150_2.angular_velocity.x,mpu9150_2.angular_velocity.y,mpu9150_2.angular_velocity.z,mpu9150_2.linear_acceleration.x,mpu9150_2.linear_acceleration.y,mpu9150_2.linear_acceleration.z])
    mpu9150_3_twist.append([mpu9150_3.header.stamp.secs,mpu9150_3.header.stamp.nsecs,mpu9150_3.angular_velocity.x,mpu9150_3.angular_velocity.y,mpu9150_3.angular_velocity.z,mpu9150_3.linear_acceleration.x,mpu9150_3.linear_acceleration.y,mpu9150_3.linear_acceleration.z])
    mpu9150_4_twist.append([mpu9150_4.header.stamp.secs,mpu9150_4.header.stamp.nsecs,mpu9150_4.angular_velocity.x,mpu9150_4.angular_velocity.y,mpu9150_4.angular_velocity.z,mpu9150_4.linear_acceleration.x,mpu9150_4.linear_acceleration.y,mpu9150_4.linear_acceleration.z])
    mpu9150_5_twist.append([mpu9150_5.header.stamp.secs,mpu9150_5.header.stamp.nsecs,mpu9150_5.angular_velocity.x,mpu9150_5.angular_velocity.y,mpu9150_5.angular_velocity.z,mpu9150_5.linear_acceleration.x,mpu9150_5.linear_acceleration.y,mpu9150_5.linear_acceleration.z])
    mpu9150_6_twist.append([mpu9150_6.header.stamp.secs,mpu9150_6.header.stamp.nsecs,mpu9150_6.angular_velocity.x,mpu9150_6.angular_velocity.y,mpu9150_6.angular_velocity.z,mpu9150_6.linear_acceleration.x,mpu9150_6.linear_acceleration.y,mpu9150_6.linear_acceleration.z])
    mpu9150_7_twist.append([mpu9150_7.header.stamp.secs,mpu9150_7.header.stamp.nsecs,mpu9150_7.angular_velocity.x,mpu9150_7.angular_velocity.y,mpu9150_7.angular_velocity.z,mpu9150_7.linear_acceleration.x,mpu9150_7.linear_acceleration.y,mpu9150_7.linear_acceleration.z])
    mpu9150_8_twist.append([mpu9150_8.header.stamp.secs,mpu9150_8.header.stamp.nsecs,mpu9150_8.angular_velocity.x,mpu9150_8.angular_velocity.y,mpu9150_8.angular_velocity.z,mpu9150_8.linear_acceleration.x,mpu9150_8.linear_acceleration.y,mpu9150_8.linear_acceleration.z])
    mpu9150_9_twist.append([mpu9150_9.header.stamp.secs,mpu9150_9.header.stamp.nsecs,mpu9150_9.angular_velocity.x,mpu9150_9.angular_velocity.y,mpu9150_9.angular_velocity.z,mpu9150_9.linear_acceleration.x,mpu9150_9.linear_acceleration.y,mpu9150_9.linear_acceleration.z])
    mpu9150_10_twist.append([mpu9150_10.header.stamp.secs,mpu9150_10.header.stamp.nsecs,mpu9150_10.angular_velocity.x,mpu9150_10.angular_velocity.y,mpu9150_10.angular_velocity.z,mpu9150_10.linear_acceleration.x,mpu9150_10.linear_acceleration.y,mpu9150_10.linear_acceleration.z])
    mpu9150_11_twist.append([mpu9150_11.header.stamp.secs,mpu9150_11.header.stamp.nsecs,mpu9150_11.angular_velocity.x,mpu9150_11.angular_velocity.y,mpu9150_11.angular_velocity.z,mpu9150_11.linear_acceleration.x,mpu9150_11.linear_acceleration.y,mpu9150_11.linear_acceleration.z])
    mpu9150_12_twist.append([mpu9150_12.header.stamp.secs,mpu9150_12.header.stamp.nsecs,mpu9150_12.angular_velocity.x,mpu9150_12.angular_velocity.y,mpu9150_12.angular_velocity.z,mpu9150_12.linear_acceleration.x,mpu9150_12.linear_acceleration.y,mpu9150_12.linear_acceleration.z])
    mpu9150_13_twist.append([mpu9150_13.header.stamp.secs,mpu9150_13.header.stamp.nsecs,mpu9150_13.angular_velocity.x,mpu9150_13.angular_velocity.y,mpu9150_13.angular_velocity.z,mpu9150_13.linear_acceleration.x,mpu9150_13.linear_acceleration.y,mpu9150_13.linear_acceleration.z])
    mpu9150_14_twist.append([mpu9150_14.header.stamp.secs,mpu9150_14.header.stamp.nsecs,mpu9150_14.angular_velocity.x,mpu9150_14.angular_velocity.y,mpu9150_14.angular_velocity.z,mpu9150_14.linear_acceleration.x,mpu9150_14.linear_acceleration.y,mpu9150_14.linear_acceleration.z])
    mpu9150_15_twist.append([mpu9150_15.header.stamp.secs,mpu9150_15.header.stamp.nsecs,mpu9150_15.angular_velocity.x,mpu9150_15.angular_velocity.y,mpu9150_15.angular_velocity.z,mpu9150_15.linear_acceleration.x,mpu9150_15.linear_acceleration.y,mpu9150_15.linear_acceleration.z])

    if counter == 0:
        json.dump(mpu9150_0_twist, open('./data/mpu9150_0_twist.txt','w'))
        json.dump(mpu9150_1_twist, open('./data/mpu9150_1_twist.txt','w'))
        json.dump(mpu9150_2_twist, open('./data/mpu9150_2_twist.txt','w'))
        json.dump(mpu9150_3_twist, open('./data/mpu9150_3_twist.txt','w')) 
        json.dump(mpu9150_4_twist, open('./data/mpu9150_4_twist.txt','w'))
        json.dump(mpu9150_5_twist, open('./data/mpu9150_5_twist.txt','w'))
        json.dump(mpu9150_6_twist, open('./data/mpu9150_6_twist.txt','w'))
        json.dump(mpu9150_7_twist, open('./data/mpu9150_7_twist.txt','w'))
        json.dump(mpu9150_8_twist, open('./data/mpu9150_8_twist.txt','w'))
        json.dump(mpu9150_9_twist, open('./data/mpu9150_9_twist.txt','w'))
        json.dump(mpu9150_10_twist, open('./data/mpu9150_10_twist.txt','w'))
        json.dump(mpu9150_11_twist, open('./data/mpu9150_11_twist.txt','w'))
        json.dump(mpu9150_12_twist, open('./data/mpu9150_12_twist.txt','w'))
        json.dump(mpu9150_13_twist, open('./data/mpu9150_13_twist.txt','w'))
        json.dump(mpu9150_14_twist, open('./data/mpu9150_14_twist.txt','w'))
        json.dump(mpu9150_15_twist, open('./data/mpu9150_15_twist.txt','w'))
    counter = counter -1


rospy.init_node('9150')

mpu9150_0_sub = message_filters.Subscriber('mpu9150_0', Imu)
mpu9150_1_sub = message_filters.Subscriber('mpu9150_1', Imu)
mpu9150_2_sub = message_filters.Subscriber('mpu9150_2', Imu)
mpu9150_3_sub = message_filters.Subscriber('mpu9150_3', Imu)
mpu9150_4_sub = message_filters.Subscriber('mpu9150_4', Imu)
mpu9150_5_sub = message_filters.Subscriber('mpu9150_5', Imu)
mpu9150_6_sub = message_filters.Subscriber('mpu9150_6', Imu)
mpu9150_7_sub = message_filters.Subscriber('mpu9150_7', Imu)
mpu9150_8_sub = message_filters.Subscriber('mpu9150_8', Imu)
mpu9150_9_sub = message_filters.Subscriber('mpu9150_9', Imu)
mpu9150_10_sub = message_filters.Subscriber('mpu9150_10', Imu)
mpu9150_11_sub = message_filters.Subscriber('mpu9150_11', Imu)
mpu9150_12_sub = message_filters.Subscriber('mpu9150_12', Imu)
mpu9150_13_sub = message_filters.Subscriber('mpu9150_13', Imu)
mpu9150_14_sub = message_filters.Subscriber('mpu9150_14', Imu)
mpu9150_15_sub = message_filters.Subscriber('mpu9150_15', Imu)

ts9150 = message_filters.TimeSynchronizer([mpu9150_0_sub, mpu9150_1_sub,mpu9150_2_sub,mpu9150_3_sub,mpu9150_4_sub,mpu9150_5_sub,mpu9150_6_sub,mpu9150_7_sub,mpu9150_8_sub,mpu9150_9_sub,mpu9150_10_sub,mpu9150_11_sub,mpu9150_12_sub,mpu9150_13_sub,mpu9150_14_sub,mpu9150_15_sub], 10)
ts9150.registerCallback(ts9150_callback)

rospy.spin()

