import math
import random

def mean(n):
    mean = 0
    for i in range(n):
        mean += i
    mean /=n
    return mean
def mean_loss_mae(n, target,predict):
    total_error = 0
    y = target
    y_hat = predict
    for i in range (n):
        absolute_error = abs(y - y_hat)
        total_error = total_error + absolute_error
    mean_absolute_error = total_error / n
    return mean_absolute_error

def mean_loss_mse(n,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    for i in range(n):
        squared_error = (y - y_hat)**2
        total_squared_error = total_squared_error + squared_error
    mean_squared_error = total_squared_error / n
    return mean_squared_error

def mean_loss_rmse(n,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    for i in range(n):
        squared_error = (y - y_hat)**2
        total_squared_error = total_squared_error + squared_error
    root_mean_squared_error = math.sqrt(total_squared_error / n)
    return root_mean_squared_error
def loss_mae(n, target,predict):
    total_error = 0
    y = target
    y_hat = predict
    for i in range (n):
        absolute_error = abs(y - y_hat)
        total_error = total_error + absolute_error
    return total_error

def loss_mse(n,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    for i in range(n):
        squared_error = (y - y_hat)**2
        total_squared_error = total_squared_error + squared_error
    return total_squared_error

def loss_rmse(n,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    for i in range(n):
        squared_error = (y - y_hat)**2
        total_squared_error = total_squared_error + squared_error
    return total_squared_error

if __name__ == "__main__":
    num_samples = input("enter number of samples: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
    else:
        n = int(num_samples)
        loss_name = ["mae", "mse", "rmse"]
        input_loss_name = input("enter loss name (mae, mse, rmse)").strip().lower()
        if input_loss_name not in loss_name:
            print(f"{input_loss_name} not found in loss name (mae, mse, rmse)")
        else:
                if input_loss_name == "mae":
                    for i  in range(n):
                        target = random.uniform(0,10)
                        predict = random.uniform(0,10)
                        result = mean_loss_mae(n, target,predict)
                        loss_name = "MAE"
                        print(f"loss name: {loss_name} , sample: {i}, pred: {predict} , target: {target} , loss: {loss_mae(n, target,predict)}")
                elif input_loss_name == "mse":
                     for i  in range(n):
                        target = random.uniform(0,10)
                        predict = random.uniform(0,10)
                        result = mean_loss_mse(n, target,predict)
                        loss_name = "MSE"
                        print(f"loss name: {loss_name} , sample: {i}, pred: {predict} , target: {target} , loss: {loss_mse(n, target,predict)}")
                elif input_loss_name == "rmse":
                     for i  in range(n):
                        target = random.uniform(0,10)
                        predict = random.uniform(0,10)
                        result = mean_loss_rmse(n, target,predict)
                        loss_name = "RMSE"
                        print(f"loss name: {loss_name} , sample: {i}, pred: {predict} , target: {target} , loss: {loss_rmse(n, target,predict)}")
                
                print(f"Final {loss_name}: {result}")
    
        
    