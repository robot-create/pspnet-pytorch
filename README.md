## PSPnet：Pyramid Scene Parsing Network语义分割模型在Pytorch当中的实现
---

## 目录
1. [所需环境 Environment](#所需环境)
2. [文件下载 Download](#文件下载)
3. [预测步骤 How2predict](#预测步骤)
4. [注意事项 Attention](#注意事项)
5. [参考资料 Reference](#Reference)


## 所需环境
torch==1.6.0   
默认使用cuda，可以将其设置为False关闭使用CPU训练（pspnet.py）

## 文件下载
预测所需的模型Epoch99-Total_Loss0.7430-Val_Loss0.7276.pth可在百度网盘下载：   
链接: https://pan.baidu.com/s/1GUZTtrRzTOdd98yKaJKq7A 提取码: ic06   

VOC拓展数据集的百度网盘如下：  
链接: https://pan.baidu.com/s/1BrR7AUM1XJvPWjKMIy2uEw 提取码: vszf    
## 预测步骤
### 使用预训练权重
在百度网盘下载Epoch99-Total_Loss0.7430-Val_Loss0.7276.pth，放入model_data，直接运行predict.py就可以了；输入。  
```python
img/street.jpg
```  
### 注意    
可以预测图像、视频和调用摄像头，具体用法，见predict.py文件内注释

## 注意事项
代码中的new.py和utils1.py文件是用于streamlit平台展示，运行时，在终端输入
```
streamlit run new.py
```  

## Reference
https://github.com/bubbliiiing/pspnet-pytorch
