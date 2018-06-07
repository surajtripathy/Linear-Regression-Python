import csv
import matplotlib.pyplot as plt

#Importing the training dataset and modifying it
with open("train.csv") as train_file:
    train_data = csv.reader(train_file, delimiter =',')
    x_train = []
    y_train = []
    c = 0
    for row in train_data:
        x_train_temp,y_train_temp = row
        if c >= 1:
            x_train_temp = int(x_train_temp)
            y_train_temp = float(y_train_temp)
            x_train.append(x_train_temp)
            y_train.append(y_train_temp)
        c +=1
#print(x_train)
#print(y_train)
        
plt.scatter(x_train, y_train,  color='black')
plt.show()

#Calculating min error for every possibility of m and c
def change(line_m,line_c_temp,learn_rate,iter):
    err_mpos_cpos = 0
    err_mpos_cneg = 0
    err_change_mpos_cpos = []
    err_change_mpos_cneg = []
    for m_change in range(iter):
        line_c_pos = line_c_temp
        line_c_neg = line_c_temp
        for c_change in range(iter):
            for i in range((c-1)):
                y_pred_mpos_cpos = line_m*x_train[i] + line_c_pos
                err_temp = y_train[i] - y_pred_mpos_cpos
                err_sqr_mpos_cpos = err_temp * err_temp
                err_mpos_cpos = err_mpos_cpos + err_sqr_mpos_cpos

                y_pred_mpos_cneg = line_m*x_train[i] + line_c_neg
                err_temp = y_train[i] - y_pred_mpos_cneg
                err_sqr_mpos_cneg = err_temp * err_temp
                err_mpos_cneg = err_mpos_cneg + err_sqr_mpos_cneg

            err_mpos_cpos = err_mpos_cpos/(c-1)
            err_mpos_cneg = err_mpos_cneg/(c-1)
            err_change_mpos_cpos.append(err_mpos_cpos)
            err_change_mpos_cneg.append(err_mpos_cneg)
            line_c_pos = line_c_pos + learn_rate
            line_c_neg = line_c_neg - learn_rate
        line_m = line_m + learn_rate
    return err_change_mpos_cpos, err_change_mpos_cneg

#Finding the corresponding m and c of min error
def find(line_m,line_c,position,learn_rate,iter, c_sign):
    dummy_pos = 0
    line_c_temp = line_c
    #print(position)
    broken = False
    for m_change in range(iter):
        line_c = line_c_temp
        for c_change in range(iter):
            if dummy_pos == position:
                broken = True
                #print(dummy_pos)
                break
            dummy_pos += 1
            if c_sign == True:
                line_c = line_c + learn_rate
            elif c_sign == False:
                line_c = line_c - learn_rate
        if broken == True:
            if c_sign == True:
                line_c = line_c - learn_rate
            elif c_sign == False:
                line_c = line_c + learn_rate
            break
        line_m = line_m + learn_rate
    return line_m,line_c
                
    
    
    
err_calculate_mpos_cpos,err_calculate_mpos_cneg = change(0.0,0.0,0.001,1000)
#print(err_calculate)
min_err_mpos_cpos = min(err_calculate_mpos_cpos)
min_err_mpos_cneg = min(err_calculate_mpos_cneg)


if min_err_mpos_cpos < min_err_mpos_cneg:
    #print(min_err_mpos_cpos)
    position = err_calculate_mpos_cpos.index(min_err_mpos_cpos)
    line_m, line_c = find(0.0, 0.0, position, 0.001, 1000, True)
    print(line_m, line_c)
elif min_err_mpos_cneg < min_err_mpos_cpos:
    #print(min_err_mpos_cneg)
    position = err_calculate_mpos_cneg.index(min_err_mpos_cneg)
    line_m, line_c = find(0.0, 0.0, position, 0.001, 1000, False)
    print(line_m, line_c)
#print(position)
#Importing the test dataset and modifying it
with open("test.csv") as test_file:
    test_data = csv.reader(test_file, delimiter =',')
    x_test = []
    y_test = []
    c2 = 0
    for row in test_data:
        x_test_temp,y_test_temp = row
        if c2 >= 1:
            x_test_temp = int(x_test_temp)
            y_test_temp = float(y_test_temp)
            x_test.append(x_test_temp)
            y_test.append(y_test_temp)
        c2 +=1
plt.scatter(x_test, y_test,  color='black')
plt.show()

y = []
err_pred = 0
for i in range((c2-1)):
    y_pred = line_m*x_test[i] + line_c
    error = y_test[i] - y_pred
    #print(y_pred)
    temp = error*error
    err_pred = err_pred + temp
    y.append(y_pred)
err_pred = err_pred/(c2-1)
print(err_pred)
#plt.scatter(x_test,y)
#plt.show()