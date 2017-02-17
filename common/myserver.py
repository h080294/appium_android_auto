import os
from http.server import BaseHTTPRequestHandler,HTTPServer
from time import sleep
from common import operateFile
from configs.config import GetVariable as gv
from multiprocessing import Process
import pickle
from common import others
pid = 0


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        d_result = {}
        find_devices="devices"
        req = self.path.split('&')
        if req[0].find(find_devices) > 0:
            d_result["devices"] = req[0].split("=")[1]
        d_result["log"] = req[1].split("=")[1]
        others.write_pickle(d_result, gv.CRASH_LOG_PATH)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"Hello World !") #发送信息给客户端
        print("do_GET")

    def write_pickle(dict_data, path="data.pickle"):
        read = others.read_pickle(path)
        result = []
        if len(read) > 0:
            read.append(dict_data)
            result = read
        else:
            result.append(dict_data)
        with open(path, 'wb') as f:
            print(result)
            pickle.dump(result, f, 0)

    def read_pickle(path):
        data = {}
        if operateFile.OperateFile(path).check_file():
            with open(path, 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    pass
        print(data)
        return data


def open_web_server():
    server = HTTPServer((gv.HOST, gv.PORT), myHandler)
    print('Started httpserver on port ', gv.PORT)
    server.serve_forever()


def closed_web_server():
    sleep(3)
    command = "lsof -i:8088"
    r = os.popen(command)
    info = r.readlines()
    for line in info:  # 按行遍历
        eachline = line.split()
        server_pid = eachline[1]
        os.popen("kill " + server_pid)


if __name__=="__main__":
    p = Process(target=open_web_server, args=())
    p.start()
    # subprocess.Popen("taskkill /F /T /PID " + str(p.pid), shell=True)
    print("kkk")



