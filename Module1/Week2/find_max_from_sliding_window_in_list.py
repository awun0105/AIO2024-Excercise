def get_user_input(prompt):
  while True:
    try:
      user_input = input(prompt)
      int_input = int(user_input)
      return int_input
    except ValueError:
      print("Invalid input, please enter an integer!")
def create_list_from_user_input():
  num_list = []
  user_input_n = get_user_input("Nhap vao so luong phan tu muon tao trong danh sach: ")
  for i in range(user_input_n):
    user_input_num = get_user_input(f"Nhap phan tu thu {i}: ")
    num_list.append(user_input_num)
  return num_list

def find_max(my_list):
  max = 0
  for i in range(len(my_list)):
    if my_list[i] > max:
      max = my_list[i]
  return max

def find_max_from_sliding_window_in_list(my_list, k):
  result_list = []
  for i in range(len(my_list) - k + 1):
      temp_list = my_list[i:i+k]
      max_value = find_max(temp_list)
      print(f"{temp_list} => max: {max_value}")
      result_list.append(max_value)
  return result_list

if __name__ == "__main__":
  num_list = create_list_from_user_input()
  user_input_k = get_user_input("Nhap vao k: ")
  if(user_input_k >= 1):
    result_list = find_max_from_sliding_window_in_list(num_list,user_input_k)
    print(f"Output: {result_list}")
  else:
    print("K khong duoc nho hon 1")
  
