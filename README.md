# bed-science

Collecting and analyzing data to improve restedness level from sleep.

## Overview

### Problem

I've been having poor quality sleep and wake up feeling unrested with "adequate hours" of sleep.

### Target Measures

* Movement Level: Objective measure of overall amount of movement during sleep (higher = more movement).
* Restedness Level: Subjective measure of how rested I feel after waking up (higher = more rested).

### Hypotheses

* Lower movement level correlates with increased restedness level.
* Movement level will be lower with lower ambient light levels.
* Movement level will be lower with temperatures in the low 60's Fahrenheit.
* Movement level will be lower with decreased amount of caffeine consumption.
* Movement level will be lower with longer time between consumption and sleep time.
* Higher duration of sleep will correlate with higher restedness level.

### Data Sources

* Accelerometer: Tracks x/y/z accelerator and x/y/z angular velocity
* Photoresistor: Track ambient light levels
* Temperature Sensor: Tracks temperature in celsius
* Humidity Sensor: Tracks relative humidity


## Getting Started

These instructions will get a copy of the project up and running on your local machine.

### Prerequisites

Instructions for installing these software are listed in the next section: Installing. These are the software packages needed to run:

* Arduino IDE
* i2cdevlib
* Processing
* Python **2.7**

These Python packages are also needed:

* Tkinter
* numpy
* pandas
* matplotlib

From a hardware perspective, the following are needed:

* Arduino board: The [Arduino Uno](https://www.amazon.com/Arduino-Uno-R3-Microcontroller-A000066/dp/B008GRTSV6) is a good option
* Breadboard: Something like [this](https://www.amazon.com/BB400-Solderless-Plug-BreadBoard-tie-points/dp/B0040Z1ERO)
* MPU 6050: Accelerometer available for purchase from [Amazon](https://www.amazon.com/MPU-6050-MPU6050-Accelerometer-Gyroscope-Converter/dp/B008BOPN40) and more information from [Arduino](https://playground.arduino.cc/Main/MPU-6050)
* DHT22: Temperature/humidity sensor available for purchase from [Amazon](https://www.amazon.com/SMAKN%C2%AE-Digital-Temperature-Humidity-Measurement/dp/B00MIBRFTI) or [Adafruit](https://www.adafruit.com/product/385)
* Photoresistor: Any type should do. This one from [Adafruit](https://www.adafruit.com/product/161) will work
* Male-to-male ribbon cable: Something like [this](https://www.amazon.com/40pcs-Color-Ribbon-Jumper-Arduino/dp/B00DFVD1TS)

### Installing

Download the latest version of the Arduino IDE [here](https://www.arduino.cc/en/Main/Software). 

Download the latest version of i2cdevlib [here](https://github.com/jrowberg/i2cdevlib), following the instructions provided in the README.

Download the latest version of Processing [here](https://processing.org/download/).

If your computer does not already have Python **2.7** installed, download it [here](https://www.python.org/downloads/).

By default, Python should come with pip (a package manager). Use it to install the following dependencies by opening the Terminal/command line and entering the commands as follows, each line as a separate command (make sure to capitalize Tkinter):

```
pip install Tkinter
pip install numpy
pip install pandas
pip install matplotlib
```


## Usage

### Basic


## Built With

* [Arduino](https://www.arduino.cc/en/Guide/Introduction) - A hardware/software board to collect sensor data
* [i2cdevlib](https://github.com/jrowberg/i2cdevlib) - Library for interfacing with MPU6050 accelerometer
* [SoftwareSerial](https://www.arduino.cc/en/Reference/softwareSerial) - (Built in) Arduino library for serial communication
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
* **Elaine Laguerta**: For her [tutorial](http://www.hackerscapes.com/2014/11/how-to-save-data-from-arduino-to-a-csv-file-using-processing/) on saving Arduino data to a CSV file using Processing
