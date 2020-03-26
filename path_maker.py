import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def show_data(x,y,angle):
    
    for i in range(angle.size):
        l = 0.01
        x1 = x[i]
        y1 = y[i]
        x2 = l * math.cos(angle[i])
        y2 = l * math.sin(angle[i])
        plt.quiver(x1,y1,x2,y2)
    plt.plot(x,y,marker="o")
    plt.show()

def judge_inside_outside(p1,p2,p3):
    v_a = np.array(p1) - np.array(p3)
    v_b = np.array(p2) - np.array(p3)
    if np.dot(v_a,v_b) < 0:
        return True
    return False
        
def make_path(path_point,resolution):
    
    
    i = 1
    point_A = [path_point[i - 1][0],path_point[i - 1][1]]
    angle_A = path_point[i - 1][2]
    path = [[point_A[0],point_A[1],angle_A]]
    while  i  < path_point.shape[0]:    
        point_B = [path_point[i][0],path_point[i][1]]
        l = math.hypot(point_A[0] - point_B[0] , point_A[1] - point_B[1]) 
        
        l -= resolution
        
        new_point = [point_A[0] *  l / (resolution + l) +  
                     point_B[0] *  resolution / (resolution + l) ,
                     point_A[1] *  l / (resolution + l) +  
                     point_B[1] *  resolution / (resolution + l)]
        
        
        if (judge_inside_outside(point_A,point_B,new_point)):
            angle_B = path_point[i][2]
            new_angle = angle_A *  l / (resolution + l) + \
                        angle_B *  resolution / (resolution + l)
                        
            path.append([new_point[0],new_point[1],new_angle])
            
            point_A = new_point
            angle_A = new_angle
        else:
            i += 1
            
    return path
if __name__ == '__main__':
    
    #meter
    resolution_1 = 0.0001
    resolution_2 = 0.01
    input_file_name = "test.csv"
    output_file_name = "output.csv"
    
    df = pd.read_csv(input_file_name, names=["x","y","angle"])

    show_data(df["x"],df["y"],np.array(df["angle"]))
    
    print(df)
        
    temp_path = np.array([df["x"],df["y"],df["angle"]]).T
    
    path = make_path(temp_path , resolution_1)
    
    p_array = np.array(path).T
#    計算重くなるので簡易表示する
#    show_data(p_array[0],p_array[1],p_array[2])
    plt.plot(p_array[0],p_array[1],marker="o")
    plt.show()
    
    
    path = make_path(np.array(path) , resolution_2)
    
    p_array = np.array(path).T
    show_data(p_array[0],p_array[1],p_array[2])
    
    np.savetxt(output_file_name,path,delimiter=',')

