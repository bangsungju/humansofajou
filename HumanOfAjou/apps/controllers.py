# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, flash, redirect
from apps import app, db
from sqlalchemy import desc
from apps.models import Humans, Surrounds
from apps.forms import HumansForm

# @error Handlers
# Handle 404 errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

#humans section

@app.route('/', methods=['GET'])
def humans_list():
    interview = {}
    interview['human_list'] = Humans.query.order_by(desc(Humans.date_created)).all()
    return render_template("home.html", interview=interview)

@app.route('/photo/get/<path:blob_key>/', methods=['GET'])
def photo_get(blob_key):
    if blob_key:
        blob_info = blobstore.get(blob_key)
        if blob_info:
            img = images.Image(blob_key=blob_key)
            logging.inf(img)
            img.im_feeling_lucky()
            thumbnail.img.execute_transforms(output_encoding=images.PNG)
            logging.info(thumbnail)

            response=make_response(thumbnail)
            response.headers['Content-Type'] = blob_info.content_type
            return response

@app.route('/humans/detail/<int:id>', methods=['GET'])
def humans_detail(id):
    humans = Humans.query.get(id)
    return render_template('humans/detail.html', humans=humans)

@app.route('/manager/humans/create/', methods=['GET', 'POST'])
def humans_create():
    form = HumansForm()
    upload_url = blobstore.create_upload_url('/manager/humans/create/')
    if request.method == 'POST':
        if form.validate_on_submit():
            f = form.photo.data
            header = f.headers['Content-Type']
            parsed_header = parse_options_header(header)
            blob_key = parsed_header[1]['blob-key']
            humans = Humans(
                text=form.text.data,
                content=form.content.data,
                Q_month=form.Q_month.data,
                img = blob_key
            )

            db.session.add(humans)
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('humans_list'))

    return render_template('manager/humans/create.html', form=form, upload_url=upload_url)


@app.route('/manager/humans/update/<int:id>', methods=['GET', 'POST'])
def humans_update(id):
    humans = Humans.query.get(id)
    form = HumansForm(request.form, obj=humans)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(humans)
            db.session.commit()
        return redirect(url_for('humans_detail', id=id))

    return render_template('manager/humans/update.html', form=form)


@app.route('/manager/humans/delete/<int:id>', methods=['GET', 'POST'])
def humans_delete(id):
    if request.method == 'GET':
        return render_template('manager/humans/delete.html', humans_id=id)
    elif request.method == 'POST':
        humans_id = request.form['humans_id']
        humans = Article.query.get(humans_id)
        db.session.delete(humans)
        db.session.commit()

        flash(u'게시글을 삭제하였습니다.', 'success')
        return redirect(url_for('humans_list'))


#ajou section

@app.route('/', methods=['GET'])
def ajou_list():
    photo = {}
    photo['ajou_list'] = Ajou.query.order_by(desc(Ajou.date_created)).all()
    return render_template("ajou.html", photo=photo)


@app.route('/humans/detail/<int:id>', methods=['GET'])
def humans_detail(id):
    humans = Humans.query.get(id)
    return render_template('humans/detail.html', humans=humans)

@app.route('/manager/humans/create/', methods=['GET', 'POST'])
def humans_create():
    form = HumansForm()
    upload_url = blobstore.create_upload_url('/manager/humans/create/')
    if request.method == 'POST':
        if form.validate_on_submit():
            f = form.photo.data
            header = f.headers['Content-Type']
            parsed_header = parse_options_header(header)
            blob_key = parsed_header[1]['blob-key']
            # humans instance create
            humans = Humans(
                text=form.text.data,
                content=form.content.data,
                Q_month=form.Q_month.data,
                img = blob_key
            )

            db.session.add(humans)
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('humans_list'))

    return render_template('manager/humans/create.html', form=form, upload_url=upload_url)


@app.route('/manager/humans/update/<int:id>', methods=['GET', 'POST'])
def humans_update(id):
    humans = Humans.query.get(id)
    form = HumansForm(request.form, obj=humans)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(humans)
            db.session.commit()
        return redirect(url_for('humans_detail', id=id))

    return render_template('manager/humans/update.html', form=form)


@app.route('/manager/humans/delete/<int:id>', methods=['GET', 'POST'])
def humans_delete(id):
    if request.method == 'GET':
        return render_template('manager/humans/delete.html', humans_id=id)
    elif request.method == 'POST':
        humans_id = request.form['humans_id']
        humans = Article.query.get(humans_id)
        db.session.delete(humans)
        db.session.commit()

        flash(u'게시글을 삭제하였습니다.', 'success')
        return redirect(url_for('humans_list'))
