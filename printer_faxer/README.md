# ROS

## Creating your workspace

Transform your folder into a workspace. Also used later to make sure everything is compiled.
```
catkin_make
```
Sourcing your workspace. This updates your environment variables so ROS understands what you're workin on.
```
source devel/setup.bash
```
Python files created on linux are not runnable by default. This command tells linux that these are runnable files. We make a program executable and find them.

- chmod = change permissions
- +x = make it executable
- /... = find path to faxer and printer
```
chmod +x src/turtlebot_tut/scripts/faxer.py
chmod +x src/turtlebot_tut/scripts/printer.py
```

## Running your program

**Note: use separate terminals for each of the following.**

Tell ROS as a whole to start running.
```
roscore
```
Run faxer.py
```
rosrun turtlebot_tut faxer.py
```
Run printer.py
```
rosrun turtlebot_tut printer.py
```

## Final thoughts
- Two complete separate programs are talking to one another through the magic of ROS!
- Not too complicated; most difficult part was getting the workspace set up
- Writing the programs is just like any other python program except with a little bit of extra spice
