## 无人机监测与跟踪项目

created by 黎鸿滔

#### 项目结构

- 整体结构依照：[projectTree.txt](projectTree.txt)
- yolov5：本次实验所采用的算法模型。
  - train.py：用于模型训练。
  - detect.py：训练完成后，用以测试数据。
  - data文件夹：存放数据配置文件，本次实验使用drone.yaml文件。
  - runs文件夹：存放训练以及测试（测试时，可更改路径）的结果，即训练后的模型和可视化数据。
- makeTestResults.py：在模型测试完毕后，生成任务结果。
-   makeTrainLabel.py：生成训练时所需要的标签格式信息。
-   空文件夹下存放有.gitkeep文件，目的在于保留其文件结构，可以在本地手动删除以防止干扰实验。

#### 实验步骤（操作系统：Windows 11）

1. 安装Anaconda3，创建实验所需环境（实验中Python版本为3.8）
2. 安装Pytorch，因为本次实验采用GPU训练模型，因此选用支持GPU的Pytorch版本，同时CUDA版本不得低于11.3：`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117`
3. 在激活环境后，进入到yolov5文件目录路径下，下载安装yolov5模型所需要的所有依赖（requirements.txt文件中关于torch和torchvision已被注释，因为默认下载CPU版本）：`pip install -r requirements.txt`
4. 执行makeTrainLabel.py，生成训练所需的标签文件
5. 修改train.py中参数，其中--weights表示预训练模型，采用yolov5s.pt，下载链接`https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt`，下载完成后将模型文件存放在与train.py同一目录下；--data表示数据配置文件，则使用data文件夹下的drone.yaml文件；--device表示使用CPU或GPU来训练模型，值为'cpu'时表示使用CPU，而为'0,1,2'等数字时，表示使用的GPU的设备号，从0开始计数，由于实验在本地环境下进行，因此只有一个GPU，因此设置值为0
6. 随后开始训练，训练完成后实验结果保存在runs/train/exp文件夹下，其中包括weights文件夹，包括训练得到的模型，其中last为最后一轮训练得到模型，best则是训练过程中，综合特征指标最优的模型，以及实验得到的可视化数据
7. 修改detect.py中参数，将--weights设置为训练得到的best.pt模型文件；--source表示待检测的目标图像文件或目录，并修改主函数，使得能对多目录下的图片集合进行检测，随后开始检测
8. 执行makeTestResults.py，生成任务所需的实验结果