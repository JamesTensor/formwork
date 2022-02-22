#coding=utf-8
import sys,os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))

class third_function:
    def __init__(self):
        pass
    def get_serial(self):
        serial = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-7:])
        return serial
    def g_s(self):
        return self.get_serial()
    def sentence_request(self,request):
        if request.method == "GET":
            getpostdict = request.args.to_dict()
        if request.method == "POST":
            getpostdict = request.form.to_dict()
        return getpostdict
    def s_r(self,request):
        return self.sentence_request(request)   
    def handle_number(self,f):
        return '%.2f'% (f) 
    def h_n(self,f):
        return self.handle_number(f)
    def is_chinese(self,word):
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False