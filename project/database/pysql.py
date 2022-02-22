#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
import json,os,sys,codecs
import pymysql

version = 2
if sys.version_info >= (3,3):
    version = 3

#print("now python version:"+str(version))

if version == 2:
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
else:
    pass


class MYSQL:
    def __init__(self,host,user,password,db,port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = int(port)
        self.cur = self.__GetConnect()
        
    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.db,port=self.port,charset="utf8mb4")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        
        查询有返回的意思
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                formwork_mysql = MYSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                result_list = formwork_mysql.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in result_list:
                    print str(id),NickName
        """
        cur = self.cur
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        result_list = cur.fetchall()

        return result_list
        
    def ExecQueryDict(self,sql):
        "Return all rows from a cursor as a dict"
        cur = self.cur
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        #result_list = cur.fetchall()
        columns = [col[0] for col in cur.description]
        return [
            dict(zip(columns, row))
            for row in cur.fetchall()
        ]

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.cur
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        self.conn.commit()
    
    def ExecQueryClose(self,sql):
        cur = self.cur
        cur.execute(sql)
        result_list = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return result_list

    def ExecNonQueryClose(self,sql):
        cur = self.cur
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def Close(self):
        self.conn.close()
        
    def secure_word_list(self):
        wordlist = ["'",'"',">","<","{","}",")","(","=",",",";","and","*","%","&","#","$","/"," \ ".replace(" ",""),"select",'from',"values","insert","into","update","like","set","delete","LIKE","AND","SELECT","FROM","VALUES","INSERT","INTO","UPDATE","SET","DELETE","AND","SELECT"]
        return wordlist
    
        
    def secure(self,string):
        for word in self.secure_word_list():
            string.replace(word,"")
        return string
       
#-usage-########################################  
#-usage-########################################     
# formwork_mysql = MYSQL(host="1.1.1.1",user="root",pwd="formwork_password",db="formwork_db")
# result_list= formwork_mysql.ExecQuery("SELECT A,B,C FROM formwork_table_name")
# for ( A,B,C ) in result_list:
#     print A,B,C
# #增加
# formwork_mysql.ExecNonQuery( "insert into formwork_table_name(A,B,C) values('{0}','{1}','{2}')".format(u"aa",u"bb",u"cc") )
# #减少
# formwork_mysql.ExecNonQuery( '''delete from formwork_table_name where A like "{0}"'''.format(u",,") )
# #改
# formwork_mysql.ExecNonQuery( '''update formwork_table_name set {2} = "{3}" where {0}="{1}"'''.format(u"aa",u"bb","cc","dd") )

# result_list = formwork_mysql.ExecQuery("SELECT A,B,C FROM formwork_table_name")
# for ( A,B,C) in result_list:
#     print A,B,C
    
# formwork_mysql.Close()
#-usage-########################################
#-usage-########################################

