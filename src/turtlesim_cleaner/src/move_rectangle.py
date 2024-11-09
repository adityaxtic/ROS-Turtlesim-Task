#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_straight(velocity_publisher, speed, duration):
    """Move the turtle straight for a specific duration."""
    vel_msg = Twist()
    vel_msg.linear.x = speed
    vel_msg.angular.z = 0.0
    
    # Publish the velocity message for the specified duration
    end_time = rospy.Time.now() + rospy.Duration(duration)
    while rospy.Time.now() < end_time:
        velocity_publisher.publish(vel_msg)
    
    # Stop the turtle after moving the specified distance
    vel_msg.linear.x = 0.0
    velocity_publisher.publish(vel_msg)

def turn_90_degrees(velocity_publisher, angular_speed, duration):
    """Rotate the turtle by 90 degrees using angular velocity."""
    vel_msg = Twist()
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = angular_speed

    # Publish the angular velocity message for the specified duration
    end_time = rospy.Time.now() + rospy.Duration(duration)
    while rospy.Time.now() < end_time:
        velocity_publisher.publish(vel_msg)

    # Stop the turtle after turning
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

def move_turtle_rectangle():
    rospy.init_node('move_turtle_rectangle_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Set parameters for speed and rectangle dimensions
    speed = 1.0               # Linear speed (m/s)
    angular_speed = 0.5       # Angular speed (rad/s)
    long_side_duration = 4.0  # Duration to travel the long side (seconds)
    short_side_duration = 2.0 # Duration to travel the short side (seconds)
    turn_duration = 1.57 / angular_speed  # Approximate duration for a 90-degree turn

    rospy.loginfo("Moving the turtle in a rectangle...")

    # Loop to move in a rectangle continuously
    while not rospy.is_shutdown():
        # Move along the long side
        move_straight(velocity_publisher, speed, long_side_duration)
        # Turn 90 degrees
        turn_90_degrees(velocity_publisher, angular_speed, turn_duration)
        
        # Move along the short side
        move_straight(velocity_publisher, speed, short_side_duration)
        # Turn 90 degrees
        turn_90_degrees(velocity_publisher, angular_speed, turn_duration)

if __name__ == '__main__':
    try:
        move_turtle_rectangle()
    except rospy.ROSInterruptException:
        pass

