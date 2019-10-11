import subprocess,os
path=os.path.dirname(os.path.abspath(__file__))
path+='/R710-Memory-info'
class Memory():
    def __init__(self, debug=True):
        self.file = path
        if debug:
            self.cmd = "grep -v '^$' %s" % self.file
        else:
            self.cmd = "dmidecode -q -t 17|grep -v '^$' "
        self.debug = debug

    def run_cmd(self, cmd):
        stat, result = subprocess.getstatusoutput(cmd)
        if not stat:
            return self.parse(result)
        else:
            print('命令错误')
            return result

    def parse(self, data):
        info_mem = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',
        }
        memory_list = [mem for mem in data.split('Memory Device') if mem]

        for item in memory_list:
            single_slot = {}

            for line in item.splitlines():
                line = line.strip()
                if len(line.split(':')) == 2:
                    key, val = line.split(':')
                    key, val = key.strip(), val.strip()
                    if key in key_map:
                        single_slot[key_map[key]] = val
            # print(single_slot)
            info_mem[single_slot["slot"]]=single_slot
        return info_mem

    def cmd_handle(self):
        return self.run_cmd(self.cmd)

if __name__ == '__main__':
    mem_obj = Memory()
    info = mem_obj.cmd_handle()
