#coding:utf-8
class CommonFn(object):
    def __init__(self):
        pass
    
    #打印对象所有集合
    def prn_obj(self,obj):
        print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
        