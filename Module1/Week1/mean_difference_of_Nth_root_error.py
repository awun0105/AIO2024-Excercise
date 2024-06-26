import math
import random

def loss_MD_nRE(m,n,p,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    root_y = y **(1/n)
    root_y_hat = y_hat **(1/n)
    difference = root_y - root_y_hat 
    loss = difference**p
    return loss
def mean_loss_MD_nRE(m,n,target,predict):
    total_squared_error = 0
    y = target
    y_hat = predict
    for i in range(m):
        root_y = y **(1/n)
        root_y_hat = y_hat **(1/n)
        difference = root_y - root_y_hat 
        loss = difference**p
    total_mean_loss_MD_nRE = loss / m
    return total_mean_loss_MD_nRE
