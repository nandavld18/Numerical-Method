import math
import numpy as np
import matplotlib.pyplot as plt

def velocity(t):
    g = 9.8
    m = 68.1
    c = 12.5
    return (g * m / c) * (1 - math.exp(-(c / m) * t))

def distance(t, num_segments):
    dt = t / num_segments
    integral = 0.5 * velocity(0)
    for i in range(1, num_segments):
        integral += velocity(i * dt)
    integral += 0.5 * velocity(t)
    integral *= dt
    return integral

t = np.linspace(0, 10, 100)  # time in seconds
v = [velocity(ti) for ti in t]
d = [distance(ti, 1000) for ti in t]

# Plotting velocity
plt.figure(figsize=(8, 4))
plt.plot(t, v, label='Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.legend()
plt.grid(True)
plt.show()

# Plotting distance
plt.figure(figsize=(8, 4))
plt.plot(t, d, label='Distance')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Distance vs Time')
plt.legend()
plt.grid(True)
plt.show()