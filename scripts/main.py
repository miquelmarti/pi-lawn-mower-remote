# -*- coding: utf-8 -*-
"""
@author: miquelmr
"""

import rospy
import numpy as np
import time
import os

from geometry_msgs.msg import Twist

import remoteGPIO as rm

class RosView():
	cmd_bindings = {'q':np.array([1,1]),
                  'w':np.array([1,0]),
                  'e':np.array([1,-1]),
                  'a':np.array([0,1]),
                  'd':np.array([0,-1]),
                  'z':np.array([-1,-1]),
                  'x':np.array([-1,0]),
                  'c':np.array([-1,1]),
                  's':np.array([0,0])
                  }
	vel = np.array([4.0, 2.0])
	def __init__(self,namespace):
		self.namespace = namespace
		self.remote = rm.RemoteGPIO()
		#init publisher for ROS messages
		try:
			rospy.init_node('remote_node', anonymous=True)
		except:
			pass
			
		self.publisher = rospy.Publisher(namespace + '/cmd_vel', Twist, queue_size=10)

	def update(self):
		#publish new velocities to gazebo model
		self.publish()

	def publish(self):
		move_command = Twist()
		cmd = self.vel*self.cmd_bindings[self.remote.state]
		# linear velocity
		move_command.linear.x = cmd[0]
		# rotational velocity
		move_command.angular.z = cmd[1]
		self.publisher.publish(move_command)

if __name__ == '__main__':
	v = RosView('robot1')

	try:
		r = rospy.Rate(10) # Hz
		while not rospy.is_shutdown():
			v.update()
			r.sleep()
	except rospy.exceptions.ROSInterruptException:
		pass
	finally:
		v.remote.exit()
