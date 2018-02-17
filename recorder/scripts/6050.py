#!/home/eboss/anaconda3/envs/py27/bin/python

# coding=<utf-8> 

import rospy 
import roslib
import numpy
import json
import message_filters
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ModelStates


mpu6050_0_twist = []
mpu6050_1_twist = []
mpu6050_2_twist = []
mpu6050_3_twist = []
mpu6050_4_twist = []
mpu6050_5_twist = []
mpu6050_6_twist = []
mpu6050_7_twist = []
mpu6050_8_twist = []
mpu6050_9_twist = []
mpu6050_10_twist = []
mpu6050_11_twist = []
mpu6050_12_twist = []
mpu6050_13_twist = []
mpu6050_14_twist = []
mpu6050_15_twist = []

gazebo = []
gazebo_x = gazebo_y = gazebo_z = 0
gazebo_qx = gazebo_qy = gazebo_qz = gazebo_qw = 0

counter = 1080000 # 24*60*60*1000/10   100HZ about 6hours

last = 0


def ts6050_callback(mpu6050_0, mpu6050_1,mpu6050_2,mpu6050_3,mpu6050_4,mpu6050_5,mpu6050_6,mpu6050_7,mpu6050_8,mpu6050_9,mpu6050_10,mpu6050_11,mpu6050_12,mpu6050_13,mpu6050_14,mpu6050_15):
    #rospy.loginfo("ts1 success!")
    global last, counter, gazebo_x, gazebo_y, gazebo_z, gazebo_qx, gazebo_qy, gazebo_qz, gazebo_qw
    # if mpu6050_0.header.stamp.nsecs - last != 10000000:
    #     print "1", mpu6050_0.header.stamp.nsecs - last
    # last = mpu6050_0.header.stamp.nsecs
    if counter % 1000 == 0
        print 'mpu6050 counter left:',counter
    if counter >= 0:
        gazebo.append([mpu6050_0.header.stamp.secs,mpu6050_0.header.stamp.nsecs,gazebo_x,gazebo_y,gazebo_z,gazebo_qx,gazebo_qy,gazebo_qz,gazebo_qw])
        mpu6050_0_twist.append([mpu6050_0.header.stamp.secs,mpu6050_0.header.stamp.nsecs,mpu6050_0.angular_velocity.x,mpu6050_0.angular_velocity.y,mpu6050_0.angular_velocity.z,mpu6050_0.linear_acceleration.x,mpu6050_0.linear_acceleration.y,mpu6050_0.linear_acceleration.z])
        mpu6050_1_twist.append([mpu6050_1.header.stamp.secs,mpu6050_1.header.stamp.nsecs,mpu6050_1.angular_velocity.x,mpu6050_1.angular_velocity.y,mpu6050_1.angular_velocity.z,mpu6050_1.linear_acceleration.x,mpu6050_1.linear_acceleration.y,mpu6050_1.linear_acceleration.z])
        mpu6050_2_twist.append([mpu6050_2.header.stamp.secs,mpu6050_2.header.stamp.nsecs,mpu6050_2.angular_velocity.x,mpu6050_2.angular_velocity.y,mpu6050_2.angular_velocity.z,mpu6050_2.linear_acceleration.x,mpu6050_2.linear_acceleration.y,mpu6050_2.linear_acceleration.z])
        mpu6050_3_twist.append([mpu6050_3.header.stamp.secs,mpu6050_3.header.stamp.nsecs,mpu6050_3.angular_velocity.x,mpu6050_3.angular_velocity.y,mpu6050_3.angular_velocity.z,mpu6050_3.linear_acceleration.x,mpu6050_3.linear_acceleration.y,mpu6050_3.linear_acceleration.z])
        mpu6050_4_twist.append([mpu6050_4.header.stamp.secs,mpu6050_4.header.stamp.nsecs,mpu6050_4.angular_velocity.x,mpu6050_4.angular_velocity.y,mpu6050_4.angular_velocity.z,mpu6050_4.linear_acceleration.x,mpu6050_4.linear_acceleration.y,mpu6050_4.linear_acceleration.z])
        mpu6050_5_twist.append([mpu6050_5.header.stamp.secs,mpu6050_5.header.stamp.nsecs,mpu6050_5.angular_velocity.x,mpu6050_5.angular_velocity.y,mpu6050_5.angular_velocity.z,mpu6050_5.linear_acceleration.x,mpu6050_5.linear_acceleration.y,mpu6050_5.linear_acceleration.z])
        mpu6050_6_twist.append([mpu6050_6.header.stamp.secs,mpu6050_6.header.stamp.nsecs,mpu6050_6.angular_velocity.x,mpu6050_6.angular_velocity.y,mpu6050_6.angular_velocity.z,mpu6050_6.linear_acceleration.x,mpu6050_6.linear_acceleration.y,mpu6050_6.linear_acceleration.z])
        mpu6050_7_twist.append([mpu6050_7.header.stamp.secs,mpu6050_7.header.stamp.nsecs,mpu6050_7.angular_velocity.x,mpu6050_7.angular_velocity.y,mpu6050_7.angular_velocity.z,mpu6050_7.linear_acceleration.x,mpu6050_7.linear_acceleration.y,mpu6050_7.linear_acceleration.z])
        mpu6050_8_twist.append([mpu6050_8.header.stamp.secs,mpu6050_8.header.stamp.nsecs,mpu6050_8.angular_velocity.x,mpu6050_8.angular_velocity.y,mpu6050_8.angular_velocity.z,mpu6050_8.linear_acceleration.x,mpu6050_8.linear_acceleration.y,mpu6050_8.linear_acceleration.z])
        mpu6050_9_twist.append([mpu6050_9.header.stamp.secs,mpu6050_9.header.stamp.nsecs,mpu6050_9.angular_velocity.x,mpu6050_9.angular_velocity.y,mpu6050_9.angular_velocity.z,mpu6050_9.linear_acceleration.x,mpu6050_9.linear_acceleration.y,mpu6050_9.linear_acceleration.z])
        mpu6050_10_twist.append([mpu6050_10.header.stamp.secs,mpu6050_10.header.stamp.nsecs,mpu6050_10.angular_velocity.x,mpu6050_10.angular_velocity.y,mpu6050_10.angular_velocity.z,mpu6050_10.linear_acceleration.x,mpu6050_10.linear_acceleration.y,mpu6050_10.linear_acceleration.z])
        mpu6050_11_twist.append([mpu6050_11.header.stamp.secs,mpu6050_11.header.stamp.nsecs,mpu6050_11.angular_velocity.x,mpu6050_11.angular_velocity.y,mpu6050_11.angular_velocity.z,mpu6050_11.linear_acceleration.x,mpu6050_11.linear_acceleration.y,mpu6050_11.linear_acceleration.z])
        mpu6050_12_twist.append([mpu6050_12.header.stamp.secs,mpu6050_12.header.stamp.nsecs,mpu6050_12.angular_velocity.x,mpu6050_12.angular_velocity.y,mpu6050_12.angular_velocity.z,mpu6050_12.linear_acceleration.x,mpu6050_12.linear_acceleration.y,mpu6050_12.linear_acceleration.z])
        mpu6050_13_twist.append([mpu6050_13.header.stamp.secs,mpu6050_13.header.stamp.nsecs,mpu6050_13.angular_velocity.x,mpu6050_13.angular_velocity.y,mpu6050_13.angular_velocity.z,mpu6050_13.linear_acceleration.x,mpu6050_13.linear_acceleration.y,mpu6050_13.linear_acceleration.z])
        mpu6050_14_twist.append([mpu6050_14.header.stamp.secs,mpu6050_14.header.stamp.nsecs,mpu6050_14.angular_velocity.x,mpu6050_14.angular_velocity.y,mpu6050_14.angular_velocity.z,mpu6050_14.linear_acceleration.x,mpu6050_14.linear_acceleration.y,mpu6050_14.linear_acceleration.z])
        mpu6050_15_twist.append([mpu6050_15.header.stamp.secs,mpu6050_15.header.stamp.nsecs,mpu6050_15.angular_velocity.x,mpu6050_15.angular_velocity.y,mpu6050_15.angular_velocity.z,mpu6050_15.linear_acceleration.x,mpu6050_15.linear_acceleration.y,mpu6050_15.linear_acceleration.z])

    if counter == 0:
        json.dump(gazebo, open('./data/gazebo.txt','w'))
        json.dump(mpu6050_0_twist, open('./data/mpu6050_0_twist.txt','w'))
        json.dump(mpu6050_1_twist, open('./data/mpu6050_1_twist.txt','w'))
        json.dump(mpu6050_2_twist, open('./data/mpu6050_2_twist.txt','w'))
        json.dump(mpu6050_3_twist, open('./data/mpu6050_3_twist.txt','w')) 
        json.dump(mpu6050_4_twist, open('./data/mpu6050_4_twist.txt','w'))
        json.dump(mpu6050_5_twist, open('./data/mpu6050_5_twist.txt','w'))
        json.dump(mpu6050_6_twist, open('./data/mpu6050_6_twist.txt','w'))
        json.dump(mpu6050_7_twist, open('./data/mpu6050_7_twist.txt','w'))
        json.dump(mpu6050_8_twist, open('./data/mpu6050_8_twist.txt','w'))
        json.dump(mpu6050_9_twist, open('./data/mpu6050_9_twist.txt','w'))
        json.dump(mpu6050_10_twist, open('./data/mpu6050_10_twist.txt','w'))
        json.dump(mpu6050_11_twist, open('./data/mpu6050_11_twist.txt','w'))
        json.dump(mpu6050_12_twist, open('./data/mpu6050_12_twist.txt','w'))
        json.dump(mpu6050_13_twist, open('./data/mpu6050_13_twist.txt','w'))
        json.dump(mpu6050_14_twist, open('./data/mpu6050_14_twist.txt','w'))
        json.dump(mpu6050_15_twist, open('./data/mpu6050_15_twist.txt','w'))
    counter = counter -1

def callback_gazebo(gazebo):
    global gazebo_x, gazebo_y, gazebo_z, gazebo_qx, gazebo_qy, gazebo_qz, gazebo_qw

    gazebo_x = gazebo.pose[0].position.x
    gazebo_y = gazebo.pose[0].position.y
    gazebo_z = gazebo.pose[0].position.z

    gazebo_qx = gazebo.pose[0].orientation.x
    gazebo_qy = gazebo.pose[0].orientation.y
    gazebo_qz = gazebo.pose[0].orientation.z
    gazebo_qw = gazebo.pose[0].orientation.w


    #rospy.loginfo("I heard Gazebo")

    # print roll,pitch,yaw



rospy.init_node('mpu6050')



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



ts6050 = message_filters.TimeSynchronizer([mpu6050_0_sub, mpu6050_1_sub,mpu6050_2_sub,mpu6050_3_sub,mpu6050_4_sub,mpu6050_5_sub,mpu6050_6_sub,mpu6050_7_sub,mpu6050_8_sub,mpu6050_9_sub,mpu6050_10_sub,mpu6050_11_sub,mpu6050_12_sub,mpu6050_13_sub,mpu6050_14_sub,mpu6050_15_sub],10)
ts6050.registerCallback(ts6050_callback)


subogazebo = rospy.Subscriber('/gazebo/model_states', ModelStates, callback_gazebo)

rospy.spin()

