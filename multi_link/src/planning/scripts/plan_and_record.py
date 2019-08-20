#!/usr/bin/env python

# This script sets the initial and the goal states of the double pendulum,
# plan a path and write it out to yaml file.

# Author: Yanhao Zhu

import os, sys, rospy, moveit_commander, moveit_msgs.msg, yaml
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

if __name__ == "__main__":
    print ""
    print "----------------------------------------------------------"
    print "Welcome to Yanhao's MoveIt MoveGroup Python Interface Tutorial"
    print ""
    print "============ Press `Enter` to begin the tutorial by setting up the moveit_commander ..."
    raw_input()

    # The section below initialize the ros py node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_and_plan', anonymous=True)
    # Provides information such as the robot's kinematic model and the robot's current joint states
    robot = moveit_commander.RobotCommander()
    # This provides a remote interface for getting, setting, and updating the robot's internal understanding of the surrounding world:
    scene = moveit_commander.PlanningSceneInterface()
    # Getting the move group - We called it motor in moveit setup assistant
    move_group = moveit_commander.MoveGroupCommander("motor")

    # Print out some debugging info
    planning_frame = move_group.get_planning_frame()
    print "============ Planning frame: %s" % planning_frame
    group_names = robot.get_group_names()
    print "============ Available Planning Groups:", robot.get_group_names()
    print "============ Printing robot state"
    print robot.get_current_state()
    print ""

    print "============ Press `Enter` to set the target and plan a path"
    raw_input()

    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = pi/2
    my_plan = move_group.plan(joint_goal)
    move_group.execute(my_plan, wait=True)
    move_group.stop()

    file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'my_plan.yaml')
    with open(file_path, "w") as plan_file:
        yaml.dump(my_plan, plan_file, default_flow_style=True)