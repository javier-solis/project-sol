# Terminology

## ROS Related

### Nodes and Topics

The structure of ROS boils down to the connections between _nodes_ and _topics_. Nodes are pieces of code, or the “things” that actually do computational work. Meanwhile, topics are the links that transfer "messages" (aka data) between nodes. Topics are also sometimes referred to as _channels_, but both mean the same thing. The diagram below is a visual example of a network of nodes and topics:  

![Network of nodes and topics](/images/diagrams/nodes-topics.png)

Each node contains what are called _publishers_ and/or _subscribers_. Publishers give (aka publish) messages to other nodes under the same topic, and subscribers receive (aka subscribe) data from other nodes under the same topic. This data transfer is possible thanks to the _ROS master_ which runs in the background and keeps track of publisher nodes and subscriber nodes, helping them communicate. 

```{note}
There's a difference between publishing and printing/logging.
```

#### Example

Consider a smart home with a thermostat and a heater. In a ROS world, the thermostat and heater are the nodes, the topic is the Internet of Things, and the ROS master runs on your smartphone or laptop to "host" the communication between both devices.

## Odometry Related

### Odometry
The process of estimating how much a robot has moved.

### Visual Odometry

The process of determining the position and orientation of a robot by "stitching" together many related camera images.

## Motor Related

### Pulse Width Modulation
Pulse Width Modulation, or PWM, is a process in which you can achieve an analog signal using digital signals. This done by having a microcontroller release oscillating square electrical signals, resembling the images[^1] below.

![PWM Example](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png) 


This is often used to vary the speed at which DC motors turns, how bright a light is, etc. To learn more, visit [Arduino's explanation page](https://www.arduino.cc/en/Tutorial/Foundations/PWM).


### Motor Encoder
This is a type of sensor where a signal is triggered every fixed segment of a spin (determined by the number of "slots" in the encoder), allowing us to find out how fast a wheel is spinning. There exist optical and magnetic motor encoders.  

[This video](https://www.youtube.com/watch?v=oLBYHbLO8W0) does a good job showcasing an implementation between DC motors and encoders.


### DC-Motor
(More info coming soon)

### Stepper-motor
(More info coming soon)

### Motor Driver

Also known as an H-bridge, a motor driver is connected to a microcontroller, a motor, and an external power supply. It's used to supply a higher voltage to a motor if the microcontroller its connected to can't supply it (this high voltage is taken from the external power supply). Technical diagrams are attached below. Different types of motors typically use different motor driver chips (e.g. DC motor and stepper motor).

(More info coming soon)

## Misc.

### Closed Feedback Loop

(More info coming soon)





[^1]: https://en.wikipedia.org/wiki/Pulse-width_modulation
