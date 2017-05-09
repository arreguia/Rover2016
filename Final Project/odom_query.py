def getCurPos(listener):
    # lookup the transform 
    try:
    	listener.waitForTransform("/map","/base_link",rospy.Time(),rospy.Duration(5.0)) 
    	(position, quaternion) = listener.lookupTransform("/map",
		"/base_link", rospy.Time(0))
    	x = position[0]
    	y = position[1]
        #  convert quat to euler
     	euler = tf.transformations.euler_from_quaternion(quaternion)
     	yaw = euler[2]
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    	rospy.logwarn("TRANSFORM_LISTENER: Exception")
    	x = -1
    	y = -1
    	yaw = -1
     
    rospy.loginfo("CURRENT POSITION: x: %s, y: %s, yaw: %s", x, y, yaw)
    return (x, y, yaw)

