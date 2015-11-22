#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.config import Config
from cached_property import cached_property_ttl, cached_property

class EnjoyCmsConfig(Config):
    """Flask Config 从配置文件或者数据库获取变量"""

    @cached_property
    def store(self):
        return dict(self)


    @cached_property_ttl(300)
    def all_setings_from_db(self):
        pass






    def load_enjoyCms_config(self, config=None, mode=None, test=None, **sets):
        self.from_object(config or 'enjoycms.settings')
        self.from_object('enjoycms.local_settings')
        app_strings = "ENJOYCMS_SETTINGS" if not test else "ENJOYCMSTEST_SETTINGS"
        self.from_envvar(app_strings, silent=True)
        self.update(sets)



