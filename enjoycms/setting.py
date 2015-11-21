# coding: utf-8

# Debug and toolbar
DEBUG = True
DEBUG_TOOLBAR_ENABLED = False

# Logger
LOGGER_ENABLED = True
LOGGER_LEVEL = 'DEBUG'
LOGGER_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
LOGGER_DATE_FORMAT = '%d.%m %H:%M:%S'


"""
数据库，本地MongoDB配置
"""
MONGODB_DB = "enjoycms_db"
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_USERNAME = None
MONGODB_PASSWORD = None


"""
Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，应该尽可能设置为一个很难猜到的值。
可采取以下方式生成：
python -c "import uuid;print uuid.uuid4()
"""
SECRET_KEY = "e10cefd0-e65a-4bd5-b808-7c0c0b30bcde"
