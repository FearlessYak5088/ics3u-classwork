robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")
# this will be printed if the ball location is greater than robot location

if robot_location > goal_location:
    print("You are beyond the goal.")
  # this will be printed if the robot location is greater than goal location

if robot_location == goal_location:
    print("The robot is at the goal.")
# this will be printed if the robot location is equal to the goal location

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")
# this will be printed if the robot location equals the goal location (after adding 5 to the robot location)

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")
  # this will be printed and the user will have the ball if the robot is at the ball

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")
  # this will be printed if the goal location is greater than the robot location (after subtracting 15)

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
# this will be printed and the user will no longer have the ball if the robot is at the goal and has the ball

  
# What is the purpose indenting in the if statement? How can we tell what code is enclosed in an if branch and what code is not? Answer in a comment.
  
    # Indenting the if statement helps make the code easier to read, showing what happens after the if statement is triggered. 

  
# Change the initial locations of the objects and get the program to output the same thing.
robot_location = 45
ball_location = 50
goal_location = 20
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
  

# What do the operators += and -= do?
    # They add or subtract from the value of the variable 
