 if __name__ == '__main__':
            odom = Odometry()
            odom.header.stamp = rospy.Time.now()
            odom.header.frame_id = '/odom'
            x = self.kf.x
            odom.pose.pose.position.x = x[0]
            odom.pose.pose.position.y = x[2]
            odom.twist.twist.linear.x = x[1]
            odom.twist.twist.linear.y = x[3]
            odom.twist.twist.angular.z = x[5]
            odom.pose.pose.orientation.x
            quaternion = quaternion_from_euler(0.0, 0.0, x[4])
            odom.pose.pose.orientation.x = quaternion[0]
            odom.pose.pose.orientation.y = quaternion[1]
            odom.pose.pose.orientation.z = quaternion[2]
            odom.pose.pose.orientation.w = quaternion[3]
            self.pub.publish(odom)
            self.tf_odom.sendTransform( (x[0], x[2], 0.0), (quaternion[0], quaternion[1],
            quaternion[2], quaternion[3]), odom.header.stamp, "base_link", "odom")
        else:
            pass
