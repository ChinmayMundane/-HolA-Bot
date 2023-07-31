# Holonomic Bot


# Table of contents
- [About the Project](#about-the-project)
  - [Tech Stack](#tech-stack)
- [Task 0](#task-0)
-  [Task 1](#task1)
-  [Task 2](#task-2)
-  [Simulation Result](#simulation-result)


# About the Project

**In this project, aim was to build a bot for deployment in an arena which is an abstraction of different settings in a Smart City.** To enable the robot to do more complex motion, there was a need to explore an exciting type of mobile locomotion, known as Holonomic Drive. Unlike the usual, more popular differential drive robots, **the holonomic drive robots can control all the three degrees of freedom possible on a plane** (translation along the x, y-axis and rotation along the z-axis). This gives the robot the ability to make art that would otherwise not be possible with the usual two-wheeled differential drive robot.
This was done on simulation and was simplified into 3 parts (or tasks)

## Tech Stack

- Python
- ros
- open cv

# Task 0

## Problem Statement

To get more familiar with ros, this proved to be immensely fruitful. The objective of the task was to move the turtle inside the turtlesim window in a vertical D shape of radius 1 unit.

## Approach

Initially making it(turtle) rotate circularly, with only velocities to control was the main idea but what worked was to use linear velocity as well as angular velocity with some combination to get this done.

## Result 



# Task 1 

## Problem Statement

The objective of this task was:

* **To explore and understand Gazebo-ROS, URDF.**
The script for urdf was given, the task was to add some missing part in the urdf to spawn the robot sucessfully

* **Implement some simple controller on a holonomic drive robot (for ex: 3 P controllers).**
In this step,task was creating a controller rospy node that will make the robot automatically go to desired goal pose (pose, refers to the position AND orientation of the robot).


## Approach
To localize, we need to know the exact position of the bot. For this purpose, We’ll need a callback function for subscribing to /odom so this was created first. This function will be automatically called everytime to update the pose of the robot (whenever there is an update in the /odom topic). From this we got z, y and theta of the bot.

However this are the vehicle or chassis (to be precise) velocities and not the velocity in global frame. hence for control loop :

* Find error (in x, y and theta) in global frame
:point_right: the /odom topic is giving present pose of the robot in global frame
:point_right: the desired pose is declared above and defined already in global frame therefore calculate error in global frame

* Calculate error in body frame
:point_right: Controller outputs robot velocity in robot_body frame,i.e. velocity are define is in x, y of the robot frame and the direction of z axis says the same in global and body frame therefore the errors will have to be calculated in body frame.

* Finally implement P controllers
to react to the error in robot_body frame
with velocities in x, y and theta in robot_body frame: [v_x, v_y, w]


Note : THis code was modified to handle a sequence of desired poses and goal poses sent by auto-evaluator script of eyantra IIT bombay.

# Task 2

## Problem Statement

This task was the repetition of task 1 but ...
* more realistic localisation:
    * specifically: using Overhead camera and Aruco Marker instead of simulator transforms
* more realistic model of the holonomic drive.
    * specifically: three omni wheel robot with input (v1, v2, v3) for three wheel velocities instead of any generic holonomic drive robot with inputs (Vx, Vy, W)


## Approach

### Part A: Localisation with OpenCV and Aruco Markers
Instead of using odom sensor to get the position of the bot, overhead camera was used to detect the aruco marker and then estimating the bot's position by calculating its centre.

### Part B: Inverse Kinematics
Same as task 1 , the difference is:
* pose is given in pixels and radians (instead of meters and radians) by subscribing to the *detected_aruco topic (NOTE: feedback python file publishes to this topic)
* one Matrix Multiplication was implemented for inverse kinematics i.e. find three omni-wheel velocities (v1, v2, v3) given velocity of the chassis (Vx, Vy, W) 


## Simulation Result


