# -*- coding: utf-8 -*-

import random
import re

from Util import EnvUtil
from DB.DbClient import DbClient
from Config.ConfigGetter import config
from Util.LogHandler import LogHandler

class UserAgentManager(object):
    def __init__(self):
        self.db = DbClient()
        self.useragent_queue = 'whatismybrowser'
        self.log = LogHandler('useragent_manager')

    def get(self):
        """
        return a useful proxy
        :return:
        """
        self.db.changeTable(self.useragent_queue)
        item_dict = self.db.getAllUserAgent()
        if item_dict:
            if EnvUtil.PY3:
                pattern = re.compile(r"'.*?'|\".*?\"")
                item_dict = random.choice(item_dict)
                item_dict = pattern.findall(str(item_dict))
                if item_dict != []:
                    return random.choice(item_dict)[1:-1]
            else:
                return random.choice(random.choice(item_dict))
        return None

if __name__ == '__main__':
    uam = UserAgentManager()