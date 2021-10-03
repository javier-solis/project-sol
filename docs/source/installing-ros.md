# Installing ROS

Installing ROS on your laptop and Jetson Nano requires the same steps. Below I've outlined `commands` that you should enter into your Ubuntu terminal, alongside their purpose. These come from the [official ROS installation guide](https://wiki.ros.org/melodic/Installation/Ubuntu) which I recommend visiting for more concise explanations.


**1.**  
Making sure your computer is up to date.
```bash
sudo apt update
sudo apt upgrade
```
**2.**  
Allowing your computer to accept ROS software/packages.
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

**3.**  
Downloading the **full** desktop installation of ROS.
```bash
sudo apt install ros-melodic-desktop-full
```

**4.**  
Adding ROS environment variables to your bash session every time a new shell is launched. In other words, this means you won't have to repeat `source /opt/ros/melodic/setup.bash` to access ROS variables on every terminal you spawn.
```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

**5.**  
Installing a few of the ROS dependancies we need.
```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

**6.**
Initializing rosdep, which better configures these external dependencies.
```bash
sudo rosdep init
rosdep update
```

**7.**
Making sure all ROS software is up to date.
```bash
sudo apt update
sudo apt upgrade
```

And that's it! In later chapters we'll cover what other packages you'll need to install.
