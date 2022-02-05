# imu_moving_average.py
"""
Author: Adarsh Malapaka (amalapak@umd.edu), 2022
Brief: Code to load IMU data (ADXL327 3-axis accelerometer) from file 
       and plot raw and moving-average filtered pitch angle data
Course: ENPM809T - Autonomous Robotics [HW01]
Date: 3rd February, 2022
"""

# Required packages
import numpy as np
import matplotlib.pyplot as plt

# Loading the data from 'imudata.txt'
file_name = 'imudata.txt'
imu_raw_data = np.loadtxt(file_name, delimiter=' ', dtype=str)    # Loaded data size: 371 by 7 
print(f"Loaded IMU data from file: {file_name}.")

data_size = np.shape(imu_raw_data)[0]

imu_pitch_angle = [int(imu_raw_data[i][4]) for i in range(data_size)]    # Pitch angle data 


def plot_data(data, window_size, smooth_data):
    """
    Plots the ADXL accelerometer pitch angle data (raw and filtered) and displays the 
    mean and standard deviation of the data on the plot for the chosen window-size of 
    the moving-average filter.

    Parameters
    ----------
    data : List
        List of integers containing the raw IMU pitch angle data
        
    window_size : int
        Window-size of the moving-average filter

    smooth_data : List
        List of integers containing the smoothened IMU pitch angle data

    Returns
    -------
    None

    """
    imu_data_avg = np.round(np.average(smooth_data), decimals=4)    # Mean of filtered data
    imu_data_std = np.round(np.std(smooth_data), decimals=4)    # Std. Dev of filtered data

    print(f"\nMean of IMU data for {window_size}-pt filtered data: {imu_data_avg}.")
    print(f"Standard Deviation of IMU data for {window_size}-pt filtered data: {imu_data_std}.")

    plt.plot(range(data_size),data,'b', range(len(smooth_data)),smooth_data,'r')
    plt.axis([0, data_size, 0, max(data)])
    plt.xlabel('Sample')
    plt.ylabel('Pitch Angle (deg)')
    plt.title('ADXL327 Accel Pitch Angle Plot')
    plt.legend(['Raw Data', f'{window_size}-pt Moving Average Data'])

    # Placing Mean and Std dev of raw & filtered data in the plot
    plt.text(100.0, 1.7, f"Mean: {imu_data_avg} deg\nStd Dev: {imu_data_std} deg",
        verticalalignment='top', horizontalalignment='left', color='red', fontsize=9)    
    plt.text(220.0, 1.7, f"Mean: {np.round(np.average(data), decimals=4)} deg\nStd Dev: {np.round(np.std(data), decimals=4)} deg",
        verticalalignment='top', horizontalalignment='left', color='blue', fontsize=9) 
    plt.show()
    print(f"Plotting IMU data for {window_size}-pt moving average filter.")


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

    plot_data(data, window_size, imu_pitch_angle_smooth)


if __name__ == "__main__":

    # Moving-average for 2, 4, 8, 16, 64, 128 points
    i = 2
    while i <= 128:
        if i is not 32:
            moving_average(imu_pitch_angle, i)
        i = i*2
