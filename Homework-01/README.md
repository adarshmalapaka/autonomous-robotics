# IMU Data Visualization and Moving Average Filter 

Consider a small ground robot using an [ADXL327 3-axis accelerometer](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl327.pdf) as part of its navigational
sensor suite. A sample of the data packets streamed from the robot to the control station
are in the file, _imudata.txt_. Each data packet contains the date and time of transmission along
with a series of sensor readings that pertain to the robot’s navigation. The data packet was 
collected with the vehicle at rest, in an effort to calibrate the accelerometer.

This is an implementation of loading and plotting the raw accelerometer data using Python, which is 
observed to be noisy. An n-point moving average filter for this raw data is implemented and plotted 
along with the raw data.   


## Plots

### Noisy Accelerometer Data
<p align="center">
  <img src="https://user-images.githubusercontent.com/40534801/152654801-f57005ab-c682-4b24-84f7-d44349357ae0.png" width="50%">
<\p>
  
### Moving-Averaged Data [^1]
2-point Moving Average    |  4-point Moving Average| 8-point Moving Average
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/152653989-e5469af7-f4b4-46a5-9279-03f7b8047b78.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/152653994-e6678372-4e7d-4a4c-9a8e-a7642b665eda.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/152654004-568639e4-d70c-470c-a2e8-338da17a64ee.png" width="100%">

16-point Moving Average   |  64-point Moving Average | 128-point Moving Average
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/152654031-d21b85bf-58bd-4749-a3bc-0042be8cb9a3.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/152654038-4c0cc6ed-c8d2-4c4f-91bd-3fece0942b55.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/152654040-bab9549f-7efb-4c8c-8ca2-a3b94970c569.png" width="100%">

### Animation [^2]
Raw Data    |  128-pt Moving Average
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/152650470-e4976922-4414-44d7-bf7b-c752b0ece5a1.gif" width="80%"> | <img src="https://user-images.githubusercontent.com/40534801/152650775-5c7f566b-0c81-44b0-ba33-068dc40c3842.gif" width="80%">

  
## Packages Used
- Python 3.7.11
- Matplotlib 3.5.0
- NumPy 1.21.2

  
## Code Execution

* Clone the repository
  ```
  git clone --recursive https://github.com/adarshmalapaka/autonomous-robotics.git
  ```
* Navigate to the Homework-01 folder containing the python scripts and `imudata.txt` file.

* Run the `imu_moving_average.py`file by:
  ```
  python imu_moving_average.py
  ```

* The matplotlib plots corresponding to 2-, 4-, 8-, 16-, 64- and 128-point moving averaged data are obtained.

* For the IMU animation, run the `imu_moving_average_animation.py`file by:
  ```
  python imu_moving_average_animation.py
  ```
    This displays a matplotlib animation of the IMU sensor with both the raw data and the 128-point moving averaged data. 
    Uncomment lines 141 and 145 to save the animation as MP4 videos. 

[^1]: Since, the data is assumed to have already been obtained and then the moving average filter is implemented, the plots 
    for both raw and filtered data start at the same time. If this were to be implemented for live sensor data, the filtered
    plot would start _window-size_ points later than the raw data. 
    
[^2]: Reference: https://pythonforundergradengineers.com/offset-piston-motion-animation-matplotlib.html
<!-- ## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>
 -->
