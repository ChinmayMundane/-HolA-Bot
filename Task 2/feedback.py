#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (HB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:		[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:		feedback.py
# Functions:
#			[ Comma separated list of functions in this file ]
# Nodes:		Add your publishing and subscribing node


######################## IMPORT MODULES ##########################


import numpy				# If you find it required
import rospy 				
from sensor_msgs.msg import Image 	# Image is the message type for images in ROS
from cv_bridge import CvBridge	# Package to convert between ROS and OpenCV Images
import cv2				# OpenCV Library
import math				# If you find it required
from geometry_msgs.msg import Pose2D	# Required to publish ARUCO's detected position & orientation
from tf.transformations import euler_from_quaternion

############################ GLOBALS #############################

aruco_publisher = rospy.Publisher('detected_aruco', Pose2D, queue_size = 10)
aruco_msg = Pose2D()

##################### FUNCTION DEFINITIONS #######################

# NOTE :  You may define multiple helper functions here and use in your code

def callback(data):
	# Bridge is Used to Convert ROS Image message to OpenCV image
	br = CvBridge()
	rospy.loginfo("receiving camera frame")
	get_frame = br.imgmsg_to_cv2(data, "mono8")		# Receiving raw image in a "grayscale" format
	current_frame = cv2.resize(get_frame, (500, 500), interpolation = cv2.INTER_LINEAR)
	cv2.imshow("abc" , current_frame)
	cv2.waitKey(3)
	h = 500
	w = 500

	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Use OpenCV to find ARUCO MARKER from the IMAGE
	#	-> You are allowed to use any other library for ARUCO detection, 
	#        but the code should be strictly written by your team and
	#	   your code should take image & publish coordinates on the topics as specified only.  
	#	-> Use basic high-school geometry of "TRAPEZOIDAL SHAPES" to find accurate marker coordinates & orientation :)
	#	-> Observe the accuracy of aruco detection & handle every possible corner cases to get maximum scores !



	# first detecting the aruco marker and its corners
	arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
	arucoParams = cv2.aruco.DetectorParameters_create()
	corners, ids, rejected = cv2.aruco.detectMarkers(current_frame, arucoDict, parameters=arucoParams)
	# print(corners)
	
	# verify *at least* one ArUco marker was detected
	# flatten the ArUco IDs list
		#ids = ids.flatten()
	# loop over the detected ArUCo corners
	for markerCorner in corners:
		# extract the marker corners (which are always returned in
		# top-left, top-right, bottom-right, and bottom-left order)
		corners = markerCorner.reshape((4, 2))
		# print(corners)
		topLeft, topRight, bottomRight, bottomLeft = corners
		# convert each of the (x, y)-coordinate pairs to integers
		# topRight = (int(topRight[0]), int(topRight[1]))
		# bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
		# bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
		# topLeft = (int(topLeft[0]), int(topLeft[1]))


	# compute and draw the center (x, y)-coordinates of the ArUco marker
	cX = ((topLeft[0] + bottomRight[0]) / 2.0)
	cY = (( topLeft[1] + bottomRight[1]) / 2.0)
	# print(cX,cY)
	
	x2 = ((topLeft[0] + topRight[0]) / 2.0)
	y2 = ((topLeft[1] + topRight[1]) / 2.0)

	# aruco_marker_side_length = 5
	# mtx = numpy.array([[1171.5121418959693, 0.0, 640.5], [0.0, 1171.5121418959693, 640.5], [0.0, 0.0, 1.0]])
	# dst = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0])
	c_theta = math.atan2(cX-x2,cY-y2)
	print(c_theta*(180/math.pi))
	# rvecs, tvecs, obj_points= cv2.aruco.estimatePoseSingleMarkers(corners,15, numpy.array([[1171.5121418959693, 0.0, 640.5],[0.0, 1171.5121418959693, 640.5],[0.0, 0.0, 1.0]]),numpy.array([0.0, 0.0, 0.0, 0.0, 0.0]))
	# transform_translation_x = tvecs[0][0][0]
	# transform_translation_y = tvecs[0][0][1]
	# transform_translation_z = tvecs[0][0][2]
			
	aruco_msg.x = cX
	aruco_msg.y = cY
	aruco_msg.theta = c_theta

	aruco_publisher.publish(aruco_msg)
	print(cX,cY,c_theta)
	

	

	############################################
      
def main():
	rospy.init_node('aruco_feedback_node')  
	rospy.Subscriber('overhead_cam/image_raw', Image, callback)
	rospy.spin()
  
if __name__ == '__main__':
  main()
