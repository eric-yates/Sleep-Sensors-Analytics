# bed-science

Collecting and analyzing data to improve restedness level from sleep.

## Overview

### Problem

I've been having poor quality sleep and wake up feeling unrested with "adequate hours" of sleep.

### Target Measures

  1) Movement Level: Objective measure of overall amount of movement during sleep (higher = more movement).
  2) Restedness Level: Subjective measure of how rested I feel after waking up (higher = more rested).

### Hypotheses

  1) Lower movement level correlates with increased restedness level.
  2) Movement level will be lower with lower ambient light levels.
  3) Movement level will be lower with temperatures in the low 60's Fahrenheit.
  4) Movement level will be lower with decreased amount of caffeine consumption.
  5) Movement level will be lower with longer time between consumption and sleep time.
  6) Higher duration of sleep will correlate with higher restedness level.

### Data Sources

  1) Accelerometer: Tracks x/y/z accelerator and x/y/z angular velocity
  2) Photoresistor: Track ambient light levels
  3) Temperature Sensor: Tracks temperature in celsius
  4) Humidity Sensor: Tracks relative humidity


## Getting Started

These instructions will get a copy of the project up and running on your local machine.

### Prerequisites

Instructions for installing these software are listed in the next section: Installing. These are the software packages needed to run:

* Arduino IDE
* Processing
* Python **2.7**

These Python packages are also needed:

* Tkinter
* numpy
* pandas
* matplotlib

From a hardware perspective, the following are needed:

* Arduino board

### Installing

Download the latest version of the Arduino IDE [here](https://www.arduino.cc/en/Main/Software). 

Then, download the latest version of Processing [here](https://processing.org/download/).

If your computer does not already have Python **2.7** installed, download it [here](https://www.python.org/downloads/).

By default, Python should come with pip (a package manager). Use it to install the following dependencies by opening the Terminal/command line and entering the commands as follows, each line as a separate command (make sure to capitalize Tkinter):

```
pip install Tkinter
pip install numpy
pip install pandas
pip install matplotlib
```


## Usage

### 

### Searching for Jobs Other than Data Scientist




## Built With

* [Arduino](https://www.arduino.cc/en/Guide/Introduction) - A hardware/software board to collect sensor data
* [SoftwareSerial](https://www.arduino.cc/en/Reference/softwareSerial) - Arduino library for serial communication
* [Processing](https://processing.org/overview/) - A sketchbook for visual arts with simple Arduino integration
* [Python](https://www.python.org/about/) - A programming language used here to create exploratory data graphs
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Python library for graphical user interfaces (GUI)
* [Numpy](http://www.numpy.org/) - Python library for mathematical and matrix operations 
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - Python library for data manipulation
* [Matplotlib](https://matplotlib.org/) - Python library for graphing data


## Authors

* **Eric Yates** - [Github Profile](https://github.com/eric-yates)

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details.

## Acknowledgments

* **B_E_N**: For his [tutorial](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing) on connecting Arduino to Processing  
