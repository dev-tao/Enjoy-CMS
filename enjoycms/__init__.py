#!/usr/bin/env python
# -*- coding: utf-8 -*-
VERSION = (0, 0, 1)

__version__ = ".".join(map(str, VERSION))
__status__ = "Alpha"
__description__ = "致力于做最好用的中文免费CMS"
__author__ = "刘 涛 <dev.tao@qq.com>"
__email__ = "dev.tao@qq.com"
__license__ = " Apache License Version 2.0"
__copyright__ = "Copyright 2015, Enjoy-CMS Project"

from enjoycms.core.app import EnjoyCmsApp



def create_app_base(config=None, test=False, admin_instance=None, **settings):
    app = EnjoyCmsApp('enjoycms')
    app.config.load_quokka_config(config=config, test=test, **settings)
    if test or app.config.get('TESTING'):
        app.testing = True
    return app


def create_app(config=None, test=False, admin_instance=None, **settings):
    app = create_app_base(
        config=config, test=test, admin_instance=admin_instance, **settings
    )
    from .ext import configure_extensions
    configure_extensions(app, admin_instance or admin)
    # app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    return app