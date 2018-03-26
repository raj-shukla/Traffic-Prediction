import numpy as np
import matplotlib.pyplot as plt
import predictionData
np.set_printoptions(threshold=np.nan)



np.random.seed(1) 

X = predictionData.inputArray
Y = predictionData.outputArray



shape_X = np.shape(X)
shape_Y = np.shape(Y)
m = np.shape(X)[1]  



def layer_sizes(X, Y):
    n_x = np.shape(X)[0] 
    n_h = 4
    #n_y = np.shape(Y)[0] 
    n_y = 1
    return (n_x, n_h, n_y)



def initialize_parameters(n_x, n_h, n_y):

    np.random.seed(2) 

    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))


    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters



def forward_propagation(X, parameters):

    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']


    Z1 = np.dot(W1, X) + b1
    #A1 = np.tanh(Z1)
    A1 = 1/(1 + np.exp(-Z1))
    Z2 = np.dot(W2, A1) + b2
    A2 = 1/(1 + np.exp(-Z2))


    assert(A2.shape == (1, X.shape[1]))

    
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    
    return A2, cache



def compute_cost(A2, Y, parameters):
    
    #m = Y.shape[1] 
    m = Y.shape[0]

    logprobs = np.multiply(np.log(A2),Y) + np.multiply(np.log(1-A2),1-Y)
    cost = -np.sum(logprobs)/m    
    cost = np.squeeze(cost)    
    assert(isinstance(cost, float))
    return cost



def backward_propagation(parameters, cache, X, Y):
    m = X.shape[1]

    W1 = parameters['W1']
    W2 = parameters['W2']        
    A1 = cache['A1']
    A2 = cache['A2']


    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, keepdims = True, axis = 1)/m
    #dZ1 = np.dot(W2.T, dZ2)*(1 - np.power(A1, 2))
    dZ1 = np.dot(W2.T, dZ2)*(A1*(1-A1))
    dW1 = np.dot(dZ1, X.T)/m
    db1 = np.sum(dZ1, keepdims = True, axis = 1)/m

    
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads



def update_parameters(parameters, grads, learning_rate = 1.2):

    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    dW1 = grads['dW1']
    db1 = grads['db1']
    dW2 = grads['dW2']
    db2 = grads['db2']
    
    W1 = W1 - learning_rate*dW1
    b1 = b1 - learning_rate*db1
    W2 = W2 - learning_rate*dW2
    b2 = b2 - learning_rate*db2
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters



def nn_model(X, Y, n_h, num_iterations = 10000, print_cost=False):

    np.random.seed(3)
    n_x = layer_sizes(X, Y)[0]
    #n_y = layer_sizes(X, Y)[2]
    n_y = 1
    
    parameters = initialize_parameters(n_x, n_h, n_y)
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    for i in range(0, num_iterations):
         
        A2, cache = forward_propagation(X, parameters)
        
        cost = compute_cost(A2, Y, parameters)
 
        grads = backward_propagation(parameters, cache, X, Y)
 
        parameters = update_parameters(parameters, grads)

        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))

    return parameters



#X_assess, Y_assess = nn_model_test_case()
parameters = nn_model(X, Y, 4, num_iterations=10000, print_cost=True)
print("W1 = " + str(parameters["W1"]))
print("b1 = " + str(parameters["b1"]))
print("W2 = " + str(parameters["W2"]))
print("b2 = " + str(parameters["b2"]))



def predict(parameters, X):

    A2, cache = forward_propagation(X, parameters)
    predictions = A2
    
    return predictions



predictions = predict(parameters, X)
print("predictions")
print(predictions)
print(np.mean((np.sqrt((predictions - Y)*(predictions - Y)))/Y))



hidden_layer_sizes = [1, 2, 3, 4, 5, 20, 50]
for i, n_h in enumerate(hidden_layer_sizes):
    #plt.subplot(5, 2, i+1)
    #plt.title('Hidden Layer of size %d' % n_h)
    parameters = nn_model(X, Y, n_h, num_iterations = 5000)
    #plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
    predictions = predict(parameters, X)
    #accuracy = float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100)
    cost = compute_cost(predictions, Y, parameters)
    print ("Accuracy for {} hidden units: {} %".format(n_h, cost))




