import os.path

from flask import Blueprint, render_template, current_app, request, jsonify

from skylines.lib.vary import vary

about_blueprint = Blueprint('about', 'skylines')


@about_blueprint.route('/')
def about():
    return render_template('ember-page.jinja')


@about_blueprint.route('/imprint')
@vary('accept')
def imprint():
    if 'application/json' not in request.headers.get('Accept', ''):
        return render_template('ember-page.jinja')

    content = current_app.config.get(
        'SKYLINES_IMPRINT',
        'Please set the `SKYLINES_IMPRINT` variable in the config file.')

    return jsonify(content=content)


@about_blueprint.route('/team')
@vary('accept')
def skylines_team():
    if 'application/json' not in request.headers.get('Accept', ''):
        return render_template('ember-page.jinja')

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', '..', '..', 'AUTHORS.md')
    with open(path) as f:
        content = f.read().decode('utf-8')

    return jsonify(content=content)


@about_blueprint.route('/license')
@vary('accept')
def license():
    if 'application/json' not in request.headers.get('Accept', ''):
        return render_template('ember-page.jinja')

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', '..', '..', 'LICENSE')
    with open(path) as f:
        content = f.read().decode('utf-8')

    return jsonify(content=content)
