from math import sin, cos
from typing import overload
from pylx16a.lx16a import LX16A
import time
import numpy as np
# from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

LX16A.initialize("COM3", 0.1)

#check for errors in each motor
for x in range (1,7):
    LX16A(x).servo_mode()
    LX16A(x).disable_torque()
        #set limits and functions
    def over_temp():
        if LX16A(x).get_temp()<40:
            return True
        else:
            return False
        
    def over_volt():
        if LX16A(x).get_vin()<5000:
            return True
        else:
            return False
    #errors set
    LX16A(x).set_led_error_triggers(over_temp(), over_volt(), LX16A(x).is_torque_enabled())
#get homing positions
    # while LX16A(1).get_physical_angle() < 83:
    #     LX16A(x).move(10,200)
    #     while LX16A(2).get_physical_angle() < 145:
    #         LX16A(x).move(10,200)

#Obtain position of the codes
#a = []
#b = []
#column names
columns = ['servo4','servo5','servo6']

#LX16A(x).get_physical_angle()
angles = np.zeros((6,100))
angles[0,0]
xdata = np.linspace(1,100,100)

t = 0
while t < 400:
    for i in range(100):
        for j in range(1,7):
            # LX16A(j).servo_mode()
            LX16A(1).disable_torque()
            LX16A(2).disable_torque()
            LX16A(3).disable_torque()
            LX16A(4).disable_torque()
            LX16A(5).disable_torque()
            LX16A(6).disable_torque()
            angles[j-1,i] = (LX16A(j).get_physical_angle())
        time.sleep(0.01)
        print(f"t = {t}")
        t += 0.01
        np.savetxt("Motor_position",angles,delimiter=",")
        #df.to_excel("C:/Users/User/OneDrive/Desktop/motor_position.xlsx", sheet_name='Sheet_name_1')
        #print('DataFrame is written to Excel File successfully.')
        
        
# y is another array which stores 3.45 times
# the sine of (values in x) * 1.334.
# The random.normal() draws random sample
# from normal (Gaussian) distribution to make
# them scatter across the base line
# angles[2] = 3.45 * np.sin(1.334 * xdata) + np.random.normal(size = 40)
 
# # Test function with coefficients as parameters
# def test(x, a, b):
#     return a * np.sin(b * x)
 
# # curve_fit() function takes the test-function
# # x-data and y-data as argument and returns
# # the coefficients a and b in param and
# # the estimated covariance of param in param_cov
# param, param_cov = curve_fit(test, x, angles[2])
 
 
# print("Sine function coefficients:")
# print(param)
# print("Covariance of coefficients:")
# print(param_cov)
 
# # ans stores the new y-data according to
# # the coefficients given by curve-fit() function
# ans = (param[0]*(np.sin(param[1]*x)))
 
'''Below 4 lines can be un-commented for plotting results
using matplotlib as shown in the first example. '''
 
# plt.plot(x, y, 'o', color ='red', label ="data")
# plt.plot(x, ans, '--', color ='blue', label ="optimized data")
# plt.legend()
# plt.show()


# def f1(a,b,c):
#     return a + b*sin(angles[0]+c)

# if t > 0.5: 
#     plt.plot([1,2,3,4,5],[5,4,3,2,1])
#     # plt.plot(angles[i,j])
#     plt.show()
