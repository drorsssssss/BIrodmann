from pyhocon import ConfigFactory


class ConfigUtils:
    def __init__(self,conf_file_path):
        self.conf_file_path=conf_file_path

    def get_conf(self):
        return ConfigFactory.parse_file(self.conf_file_path)



