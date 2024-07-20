# Project 3 – Program the Real Robot!

## Introduction

This project involves programming a real robot using ROS Melodic and Python 2 to navigate from point A to point B. The robot will turn 45 degrees counterclockwise and then move forward for 2 meters before stopping.

## Steps to Run the Project

1. **SSH into the Robot:**
   Establish a connection with the robot using SSH.

   ```sh
   ssh username@robot_ip_address
   ```
   
2. **Transfer Files to the Robot:**

  Use the scp command to move the necessary files to the robot's directory.

  ```sh
  scp project3.py username@robot_ip_address:~/jetauto_ws/src/jetauto_example/scripts
  ```

3. **Run the ROS Node:**

Navigate to the appropriate directory and run the ROS node.

  ```sh
  cd ~/jetauto_ws/src/jetauto_example/scripts
  rosrun jetauto_ws project3.py
  ```
