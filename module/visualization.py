"""
This module provides basic visualization of the sensor data:
temperature, humidity, brightness, x/y/z acceleration, and
x/y/z angular velocity. These graphs are useful for exploratory
data analysis.

The 'base-arduino' module collects the data from sensors. Then, the
'base-processing' module stores the sensor data into a CSV file.
Finally, this module plots the sensor data.

The tkinter library is used to choose which CSV file to open. The
pandas library reads the CSV. The numpy library is used to clean up
the sensor data. The matplotlib.pyplot library plots the sensor data
into various graphs.
"""

import pandas as pd
import numpy as np
import Tkinter as tk

from tkFileDialog import askopenfilename as tkopen

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class LoadFile(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.path = ''

        self.init_widgets()
        self.arrange()

    def init_widgets(self):

        self.okButton = tk.Button(root, text='OK', command=self.quit)
        self.cancelButton = tk.Button(root, text='Cancel', command=self.cancel)
        self.quitButton = tk.Button(root, text='Quit', command=self.quit)

        root.update()
        
        self.path = tkopen(initialdir = cd,
                           title = 'Select sleep table to open.',
                           filetypes = (("CSV Files", "*.csv"),
                                        ("All Files", "*.*")))

        self.text = tk.Text(root, height=5, width=len(self.path)+20, wrap=tk.WORD)
        self.text.insert(tk.INSERT, "Selected File: \n \n" + self.path)

    def arrange(self):
        
        self.cancelButton.grid(row=3, sticky='W', padx=55)
        self.okButton.grid(row=3, sticky='W', padx=4)
        self.quitButton.grid(row=3, sticky='E', padx=10)
        self.text.grid(row=1, sticky='W')

    def cancel(self):
        
        self.path = tkopen(initialdir = "/", title = "Select file",
                           filetypes = ((self.loadType + " Files",
                                         "*."+ self.loadType.lower()),
                                        ("All Files","*.*")))
        
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.INSERT, "Selected File: \n \n" + self.path)

    def quit(self):
        
        root.quit()

def graph(table=None, index=9, label=None, title=None,
            xlabel='Time (seconds)', ylabel=None):

    if not title:
        plt.title('Table[' + str(index) + ']')

    else:
        plt.title(title)

    plt.plot(table.iloc[:, index], label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def fit_poly(table=None):

    length = len(table)
    x = np.linspace(1, 40000, 40000)

    poly_deg = 10
    coefs = np.polyfit(x, table.iloc[:, 9], poly_deg)
    y_poly = np.polyval(coefs, x)
    plt.plot(x, y_poly, label='Polynomial Fit')

def trim_gyro(table=None):

    length = len(table)

    dev = 0

    for j in [14, 15, 16]:
        average = np.mean(table[:, j])
        
        for i in xrange(length):
            if average - dev < table[i][j] < average + dev:
                table[i][j] = average
            i += 1

    return table
    
if __name__ == "__main__":
    
    # Choose the directory containing the CSV files.
    cd = # Typically in the Processing directory.

    root = tk.Tk()
    ui = LoadFile(root)
    ui.mainloop()
    root.destroy()
    
    df_table = pd.read_csv(ui.path)
    np_table = df_table.as_matrix()

    # Trims noise from gyrometer values (angular velocity)
    np_table = trim_gyro(table=np_table)

    df_table = pd.DataFrame(np_table)

    # Temperature
    graph(table=df_table, index=9, ylabel='Temperature (C)')

    # Humidity
    graph(table=df_table, index=8, ylabel='Humidity (%)')

    # Brightness
    graph(table=df_table, index=10, ylabel='Brightness (Ohms)')

    # x Acceleration
    graph(table=df_table, index=11, ylabel='x Acceleration')

    # y Acceleration
    graph(table=df_table, index=12, ylabel='y Acceleration')

    # z Acceleration
    graph(table=df_table, index=13, ylabel='z Acceleration')

    # x Angular Velocity
    graph(table=df_table, index=14, ylabel='x Angular Velocity')

    # y Angular Velocity
    graph(table=df_table, index=15, ylabel='y Angular Velocity')

    # z Angular Velocity
    graph(table=df_table, index=16, ylabel='z Angular Velocity')
