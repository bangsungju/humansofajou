# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, flash, redirect
from apps import app, db
from sqlalchemy import desc
from apps.models import Humans, Ajou
from apps.forms import HumansForm, AjouForm

#
# @error Handlers
#
# Handle 404 errors



@app.route('/', methods=['GET'])
def humans_list():
    interview = {}
    interview['humans_list'] = Humans.query.order_by(desc(Humans.date_created)).all()
    return render_template("index.html", interview=interview, active_tab='humans_tab')

@app.route('/', methods=['GET'])
def ajou_list():
    context = {}
    context['ajou_list'] = Ajou.query.order_by(desc(Ajou.date_created)).all()
    return render_template("ajou_sec.html", context=context, active_tab='ajou_tab')
