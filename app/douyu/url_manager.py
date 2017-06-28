#coding:utf-8
        
class UrlManager(object):
    def __init__(self):
        self.url = ''
    
    def has_new_url(self):
        return self.url != ''

    
    def get_new_url(self):
        if self.url == '':
            return None
        
        return self.url

    
    def add_new_url(self,url):
        self.url = url