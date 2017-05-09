move_base_msgs::MoveBaseGoal createGoal(struct pos2d pos, bool global)
{
	move_base_msgs::MoveBaseGoal goal;
	pos2d curPos = getCurrentPos();
	struct pos2d target;

	// goal header
  	goal.target_pose.header.frame_id = "map";
  	goal.target_pose.header.stamp = ros::Time::now();
	
	// convert global position to relitive position for sending goals
        if (global == false)
        {
	        target.x = pos.x - curPos.x;
	        target.y = pos.y - curPos.y;
        }

	// set goal
  	goal.target_pose.pose.position.x = target.x;
	goal.target_pose.pose.position.y = target.y;
  	goal.target_pose.pose.orientation.w = tf::createQuaternionMsgFromYaw
		(pos.w).w; // pos.w is in radians;

	// print target goal
	ROS_INFO("x: %f, y: %f, w: %f",goal.target_pose.pose.position.x, 
		goal.target_pose.pose.position.y, goal.target_pose.pose.orientation.w); 

	return goal;
}
