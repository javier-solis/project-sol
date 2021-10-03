# Installing Packages

We now begin installing additional packages that you will need to get started. Later on there may be additional installations but these are the core ones.

Replicate the numbered steps below using the terminal, on **both** your Jetson Nano and laptop. Note, these are taken from [Intel's Realsense Github](https://github.com/IntelRealSense/realsense-ros#installation-instructions).

**0.**  
These come preinstalled with ROS Melodic and there is no need for additional downloads, they are just worth pointing out. 
* `ros-melodic-rospy`
* `rviz`

**1.**  
This package is essential for SLAM, which we will get to testing soon. To learn more, visit their [ROS Wiki](http://wiki.ros.org/rtabmap_ros).

```bash
sudo apt-get install ros-melodic-rtabmap
```

**2.**  
This will download many camera dependencies that we need, where the most notable is `librealsense2`.

```bash
sudo apt-get install ros-melodic-realsense-camera 
```

**3.**  
The following lettered steps are to be carried out on your Jetson Nano only. These are taken from [Intel's documentation]( https://dev.intelrealsense.com/docs/nvidia-jetson-tx2-installation).

```{tip}
If you're curious, these additional steps are not needed on a laptop due to the Jetson's Linux image having different kernel configurations
```
**a.**   
This allows your computer to accept the origin of the packages

```bash
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver 
hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
```

**b.**  
Installing the packages
```bash
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo bionic main" -u
sudo apt-get install librealsense2-utils
sudo apt-get install librealsense2-dev
```

```{warning}
A possible mistake you can make is installing the packages out of order. When this is done, sometimes the inner dependencies don't line up and you get an error, causing you to reinstall the packages from scratch. A loose example/answer can be seen [here](https://askubuntu.com/questions/1162356/failed-to-fix-broken-packages-in-ubuntu-16-04)
```

**4.**  
Now you can check that the camera works (on both devices) by plugging it in into your device and typing `realsense-viewer` on the terminal. This will load the stock Intel RealSense Camera software. If you're requested to update the camera's drivers, feel free to do so.



## Reference Table:

| PC | Both | Jetson Nano |
| --- | --- | --- |
| rtabmap | ROS Melodic, Full | rosserial |
| navigation | Comes with ROS: RVIZ and rospy | rosserial-arduino |
| (More info coming soon) |(More info coming soon) | (More info coming soon) |

