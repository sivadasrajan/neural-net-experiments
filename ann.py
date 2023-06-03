#https://github.com/tensorflow/playground/blob/master/src/nn.ts#L358
import random
import math


class ErrorFunction:
    def error(self,target,computed):
        pass
    def derivative(self,target,computed):
        pass
class ActivationFunction:
    def activation(self,input):
        pass
    def derivative(self,input):
        pass


class MeanSquareError(ErrorFunction):
    def error(self, target, computed):
        return 0.5 * (math.pow(computed-target,2))
    def derivative(self, target, computed):
        return computed - target

class ReLU(ActivationFunction):
    def activation(self, input):
        return math.max(input,0)
    def derivative(self, input):
        return  input <= 0 if 0 else 1


class Link:
    def __init__(self, src, dst):
        self.weight = random.uniform(-1, 1)
        self.src:Node = src
        self.dst:Node = dst
        self.err_derivative: float = 0
        self.err_derivative_sum: float = 0
        self.err_derivative_count: float = 0

class Node:
    def __init__(self,activation_fn = ReLU()):
        self.bias: float = 0.5
        self.input_links: Link = []
        self.output_links: Link = []
        self.activation_fn = activation_fn
        # sum(weights*input) + bias
        self.total_input: float = 0

        #activation(total_input)
        self.output: float = 0

        self.input_derivative: float = 0
        self.output_derivative: float = 0

        self.input_derivative_sum = 0
        self.input_derivative_count = 0

        
    def update_output(self):
        self.total_input = self.bias
        for link in self.input_links:
            self.total_input += link.weight*link.src.output
        self.output = activation_sigmoid(self.total_input)
        return self.output

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
    
    def back_propagate(self,target,error_fn = MeanSquareError()):
        network_length = len(self.network)
        op_node = self.network[network_length - 1][0]
        op_node.output_derivative = error_fn.derivative(target, op_node.output)

        # length - 1 to 1 because layer 0 is input layer
        for i in range(network_length-1,0,-1):
            current_layer = self.network[i]
            for node in current_layer:
                node.input_derivative = node.output_derivative * node.activation_fn.derivative(node.total_input)
                node.input_derivative_sum += node.input_derivative
                node.input_derivative_count += 1
            for node in current_layer:
                for i_link in node.input_links:
                    i_link.err_derivative = node.input_derivative * i_link.src.output
                    i_link.err_derivative_sum += i_link.err_derivative
                    i_link.err_derivative_count += 1
            # becasue i = 0 is input layer                
            if i == 1:
                continue

            prev_layer = self.network[i-1]
            for node in prev_layer:
                node.output_derivative = 0
                for o_link in node.output_links:
                    node.output_derivative += output_links.weight * output.dst.input_derivative
    def update_weights(self,learning_rate = 0.05):
        for i in range(1,len(self.network)):
            current_layer = self.network[i]
            for node in current_layer:
                if node.input_derivative_count > 0:
                    node.bias -= learning_rate * (node.input_derivative_sum / node.input_derivative_count)
                    node.input_derivative_sum = 0
                    node.input_derivative_count = 0
                
                for input_link in node.input_links:

                    #TODO : Regularization

                    if input_link.err_derivative_count > 0:
                        input_link.weight = input_link.weight - (learning_rate/input_link.err_derivative_count) * input_link.err_derivative_sum
                    #TODO : Regularization

                    input_link.err_derivative_count = 0
                    input_link.err_derivative_sum = 0



x  = Network()
x.buildNetwork([2,2])
x.print_network() 
print(x.forward_propagate([5,5]))
x.print_network() 

