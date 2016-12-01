# -*-coding=utf-8-*-
__author__ = 'Rocky'
#每天的涨跌停
#url=http://stock.jrj.com.cn/tzzs/zdtwdj/zdforce.shtml
import urllib2,re
class GetZDT():
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"

        #self.url='http://stock.jrj.com.cn/tzzs/zdtwdj/zdforce.shtml'
        #self.url='http://home.flashdata2.jrj.com.cn/limitStatistic/ztForce/20161201.js'
        self.url='http://home.flashdata2.jrj.com.cn/limitStatistic/ztForce/20161201.js'
        self.host="home.flashdata2.jrj.com.cn"
        self.reference="http://stock.jrj.com.cn/tzzs/zdtwdj/zdforce.shtml"
        self.header = {"User-Agent": self.user_agent,"DNT":"1","Host":self.host,"Referer":self.reference}
        #self.getData()

    def getData(self):
        req=urllib2.Request(headers=self.header,url=self.url)
        resp=urllib2.urlopen(req)
        content= resp.read()
        return content

    def fetchData(self):
        p=re.compile(r'"Data":(.*)};',re.S)
        #temp_content=open("zdt.html",'r').read()
        #print temp_content
        content=self.getData()
        result=p.findall(content)
        t1= result[0]
        t2=list(eval(t1))
        #print type(t2)
        #print t2
        '''
        for i in t2:
            for j in i:
                print j
        '''
        return t2


    def storeData(self):
        data=self.fetchData()
        print data

if __name__=='__main__':
    obj=GetZDT()
    obj.storeData()

