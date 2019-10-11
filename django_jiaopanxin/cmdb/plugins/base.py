import pymysql,subprocess

class Base:
    def run_cmd(self,cmd):
        stat, result = subprocess.getstatusoutput(cmd)
        if not stat:
            return self.parse(result)

    def parse(self,data):
        if data.endswith('_'):
            data = data[:-1]
        return data

    """
    操作系统  uname -s 
    系统架构  uname -m
    系统版本信息  cat /etc/redhat-release
    主机名      hostname
    内核信息   uname -r
    """

    def cmd_handle(self):
        result = {
            'os_name': self.run_cmd('uname -s').strip(),
            'machine': self.run_cmd("uname -m").strip(),
            'os_version': self.run_cmd("cat /etc/redhat-release || cat /etc/issue").strip().split('\n')[0],
            'host_name': self.run_cmd("hostname").strip(),
            'kernel': self.run_cmd('uname -r')
        }
        return result


result = Base().cmd_handle()
#print(result)
