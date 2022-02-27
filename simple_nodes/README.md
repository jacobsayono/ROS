# Simple Nodes

I made 3 simple nodes that can communicate with each other with the following architecture:

`
vision -> plan -> drive
`

**Vision:** This program creates a counter to immitate visual data being received over time

**Plan:** This program receives data from Vision and identifies whether the number is even or odd to immitate parsing data and decision making

**Drive:** This program receives commands from Plan and tells the robot to go left or right to immitate motor controls

`
1 2 3 4 5 ... -> odd even odd even odd even ... -> right left right left right
`

I have attached some of my notes into this folder regarding my experience building 3 nodes.
