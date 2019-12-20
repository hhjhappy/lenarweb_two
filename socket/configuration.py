import os
import configparser

#读取配置文件，并返回字典

class configValue():
    def __init__(self,config,sections = None):
        self.config = config
        self.sections = sections

    def getValue(self):
        if os.path.isfile(self.config):
            cf = configparser.ConfigParser()
            cf.read(self.config)
            try:
                return dict(cf.items(self.sections))
            except configparser.Error as error:
                print(error)
