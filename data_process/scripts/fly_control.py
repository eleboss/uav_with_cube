#!/home/eboss/anaconda3/envs/py27/bin/python


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


import rospy 
import roslib
import time
import numpy as np
from __future__ import division
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import PositionTarget, AttitudeTarget, State
from geometry_msgs.msg import TransformStamped, PoseStamped, Point, PointStamped, Vector3, Vector3Stamped, TwistStamped, QuaternionStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion

counter = 1440000 #50hz 8*60*60*50
count_np.cos = 0
r = 2

def callback_odom(pose):
    global count_np.cos, r

    set_position = Point()
    set_velocity = Vector3()

    set_velocity.x = 0
    set_velocity.y = output_y
    set_velocity.z = output_z
    if counter > 1400000:
        #do nothing
    if counter < 1400000 and counter > 1350000:
    # verticle hold still 
    set_position.x = 0
    set_position.y = 0
    set_position.z = 15
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    if counter < 1350000 and counter > 1150000:
    # np.cos xy fly 
    if theta // 360 == 0:
        r = r + 1
    if r == 10:
        r = 2
    theta = counter - 1150000
    set_position.x = r*np.sin(theta)
    set_position.y = r*np.cos(theta)
    set_position.z = 15
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    if counter < 1150000 and counter > 950000:
    # np.cos yz fly 
    if theta // 360 == 0:
        r = r + 1
    if r == 10:
        r = 2
    theta = counter - 950000
    set_position.x = 1
    set_position.y = r*np.sin(theta)
    set_position.z = r*np.cos(theta)
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    if counter < 950000 and counter > 750000:
    # np.cos xz fly 
    if theta // 360 == 0:
        r = r + 1
    if r == 10:
        r = 2
    theta = counter - 750000
    set_position.x = r*np.sin(theta)
    set_position.y = 1
    set_position.z = r*np.cos(theta)
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    if counter < 750000 and counter > 550000:
    # np.cos xyz fly 
    if theta // 360 == 0:
        r = r + 1
    if r == 10:
        r = 2
    theta = counter - 550000
    set_position.x = r*np.sin(theta)
    set_position.y = r*np.cos(theta)
    set_position.z = r*np.cos(theta)
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )
    
    if counter < 550000 and counter > 1:
    # random fly
    if counter % 500 == 0
        set_position.x = random.randint(0, 15)
        set_position.y = random.randint(0, 15)
        set_position.z = random.randint(5, 15)
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    if counter == 0:
    set_position.x = 1
    set_position.y = 1
    set_position.z = 1
    
    msg = PositionTarget(coordinate_frame=PositionTarget.FRAME_LOCAL_NED,
                             type_mask=PositionTarget.IGNORE_PX + PositionTarget.IGNORE_PY + PositionTarget.IGNORE_PZ +
                                       PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ +
                                       PositionTarget.IGNORE_YAW_RATE,
                             position=set_velocity, 
                             yaw = set_yaw )

    stamp = rospy.get_rostime()
    msg.header.stamp = stamp
    position_pub.publish(msg)
    counter = counter -1





    


rospy.init_node('fly_control')

subodom = rospy.Subscriber('/mavros/local_position/odom', Odometry, callback_odom)
position_pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=1)

rospy.spin()