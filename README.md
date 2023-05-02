# Robotics-Project

All the code I wrote to that control the servo motors on a bipedal robot I built for **MECE 4611 Robotics Studio** 

Initially I duplicated the movement for each leg, but then I needed to figure out how to coordinate both legs.

I used keyframing to model the robot gait. My process was as follows:
- Connect the built robot to my computer via USB
- Run the Position Test.py file and direct the robot's movements.
- Once satsified with the robot gait, run Optimise Line.py on each line of data to generate a sine wave that models the movement I simulated.
- Insert the new sine equation in the respective move function in walking_computer.py file.
- Observe the gait and decide on corrections.
