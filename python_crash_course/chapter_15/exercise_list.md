## 15-1. Cubes: 
A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5,000 cubic numbers.

## 15-2. Colored Cubes: 
Apply a colormap to your cubes plot.

## 15-3. Molecular Motion: 
Modify rw_visual.py by replacing ax.scatter() with
ax.plot(). To simulate the path of a pollen grain on the surface of a drop of
water, pass in the rw.x_values and rw.y_values, and include a linewidth argu-
ment. Use 5,000 instead of 50,000 points to keep the plot from being too busy.

## 15-4. Modified Random Walks: 
In the RandomWalk class, x_step and y_step are
generated from the same set of conditions. The direction is chosen randomly
from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify 
the values in these lists to see what happens to the overall shape of your 
walks. Try a longer list of choices for the distance, such as 0 through 8, or 
remove the −1 from the x- or y-direction list.

## 15-5. Refactoring: 
The fill_walk() method is lengthy. Create a new method
called get_step() to determine the direction and distance for each step, and 
then calculate the step. You should end up with two calls to get_step() in 
fill_walk(): 

x_step = self.get_step()
y_step = self.get_step()

This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.

## 15-6. Two D8s: 
Create a simulation showing what happens when you roll two
eight-sided dice 1,000 times. Try to picture what you think the visualization 
will look like before you run the simulation, then see if your intuition was 
correct. Gradually increase the number of rolls until you start to see the 
limits of your system’s capabilities.

## 15-7. Three Dice: 
When you roll three D6 dice, the smallest number you can roll
is 3 and the largest number is 18. Create a visualization that shows what hap-
pens when you roll three D6 dice.

## 15-8. Multiplication: 
When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if 
you multiply these numbers by each other instead.

## 15-9. Die Comprehensions: 
For clarity, the listings in this section use the long
form of for loops. If you’re comfortable using list comprehensions, try writing
a comprehension for one or both of the loops in each of these programs.

## 15-10. Practicing with Both Libraries: 
Try using Matplotlib to make a die-rolling
visualization, and use Plotly to make the visualization for a random walk. 
(You’ll need to consult the documentation for each library to complete this 
exercise.)