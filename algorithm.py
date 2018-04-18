import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
import predictionData
import functions

#layers_dims = [5, 20, 7, 5, 1] 
layers_dims = [20, 25, 25, 1] 

def L_layer_model(X, Y, layers_dims, learning_rate = 1.5, num_iterations = 10000, print_cost=False):#lr was 0.009

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
            
    #plt.ylabel('cost')
    #plt.xlabel('iterations (per tens)')
    #plt.title("Learning rate =" + str(learning_rate))
    #plt.show()
    
    return parameters


train_x = predictionData.inputData[:, 0:4000]
train_y = predictionData.outputData[:, 0:4000]
test_x = predictionData.inputData[:, 4000:4600]
test_y = predictionData.outputData[:, 4000:4600]
test_y_List = predictionData.outputList 


parameters = L_layer_model(train_x, train_y, layers_dims, num_iterations = 10000, print_cost = True)
pred_test, cost = functions.predict(test_x, test_y, parameters)


print(pred_test)
print(cost)
print(np.shape(pred_test))
print(np.shape(test_y))

for i in range(0, 12):
    print(np.shape(test_y_List[i]))
    pred_test, cost = functions.predict(test_x, test_y_List[i][:, 4000:4600], parameters)
    test_x[0] = pred_test
    print (cost)

'''
plt.figure(1)
x = np.arange(0, 500)
plt.plot(x, pred_test[0], 'bs', label='Predicted') 
plt.plot( x, test_y[0], 'g^', label='Actual')
plt.gca().legend(('Predicted','Actual'))
plt.xlabel("Time slot")
plt.ylabel("Normalized traffic")

plt.figure(2)
x = np.arange(0, 500)
plt.plot(pred_test[0]-test_y[0] )
#plt.axis([0, 1000, 0, 0.050])
plt.xlabel("Time slot")
plt.ylabel("Error")
plt.show()
#pred_test = predict(test_x, test_y, parameters)
'''
