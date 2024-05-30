import sys
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

def read_values_from_file(filename):
    x_values=[]
    y_values=[]
    try:
        data = pd.read_csv(filename)
        x_values=data['x'].tolist()
        y_values=data['f(x)'].tolist()
        return x_values, y_values
    except FileNotFoundError:
        print("File not Found")
        sys.exit(1)
    except Exception as e:
        print("Error while reading: ",e)
        sys.exit(1)
        
def plot_with_values(x_values,y_values, input_string='y=f(x)'):
    plt.plot(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(input_string)
    plt.grid(True)
    plt.show()
    
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите имя файла с данными в качестве аргумента командной строки.")
        sys.exit(1)
    
    args_lentgh=0
    for arg in sys.argv[1:]:
        args_lentgh+=1
    
    file_name = sys.argv[1]
    x_arr, y_arr = read_values_from_file(file_name)
    if (args_lentgh>1):
        input_string=str(sys.argv[2])
        plot_with_values(x_arr,y_arr, input_string)
    else:
        plot_with_values(x_arr,y_arr)
        
