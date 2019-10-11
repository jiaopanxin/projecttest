import importlib     #第一行是内置模块

#第二行三方模块

#第三行导入自定义模块
from conf.settings import PLUGINS_DIC as plugins   #导入配置文件内的settings内的字典

def main():
    server_dict={}   #定义一个字典
    for key,val in plugins.items():  #循环字典
        mod_path,cls_name= val.rsplit('.',1)  #对字典的值反转切割一个
        mod_obj=importlib.import_module(mod_path) #python的反射机制        使用字符串导入一个模块对象     等同与import plugins.cpu
        cls=getattr(mod_obj,cls_name)            #获得导入的包的中的类对象
        info =cls().cmd_handle()            #实例化类并且调用cmd_handle函数
        server_dict[key]=info   #将所有输出信息嵌套在一个字典李
    return server_dict   #返回大字典
