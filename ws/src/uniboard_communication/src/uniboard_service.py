#!/usr/bin/env python

import rospy
import Queue
from uniboard_communication.srv import *
# Fake uniboard
# from fake_uniboard import Uniboard
# Real uniboard
from uniboard_software.roverlib.uniboard import Uniboard


class UniboardCommunication(Queue.PriorityQueue):
    """
    Handles all communciation with the uniboard for 2016 mars rover
    access functions through ros services never call directly.
    """
    def __init__(self, maxsize=10):
        Queue.PriorityQueue.__init__(self)
        self.board = Uniboard("/dev/ttyUSB2")
        self.s = rospy.Service('uniboard_service', 
                            communication, 
                            self.addToQueue)

    def addToQueue(self, req):
        if self.full():
            return [False, 'queue_full', None]
        else:
            try:
                fun = self.board.__getattribute__(req.function)
            except:
                return [False, 'No Function', None]
            resp = [False, '', '']
            if req.key_word is not '':
                try:
                    arg = float(req.arg)
                except:
                    try:
                        arg = bool(req.arg)
                    except:
                        return [False, 'Arg must be float or bool', None]
            else:
                arg = None

            self.put((req.priority, fun, req.key_word, arg, req.timestamp, resp, req.axis))
            self.join()
            return resp

    def worker(self):
        while not rospy.is_shutdown():
            if not self.empty():
                kwargs = dict()
                item = self.get()
                try:
                    if item[6] is not '':
                        kwargs = dict(axis=item[6])
                    if item[2] is not '':
                        kwargs[item[2]]=item[3]
                    if len(kwargs) > 0:
                        resp = item[1](self.board, **kwargs)
                    elif item[3] is not None:
                        resp = item[1](self.board, item[3])
                    else:
                        resp = item[1](self.board)
                    item[5][0] = True
                    item[5][1] = 'Returned in {} nano seconds'.format(rospy.Time.now().nsecs-item[4].nsecs)
                    item[5][2] = str(resp)
                    self.task_done()
                except Exception as ex:
                    item[5][0] = False
                    item[5][1] = str(ex)
                    item[5][2] = None
                    self.task_done()
                

if __name__ == '__main__':
    # Initialize the node
    rospy.init_node('uniboard_communication')
    controller = UniboardCommunication()
    controller.worker()
    rospy.spin()