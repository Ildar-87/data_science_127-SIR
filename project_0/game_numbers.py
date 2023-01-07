import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0

low_point = 0
top_point = 100
predict_number = int((low_point + top_point)/2) # предполагаемое число

while True:
    count += 1
    
    if predict_number < number:
         low_point = predict_number   
         predict_number = int((predict_number + top_point)/2)              
    elif predict_number > number:
         top_point = predict_number
         predict_number = int((low_point + predict_number)/2)       
    else:
        print("Вы угадали, загаданное число:", predict_number) # выход из цикла, если угадали
        break
    
print("Количество попыток:", count)

