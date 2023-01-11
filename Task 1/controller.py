#!/usr/bin/env python3


import rospy
import numpy as np
# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Point,Twist,Quaternion
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray
# for finding sin() cos() 
import math

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from tf.transformations import euler_from_quaternion


hola_x = 0
hola_y = 0
hola_theta = 0
hola_z = 0
x_goals = [0]
y_goals = [0]
theta_goals = [0]

def task1_goals_Cb(msg):
	global x_goals, y_goals, theta_goals

	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)

		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion (orientation_list)[2]
		theta_goals.append(theta_goal)


def odometryCb(msg):
	global hola_x, hola_y,hola_z, hola_theta

	# Write your code to take the msg and update the three variables
	hola_x = msg.pose.pose.position.x
	hola_y = msg.pose.pose.position.y
	hola_z = msg.pose.pose.position.z

	print("Hola X = ",180*hola_x/3.14)
	print("Hola Y = ",180*hola_y/3.14)
	print("Hola Z = ",180*hola_z/3.14)
	print("Hola theta = ",180*hola_theta/3.14)
	rot_q = msg.pose.pose.orientation
	(roll, pitch, hola_theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
	


def main():
	global hola_x, hola_y,hola_z, hola_theta,x_goals,y_goals,theta_goals
	
	# Initialze Node
	# We'll leave this for you to figure out the syntax for 
	# initialising node named "controller"
	rospy.init_node('controller', anonymous=True)
	
	# Initialze Publisher and Subscriber
	# We'll leave this for you to figure out the syntax for
	# initialising publisher and subscriber of cmd_vel and odom respectively
	sub = rospy.Subscriber("/odom", Odometry, odometryCb)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('task1_goals', PoseArray, task1_goals_Cb)


	

	# Declare a Twist message
	vel = Twist()
	
	# Initialise the required variables to 0
	# <This is explained below>
	goal = Point ()
	goal.z = 0
	# x_goals = [1, -1, -1, 1, 0]
	# y_goals = [1, 1, -1, -1, 0]
	# theta_goals = [0.765, 2.295, -2.295, -0.765, 0]
	Kp_x = 1.7
	Kp_y = 1.7
	Kp_z = 3.92
	final = Quaternion ()
	# final.w = 1.53
	i=0
	


	
	# For maintaining control loop rate.
	rate = rospy.Rate(100)
	
	
	# Initialise variables that may be needed for the control loop
	# For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
	# and also Kp values for the P Controller
	


	while not rospy.is_shutdown():
			l=len(x_goals)

		# Find error (in x, y and theta) in global frame
		# the /odom topic is giving pose of the robot in global frame
		# the desired pose is declared above and defined by you in global frame
		# therefore calculate error in global frame
		
			goal.x = x_goals[i]
			goal.y = y_goals[i]
			final.w = theta_goals[i]
			e_x = goal.x - hola_x
			e_y = goal.y - hola_y
			e_z = goal.z - hola_z
			e_theta = final.w - hola_theta
			error = np.array([e_x,e_y,e_z])

			if abs(e_x) <= 0.01 and abs(e_y) <= 0.01 and abs(e_theta) <= 0.1170:
				#vel.angular.z = 0
				# vel.linear.x = 0
				# vel.linear.y = 0
				if i < l-1 :
					i=i+1
				
				rospy.sleep(1)


			# (Calculate error in body frame)
			# But for Controller outputs robot velocity in robot_body frame, 
			# i.e. velocity are define is in x, y of the robot frame, 
			# Notice: the direction of z axis says the same in global and body frame
			# therefore the errors will have have to be calculated in body frame.
			rot_mat = np.array([[math.cos(0)*math.cos(hola_theta),math.sin(hola_theta)*math.cos(0),-math.sin(0)],
								[math.sin(0)*math.sin(0)*math.cos(hola_theta)-math.cos(0)*math.sin(hola_theta),
								math.sin(0)*math.sin(0)*math.sin(hola_theta)+math.cos(0)*math.cos(hola_theta),
								math.sin(0)*math.cos(0)],
								[math.cos(0)*math.sin(0)*math.cos(hola_theta)+math.sin(0)*math.sin(hola_theta),
								math.cos(0)*math.sin(0)*math.sin(hola_theta)-math.sin(0)*math.cos(hola_theta),
								math.cos(0)*math.cos(0)]])
			final_error = np.dot(rot_mat , error.T)

			print(final_error)


			# This is probably the crux of Task 1, figure this out and rest should be fine.


			# Finally implement a P controller 
			# to react to the error with velocities in x, y and theta.
			vel.linear.x = Kp_x * final_error[0]
			vel.linear.y = Kp_y * final_error[1]
			vel.angular.z = Kp_z * e_theta

			# if abs(vel.linear.x) < 0.0095 and abs(vel.linear.y) < 0.0095 and abs(vel.angular.z) < 0.09:
			
				
			# Safety Check
			# make sure the velocities are within a range.
			# for now since we are in a simulator and we are not dealing with actual physical limits on the system
			# we may get away with skipping this step. But it will be very necessary in the long run.
			
			

			pub.publish(vel)
			rate.sleep()


if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
