bool locator(locate_home_base::locate_base::Request  &req,
	locate_home_base::locate_base::Response &res)
{
	ImageConverter ic; 
	// runs with spin once to ensure that an image has been grabbed in the subscriber

	while (ic.avail != 0)
	{
		ROS_INFO("LOCATOR SERVICE: Waiting on ZED");
		ros::Duration(0.1).sleep();
		ros::spinOnce();
	}
	ROS_INFO("LOCATOR SERVICE: sending back response");

	res.distance = ic.base_distance;
	res.angle = ic.base_angle;
  	return true;
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "image_converter");
	ros::NodeHandle server_nh;
	ros::ServiceServer service = server_nh.advertiseService("locate_base", locator);
	ros::spin();
	return 0;
}
