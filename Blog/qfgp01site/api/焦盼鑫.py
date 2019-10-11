import os


class existence_ping:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def run_cmd(self, cmd):
        stat = os.system(cmd)
        return stat

    def prints(self, data):
        if not data:
            print("该网段没有连续工作的ip")
        else:
            for ip in data[::2]:
                next_ip = data[data.index(ip)+1]
                print(f"{ip}------------{next_ip}之间能ping通")

    def cmd_handle(self):
        result = []  # 列表内存放的是 能ping通的起始和结束ip
        count = 0  # count  代表连续能ping通的ip数
        for ip in range(self.start, self.end+1):
            stat = self.run_cmd(f"ping 10.0.122.{ip} -c1 -i 0.5 &> /dev/null")
            if not stat:  # ping通了
                if len(result) % 2 == 0:  # 长度为偶数
                    result.append(ip)  # 把第一个能ping通的加上去
                    continue
                count += 1  # 长度为奇数的话  count+1   count代表连续能ping通的ip的间隔
            else:  # ping不通
                if len(result) % 2 == 1:  # 列长度为奇数
                    if count:  # 有连续的
                        result.append(result[-1]+count)  # 添加截至ip
                        count = 0  # 恢复默认
                    else:  # 没有连续的  代表ip不是一个段  只是一个ip能通
                        result.pop()  # 删除添加的那一个
        else:
            if len(result) % 2 == 1:   
                result.pop()
        self.prints(result)


existence_ping(30, 40).cmd_handle()
