# pi-lawn-mower-remote
Control a ROS-enabled lawn-mower by pressing some buttons connected to a Raspberry Pi

- Check bi-directional connectivity between RaspberryPi and computer running simulation and ROS master by 'ping raspberry' and 'ping hostname'. Add entries to '/etc/hosts' if needed.
- In RaspberryPi, execute 'export ROS_MASTER_URI=http//hostname:11311' before running 'main.py'
