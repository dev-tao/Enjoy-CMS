# -*- coding: UTF-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import hashlib
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:111111@localhost:33306/enjoycmspre'
db = SQLAlchemy(app)


################################
###字段配置
################################
class EnjoycmsConfig(db.Model):
    __tablename__ = 'enjoycms_config'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50),unique=True,nullable=False)
    name = db.Column(db.String(50),unique=True,nullable=False)
    config_value = db.Column(db.String(50))
    order_num = db.Column(db.Integer)

    def __init__(self, code,name,confg_value,order_num=None,):
        self.code = code
        self.name = name
        self.config_value = confg_value
        if order_num is None:
            order_num = 0
        self.order_num = order_num

    def __repr__(self):
         return '<Config name: %r  id: %r>' % self.name,self.id


################################
###权限管理
################################

class EnjoycmsUser(db.Model):
    __tablename__ = 'enjoycms_user'
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(50),unique=True,nullable=False)
    name = db.Column(db.String(50),nullable=False)
    pwd = db.Column(db.String(50),nullable=False)
    sex = db.Column(db.String(10))
    birthday = db.Column(db.DateTime)
    tel = db.Column(db.Integer)
    mobile_phone = db.Column(db.Integer)
    email = db.Column(db.String(30))
    state = db.Column(db.Integer)
    last_login_time = db.Column(db.DateTime)
    add_time = db.Column(db.DateTime)
    depart_names  = db.Column(db.String(30))
    depart_ids = db.Column(db.Integer,nullable=False)
    role_names = db.Column(db.String(30))

    def __init__(self, login_name,name,pwd,sex,birthday,tel,mobile_phone,email,depart_names,depart_ids,role_names,add_time=None,last_login_time=None,state=None):
        self.login_name = login_name
        self.name = name
        self.pwd = hashlib.md5(pwd)
        self.sex = sex
        self.birthday = birthday
        self.tel = tel
        self.mobile_phone = mobile_phone
        self.email = email
        if state is None:
            state = 1
        self.state = state
        if last_login_time is None:
            last_login_time = last_login_time,
        self.last_login_time = last_login_time
        if add_time is None:
            add_time = datetime.now()
        self.add_time = add_time
        self.depart_names = depart_names
        self.depart_ids = depart_ids
        self.role_names = role_names


    def __repr__(self):
        return '<EnjoycmsUser login_name:%r id:%r>' % self.login_name,self.id



class EnjoycmsDepart(db.Model):
    __tablename__ = 'enjoycms_depart'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    par_id =  db.Column(db.Integer)
    state = db.Column(db.Integer)

    def __init__(self, name,par_id,state=None):
        self.name = name
        self.par_id = par_id
        if state is None:
            state = 1
        self.state = state

    def __repr__(self):
        return '<EnjoycmsDepart name:%r id:%r>' % self.name,self.id


class EnjoycmsDepartUsers(db.Model):
    __tablename__ = 'enjoycms_depart_users'
    id = db.Column(db.Integer, primary_key=True)
    depart_id =  db.Column(db.Integer)
    user_id =  db.Column(db.Integer)
    def __init__(self, depart_id,user_id):
        self.depart_id = depart_id
        self.user_id=user_id

    def __repr__(self):
        return '<EnjoycmsDepartUsers id:%r>' % self.id

class EnjoycmsFunc(db.Model):
    __tablename__ = 'enjoycms_func'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    par_id = db.Column(db.Integer)
    state = db.Column(db.Integer)
    order_num = db.Column(db.Integer)
    url = db.Column(db.String(80))


    def __init__(self, name,par_id,url,state=None,order_num=None):
        self.name = name
        self.par_id = par_id
        if state is None:
            state = 1
        self.state = state
        self.url = url
        if order_num is None:
            self.order_num = 0

    def __repr__(self):
        return '<EnjoycmsFunc name:%r id:%r>' % self.name,self.id


class EnjoycmsRoles(db.Model):
    __tablename__ = 'enjoycms_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    state = db.Column(db.Integer)
    add_user = db.Column(db.String(80))


    def __init__(self, name,add_user,state=None):
        self.name = name
        if state is None:
            state = 1
        self.state = state
        self.add_user = add_user

    def __repr__(self):
        return '<EnjoycmsRoles name:%r id:%r>' % self.name,self.id


class EnjoycmsRoleUsers(db.Model):
    __tablename__ = 'enjoycms_role_users'
    id = db.Column(db.Integer, primary_key=True)
    role_id =  db.Column(db.Integer)
    user_id =  db.Column(db.Integer)
    def __init__(self, role_id,user_id):
        self.role_id = role_id
        self.user_id = user_id

    def __repr__(self):
        return '<EnjoycmsRoleUser id:%r>' % self.id

class EnjoycmsRoleSite(db.Model):
    __tablename__ = 'enjoycms_role_site'
    id = db.Column(db.Integer, primary_key=True)
    role_id =  db.Column(db.Integer)
    site_id =  db.Column(db.Integer)
    site_admin =  db.Column(db.Integer)
    def __init__(self, role_id,site_id,site_admin):
        self.role_id = role_id
        self.site_id = site_id
        self.site_admin = site_admin

    def __repr__(self):
        return '<EnjoycmsRoleSite id:%r site:%r>' % self.id,self.site_id

class EnjoycmsRoleChannel(db.Model):
    __tablename__ = 'enjoycms_role_channel'
    id = db.Column(db.Integer, primary_key=True)
    role_id =  db.Column(db.Integer)
    channel_id =  db.Column(db.Integer)
    def __init__(self,role_id,channel_id):
        self.role_id = role_id
        self.channel_id = channel_id

    def __repr__(self):
        return '<EnjoycmsRoleChannel id:%r role_id:%r>' % self.id,self.role_id


class EnjoycmsRoleFunc(db.Model):
    __tablename__ = 'enjoycms_role_func'
    id = db.Column(db.Integer, primary_key=True)
    role_id =  db.Column(db.Integer)
    func_id =  db.Column(db.Integer)
    def __init__(self, role_id,func_id):
        self.role_id = role_id
        self.func_id = func_id

    def __repr__(self):
        return '<EnjoycmsRoleFunc id:%r role_id:%r>' % self.id,self.role_id


################################
###栏目信息
################################

class EnjoycmsSite(db.Model):
    __tablename__ = 'enjoycms_site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    par_id =  db.Column(db.Integer)
    state = db.Column(db.Integer)
    source_path = db.Column(db.String(80))

    def __init__(self, name,par_id,source_path,state=None):
        self.name = name
        self.par_id = par_id
        if state is None:
            state = 1
        self.state = state
        self.source_path = source_path

    def __repr__(self):
        return '<EnjoycmsSite id:%r name:%r>' % self.id,self.name


class EnjoycmsChannel(db.Model):
    __tablename__ = 'enjoycms_channel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    par_id =  db.Column(db.Integer)
    state = db.Column(db.Integer)
    site = db.Column(db.Integer)
    url = db.Column(db.String(80))
    order_num = db.Column(db.Integer)
    navigation = db.Column(db.Integer)
    page_mark = db.Column(db.String(30))

    def __init__(self, name,par_id,site,url,page_mark,state=None,order_num=None,navigation=None):
        self.name = name
        self.par_id = par_id
        self.site  = site
        self.url = url
        self.page_mark =page_mark
        if state is None:
            state = 1
        self.state = state
        if order_num is None:
            order_num = 0
        self.order_num = order_num
        if navigation is None:
            navigation = 1
        self.navigation = navigation

    def __repr__(self):
        return '<EnjoycmsChannel id:%r name:%r>' % self.id,self.name

class EnjoycmsInfo(db.Model):
    __tablename__ = 'enjoycms_info'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.Integer)
    channel = db.Column(db.Integer)
    title = db.Column(db.String(80))
    short_title = db.Column(db.String(80))
    author = db.Column(db.String(30))
    publisher = db.Column(db.String(30))
    description = db.Column(db.TEXT)
    content = db.Column(db.TEXT)
    imgs = db.Column(db.String(100))
    attaches = db.Column(db.String(100))
    add_time = db.Column(db.DATETIME)
    template = db.Column(db.String(30))
    is_top = db.Column(db.Integer)
    click_num = db.Column(db.Integer)
    add_user = db.Column(db.Integer)

    def __init__(self, site,channel,title,short_title,author,publisher,description,content,imgs,attaches,template,is_top,click_num,add_user,add_time=None):
        self.site = site
        self.channel = channel
        self.title = title
        self.short_title = short_title
        self.author = author
        self.publisher = publisher
        self.description = description
        self.content = content
        self.imgs = imgs
        self.attaches = attaches
        self.template = template
        self.is_top = is_top
        self.click_num = click_num
        self.add_user = add_user
        if add_time is None:
            add_time = datetime.now()
        self.add_time = add_time

    def __repr__(self):
        return '<EnjoycmsInfo id:%r title:%r>' % self.id,self.title

class EnjoycmsLink(db.Model):
    __tablename__ = 'enjoycms_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    par_id =  db.Column(db.Integer)
    url = db.Column(db.String(80))
    state = db.Column(db.Integer)
    order_num = db.Column(db.Integer)
    site = db.Column(db.Integer)
    type = db.Column(db.Integer)
    img = db.Column(db.Integer)
    page_mark = db.Column(db.String(30))

    def __init__(self, name,par_id,url,site,type,img,page_mark,order_num=None,state=None):
        self.name = name
        self.par_id = par_id
        self.url = url
        self.site = site
        self.type = type
        self.img = img
        self.page_mark = page_mark
        if order_num is None:
            order_num = 0
        self.order_num = order_num
        if state is None:
            state = 1
        self.state = state

    def __repr__(self):
        return '<EnjoycmsLink id:%r name:%r>' % self.id,self.name


################################
###操作日志
################################
class EnjoycmsOperaLogs(db.Model):
    __tablename__ = 'enjoycms_opera_logs'
    id = db.Column(db.Integer, primary_key=True)
    log_name = db.Column(db.String(50))
    opera_time = db.Column(db.DATETIME)
    content = db.Column(db.TEXT)
    ip = db.Column(db.String(30))

    def __init__(self, log_name,content,ip,opera_time = None):
        self.log_name = log_name
        self.opera_time = opera_time
        self.content = content
        self.ip = ip
        if opera_time is None:
            opera_time = datetime.now()
        self.opera_time = opera_time

    def __repr__(self):
        return '<EnjoycmsOperaLogs id:%r log_name:%r>' % self.id,self.log_name



################################
###template相关表
################################
class EnjoycmsTemplate(db.Model):
    __tablename__ = 'enjoycms_template'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    state = db.Column(db.INTEGER)
    order_num = db.Column(db.INTEGER)
    site = db.Column(db.INTEGER)
    add_user = db.Column(db.INTEGER)

    def __init__(self, name,site,add_user,state = None,order_num =None):
        self.name = name
        if state is None:
            state = 1
        self.state = state
        if order_num is None:
            order_num = 0
        self.order_num = order_num
        self.site = site
        self.add_user = add_user

    def __repr__(self):
        return '<EnjoycmsTemplate id:%r name:%r>' % self.id,self.name


class EnjoycmsTemplateChannel(db.Model):
    __tablename__ = 'enjoycms_template_channel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    state =  db.Column(db.INTEGER)
    template = db.Column(db.String(30))
    par_id =  db.Column(db.INTEGER)
    site = db.Column(db.INTEGER)
    order_num =  db.Column(db.INTEGER)
    click_num =  db.Column(db.INTEGER)
    navigation =  db.Column(db.INTEGER)
    page_mark = db.Column(db.String(30))
    template_id =  db.Column(db.INTEGER)

    def __init__(self, name,template,par_id,site,page_mark,template_id,navigation = None,click_num = None,order_num = None,state=None):
        self.name = name
        self.template = template
        self.par_id  = par_id
        self.site = site
        self.page_mark = page_mark
        self.template_id =template_id
        if navigation is None:
            navigation =1
        self.navigation = navigation
        if click_num is None:
            click_num = 0
        self.click_num = click_num
        if order_num is None:
            order_num = 0
        self.order_num = order_num
        if state is None:
            state = 1
        self.state = state

    def __repr__(self):
        return '<EnjoycmsTemplateChannel id:%r name:%r>' % self.id,self.name



if __name__=='__main__':
    db.drop_all()
    db.create_all()


