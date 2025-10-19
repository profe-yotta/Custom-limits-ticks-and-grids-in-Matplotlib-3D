# Custom limits ticks and grids in Matplotlib-3D
Since there's no available minor ticks and grids available online, I decided to create one.

## Where to Find
- Go to the Pythons folder in this repository
- Choose the `Custom.py` file
- Do whatever you want with that file

## What to Understand
As you can see, this file contains just a single function to create both of them. \
I will update them later when I have time to separate both funcionality. \
As of now [19-Oct-25], the function name was quite long, so here's how it works
```.py
def draw_custom_limits_ticks_grids(ax, x_min, x_max, y_min, y_max, z_min, z_max,
.                       x_minor, y_minor, z_minor, x_major, y_major, z_major):
.
.
```
The parameters must be assigned in order, as an example below:
```.py
x_min, x_max, x_minor, x_major = -15, 15, 1, 5
y_min, y_max, y_minor, y_major = -15, 15, 1, 5
z_min, z_max, z_minor, z_major = -50, 50, 5, 25
```
Those variables represents:
- `min` : The minimum limit for the figure
- `max` : The maximum limit for the figure
- `minor` : The minor ticks and/or grids
- `major` : The major ticks and/or grids

## How to Use
After you got the function, assign those paramaters as example:
```.py
x_min, x_max, x_minor, x_major = -15, 15, 1, 5
y_min, y_max, y_minor, y_major = -15, 15, 1, 5
z_min, z_max, z_minor, z_major = -50, 50, 5, 25

draw_custom_limits_ticks_grids(ax, x_min, x_max, y_min, y_max, z_min, z_max, 
                        x_minor, y_minor, z_minor, x_major, y_major, z_major)
```
However, there'll be some errors or bugs with this due to:
- Grids sometimes won't snap to the limit, resulting in a non-symmetry lines
- Ticks with axis limit variation, making the thickness and lengths invisible
- Other complex problem may rise from you as a user as well 
