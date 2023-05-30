import random 
import csv
import numpy as np

class Layer:
   
    def __init__(self,n = 1):
        self.n = n
        self.weights = []
        self.biases = []
        self.outputs = []
        for i in range(0,n):
            self.weights.append(random.uniform(-1, 1))
            self.biases.append(random.uniform(-1, 1))
            self.outputs.append(None)

 
    def calculate_output(self,prev_outputs):
        for j in range(0,self.n):
            for i,output_value in enumerate(prev_outputs):
                self.outputs[j] = self.weights[j]*output_value + self.biases[j]
        self.print_outputs()

        return self

    def print_outputs(self):
        print('[',end='')
        for x in self.outputs:
            print(round(x,2),end=',')
        print(']',end='\n')




with open('iris-mini.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("row----------")
        print([float(row['sepal_length']),float(row['sepal_width']),float(row['petal_length']),float(row['petal_width'])])
        input_layer = [float(row['sepal_length']),float(row['sepal_width']),float(row['petal_length']),float(row['petal_width'])]
        h1 = Layer(10).calculate_output(input_layer)
        h2 = Layer(15).calculate_output(h1.outputs)
        h3 = Layer(3).calculate_output(h2.outputs)

        h3.outputs 