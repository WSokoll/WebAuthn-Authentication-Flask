from flask import Blueprint, render_template
from flask_login import current_user

from app.app import db
from app.models import WebAuthn

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
@bp.route('/home', methods=['GET'])
def get():

    if current_user.is_authenticated:
        if db.session.query(WebAuthn.query.filter_by(user_id=current_user.id).exists()).scalar():
            return render_template('home.jinja', webauthn_enabled=True)

    return render_template('home.jinja', webauthn_enabled=False)
