import numpy as np
from filterpy.common import Q_discrete_white_noise

# Using data from data/srcMotion xconcrete.txt
# Assuming actual velocity of 0.5 m/s
# 581 data points 
# Minimum Value = 23.0
# Maximum Value = 37.0
# Mean Value = 33.2358003442
# Standard Deviation = 1.82292503542
# Variance = 3.32305568475
# Median Value = 34.0
class Flow(object):
    dt = float(1.0)/float(100)
    # Length of state array
    dim_x = 1
    # Initial state [pos, vel]
    x = np.array([[0.0]])
    # State transfrom matrix such that x(t) = F*x(t-1)
    F = np.array([[1]]) 
    # State transfrom noise the variance needs to be tuned when we know how fast we 
    # can accelerate or decelerate.
    Q = np.array([[1E-5]])
    # Initial variance for position set at 0 since we know our starting location
    P = np.array([[0]])
    # Size of measurement array
    dim_z = 1
    # Measurement transform such that z = H*x, [0, mean_motion/actual_vel]
    H = np.array([[72.28]]) 
    # Measurment variance
    R = np.array([[0.66]])

class Rotation(object):
    dt = float(1.0)/float(100)
    # Length of state array
    dim_x = 1
    # Initial state [pos, vel]
    x = np.array([[0.0]])
    # State transfrom matrix such that x(t) = F*x(t-1)
    F = np.array([[1]]) 
    # State transfrom noise the variance needs to be tuned when we know how fast we 
    # can accelerate or decelerate.
    Q = np.array([[1E-6]])
    # Initial variance for position set at 0 since we know our starting location
    P = np.array([[0]])
    # Size of measurement array
    dim_z = 1
    # Measurement transform such that z = H*x, [0, mean_motion/actual_vel]
    H = np.array([[1]]) 
    # Measurment variance
    R = np.array([[0.06]])
    
class VelLeft(object):
    dt = float(1.0)/float(60)
    # Length of state array
    dim_x = 1
    # Initial state [pos, vel]
    x = np.array([[0.0]])
    # State transfrom matrix such that x(t) = F*x(t-1)
    F = np.array([[1]]) 
    # State transfrom noise the variance needs to be tuned when we know how fast we 
    # can accelerate or decelerate.
    Q = np.array([[1E-6]])
    # Initial variance for position set at 0 since we know our starting location
    P = np.array([[0]])
    # Size of measurement array
    dim_z = 1
    # Measurement transform such that z = H*x, [0, mean_motion/actual_vel]
    H = np.array([[70.26]]) 
    # Measurment variance
    R = np.array([[2.907]])

class VelRight(object):
    dt = float(1.0)/float(60)
    # Length of state array
    dim_x = 1
    # Initial state [pos, vel]
    x = np.array([[0.0]])
    # State transfrom matrix such that x(t) = F*x(t-1)
    F = np.array([[1]]) 
    # State transfrom noise the variance needs to be tuned when we know how fast we 
    # can accelerate or decelerate.
    Q = np.array([[1E-6]])
    # Initial variance for position set at 0 since we know our starting location
    P = np.array([[0]])
    # Size of measurement array
    dim_z = 1
    # Measurement transform such that z = H*x, [0, mean_motion/actual_vel]85.897
    H = np.array([[85.897]]) 
    # Measurment variance
    R = np.array([[2.986]])

class Odometry(object):
    def __init__(self):


        dt = float(1.0)/float(60)
        # Length of state array
        self.dim_x = 6
        # Initial state [pos_x, vel_x, pos_y, vel_y, theta, vel_theta]
        self.x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        # State transfrom matrix such that x(t) = F*x(t-1)
        self.F = np.array([[1.0, dt, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 1.0, dt, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 1.0, dt],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]) 
        # State transfrom noise the variance needs to be tuned when we know how fast we 
        # can accelerate or decelerate.
        a = (dt**4)/4
        b = (dt**3)/2
        c = dt**2
        var = 0.5
        self.Q = np.array([[a*var, b*var, 0.0, 0.0, 0.0, 0.0],
                           [b*var, c*var, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, a*var, b*var, 0.0, 0.0],
                           [0.0, 0.0, b*var, c*var, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0, a*var, b*var],
                           [0.0, 0.0, 0.0, 0.0, b*var, c*var]])
        # Initial variance for position set at 0.0 since we know our starting location
        self.P = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        # Size of measurement array
        self.dim_z = 4
        self.H = self.get_h()

        self.R = np.array([[0.05, 0.0, 0.0, 0.0],
                           [0.0, 0.05, 0.0, 0.0],
                           [0.0, 0.0, 0.05, 0.0],
                           [0.0, 0.0, 0.0, 0.5]])

    def get_h(self, theta=0.0):
        # Wheel base width of rover
        b = 1.0
        return np.array([[0.0, np.cos(theta), 0.0, np.sin(theta), 0.0, 0.0],
                         [0.0, -np.sin(theta), 0.0, np.cos(theta), 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, b/2]])



flow = Flow()
vel_left = VelLeft()
vel_right = VelRight()
odometry = Odometry()
rotation = Rotation()
