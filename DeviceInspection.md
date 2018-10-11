# 设备巡检python脚本

## 采集信息内容

| 信息名称        | 文本示例            | 正则表达式                      | 子组号 |
| --------------- | ------------------- | ------------------------------- | ------ |
| Hostname        | DLC_JC_0105_3560B   | (?<=hostname\s)(.*)             | 1      |
| MGMT_IP         | 10.10.83.3          | ^Vlan.*(10.10.\d{1,3}.\d{1,3})  | 1      |
| SN              | FDO1507V07X         | ^System serial number.*?(\w+)   | 1      |
| Model           | WS-C3560V2-48TS     | ^Model number.*?(\w+.*)         | 1      |
| Software_Verion | Version 12.2(50)SE1 | ^Cisco\sIOS.*Version\s(.*)..REL | 1      |
| CPU_Usage       | 7%                  | ^CPU.*?(\d{1,3}%)               | 1      |
| MEM_Total       | 85443596            | ^Processor.*?(\d+)\sUsed        | 1      |
| MEM_Usage       | 17230416            | ^Processor.*?(\d+)\sFree        | 1      |
| MEM_Free        | 68213180            | ^Processor.*Free:\s+(\d+)       | 1      |
| FAN             | OK                  | ^FAN\sis\s(\w+)                 | 1      |
| TEMPERATURE     | OK                  | ^TEMPERATURE\sis\s(\w+)         | 1      |
| Power           | GOOD                | Built-in\s+(\w+)                | 1      |



## 相关文件

* **待巡检文件**: 通过相关巡检命令,从网络设备收集的log文件
* **待巡检文件所在目录**: 当待巡检文件数量校大可以集中放入一个目录,以便进行指巡检
* **巡检配置文件**: 巡检配置文件为CSV格式文件, 第一列为巡检字段名称, 第二列为正则表达式, 第三列为默认值(可选)
* **巡检报告输出目录**: 用于输出巡检报告



## 类和方法的定义

```python
from collections import OrderedDict

class DeviceInspector(obj):
    inspect_para = OrderedDict()
    log_f = None
    report = OrderedDict()
    
    def __init__(self, log_f, para_dict):
   		self.log_f = log_f
        self.inspect_para = para_dict
    
    
```
