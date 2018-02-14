#!/home/eboss/anaconda3/envs/py27/bin/python

# coding=<utf-8> 

import rospy 
import roslib
import numpy
import message_filters
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ModelStates


gazebo_x = gazebo_y = gazebo_z = 0
gazebo_roll = gazebo_pitch = gazebo_yaw = 0
gazebo_qx = gazebo_qy = gazebo_qz = gazebo_qw = 0

last = 0
last1 = 0
last2 = 0
last3 = 0

# def ts_callback(
# mpu6050_0, mpu6050_1,mpu6050_2,mpu6050_3,mpu6050_4,mpu6050_5,mpu6050_6,mpu6050_7,mpu6050_8,mpu6050_9,mpu6050_10,mpu6050_11,mpu6050_12,mpu6050_13,mpu6050_14,mpu6050_15,
# mpu6500_0, mpu6500_1,mpu6500_2,mpu6500_3,mpu6500_4,mpu6500_5,mpu6500_6,mpu6500_7,mpu6500_8,mpu6500_9,mpu6500_10,mpu6500_11,mpu6500_12,mpu6500_13,mpu6500_14,mpu6500_15,
# mpu9150_0, mpu9150_1,mpu9150_2,mpu9150_3,mpu9150_4,mpu9150_5,mpu9150_6,mpu9150_7,mpu9150_8,mpu9150_9,mpu9150_10,mpu9150_11,mpu9150_12,mpu9150_13,mpu9150_14,mpu9150_15,
# mpu9250_0, mpu9250_1,mpu9250_2,mpu9250_3,mpu9250_4,mpu9250_5,mpu9250_6,mpu9250_7,mpu9250_8,mpu9250_9,mpu9250_10,mpu9250_11,mpu9250_12,mpu9250_13,mpu9250_14,mpu9250_15):
#     rospy.loginfo("ts1 success!")
#     global last
#     if mpu6050_0.header.stamp.nsecs - last != 10000000:
#         print mpu6050_0.header.stamp.nsecs - last
#     last = mpu6050_0.header.stamp.nsecs
def ts6050_callback(mpu6050_0, mpu6050_1,mpu6050_2,mpu6050_3,mpu6050_4,mpu6050_5,mpu6050_6,mpu6050_7,mpu6050_8,mpu6050_9,mpu6050_10,mpu6050_11,mpu6050_12,mpu6050_13,mpu6050_14,mpu6050_15):
    rospy.loginfo("ts1 success!")
    global last
    if mpu6050_0.header.stamp.nsecs - last != 10000000:
        print "1", mpu6050_0.header.stamp.nsecs - last
    last = mpu6050_0.header.stamp.nsecs

def ts6500_callback(mpu6500_0, mpu6500_1,mpu6500_2,mpu6500_3,mpu6500_4,mpu6500_5,mpu6500_6,mpu6500_7,mpu6500_8,mpu6500_9,mpu6500_10,mpu6500_11,mpu6500_12,mpu6500_13,mpu6500_14,mpu6500_15):
    rospy.loginfo("ts2 success!")
    global last1
    if mpu6500_0.header.stamp.nsecs - last1 != 10000000:
        print "2", mpu6500_0.header.stamp.nsecs - last1
    last1 = mpu6500_0.header.stamp.nsecs

def ts9150_callback(mpu9150_0, mpu9150_1,mpu9150_2,mpu9150_3,mpu9150_4,mpu9150_5,mpu9150_6,mpu9150_7,mpu9150_8,mpu9150_9,mpu9150_10,mpu9150_11,mpu9150_12,mpu9150_13,mpu9150_14,mpu9150_15):
    rospy.loginfo("ts3 success!")
    global last2
    if mpu9150_0.header.stamp.nsecs - last2 != 10000000:
        print "3", mpu9150_0.header.stamp.nsecs - last2
    last2 = mpu9150_0.header.stamp.nsecs

def ts9250_callback(mpu9250_0, mpu9250_1,mpu9250_2,mpu9250_3,mpu9250_4,mpu9250_5,mpu9250_6,mpu9250_7,mpu9250_8,mpu9250_9,mpu9250_10,mpu9250_11,mpu9250_12,mpu9250_13,mpu9250_14,mpu9250_15):
    rospy.loginfo("ts4 success!")
    global last3
    if mpu9250_0.header.stamp.nsecs - last3 != 10000000:
        print "4", mpu9250_0.header.stamp.nsecs - last3
    last3 = mpu9250_0.header.stamp.nsecs


def callback_gazebo(gazebo):
    global gazebo_x, gazebo_y, gazebo_z, gazebo_qx, gazebo_qy, gazebo_qz, gazebo_qw

    gazebo_x = gazebo.pose[1].position.x
    gazebo_y = gazebo.pose[1].position.y
    gazebo_z = gazebo.pose[1].position.z

    gazebo_qx = gazebo.pose[1].orientation.x
    gazebo_qy = gazebo.pose[1].orientation.y
    gazebo_qz = gazebo.pose[1].orientation.z
    gazebo_qw = gazebo.pose[1].orientation.w


    #rospy.loginfo("I heard Gazebo")

    # print roll,pitch,yaw


rospy.init_node('data_process')

mpu6050_0_sub = message_filters.Subscriber('mpu6050_0', Imu)
mpu6050_1_sub = message_filters.Subscriber('mpu6050_1', Imu)
mpu6050_2_sub = message_filters.Subscriber('mpu6050_2', Imu)
mpu6050_3_sub = message_filters.Subscriber('mpu6050_3', Imu)
mpu6050_4_sub = message_filters.Subscriber('mpu6050_4', Imu)
mpu6050_5_sub = message_filters.Subscriber('mpu6050_5', Imu)
mpu6050_6_sub = message_filters.Subscriber('mpu6050_6', Imu)
mpu6050_7_sub = message_filters.Subscriber('mpu6050_7', Imu)
mpu6050_8_sub = message_filters.Subscriber('mpu6050_8', Imu)
mpu6050_9_sub = message_filters.Subscriber('mpu6050_9', Imu)
mpu6050_10_sub = message_filters.Subscriber('mpu6050_10', Imu)
mpu6050_11_sub = message_filters.Subscriber('mpu6050_11', Imu)
mpu6050_12_sub = message_filters.Subscriber('mpu6050_12', Imu)
mpu6050_13_sub = message_filters.Subscriber('mpu6050_13', Imu)
mpu6050_14_sub = message_filters.Subscriber('mpu6050_14', Imu)
mpu6050_15_sub = message_filters.Subscriber('mpu6050_15', Imu)

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

mpu9250_0_sub = message_filters.Subscriber('mpu9250_0', Imu)
mpu9250_1_sub = message_filters.Subscriber('mpu9250_1', Imu)
mpu9250_2_sub = message_filters.Subscriber('mpu9250_2', Imu)
mpu9250_3_sub = message_filters.Subscriber('mpu9250_3', Imu)
mpu9250_4_sub = message_filters.Subscriber('mpu9250_4', Imu)
mpu9250_5_sub = message_filters.Subscriber('mpu9250_5', Imu)
mpu9250_6_sub = message_filters.Subscriber('mpu9250_6', Imu)
mpu9250_7_sub = message_filters.Subscriber('mpu9250_7', Imu)
mpu9250_8_sub = message_filters.Subscriber('mpu9250_8', Imu)
mpu9250_9_sub = message_filters.Subscriber('mpu9250_9', Imu)
mpu9250_10_sub = message_filters.Subscriber('mpu9250_10', Imu)
mpu9250_11_sub = message_filters.Subscriber('mpu9250_11', Imu)
mpu9250_12_sub = message_filters.Subscriber('mpu9250_12', Imu)
mpu9250_13_sub = message_filters.Subscriber('mpu9250_13', Imu)
mpu9250_14_sub = message_filters.Subscriber('mpu9250_14', Imu)
mpu9250_15_sub = message_filters.Subscriber('mpu9250_15', Imu)

# ts = message_filters.TimeSynchronizer([mpu6050_0_sub, mpu6050_1_sub,mpu6050_2_sub,mpu6050_3_sub,mpu6050_4_sub,mpu6050_5_sub,mpu6050_6_sub,mpu6050_7_sub,mpu6050_8_sub,mpu6050_9_sub,mpu6050_10_sub,mpu6050_11_sub,mpu6050_12_sub,mpu6050_13_sub,mpu6050_14_sub,mpu6050_15_sub,
# mpu6500_0_sub, mpu6500_1_sub,mpu6500_2_sub,mpu6500_3_sub,mpu6500_4_sub,mpu6500_5_sub,mpu6500_6_sub,mpu6500_7_sub,mpu6500_8_sub,mpu6500_9_sub,mpu6500_10_sub,mpu6500_11_sub,mpu6500_12_sub,mpu6500_13_sub,mpu6500_14_sub,mpu6500_15_sub,
# mpu9150_0_sub, mpu9150_1_sub,mpu9150_2_sub,mpu9150_3_sub,mpu9150_4_sub,mpu9150_5_sub,mpu9150_6_sub,mpu9150_7_sub,mpu9150_8_sub,mpu9150_9_sub,mpu9150_10_sub,mpu9150_11_sub,mpu9150_12_sub,mpu9150_13_sub,mpu9150_14_sub,mpu9150_15_sub,
# mpu9250_0_sub, mpu9250_1_sub,mpu9250_2_sub,mpu9250_3_sub,mpu9250_4_sub,mpu9250_5_sub,mpu9250_6_sub,mpu9250_7_sub,mpu9250_8_sub,mpu9250_9_sub,mpu9250_10_sub,mpu9250_11_sub,mpu9250_12_sub,mpu9250_13_sub,mpu9250_14_sub,mpu9250_15_sub], 1)
# ts.registerCallback(ts_callback)

ts6050 = message_filters.TimeSynchronizer([mpu6050_0_sub, mpu6050_1_sub,mpu6050_2_sub,mpu6050_3_sub,mpu6050_4_sub,mpu6050_5_sub,mpu6050_6_sub,mpu6050_7_sub,mpu6050_8_sub,mpu6050_9_sub,mpu6050_10_sub,mpu6050_11_sub,mpu6050_12_sub,mpu6050_13_sub,mpu6050_14_sub,mpu6050_15_sub],1)
ts6050.registerCallback(ts6050_callback)

ts6500 = message_filters.TimeSynchronizer([mpu6500_0_sub, mpu6500_1_sub,mpu6500_2_sub,mpu6500_3_sub,mpu6500_4_sub,mpu6500_5_sub,mpu6500_6_sub,mpu6500_7_sub,mpu6500_8_sub,mpu6500_9_sub,mpu6500_10_sub,mpu6500_11_sub,mpu6500_12_sub,mpu6500_13_sub,mpu6500_14_sub,mpu6500_15_sub], 1)
ts6500.registerCallback(ts6500_callback)

ts9150 = message_filters.TimeSynchronizer([mpu9150_0_sub, mpu9150_1_sub,mpu9150_2_sub,mpu9150_3_sub,mpu9150_4_sub,mpu9150_5_sub,mpu9150_6_sub,mpu9150_7_sub,mpu9150_8_sub,mpu9150_9_sub,mpu9150_10_sub,mpu9150_11_sub,mpu9150_12_sub,mpu9150_13_sub,mpu9150_14_sub,mpu9150_15_sub], 1)
ts9150.registerCallback(ts9150_callback)

ts9250 = message_filters.TimeSynchronizer([mpu9250_0_sub, mpu9250_1_sub,mpu9250_2_sub,mpu9250_3_sub,mpu9250_4_sub,mpu9250_5_sub,mpu9250_6_sub,mpu9250_7_sub,mpu9250_8_sub,mpu9250_9_sub,mpu9250_10_sub,mpu9250_11_sub,mpu9250_12_sub,mpu9250_13_sub,mpu9250_14_sub,mpu9250_15_sub], 1)
ts9250.registerCallback(ts9250_callback)



subogazebo = rospy.Subscriber('/gazebo/model_states', ModelStates, callback_gazebo)

rospy.spin()

