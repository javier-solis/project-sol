# SLAM Test

The following is a simplified version of [Intel's SLAM guide](https://github.com/IntelRealSense/realsense-ros/wiki/SLAM-with-D435i)

**1.**  
Install the following dependencies
```bash
sudo apt-get install ros-melodic-imu-filter-madgwick
sudo apt-get install ros-melodic-rtabmap-ros
sudo apt-get install ros-melodic-robot-localization
```

**2.**  
Download [this](https://raw.githubusercontent.com/IntelRealSense/realsense-ros/development/realsense2_camera/launch/opensource_tracking.launch) launch file (using "save page as")

**3.**   
Launch ROS with the above file

```bash
roslaunch realsense2_camera opensource_tracking.launch
```

**4.**  
On rviz, replicate these toggles (leave the others off, they are redundant for now):

![rviz settings](https://raw.githubusercontent.com/wiki/intel-ros/realsense/pictures/os_tracking_display_panel.jpg)

Don't forget to toggle "pointcloud2", which is not highlighted above.

**5.**  
You can now _slowly_ move your camera around to capture a pointcloud map of your room. Don't make sharp turns and keep the camera's POV continous (don't block it with your hand as it moves places, etc.) On your laptop it's easy to move anywhere in your room as your laptop is mobile, but on a Jetson Nano it might be hard to move around given that the Jetson is tethered to a power outlet. In a future section we will cover how to use the Jetson in "headless mode", allowing you to move freely by using a portable battery.

```{tip}
To save the pointcloud you generate, run `rosrun pcl_ros pointcloud_to_pcd input:=/rtabmap/cloud_map`

Then, install `sudo apt-get install pcl-tools` to see the map via `pcl_viewer 1543906154413083.pcd`
```

