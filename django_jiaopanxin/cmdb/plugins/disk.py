import os,subprocess
path=os.path.dirname(os.path.abspath(__file__))
path+='/R710-disk-info'

class Disk:
    def __init__(self,debug=False):
        self.file=path
        if debug==False:
            self.cmd="grep -v '^$' %s " % self.file 

        self.debug=debug
    
    def run_cmd(self,cmd):
        stat,result=subprocess.getstatusoutput(cmd)
        if not stat:
            return self.prase(result)
        else:
            print("命令错误")
            return result

    def prase(self,data):
        disk_infos={}
        disk_map={
            "Slot Number":"slot",
            "PD Type":"type",
            "Raw Size":"size"
        }
        disk_list=[disk for disk in data.split("Enclosure Device") if disk]
        for disk in disk_list:
            disk_info={}
            for line in disk.splitlines():
                line=line.strip()
                if len(line.split(':')) == 2:
                    key,val=line.split(':')
                    if 'Size' in key:
                        key,val=key.strip(),' '.join(val.split()[:-2])
                    else:
                        key,val=key.strip(),val.strip()
                    if key in disk_map:
                        disk_info[disk_map[key]]=val
            disk_infos[disk_info["slot"]]=disk_info 
        return disk_infos
        
        

    def cmd_handle(self):
        info=self.run_cmd(self.cmd)
        return info





