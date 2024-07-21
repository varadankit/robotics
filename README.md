# Project 3 – Program the Real Robot!

## Introduction

This project involves programming a real robot using ROS Melodic and Python 2 to navigate from point A to point B. The robot will turn 45 degrees counterclockwise and then move forward for 2 meters before stopping.

Main code can be found in **project3.py**.

## Steps to Run the Project

1. **SSH into the Robot:**
   Establish a connection with the robot using SSH.
   Connect to the robot's wifi network.

   ```sh
   ssh jetauto@192.168.145.1
   ```
   
3. **Transfer Files to the Robot:**

  Use the scp command to move the necessary files to the robot's directory.

  ```sh
  scp project3.py jetauto@192.168.145.1:~/jetauto_ws/src/jetauto_example/scripts
  ```

3. **Run the ROS Node:**

Navigate to the appropriate directory and run the ROS node.

  ```sh
  cd ~/jetauto_ws/src/jetauto_example/scripts
  rosrun jetauto_ws project3.py
  ```
