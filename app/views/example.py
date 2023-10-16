from flask import Blueprint, render_template

bp = Blueprint('example', __name__)


@bp.route('/example/<int:value>', methods=['GET'])
def example(value: int = 1):
    return render_template('example.jinja', value=value)
