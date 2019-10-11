import django
import os
import sys

# 获取到项目的根目录
project_path = os.path.dirname(os.path.abspath('__file__'))
print(project_path)

# 把项目的根目录加到环境变量中
sys.path.insert(0, project_path)

# 设置环境变量
os.environ["DJANGO_SETTINGS_MODULE"] = 'qfgp01site.settings'
django.setup()

if __name__ == "__main__":
    """在这里写自己的测试代码"""
    # 导入 映射类
    from users.models import UsersProfile

    # 获取表中的第一条数据
    user = UsersProfile.objects.all().first()
    print(user.username, user.email)
