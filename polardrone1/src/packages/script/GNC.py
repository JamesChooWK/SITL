# -*- coding: utf-8 -*-
'''
Created on Monday 28.10.2019
Copyright (©) Choo Wai Keong
Author: Choo Wai Keong
Email: choo_wk_chonghua@hotmail.com
'''




import mavros
import rospy
import time
import numpy as np
from threading import Thread
from mavros_msgs.msg import Waypoint    # define waypoints
from sensor_msgs.msg import NavSatFix   # [lat,long,alt]
from mavros_msgs.msg import WaypointList # Waypoints
from mavros_msgs.srv import CommandHome # Return home
from mavros_msgs.srv import CommandBool # arming
from mavros_msgs.srv import SetMode     # setMode
from mavros_msgs.srv import WaypointPush # push Waypoint
from mavros_msgs.srv import WaypointClear # clear Waypoint
from mavros_msgs.srv import WaypointPull # Pull Waypoint
from std_msgs.msg import Float64



class UAV():
    def __init__ (self):
        self.counter =0

    def getPosition(self, data):
        self.position = [data.latitude, data.longitude, data.altitude] # [degree, degree, degree]
        # print(self.position[:])

    def getRelativeAltitude(self, data):
        self.relativeAltitude = [data] # [meter]
        # print(self.relativeAltitude[0])

    def setHomeLocation(self, data):
        self.homeLocation= data # [lat, long, alt]
        rospy.wait_for_service("mavros/cmd/set_home")
        try:
            lat, long, alt = self.homeLocation[0], self.homeLocation[1], self.homeLocation[2]
            setHomeRequest = rospy.ServiceProxy("mavros/cmd/set_home", CommandHome)
            setHomeResponse = setHomeRequest(current_gps = False, latitude=lat, longitude=long, altitude=alt)
            flag = setHomeResponse.success
            if flag == True:
                print('SUCCESS: Set Home Location')
            elif flag == False:
                print('FAILURE: Set Home Location')
        except rospy.ServiceException as e:
            rospy.loginfo("SetHomePosition failed: %s" %e)




class GNC(object):
    """docstring for GNC."""

    def __init__(self):
        super(GNC, self).__init__()
        self.counter = 0



    def setFlightMode(self,mode):
        print('Set Flight mode to %s \n', mode)
        rospy.wait_for_service("mavros/set_mode")
        try:
            setModeRequest = rospy.ServiceProxy("mavros/set_mode", SetMode)
            setModeResponse = setModeRequest(custom_mode=mode)
            setFlightMode_flag = setModeResponse.mode_sent
            if setFlightMode_flag == True:
                print('SUCCESS: %s \n',mode)
            elif setFlightMode_flag == False:
                print('FAILURE: %s \n',mode)
        except rospy.ServiceException as e:
            rospy.loginfo("setFlightMode failed: %s\n" %e)


    def setWayPoint(self, index, waypoints):
        print('Set WayPoints \n')
        rospy.wait_for_service("mavros/mission/push")
        try:
            pushWayPointRequest = rospy.ServiceProxy("mavros/mission/push", WaypointPush)
            pushWayPointResponse = pushWayPointRequest(start_index=index, waypoints=waypoints)
            pushWayPoint_flag = pushWayPointResponse.success
            if pushWayPoint_flag == True:
                print('SUCCESS: Pushing waypoints \n')
            elif pushWayPoint_flag == False:
                print('FAILURE: Pushing waypoints \n')
        except rospy.ServiceException as e:
            rospy.loginfo("setWayPoint failed: %s\n" %e)

    def arming(self):
        print('arming \n')
        rospy.wait_for_service("mavros/cmd/arming")
        try:
            armingRequest = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
            armingResponse = armingRequest(value = True)
            arm_flag = armingResponse.success
            if arm_flag == True:
                print('SUCCESS: Arming \n')
            elif arm_flag == False:
                print('FAILURE: Arming \n')
        except rospy.ServiceException as e:
            rospy.loginfo("SetHomePosition failed: %s \n" %e)


    def waypt(self):
        wplist = []
        wp = Waypoint()
        wp.frame = 3
        wp.command = 22
        wp.is_current = True
        wp.autocontinue = True
        wp.param1 = 0
        wp.param2 = 0
        wp.param3 = 0
        wp.param4 = float('nan')
        wp.x_lat = 2.909520
        wp.y_long = 101.655192
        wp.z_alt = 5
        wplist.append(wp)

        # Second Waypoint
        wp1 = Waypoint()
        wp1.frame = 3
        wp1.command = 16
        wp1.is_current = False
        wp1.autocontinue = True
        wp1.param1 = 0
        wp1.param2 = 0
        wp1.param3 = 0 # radius to consider passing through waypoint
        wp1.param4 = float('nan')
        wp1.x_lat = 2.909732
        wp1.y_long = 101.655451
        wp1.z_alt = 15
        wplist.append(wp1)

        # Third Waypoint
        wp2 = Waypoint()
        wp2.frame = 3
        wp2.command = 16
        wp2.is_current = False
        wp2.autocontinue = True
        wp2.param1 = 0
        wp2.param2 = 0
        wp2.param3 = 0
        wp2.param4 = float('nan')
        wp2.x_lat = 2.909395
        wp2.y_long = 101.655569
        wp2.z_alt = 12
        wplist.append(wp2)

        # Third Waypoint
        wp3 = Waypoint()
        wp3.frame = 3
        wp3.command = 16
        wp3.is_current = False
        wp3.autocontinue = True
        wp3.param1 = 0
        wp3.param2 = 0
        wp3.param3 = 0 # radius to consider passing through waypoint
        wp3.param4 = float('nan')
        wp3.x_lat = 2.908940
        wp3.y_long = 101.655744
        wp3.z_alt = 10
        wplist.append(wp3)

        # Fourth Waypoint
        wp4 = Waypoint()
        wp4.frame = 3
        wp4.command = 16
        wp4.is_current = False
        wp4.autocontinue = True
        wp4.param1 = 0
        wp4.param2 = 0
        wp4.param3 = 0 # radius to consider passing through waypoint
        wp4.param4 = float('nan')
        wp4.x_lat = 2.908913
        wp4.y_long = 101.655387
        wp4.z_alt = 5
        wplist.append(wp4)

        # Fifth Waypoint
        wp5 = Waypoint()
        wp5.frame = 3
        wp5.command = 22
        wp5.is_current = False
        wp5.autocontinue = True
        wp5.param1 = 0
        wp5.param2 = 0
        wp5.param3 = 0 # radius to consider passing through waypoint
        wp5.param4 = float('nan')
        wp5.x_lat = 2.909197
        wp5.y_long = 101.655167
        wp5.z_alt = 25
        wplist.append(wp5)
        print(wplist)
        self.setWayPoint(0, wplist)

    def clear_wayPoint(self):
        print('Clear Waypoint \n')
        rospy.wait_for_service("mavros/mission/clear")
        try:
            clear_wayPointRequest = rospy.ServiceProxy("mavros/mission/clear", WaypointClear)
            clear_wayPointRequest = clear_wayPointRequest()
            clear_wayPoint_flag = clear_wayPointRequest.success
            if clear_wayPoint_flag == True:
                print('SUCCESS: clear waypoints \n')
            elif clear_wayPoint_flag == False:
                print('FAILURE: clear waypoints \n')
        except rospy.ServiceException as e:
            rospy.loginfo("clear waypoints failed: %s\n" %e)


    def pull_wayPoint(self):
        print('Pull Waypoint\n')
        rospy.wait_for_service("mavros/mission/pull")
        try:
            pull_wayPointRequest = rospy.ServiceProxy("mavros/mission/pull", WaypointPull)
            pull_wayPointRequest = pull_wayPointRequest()
            pull_wayPoint_flag = pull_wayPointRequest.success
            # print(pull_wayPointRequest.wp_received[0])
            if pull_wayPoint_flag == True:
                print('SUCCESS: Pull waypoints \n')
            elif pull_wayPoint_flag == False:
                print('FAILURE: Pull waypoints \n')
        except rospy.ServiceException as e:
            rospy.loginfo("Pull waypoints failed: %s\n" %e)





class UAV_Node():
    uav = UAV()

    uav.setHomeLocation([2.909368, 101.655304, 47.15991831094613]) # Return to Home

    # Initiate this GNC Node
    rospy.init_node('GNC_Node', anonymous=True)
    rospy.loginfo('Initialised GNC Node')

    # Initiate subscription to the GPS location topic
    rospy.Subscriber("/mavros/global_position/global", NavSatFix, uav.getPosition)
    rospy.loginfo("Initialised Subscribing to mavros/global_position/global ")

    # Initiate Subscription to the relative altitude
    rospy.Subscriber("/mavros/global_position/rel_alt", Float64, uav.getRelativeAltitude)
    rospy.loginfo(" Initialised Subscribing to mavros/global_position/rel_alt ")




class GNC_Node():
    print("GNC_node initialising")
    gnc = GNC()
    gnc.clear_wayPoint()

    rospy.sleep(2)
    gnc.waypt()

    print("Arming")
    rospy.sleep(10)
    gnc.arming()

    rospy.sleep(2)
    gnc.setFlightMode('AUTO.MISSION')





if __name__ == '__main__':

    x = Thread(target = GNC, args=())
    x.start()
    x.join()
    # UAV_Node()
