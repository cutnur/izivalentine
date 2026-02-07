import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup the 3D grid
u = np.linspace(-1.5, 1.5, 50) # Lower resolution for smoother animation
x, y, z = np.meshgrid(u, u, u)

# 2. Define the heart equation
heart = (x**2 + 2.25*y**2 + z**2 - 1)**3 - x**2 * z**3 - 0.1125 * y**2 * z**3

# 3. Initialize the figure and 3D axis
fig = plt.figure(figsize=(8, 8), facecolor='white')
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    ax.set_axis_off()
    
    # Set the viewing angle (rotates based on the frame number)
    ax.view_init(elev=10, azim=frame)
    
    # Re-draw the heart
    ax.voxels(heart <= 0, facecolors='hotpink', edgecolor='deeppink', alpha=0.7)
    
    return fig,

# 4. Create the animation (spins 360 degrees)
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

plt.show()
input("Press Enter to close...")