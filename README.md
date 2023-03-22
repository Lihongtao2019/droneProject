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
4. 执行makeTrainLabel.py，生成训练所需的标签文件存放于labels/train
5. 执行yolov5文件下detect.py，将会在labels/test文件夹下生成对应的test图像的标签
8. 执行makeTestResults.py，生成任务所需的实验结果