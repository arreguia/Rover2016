bool executeGoal(move_base_msgs::MoveBaseGoal goal, MoveBaseClient *client, int timeout)
{
	ROS_INFO("Sending goal");
  	client->sendGoal(goal);

	// wait for result or time out after 60s 
  	bool finished_before_timeout = client->waitForResult(ros::Duration(timeout));
	
	// check goal outcome
	if (finished_before_timeout)
  	{
		if(client->getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
		{
			ROS_INFO("executeGoal: goal met");
			return(true);
		}
  		else
		{
			ROS_INFO("executeGoal: missed goal");
			return(false);
		}
  	}
  	else
	{
		ROS_INFO("executeGoal: time out");
		return(false);
	}
}
