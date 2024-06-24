#Hàm lấy và kiểm tra input từ user
def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            int_input = int(user_input)
            if int_input > 0:
                return int_input
            else:
                print("Input value must be greater than 0!")
        except ValueError:
            print("Invalid input, please enter an integer!")

#Hàm tính toán các chỉ số đánh giá
def calculate_evaluate_classification_model(tp,fp,fn):
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    F1Score = 2 * (precision*recall) / (precision+recall)
    print(f"fp: {fp}")
    print(f"fn: {fn}")
    print(f"tp: {tp}")
    print(f'Precision: {precision:.4f}')
    print(f"recall: {recall:.4f}")
    print(f"F1-Score: {F1Score:.4f}")

#Nhận input từ user
tp = get_user_input("Nhap vao tp: ")
fp = get_user_input("Nhap vao fp: ")
fn = get_user_input("Nhap vao fn: ")

#Gọi hàm tính các chỉ số đánh giá
calculate_evaluate_classification_model(tp,fp,fn)