# Ubuntu On Jetson Nano

The Jetson Nano uses a microSD card as it's main memory source and uses a modified 
version of Ubuntu 18 called [Tegra](https://en.wikipedia.org/wiki/Linux_for_Tegra). 
Thus, it requires a different installation file and method of installation compared to a laptop. The specifc 
installation file that I've been using and you should install too (for consistancy) can 
be found [here](https://developer.nvidia.com/jetpack-sdk-451-archive) (Jetpack version v.4.5.1). 
Once you have it, flash it onto a microSD card using [Etcher](https://www.balena.io/etcher/). 
The flashing process on Etcher is just a few self-described clicks. 

```{note}
Those that have used Raspberry Pi's before would recall that flashing is what occurs when installing Rasbian on a Pi.
```

After flashing, insert the microSD card into your Jetson, power it on, and proceed with the system configuration process. As before, their recommended settings will work well.s
