import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
import predictionData
import functions

#layers_dims = [5, 20, 7, 5, 1] 
layers_dims = [5, 4, 1] 

def L_layer_model(X, Y, layers_dims, learning_rate = 1.2, num_iterations = 3000, print_cost=False):#lr was 0.009

    np.random.seed(1)
    costs = []                  
    
    parameters = functions.initialize_parameters_deep(layers_dims)
    
    for i in range(0, num_iterations):

        AL, caches = functions.L_model_forward(X, parameters)
        
        cost = functions.compute_cost(AL, Y)
    
        grads = functions.L_model_backward(AL, Y, caches)
 
        parameters = functions.update_parameters(parameters, grads, learning_rate)
                
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)
            
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    
    return parameters
train_x = predictionData.inputArray
train_y = predictionData.outputArray

parameters = L_layer_model(train_x, train_y, layers_dims, num_iterations = 2500, print_cost = True)
pred_train, cost = functions.predict(train_x, train_y, parameters)
print(pred_train)
print(cost)
#pred_test = predict(test_x, test_y, parameters)
