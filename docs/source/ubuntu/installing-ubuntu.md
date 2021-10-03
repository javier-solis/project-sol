# Installing Ubuntu

We will now begin the process of downloading and installing all the software that you'll need. Foremost in this process is the installation of the Ubuntu 18 desktop operating system on your laptop and Jetson Nano.

## Why Ubuntu?

By using Ubuntu we are setting our project in a Linux[^1] environment and that is essential as Linux's library of open source software is something that we'll be using extensively. Ubuntu is what's called a distro or "flavor" of Linux. While in theory we can use any distro of Linux for this project, we're sticking with Ubuntu because it's one of the best entry-level Linux distros and it's very well documented/functional with ROS. Furthemore, we'll be using Ubuntu's 18th version (known as Bionic Beaver) as that is the Ubuntu version that **ROS Melodic** is attached to, which is the ROS version we'll be using. There are [newer versions of ROS](http://wiki.ros.org/Distributions) and even a [ROS 2.0](https://docs.ros.org/en/foxy/index.html) but we're sticking with ROS Melodic because it's what the Jetson Nano natively supports and the camera we're using has a longer history on Melodic than any other version of ROS.


```{toctree}
:maxdepth: 2
:hidden:

pc-ubuntu
jetson-ubuntu
ubuntu-notes
```

[^1]: Technically referred to as GNU/Linux for reasons outlined [here](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy)

