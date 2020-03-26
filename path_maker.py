import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#meter
resolution_1 = 0.001
resolution_2 = 0.2
read_file_name = "test.csv"

df = pd.read_csv(read_file_name, names=["x","y"])
plt.plot(df["x"],df["y"],marker="o")
plt.show()

print(df)

def judge_inside_outside(p1,p2,p3):
    v_a = np.array(p1) - np.array(p3)
    v_b = np.array(p2) - np.array(p3)
    if np.dot(v_a,v_b) < 0:
        return True
    return False
        
def make_path(path_point,resolution):
    
    
    i = 1
    point_A = [path_point[i - 1][0],path_point[i - 1][1]]
    path = [point_A]
    while  i  < path_point.shape[0]:    
        point_B = [path_point[i][0],path_point[i][1]]
        l = math.hypot(point_A[0] - point_B[0] , point_A[1] - point_B[1]) 
        
        if (l < resolution):
            i += 1
            continue
        
        l -= resolution
        
        new_point = [point_A[0] *  l / (resolution + l) +  
                     point_B[0] *  resolution / (resolution + l) ,
                     point_A[1] *  l / (resolution + l) +  
                     point_B[1] *  resolution / (resolution + l)]
        
        
        if (judge_inside_outside(point_A,point_B,new_point)):
            path.append(new_point)
            point_A = new_point
        else:
            i += 1
            
    return path
        
temp_path = np.array([df["x"],df["y"]]).T

path = make_path(temp_path , resolution_1)

p_array = np.array(path).T
plt.plot(p_array[0],p_array[1],marker="o")
plt.show()


path = make_path(np.array(path) , resolution_2)

p_array = np.array(path).T
plt.plot(p_array[0],p_array[1],marker="o")
plt.show()
