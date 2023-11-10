import math

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

t = 10  # time in seconds
num_segments = [10, 100, 1000, 10000]  # different numbers of segments

for segments in num_segments:
    d = distance(t, segments)
    print(f"Number of segments: {segments}, Distance: {d}")

