#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from enjoycms.core.config import EnjoyCmsConfig



class EnjoyCmsApp(Flask):
    config_class = EnjoyCmsConfig

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return self.config_class(root_path, self.default_config)


