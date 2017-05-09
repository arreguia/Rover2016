""" toggle param sets the node communication parameter to bool setting """
def toggleParam(setting):
        rospy.set_param("/base_goal_param", setting)

""" waifForToggle watches the parameter and waits for it to become true """
def waitForToggle():
        control = rospy.get_param("/base_goal_param")
        while (control is True):
                time.sleep(0.5)
                try:
                        control = rospy.get_param("/base_goal_param")
                        if (control is False):
                                break
                except KeyError:
                        print 'waitForToggle: param was not set correctly'

