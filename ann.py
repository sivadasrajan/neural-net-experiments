#https://github.com/tensorflow/playground/blob/master/src/nn.ts#L358
import random
import math
def activation_sigmoid(x):
    return 1/(1+math.exp(-x))

class Link:
    def __init__(self, src, dst):
        self.weight = random.uniform(-1, 1)
        self.src:Node = src
        self.dst:Node = dst
        self.err_derivative: float = 0

class Node:
    def __init__(self,):
        self.bias: float = 0.5
        self.input_links: Link = []
        self.output_links: Link = []
        
        # sum(weights*input) + bias
        self.total_input: float = 0

        #activation(total_input)
        self.output: float = 0

        self.input_derivative: float = 0
        self.output_derivative: float = 0
        
    def update_output(self):
        self.total_input = self.bias
        for link in self.input_links:
            self.total_input += link.weight*link.src.output
        self.output = activation_sigmoid(self.total_input)
        return self.output

class ErrorFunction:
    def error(self,target,computed):
        pass
    def derivative(self,target,computed):
        pass
class MeanSquare(ErrorFunction):
    def error(self, target, computed):
        return 0.5 * (math.pow(target-computed,2))
    def derivative(self, target, computed):
        return target - computed

class Network:
    def __init__(self):
        pass

    def buildNetwork(self, network_size: list):
        network = []
        for i in range(0, len(network_size)):

            is_output_layer = i == len(network_size)-1
            is_input_layer = i == 0
            layer = []

            for j in range(0, network_size[i]):
                new_node = Node()
                if i >= 1:
                    prevLayer = network[i-1]
                    for prev_node in prevLayer:
                        link = Link(prev_node, new_node)
                        new_node.input_links.append(link)                        
                        prev_node.output_links.append(link)
                layer.append(new_node)
            network.append(layer)
        self.network = network

    def print_network(self):
        for i,layer in enumerate(self.network):
            print("Layer",i)
            for j,node in enumerate(layer):
                print("\tNode",i,j)
                print("\t\tBias:",node.bias)
                print("\t\tOutput Weights: ",end='')
                for w in node.output_links:
                    print(round(w.weight,2),end=',')
                print("")
                print("\t\tInput Weights : ",end='')
                for w in node.input_links:
                    print(round(w.weight,2),end=',')
                print("")
                print("\t\tOutput: ",node.total_input)
                print("\t\tActivation: ",node.output)




    def forward_propagate(self,inputs:list):
        input_layer = self.network[0]
        
        if len(input_layer) != len(inputs):
            raise Exception("The number of inputs must match the number of nodes in the input layer")
        
        for i,node in enumerate(input_layer):
            node.output = inputs[i]
        for i in range(1,len(self.network)):
            current_layer = self.network[i]
            for j,node in enumerate(current_layer):
                node.update_output()
        
        return self.network[len(self.network) - 1][0].output

x  = Network()
x.buildNetwork([2,2])
x.print_network() 
print(x.forward_propagate([5,5]))
x.print_network() 

