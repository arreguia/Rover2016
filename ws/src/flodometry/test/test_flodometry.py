#!/usr/bin/env python
import unittest
from nose import with_setup
import numpy as np
from bunch import Bunch
import rosbag
import rospy
import rostest
import sys, os
import matplotlib.pyplot as plt

PKG='test_flodometry'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.Flodometry import Flodometry

class TestFlodometry(unittest.TestCase):
    """TestFlodometry"""

    def test_real_roving_data(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data = np.loadtxt(os.path.join(path, 'data/motion_concrete.txt'), delimiter=',')
        f = Flodometry()
        f.setup_kalman()
        rospy.loginfo(f.kf.x)
        rospy.loginfo(f.kf.R)
        rospy.loginfo(f.kf.H)
        rospy.loginfo(f.kf.Q)

        motion_x = [val[1] for val in data]
        x = []
        for val in data:
            motion = Bunch()
            #rospy.logwarn(val[1])
            motion.dx = val[1]
            f.update(motion)
            x.append(f.kf.x)
            #rospy.logwarn(f.kf.x)
        vel = [val[1] for val in x]
        pos = [val[0] for val in x]
        x_time = [val[0] for val in data]
        self.plot(x_time, motion_x, 'Motion')
        self.plot(x_time, vel, 'Velocity')

    def plot(self, x, y, title):
        """Plots and saves data compiled in test
        
        Args:
            x (List): X-value to plot
            y (List): Y-value to plot
            title (str): Title of plot
        
        Returns:
            None
        """
        if len(x) > 0 and len(y) > 0:
            plt.figure()
            plt.plot(x,y)
            plt.title(title)
            plt.axis([min(x), max(x), min(y), max(y)])
            plt.show()
        else:
            rospy.logerr('No data for {}'.format(title))






    # def testUpdate_one(self):
    #     self.f = Flodometry()
    #     bag = rosbag.Bag('2016-03-09-21-01-43.bag')
    #     for topic, msg, t in bag.read_messages(topics=['/optical_flow']):
    #         try:
    #             self.f.update(msg)
    #         except Exception as ex:
    #             import IPython; IPython.embed()
    #     bag.close()
    #     print self.f.kf.x
    #     self.assertEquals(True, abs(abs(self.f.kf.x[0])-10) < 1)

    # def testUpdate_two(self):
    #     self.f = Flodometry()
    #     bag = rosbag.Bag('2016-03-09-21-03-00.bag')
    #     for topic, msg, t in bag.read_messages(topics=['/optical_flow']):
    #         try:
    #             self.f.update(msg)
    #         except Exception as ex:
    #             import IPython; IPython.embed()
    #     bag.close()
    #     print self.f.kf.x
    #     self.assertEquals(True, abs(abs(self.f.kf.x[0])-10) < 1)

    # def testUpdate_three(self):
    #     self.f = Flodometry()
    #     bag = rosbag.Bag('2016-03-09-21-07-21.bag')
    #     for topic, msg, t in bag.read_messages(topics=['/optical_flow']):
    #         try:
    #             self.f.update(msg)
    #         except Exception as ex:
    #             import IPython; IPython.embed()
    #     bag.close()
    #     print self.f.kf.x
    #     self.assertEquals(True, abs(abs(self.f.kf.x[0])-10) < 1)
if __name__ == '__main__':
    rostest.rosrun(PKG, 'test_flodometry', TestFlodometry)
        