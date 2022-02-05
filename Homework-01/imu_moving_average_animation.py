# imu_moving_average_animation.py
"""
Author: Adarsh Malapaka (amalapak@umd.edu), 2022
Brief: Code to load IMU data (ADXL327 3-axis accelerometer) from file 
       and plot raw and moving-average filtered pitch angle data
Course: ENPM809T - Autonomous Robotics [HW01]
Date: 4th February, 2022

Reference: https://pythonforundergradengineers.com/offset-piston-motion-animation-matplotlib.html
"""

# Required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

imu_width = 4.0     # Width of the ADXL327 sensor [mm] 

# Loading the data from 'imudata.txt'
file_name = 'imudata.txt'
imu_raw_data = np.loadtxt(file_name, delimiter=' ', dtype=str)    # Loaded data size: 371 by 7 
print(f"Loaded IMU data from file: {file_name}.")

data_size = np.shape(imu_raw_data)[0]

imu_pitch_angle = [int(imu_raw_data[i][4]) for i in range(data_size)]    # Pitch angle data 


def moving_average(data, window_size):
    """
    Computes the window-size point moving-average value of the raw IMU data and calls the plot_data function to plot the data.

    Parameters
    ----------
    data : List
        List of integers containing the raw IMU pitch angle data
        
    window_size : int
        Window-size of the moving-average filter

    Returns
    -------
    None

    """
    imu_pitch_angle_smooth = []
    for i in range(0,data_size-window_size+1):
       sub_data = data[i:i+window_size]    # Slicing data into 'window-size' parts 
       avg = np.mean(sub_data)
       imu_pitch_angle_smooth.append(avg)

    return imu_pitch_angle_smooth



imu_pitch_angle_smooth = moving_average(imu_pitch_angle, 128)    # 128-pt moving average pitch angle data

# Representing the IMU sensor as a line in plot
x_raw = np.zeros(len(imu_pitch_angle))    # x-position of one end of IMU (raw data)
y_raw = np.zeros(len(imu_pitch_angle))    # y-position of one end of IMU (raw data)
x_smooth = np.zeros(len(imu_pitch_angle_smooth))    # x-position of one end of IMU (smooth data)
y_smooth = np.zeros(len(imu_pitch_angle_smooth))    # y-position of one end of IMU (smooth data)

for i,theta in enumerate(imu_pitch_angle, start=0):
    x_raw[i] = (imu_width/2)*np.cos(theta*(np.pi/180))    # x-coordinate of IMU (raw)
    y_raw[i] = (imu_width/2)*np.sin(theta*(np.pi/180))    # y-cooridnate of IMU (raw)

for i,theta in enumerate(imu_pitch_angle_smooth, start=0):
    x_smooth[i] = (imu_width/2)*np.cos(theta*(np.pi/180))    # x-coordinate of IMU (smooth)
    y_smooth[i] = (imu_width/2)*np.sin(theta*(np.pi/180))    # y-cooridnate of IMU (smooth)


# Plot handles for both raw and smooth data plots
fig_raw = plt.figure()
ax_raw = fig_raw.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-3,3), ylim=(-3,3))
ax_raw.grid()
ax_raw.set_title('ADXL327 Accel Pitch Angle Animation')

label_raw = ax_raw.text(0, 2, '', color="Red")
line_raw, = ax_raw.plot([], [], 'o-', lw=5, color='#000000')

fig_smooth = plt.figure()
ax_smooth = fig_smooth.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-3,3), ylim=(-3,3))
ax_smooth.grid()
ax_smooth.set_title('ADXL327 Accel Pitch Angle Animation')

label_smooth = ax_smooth.text(0, 2, '', color="Red")
line_smooth, = ax_smooth.plot([], [], 'o-', lw=5, color='#000000')


def raw_animate(i):
    """
    Generates the animation for raw data using the frame number. 

    Parameters
    ----------
    i: int
        Frame number

    Returns
    -------
    line: Tuple
        Line2D plot objects 

    """
    x_points = [-x_raw[i], 0, x_raw[i]]
    y_points = [-y_raw[i], 0, y_raw[i]]

    label_raw.set_text(f"Angle (deg): {np.round(imu_pitch_angle[i], decimals=2)}")
    line_raw.set_data(x_points, y_points)

    return line_raw, label_raw


def smooth_animate(i):
    """
    Generates the animation for smooth data using the frame number. 

    Parameters
    ----------
    i: int
        Frame number

    Returns
    -------
    line: Tuple
        Line2D plot objects 

    """
    x_points = [-x_smooth[i], 0, x_smooth[i]]
    y_points = [-y_smooth[i], 0, y_smooth[i]]

    label_smooth.set_text(f"Angle (deg): {np.round(imu_pitch_angle_smooth[i], decimals=2)}")
    line_smooth.set_data(x_points, y_points)

    return line_smooth, label_smooth


print("\nPlotting IMU data animation for raw data.")
raw_ani = animation.FuncAnimation(fig_raw, raw_animate, frames=len(x_raw)-1, interval=40, blit=True, repeat=False)
# raw_ani.save('IMU_animation_raw.mp4', fps=30)    # Uncomment to save video

print(f"\nPlotting IMU data animation for 128-pt moving average filter data.")
smooth_ani = animation.FuncAnimation(fig_smooth, smooth_animate, frames=len(x_smooth)-1, interval=40, blit=True, repeat=False)
# smooth_ani.save('IMU_animation_smooth.mp4', fps=30)    # Uncomment to save video

plt.show()