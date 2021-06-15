import cv2
import pickle
import numpy as np
import os
def pickleloadtotxt(data,folder, index):
    '''
        parameters:
            data: 深度图片数据
            folder：存储目录
            index: 存储图片索引
        function:
            将深度图片大小变为 （425，512），过滤掉距离小于1m或者大于2m的距离信息，存储为png图片
    '''
    #print(data.shape)
    data=data.astype(np.uint8)
    data=np.reshape(data,(424, 512))  #单位 mm，表示物体到摄像头距离
    data[data<200]=0
    data[data>2000]=0
    #data=data/1000.0000
    #np.savetxt("1.txt",data,fmt='%s',delimiter=' ')   #存储到txt文件，用于观察数据
    #用于显示深度数据
    cv2.imshow('imgOri',data)   #如果把范围之外设置为0，图片表示就比较明显
    #cv2.waitKey(0)  #  这个得敲击esc 才进行下一张图片显示
    #用于存储到png图片中
    cv2.imwrite("{}/{}.png".format(folder,index),data)   #如果范围之外设置为0，这里看的不明显，基本全黑，如果设置5000，存储的图片看的就比较明显
    #data = cv2.cvtColor(data, cv2.COLOR_GRAY2RGB)
    #print(data.shape)
    #cv2.imwrite("color.png",data)



def dataload(filename):
    datafile = open( filename + ".pickle", "rb")
    # datafile = open("DEPTH." + FILE_NAME + ".pickle", "rb")
    frame = pickle.load(datafile)
    #pickleloadtotxt(frame)

def depth2video(FILE_NAME):
    print("stiching colour frames into video")
    
    #Load first colour frame, to get colour frame properties
    datafile = open( FILE_NAME + ".pickle", "rb")
    # datafile = open("DEPTH." + FILE_NAME + ".pickle", "rb")
    frame = pickle.load(datafile)
    frame=np.reshape(frame,(424, 512))
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    height, width,channels= frame.shape
    print( (int(width), int(height)))
    
    #define video properties
    out = cv2.VideoWriter(FILE_NAME + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, (int(width), int(height)))   #todo 这里存储出现问题
    
    #display first frame on a screen for progress (some duplication of later code as first frame needs to be loaded seperately to the rest so we can get the frame dimensions from it)
    out.write(frame)
    cv2.imshow('Stiching Video',frame)

    #Cycle through the rest of the colour frames, stiching them together
    while True:
        try:
            frame = pickle.load(datafile)
            frame=np.reshape(frame,(424, 512))
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            out.write(frame)
            cv2.imshow('Stiching Video',frame)
            if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
                break
        except EOFError:
            print("Video Stiching Finished")
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()


def frames_to_video(FILE_NAME):
    """Code to stitch a video based on frames saved in a pickle file"""
    
    print("stiching colour frames into video")
    
    #Load first colour frame, to get colour frame properties
    datafile = open( FILE_NAME + ".pickle", "rb")
    # datafile = open("DEPTH." + FILE_NAME + ".pickle", "rb")
    frame = pickle.load(datafile)
    print(type(frame),frame.shape)
    height, width, channels = frame.shape
    
    #define video properties
    out = cv2.VideoWriter(FILE_NAME + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, (int(width), int(height))) 
    
    #display first frame on a screen for progress (some duplication of later code as first frame needs to be loaded seperately to the rest so we can get the frame dimensions from it)
    out.write(frame)
    cv2.imshow('Stiching Video',frame)

    #Cycle through the rest of the colour frames, stiching them together
    while True:
        try:
            frame = pickle.load(datafile)
            out.write(frame)
            cv2.imshow('Stiching Video',frame)
            if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
                break
        except EOFError:
            print("Video Stiching Finished")
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

def depthToPNG(filename,folder):
    datafile = open( filename + ".pickle", "rb")
    isExists=os.path.exists(folder)
    if not isExists:
        os.makedirs(folder) 
    # datafile = open("DEPTH." + FILE_NAME + ".pickle", "rb")
    index=0
    while True:
        try:
            frame = pickle.load(datafile)
            pickleloadtotxt(frame,folder,index)
            index=index+1
            if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
                break
        except EOFError:
            print("Video Stiching Finished")
            break

    # Release everything if job is finished
    cv2.destroyAllWindows()
    
if __name__ == '__main__': 
    
    #replace name below with the corresponding section of the name of your saved depth data (for reference, the full name of my saved colour data file was COLOUR.test.1.29.13.17.pickle)
    #frames_to_video('COLOUR.temp.13.6.21.54')
    #depth2video('DEPTH.temp.13.6.21.54')
    depthToPNG('DEPTH.w.15.6.10.53',"temp")