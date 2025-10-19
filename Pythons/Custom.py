import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.ticker import MultipleLocator

def draw_custom_limits_ticks_grids(ax, x_min, x_max, y_min, y_max, z_min, z_max,
                        x_minor, y_minor, z_minor, x_major, y_major, z_major):

    # Define the range for the grid
    x_range = np.arange(x_min, x_max, x_minor)
    y_range = np.arange(y_min, y_max, y_minor)
    z_range = np.arange(z_min, z_max, z_minor)

    # Generate the line segments for the custom grid
    lines_x = []
    lines_y = []
    lines_z = []

    for x in x_range:
        lines_y.append([(x, y_max, z_min), (x, y_max, z_max)])
        lines_z.append([(x, y_min, z_min), (x, y_max, z_min)])

    for y in y_range:
        lines_z.append([(x_min, y, z_min), (x_max, y, z_min)])
        lines_x.append([(x_min, y, z_min), (x_min, y, z_max)])

    for z in z_range:
        lines_x.append([(x_min, y_min, z), (x_min, y_max, z)])
        lines_y.append([(x_min, y_max, z), (x_max, y_max, z)])

    # Create the Line3DCollection
    grids_x = Line3DCollection(lines_x, colors='black', alpha=0.1)
    grids_y = Line3DCollection(lines_y, colors='black', alpha=0.1)
    grids_z = Line3DCollection(lines_z, colors='black', alpha=0.1)

    # Plot the minor gridlines
    ax.add_collection(grids_x)
    ax.add_collection(grids_y)
    ax.add_collection(grids_z)

    # Set axis limits to match the grid
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    # Generate major ticks and grids
    ax.xaxis.set_major_locator(MultipleLocator(x_major))
    ax.yaxis.set_major_locator(MultipleLocator(y_major))
    ax.zaxis.set_major_locator(MultipleLocator(z_major))

    def draw_custom_ticks(axis, color, width, length,
                          x_locs=x_range, y_locs=y_range, z_locs=z_range,):
        tick_segments = []

        # Get axis limits for drawing the ticks
        xlim, ylim, zlim = ax.get_xlim(), ax.get_ylim(), ax.get_zlim()
        xtot = (xlim[1] - xlim[0])/2
        ytot = (ylim[1] - ylim[0])/2
        ztot = (zlim[1] - zlim[0])/2

        for loc in x_locs:
            tick_segments.append([[loc, ylim[0], zlim[0]],
             [loc, ylim[0] - length*ytot, zlim[0]]])

        for loc in y_locs:
            tick_segments.append([[xlim[1], loc, zlim[0]],
             [xlim[1] + length*xtot, loc, zlim[0]]])

        for loc in z_locs:
            tick_segments.append([[xlim[1], ylim[1], loc],
             [xlim[1] + length*xtot, ylim[1], loc]])

        tick_collection = Line3DCollection(tick_segments, colors=color,
                                           linewidths=width)
        ax.add_collection(tick_collection)

    # Draw custom minor ticks for each axis
    tick_length = 0.02 # Adjust based on axis scale
    tick_width = 0.2
    draw_custom_ticks(ax.xaxis, 'black', tick_width, tick_length)
    draw_custom_ticks(ax.yaxis, 'black', tick_width, tick_length)
    draw_custom_ticks(ax.zaxis, 'black', tick_width, tick_length)
