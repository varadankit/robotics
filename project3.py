#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def turn_robot(velocity_publisher, angle, speed):
    # Create a Twist message
    vel_msg = Twist()

    # Set angular speed (in rad/s)
    angular_speed = speed * (math.pi / 180)  # converting from degrees to radians

    # Set the direction (positive for counterclockwise)
    vel_msg.angular.z = angular_speed

    # Set the rate to publish messages
    rate = rospy.Rate(10)  # 10 Hz

    # Calculate the time duration to turn the given angle
    duration = abs(angle / speed)

    # Record the start time
    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # Stop the rotation
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def move_robot(velocity_publisher, distance, speed):
    # Create a Twist message
    vel_msg = Twist()

    # Set linear speed (in m/s)
    vel_msg.linear.x = speed

    # Set the rate to publish messages
    rate = rospy.Rate(10)  # 10 Hz

    # Calculate the time duration to move the given distance
    duration = abs(distance / speed)

    # Record the start time
    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # Stop the movement
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def main():
    # Initialize the ROS node
    rospy.init_node('jetauto_velocity_controller', anonymous=True)

    # Create a publisher object to send messages to the /jetauto_controller/cmd_vel topic
    velocity_publisher = rospy.Publisher('/jetauto_controller/cmd_vel', Twist, queue_size=10)

    # Turn the robot 45 degrees counterclockwise
    turn_robot(velocity_publisher, angle=45, speed=45)  # angle in degrees, speed in degrees per second

    # Move the robot forward for 2 meters
    move_robot(velocity_publisher, distance=2, speed=0.5)  # distance in meters, speed in meters per second

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
