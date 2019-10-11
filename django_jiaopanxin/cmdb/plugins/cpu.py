import subprocess,os
path=os.path.dirname(os.path.abspath(__file__))
path+='/cpu_info.txt'
class Cpu:
    def run_cmd(self,cmd):
        stat, result = subprocess.getstatusoutput(cmd)
        if not stat:
            return result

    def cmd_handle(self):
        cpu_info = {}
        cpu_info['model_name'] = self.run_cmd("awk -F': ' '/model name/ {print $2}' " + path + " | tr  -s ' ' |tr ' ' '_' |uniq")
        cpu_info['cpu_type'] = self.run_cmd("uname -p")
        cpu_info['physical_count'] = self.run_cmd("awk -F': ' '/physical id/ {print $2}' "+ path+ " | sort -u|wc -l")
        cpu_info['cpu_cores'] = self.run_cmd("awk -F': ' '/cpu cores/ {print $2}' "+ path+" |uniq")
        return cpu_info
