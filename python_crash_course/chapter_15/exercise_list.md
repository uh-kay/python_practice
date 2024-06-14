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
walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x- or y-direction list.

## 15-5. Refactoring: 
The fill_walk() method is lengthy. Create a new method
called get_step() to determine the direction and distance for each step, and 
then calculate the step. You should end up with two calls to get_step() in fill_walk(): 

x_step = self.get_step()
y_step = self.get_step()

This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.