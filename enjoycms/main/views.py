# -*- coding: UTF-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/login/', methods=['GET', 'POST'])
def admin_login():
    return render_template('admin/login.html')


@main.route('/admin/index', methods=['GET', 'POST'])
def admin_index():
    return render_template('admin/index.html')