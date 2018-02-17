#!/home/eleboss/anaconda3/envs/py27/bin/python


# Example of vel contorl and position control

    # msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
    #                          type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
    #                                    PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
    #                                    PositionTarget.IGNORE_YAW_RATE,
    #                          velocity=set_velocity, 
    #                          yaw = set_yaw )

    # msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
    #                          type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
    #                                    PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
    #                                    PositionTarget.IGNORE_YAW_RATE,
    #                          position=set_position, 
    #                          yaw = set_yaw )

from __future__ import division
import rospy 
import roslib
import time
import numpy as np
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import PositionTarget, AttitudeTarget, State
from geometry_msgs.msg import TransformStamped, PoseStamped, Point, PointStamped, Vector3, Vector3Stamped, TwistStamped, QuaternionStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion

counter = 500000 #50hz 8*60*60*50
r = 8
theta = 0
set_position = Point()
set_position.x = 0
set_position.y = 0
set_position.z = 0
set_yaw = 0
wn = 0.03
msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                            type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                    PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                    PositionTarget.IGNORE_YAW_RATE,
                            position=set_position, 
                            yaw = set_yaw )

def callback_odom(pose):
    global r, counter,theta,msg, set_position,set_yaw,wn
    
    print 'looping:', counter
    if counter < 480000 and counter > 450000:
    # verticle hold still
        
        set_position.x = 0
        set_position.y = 0
        set_position.z = 15
        set_yaw = 0
        print "  hold still fly 0 0 15" ,'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter < 450000 and counter > 370000:
    # np.cos xy fly 
        
        theta = (counter - 370000)*wn
        if (counter - 370000)%26666 == 0:
            wn = wn * 0.1
        if wn == 0.0003 and counter == (370000 + 1):
            wn = 0.03
        set_position.x = r*np.sin(theta)
        set_position.y = r*np.cos(theta)
        set_position.z = 15
        set_yaw  = 0
        print "xy cos fly ",'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z,'wn:',wn
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter < 370000 and counter > 290000:
    # np.cos yz fly 

        theta = (counter - 290000)*wn
        if (counter - 290000)%26666 == 0:
            wn = wn * 0.1
        if wn == 0.0003 and counter == (290000 + 1):
            wn = 0.03
        set_position.x = 1
        set_position.y = r*np.sin(theta)
        set_position.z = 5 + r*np.cos(theta)
        set_yaw = 0
        print "yz cos fly ",'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z,'wn:',wn
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter < 290000 and counter > 210000:
    # np.cos xz fly 
        if (counter - 210000)%26666 == 0:
            wn = wn * 0.1
        if wn == 0.0003 and counter == (210000 + 1):
            wn = 0.03
        theta = (counter - 210000)*wn
        set_position.x = r*np.sin(theta)
        set_position.y = 1
        set_position.z = 5 + r*np.cos(theta)
        set_yaw = 0
        print "xz cos fly ",'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z,'wn:',wn
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter < 210000 and counter > 130000:
    # np.cos xyz fly 
        if (counter - 130000)%26666 == 0:
            wn = wn * 0.1
        if wn == 0.0003 and counter == (130000 + 1):
            wn = 0.03
        theta = (counter - 130000)*wn
        set_position.x = r*np.sin(theta)
        set_position.y = r*np.cos(theta)
        set_position.z = 5 + r*np.cos(theta)
        set_yaw = r*np.cos(theta)
        print "xyz cos fly ",'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z,'wn:',wn
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter < 130000 and counter > 1:
    # random fly
        
        if counter % 200 == 0:
            set_position.x = np.random.randint(0, 15)
            set_position.y = np.random.randint(0, 15)
            set_position.z = np.random.randint(5, 15)
            set_yaw = 0
        print "random fly ",'X:',set_position.x,'Y:',set_position.y,'Z:',set_position.z
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                               PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    if counter == 0:
        print 'Flying test over hold still at 1 1 1'
        set_position.x = 1
        set_position.y = 1
        set_position.z = 1
        set_yaw = 0
        msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                                type_mask=PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ +
                                        PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                        PositionTarget.IGNORE_YAW_RATE,
                                position=set_position, 
                                yaw = set_yaw )
        stamp = rospy.get_rostime()
        msg.header.stamp = stamp
        position_pub.publish(msg)

    counter = counter -1





    


rospy.init_node('fly_control')

subodom = rospy.Subscriber('/mavros/local_position/odom', Odometry, callback_odom)
position_pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=1)

rospy.spin()
