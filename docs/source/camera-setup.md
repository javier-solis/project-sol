# Camera Setup

We're now going to set up the foundation of our project and test/see that the camera can generate a point cloud. These instructions will work on both your laptop and Jetson Nano. They are also a simplified version of the instructions from the [IntelRealSense Github]((https://github.com/IntelRealSense/realsense-ros).  

**1.**  
Create an empty nest of directories for a [catkin workspace](http://wiki.ros.org/catkin). Essentially, a catkin workspace is where all the files of a ROS project are housed.

```bash
mkdir -p ~/catkin_ws/src
```

**2.**  
Run the following commands

```bash
cd ~/catkin_ws/src
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
cd ..
catkin_init_workspace
cd ..
```

```{danger}
On this next command I encountered an error on my Jetson Nano that read as followed:


	CMake Error at /opt/ros/melodic/share/cv_bridge/cmake/cv_bridgeConfig.cmake:113 (message):
	  Project 'cv_bridge' specifies '/usr/include/opencv' as an include dir,
	  which is not found.  It does neither exist as an absolute directory nor in
	  '${{prefix}}//usr/include/opencv'.  Check the issue tracker
	  'https://github.com/ros-perception/vision_opencv/issues' and consider
	  creating a ticket if the problem has not been reported yet.
	[…]
	-- Configuring incomplete, errors occurred!
	[…]
	Invoking "cmake" failed


To resolve this, you need to run the following command: ` sudo ln -s /usr/include/opencv4/opencv2/ /usr/include/opencv`. Credits go to [this thread](https://answers.ros.org/question/199279/installation-from-source-fails-because-of-cv_bridge-include-dir/?answer=377300#post-id-377300) for the solution. You can now rerun `catkin_make`.
But now you might also notice a new error:


	/opt/ros/melodic/include/cv_bridge/cv_bridge.h:43:10: fatal error: opencv2/core/core.hpp: No such file or directory

	
To fix this, run the following:

	sudo apt -y --allow-downgrades install libopencv-dev=3.2.0+dfsg-4ubuntu0.1
	sudo apt-mark hold libopencv-dev

Credits go to [this thread](https://answers.ros.org/question/347754/jetson-nano-comes-with-opencv-411-do-i-need-to-downgrade-to-32-for-melodic/?answer=351831#post-id-351831).

```


```bash
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
```

```{note}
It may be possible to replace the above 3 commands with just `catkin_make`. It appeared to work when I tried it, but Intel recommends otherwise.
```

**3.**  
Initialize your workspace

```bash
cd ~/catkin_ws
source devel/setup.bash
```

**4.**  
Setting up your terminal (technically Bash) settings such that they initialize your workspace each time a new terminal window is open. This step is kind of optional, but it's worth doing to avoid having to do step 3 each time you open a new terminal window to work on your ROS project.

```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

```{note}
For more insight what it means to source your setup.bash file, I recommend checking out these links: [first](https://stackoverflow.com/questions/56139647/), [second](https://answers.ros.org/question/251292/)
```


## Testing

**1.**  
Initializing ROS and launching the roslaunch file

```{note}
The `&` character puts a process in the background, allowing us to multitask in the same terminal window
```

```bash
roscore &
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
```

**2.**  

Run either `rosrun rviz rviz &` or just `rviz &`. They do the same action of launching [rviz](http://wiki.ros.org/rviz), a platform where we can see the camera's output


```{warning}
rviz must be launched after the camera is plugged into your laptop, and after the above roslaunch has been launched
```

**3.**  
At this point you can see a little bit of what the camera is outputting. We will now refine what we see, focusing on the point cloud. The steps to do this are different between a laptop and a Jetson Nano. 

**a.**  
**In your laptop:** Open the rviz window, make your fixed frame the camera_link (on the left), click the add/"+" symbol (on the bottom left), head over to "by topic" --> "depth-registered" --> "points" - -> and toggle "pointcloud"

**b.**  
**In your Jetson:** Open the rviz window, make your fixed frame the camera_link, click "Add", go to "by topic" --> "depth" --> "color" --> "points" --> and toggle "pointcloud2"


**4.**  
And that's all there is to it! To quit everything, you can close  the terminal altogether or press `CTRL+c` in it.

