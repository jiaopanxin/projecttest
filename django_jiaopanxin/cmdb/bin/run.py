#!/usr/bin/env python3
import sys,os,requests
path=os.path.abspath(__file__)  #获取当前文件的绝对路径
path=os.path.dirname(path)   #只获取这个路径的目录
path=os.path.dirname(path)   #在一次执行这个，把bin去掉

Base_dir=path             #将这个路径作为基础路径
sys.path.insert(0,Base_dir)  #插入到sys.path中，导入模块时以这个路径为基础路径

from core.main import main  #导入core下的main模块的main对象


if __name__ == "__main__":
    info=main()    #实例化对象并且接受返回值
    print(info)
#    print(info)    #输出返回值
    requests.post(url="http://127.0.0.1:8000/cmdb/asset/",json=info)
