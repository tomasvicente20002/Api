import configparser


class Source:
    def __init__(self):
        self.config = self.readconfig('../App/config.ini')
        
    def readconfig(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config