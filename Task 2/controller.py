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


################### IMPORT MODULES #######################

import rospy
import signal		# To handle Signals by OS/user
import sys		# To handle Signals by OS/user

from geometry_msgs.msg import Wrench		# Message type used for publishing force vectors
from geometry_msgs.msg import PoseArray	# Message type used for receiving goals
from geometry_msgs.msg import Pose2D		# Message type used for receiving feedback
import numpy as np
import time
import math		# If you find it useful

from tf.transformations import euler_from_quaternion	# Convert angles

################## GLOBAL VARIABLES ######################

PI = 3.14

x_goals = [249.5]
y_goals = [249.5]
theta_goals = [0]

right_wheel_pub = None
left_wheel_pub = None
front_wheel_pub = None

hola_x = 0
hola_y = 0
hola_theta = 0
hola_z = 0


##################### FUNCTION DEFINITIONS #######################

# NOTE :  You may define multiple helper functions here and use in your code

# def signal_handler(sig, frame):
	  
# 	# NOTE: This function is called when a program is terminated by "Ctr+C" i.e. SIGINT signal 	
# 	print('Clean-up !')
# 	cleanup()
# 	sys.exit(0)

# def cleanup():
	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Not mandatory - but it is recommended to do some cleanup over here,
	#	   to make sure that your logic and the robot model behaves predictably in the next run.

	############################################
  



def task2_goals_Cb(msg):
	global x_goals, y_goals, theta_goals
	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)

		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion(orientation_list)[2]
		theta_goals.append(theta_goal)

def aruco_feedback_Cb(msg):
	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Receive & store the feedback / coordinates found by aruco detection logic.
	#	-> This feedback plays the same role as the 'Odometry' did in the previous task.

	global hola_x, hola_y,hola_z, hola_theta

	# Write your code to take the msg and update the three variables
	hola_x = msg.x
	hola_y = msg.y
	hola_z = 0
	hola_theta = msg.theta
	
	# print("Hola X",hola_x)
	# print("Hola Y",hola_y)
	# print("Hola theta",hola_theta)

	############################################


# def inverse_kinematics():
	
	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Use the target velocity you calculated for the robot in previous task, and
	#	Process it further to find what proportions of that effort should be given to 3 individuals wheels !!
	#	Publish the calculated efforts to actuate robot by applying force vectors on provided topics
	############################################
	

	

	

	
	


def main():
	Kp_x = 2.80
	Kp_y = 2.80
	Kp_z = 0.95
	i=0
	d=1

	global x_goals, y_goals, theta_goals
	global hola_x, hola_y,hola_z, hola_theta

	rospy.init_node('controller_node')

	# signal.signal(signal.SIGINT, signal_handler)

	# NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	#	Use the below given topics to generate motion for the robot.
	right_wheel_pub = rospy.Publisher('/right_wheel_force', Wrench, queue_size=10)
	front_wheel_pub = rospy.Publisher('/front_wheel_force', Wrench, queue_size=10)
	left_wheel_pub = rospy.Publisher('/left_wheel_force', Wrench, queue_size=10)

	rospy.Subscriber('detected_aruco',Pose2D,aruco_feedback_Cb)
	rospy.Subscriber('task2_goals',PoseArray,task2_goals_Cb)
	vel = Wrench()
	vel2 = Wrench()
	vel3 = Wrench()
	rate = rospy.Rate(100)

	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Make use of the logic you have developed in previous task to go-to-goal.
	#	-> Extend your logic to handle the feedback that is in terms of pixels.
	#	-> Tune your controller accordingly.
	# 	-> In this task you have to further implement (Inverse Kinematics!)
	#      find three omni-wheel velocities (v1, v2, v3) = left/right/center_wheel_force (assumption to simplify)
	#      given velocity of the chassis (Vx, Vy, W)
	#	   

		
	while not rospy.is_shutdown():
		
		goal_z =0
		# Calculate Error from feedback
		goal_x = x_goals[i]
		l=len(x_goals)
		goal_y = y_goals[i]
		goal_w = theta_goals[i]
		e_x = goal_x - hola_x
		e_y = goal_y - hola_y
		e_z = goal_z - hola_z
		e_theta = goal_w - hola_theta
		error = np.array([e_x,e_y,e_z])
		print("ex ", e_x)
		print("ey ",e_y)
		print("e thet ", e_theta)

		if abs(e_x) <= 4 and abs(e_y) <= 4 and abs(e_theta) <= 0.1:
				# vel.force.x = 0
				# vel2.force.x = 0
				# vel3.force.x = 0
				print("Within error")
				print(x_goals)
				if i < l-1 :
					i=i+1
					print(i)
				
				rospy.sleep(1)

		# Change the frame by using Rotation Matrix (If you find it required)
		rot_mat = np.array([[math.cos(0)*math.cos(hola_theta),math.sin(hola_theta)*math.cos(0),-math.sin(0)],
							[math.sin(0)*math.sin(0)*math.cos(hola_theta)-math.cos(0)*math.sin(hola_theta),
							math.sin(0)*math.sin(0)*math.sin(hola_theta)+math.cos(0)*math.cos(hola_theta),
							math.sin(0)*math.cos(0)],
							[math.cos(0)*math.sin(0)*math.cos(hola_theta)+math.sin(0)*math.sin(hola_theta),
							math.cos(0)*math.sin(0)*math.sin(hola_theta)-math.sin(0)*math.cos(hola_theta),
							math.cos(0)*math.cos(0)]])
		final_error = np.dot(rot_mat , error.T)

		# print(final_error)
	
		

		# Calculate the required velocity of bot for the next iteration(s)
		v_x = Kp_x * final_error[0]
		v_y = Kp_y * final_error[1]
		# hola_theta=0
		v_z = Kp_z * e_theta
		
		# Find the required force vectors for individual wheels from it.(Inverse Kinematics)
		# rot_mat_2 = np.array([[-d,1,0],
		# 				[-d,-math.cos(math.radians(60)),-math.sin(math.radians(60))],
		# 				[-d,-math.cos(math.radians(60)),math.sin(math.radians(60))]])
		rot_mat_2 = np.array([[-d,1,0],
						[-d,-math.cos(math.radians(60)),-math.sin(math.radians(60))],
						[-d,-math.cos(math.radians(60)),math.sin(math.radians(60))]])

		orig_vel = np.array([v_z,v_x,v_y])
		print(orig_vel)

		final = np.dot(rot_mat_2 , orig_vel.T)


		# Apply appropriate force vectors
		vel.force.x = final[0]
		vel2.force.x = final[1]
		vel3.force.x = final[2]

		right_wheel_pub.publish(vel3)
		front_wheel_pub.publish(vel)
		left_wheel_pub.publish(vel2)

		# Modify the condition to Switch to Next goal (given position in pixels instead of meters)		
		

		rate.sleep()

    ############################################

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass

