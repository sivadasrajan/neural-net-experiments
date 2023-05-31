import random 
from math import exp
from math import pow
class Layer:
   
    def __init__(self,nodes_in = 1,nodes_out = 1):
        self.nodes_in = nodes_in
        self.nodes_out = nodes_out
        self.inputs  = []
        self.weights = []
        self.biases = []
        self.outputs = []
        self.activations = []
        for i in range(0,nodes_in*nodes_out):
            self.weights.append(random.uniform(-1, 1))
        for i in range(0,nodes_out):
            self.biases.append(random.uniform(-1, 1))
            self.outputs.append(None)
            self.activations.append(None)

 
    def calculate_output(self,inputs):
        weighted_outs = []

        for i in range(0,self.nodes_out):
            for i in range(0,self.nodes_in):


        for 
        self.print_outputs()
        return self

    def get_weight(self,node_in,node_out):
        return self.weights[node_out * self.n]

    def sigmoid(self,z):
        return 1 / (1 + exp(-1 * z))

    def print_outputs(self):
        print('[',end='')
        for x in self.outputs:
            print(round(x,2),end=',')
        print(']',end='\n')

    def mse(self,one_hot):
        loss = []
        for i,output in enumerate(self.outputs):
            loss.append(pow(one_hot[i] - output,2))
        return loss #/ len(one_hot)
    
    def gradient_for_weight(self,one_hot):
        gradient = []
        for i,weight in enumerate(self.weights):
            temp = (2/len(one_hot)) * (one_hot[i] - self.outputs[i])
            temp *= (self.activations[i]*(1-self.activations[i]))
            gr1.append(temp)
        return  gr1

    


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