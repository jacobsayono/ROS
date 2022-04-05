# ROS

## Creating your workspace

Make a directory. "src" is where you will transform the folder into a workspace.
```
mkdir -p <your_workspace_name>/src
```
Transform your folder into a workspace. Also used later to make sure everything is compiled. Write this command under src directory:
```
catkin_make
```
Sourcing your workspace. This updates your environment variables so ROS understands what you're workin on.
```
source devel/setup.bash
```
## Quick little shortcut

Note: you have to write that command above manually everytime you open a new terminal, so try this instead:
```
gedit ~/.bashrc
```
When the gedit file opens, scroll to:
```
source /opt/ros/noetic/setup.bash
```
Then just write this line underneath it in the gedit file:
```
source ~/<your_workspace_name>/devel/setup.bash
```
## Continuing... creating a package
Okay, now make directories where you will create and write .py files. Make sure you are in the src directory.
```
catkin_create_pkg <your_package_name> std_msgs geometry_msgs rospy
```
The things after <your_package_name> are your dependencies where you can import into your ROS scripts. Above are common examples.

Create another folder (there is a new "src" folder; this is for c++ files. the one we will make is for python files). This should be under the <your_package_name> directory:
```
mkdir python_scripts
```
Now you are ready to start writing Python programs in ROS!

Once you have written your code and want to test/run them, first go back to <your_workspsace_name> directory, then write this command to make sure everything is compiled:
```
catkin_make
```
Lastly, Python files created on linux are not runnable by default. This command tells linux that these are runnable files. We make a program executable and find them.

Write these commands under <your_workspace_name> directory:
```
chmod +x src/turtlebot_tut/scripts/faxer.py
chmod +x src/turtlebot_tut/scripts/printer.py
```
- chmod = change permissions
- +x = make it executable
- /... = find path to faxer and printer

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
