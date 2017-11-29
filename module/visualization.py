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

def visualize(table=None):

##    length = len(table)
##    x = np.linspace(1, 40000, 40000)
##
##    poly_deg = 10
##    coefs = np.polyfit(x, table.iloc[:, 9], poly_deg)
##    y_poly = np.polyval(coefs, x)
##    plt.plot(x, y_poly, label='Polynomial Fit')
    
    plt.plot(table.iloc[:, 9], label='Data Points')
    plt.title('Temperature vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Temperature (C)')
    plt.legend()
    plt.show()

    plt.plot(table.iloc[:, 8])
    plt.title('Brightness vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Brightness')
    plt.show()

    plt.plot(table.iloc[:, 10])
    plt.title('Humidity vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Humidity')
    plt.show()

    plt.plot(table.iloc[:, 11])
    plt.title('x Acceleration vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('x Acceleration')
    plt.show()

    plt.plot(table.iloc[:, 12])
    plt.title('y Acceleration vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('y Acceleration')
    plt.show()

    plt.plot(table.iloc[:, 13])
    plt.title('z Acceleration vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('z Acceleration')
    plt.show()

    plt.plot(table.iloc[:, 14])
    plt.title('x  Gyro vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('x Gyro')
    plt.show()

    plt.plot(table.iloc[:, 15])
    plt.title('y  Gyro vs. Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('y Gyro')
    plt.show()

    plt.plot(table.iloc[:, 16])
    plt.title('z  Gyro vs. Time')
    plt.xlabel('Time')
    plt.ylabel('z Gyro')
    plt.show()

def calculate_movement(table=None):

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
    
    cd = '/Users/ericyates/Documents/Processing/base_processing/Data/'

    path = cd + '2017y-11m-16d-9h-12m.csv'

    root = tk.Tk()
    ui = LoadFile(root)
    ui.mainloop()
    root.destroy()

    path = ui.path


    df_table = pd.read_csv(path)
    np_table = df_table.as_matrix()

    np_table = calculate_movement(table=np_table)

    df_table = pd.DataFrame(np_table)

    visualize(table=df_table)
