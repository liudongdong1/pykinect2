### 1 Environment

- Windows 10
- Anaconda 64-bit（32-bit is ok）
- NumPy
- comtypes==1.1.4
- PyGame

## 2 Preparation

1. Install Kinect for Windows SDK v2 [Baidu Yun](https://pan.baidu.com/s/1i0VZkBdmeofV8MatbzQHfA) Code:p73c

2. Install PyKinect2 [Git](https://github.com/Kinect/PyKinect2)

   Anaconda 64-bit version: copy ./pykinect2 to path/to/your/Anaconda/site-package

   Anaconda 32-bit version:

   ```shell
   pip install pykinect2 comtypes numpy pygame
   ```
>如果使用pip安装，注意需要替换pip kinect2安装包的的PyKinectRuntime.py和PyKinectV2.py文件，由于python3.8中time函数进行了改变，time.clock（）功那移除，所以尽量使用python 3.6或者一下版本
## 3 Run

1. read RGB frames and Depth frames

```
cd ./demo
python read_stream.py
```

2. read RGB frames and Depth frames (RGB and Depth are mapped) and save it in ./result

```
cd ./demo
python mapper.py
```

#### 4 Resource From

- https://github.com/Kinect/PyKinect2
- https://github.com/NklausMikealson/Python-Kinectv2