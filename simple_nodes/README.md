# Simple Nodes

I made 3 simple nodes that can communicate with each other with the following architecture:

`
vision -> plan -> drive
`

**Vision:** This program creates a counter to immitate visual data being received over time

**Plan:** This program receives data from Vision and identifies whether the number is even or odd to immitate parsing data and decision making

**Drive:** This program receives commands from Plan and tells the robot to go left or right to immitate motor controls

`
1 2 3 4 5 ... -> odd even odd even odd even ... -> right left right left right ...
`

# Notes:

- Fine tuned virtual machine processing settings to remove scrolling lag and adjusted linux screen resolution
	-Installed some extensions as well to adjust desktop icon sizes

- Removed "junks" that did not affect python program in ROS (but the "junks" can be of more importance for more complex systems and applications)

- Architecture: 3 nodes (vision, plan, drive)
	- **Vision** creates a counter
	- **Plan** receives data from vision and identifies the integer as even or odd
	- **Drive** receieves data from vision and tells robot to turn left if even and right if odd

- Subscriber cannot identify an integer from input() in publisher. i think input() converts your number automatically into a string
	- Used a counter instead

- I think publisher+subscriber node cannot have multiple functions in the program(?)

- **Topic names must match!** for a single "phone line" communication

- Used Int32 and String (ROS data type keywords) for int and string (typical Python/C++ data type keywords)

- Can process data either in publisher node first (then just print onto subsriber node later) or in subsriber node (process data there and print in that program)
	- 2nd way makes more sense
	- Possibly putting all processors into **Plan** and let **Drive** only print
