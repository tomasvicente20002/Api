import configparser

class Configuration:
    def __init__(self,file_name = ""):
        self.config = self.readconfig('config.ini' if file_name == '' else file_name)
        
    def readconfig(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config

    def get_database_name(self):
        return self.config["DATABASE"]["name"]


