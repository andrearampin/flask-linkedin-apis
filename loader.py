import ConfigParser


######################
# Configuration Loader
######################
class ConfigLoader:
    config = None

    # Init Configuration Loader
    def __init__(self, path):
        self.config = ConfigParser.ConfigParser()
        self.config.read(path)

    # Retrieve data
    def get(self, section):
        dictionary = {}
        options = self.config.options(section)
        for option in options:
            try:
                dictionary[option] = self.config.get(section, option)
            except:
                dictionary[option] = None
        return dictionary
