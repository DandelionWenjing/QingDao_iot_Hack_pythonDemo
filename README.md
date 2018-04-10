# QingDao_iot_OpenHack_pythonDemo  

该demo为[Openhack](https://github.com/Nick287/IoT-Hastfest-Qingdao)挑战的参考

## 挑战1

- 步骤 1 - 在 Azure 门户中创建一个 IoT Hub  
直接参考文档完成Azure门户中iot hub的创建

- 步骤 2 - 向IoT Hub发送消息
在物联网技术实际场景使用中，我们需要利用设备与云端进行通信。为了更好的对接设备，我们需要在本地PC机上模拟设备进行数据上传。  
因此，发送消息之前，我们需要创建设备标识，参考如下两种方法：  
1. 在Azure 门户中[创建设备](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-csharp-csharp-device-management-get-started)
2. 参考代码中CreateDeviceIdentity.py，使用iot hub SDK创建设备标识

- 步骤 3 - 使用Azure IoT Hub Device Explorer检查数据上传结果  
在挑战一环节中，我们需要如下几个步骤进行在Azure平台上创建iot hub服务，创建设备标识，。
创建设备标识有多种方法：我们可以通过在Azure门户中创建  
该挑战可以参考CreateDeviceIdentity.py文件创建设备的

## 挑战2

- 步骤 1 模拟5列云霄飞车数据并且数据上传到 IoT Hub

步骤 2 Stream Processing / 流分析

步骤 3 Data Archival / 数据归档

步骤 4 生成报告
