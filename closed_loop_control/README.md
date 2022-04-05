## Closed Loop Control
In this demonstration, I added complexity of simple_nodes using a simple closed loop controls architecture.

CL = Closed Loop

The architecture is as follows:
1. **CLVision.py**: generates a random number between 1-9.
2. **CLPlan.py**: finds how far away from the number 5, then sends that information back to Vision.
3. Then, Vision corrects the error and sends to drive.
4. **CLDrive.py**: makes sure random number generated is corrected and always outputting '5'.
