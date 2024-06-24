import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid_function(x):
    try:
        return  1 / (1 + math.exp(-x))
    except OverflowError:
        return 0.0  # Đối với giá trị rất lớn, trả về gần 0

def relu_function(x):
    return max(0,x)

def elu_function(x, alpha = 0.01):
    return x if x >= 0 else alpha * (math.exp(x) - 1)

if __name__ == "__main__":
    x = input("Nhap vao x: ")
    
    # Kiểm tra x có hợp lệ không
    if not is_number(x):
        print("x must be a number")
    else:
        x = float(x)
        if x > 0:
            activation_function = input("Nhap ten activation function (sigmoid, relu, elu): ").strip().lower()
            
            # Kiểm tra tên activation function có hợp lệ không
            if activation_function not in ["sigmoid", "relu", "elu"]:
                print(f"{activation_function} is not supported")
            else:
                # Tính giá trị f(x) theo hàm kích hoạt tương ứng
                if activation_function == "sigmoid":
                    result = sigmoid_function(x)
                elif activation_function == "relu":
                    result = relu_function(x)
                elif activation_function == "elu":
                    result = elu_function(x)
                
                print(f"{activation_function}: f({x})={result}")