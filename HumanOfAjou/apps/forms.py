# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    TextAreaField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField


class HumansForm(Form):
    text = StringField(
        u'제목',
        [validators.data_required(u'제목을 입력하시기 바랍니다.')],
        description={'placeholder': u'제목을 입력하세요.'}
    )
    content = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )

    Q_month = TextAreaField(
        u'이달의 질문',
        [validators.data_required(u'질문을 입력하시기 바랍니다.')],
        description={'placeholder': u'질문을 입력하세요.'}
    )
