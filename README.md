这是原子格林函数求解石墨烯声子透射率的一个例子。下面是详细的步骤。
1. 使用phonopy计算简谐力常数 ----> FORCE_CONSTANTS
2. 使用phonopy生成的SPOSCAR文件，将体系划分成(left lead, scattering region, and rightlead)三个区域 ---->layer_map
3. 运行脚本hm.py，获得相互作用矩阵
4. 运行脚本agf.py，获得声子透射率
