import os
import cv2
import numpy as np
path = 'D:/mango_abc/val/A/'
path1 = 'D:/val/mango_kernel_sharpen/A/'



folder_content = os.listdir(path)
print(folder_content)


for i in range(len(folder_content)):

    image = cv2.imread(path + folder_content[i])

    #自定義卷積核
    #img_Guassian = cv2.GaussianBlur(image,(3,3),0)
    kernel_sharpen_1 = np.array([
            [-2,-1,0],
            [-1,1,1],
            [0.5,1,1.8]])

    #卷積
    output_1 = cv2.filter2D(image ,-1,kernel_sharpen_1)
    #output_2 = cv2.filter2D(image,-1,kernel_sharpen_2)
    #output_3 = cv2.filter2D(image,-1,kernel_sharpen_3)
    #顯示銳化效果

    #cv2.imshow('Original Image',image)
    #cv2.imshow(folder_content[i],output_1)
    #cv2.imshow('sharpen_2 Image',output_2)
    #cv2.imshow('sharpen_3 Image',output_3)
    cv2.imwrite(path1+folder_content[i],output_1)
#停頓
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
