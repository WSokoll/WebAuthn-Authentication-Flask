from flask_security import RoleMixin, UserMixin
from sqlalchemy.orm import declared_attr
from sqlalchemy import types

from app.app import db


class StringListColumn(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        if value is not None and value != '':
            return ','.join(value)
        return ''

    def process_result_value(self, value, dialect):
        if value is not None and value != '':
            return value.split(',')
        return ''


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(db.Text())
    update_datetime = db.Column(db.DateTime())


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(64))
    current_login_ip = db.Column(db.String(64))
    login_count = db.Column(db.Integer())
    tf_primary_method = db.Column(db.String(64))
    tf_totp_secret = db.Column(db.String(255))
    tf_phone_number = db.Column(db.String(128))
    create_datetime = db.Column(db.DateTime())
    update_datetime = db.Column(db.DateTime())
    username = db.Column(db.String(255))
    us_totp_secrets = db.Column(db.Text())
    us_phone_number = db.Column(db.String(128))
    email_change_new = db.Column(db.String(255))
    email_change_code = db.Column(db.String(20))
    email_change_last = db.Column(db.DateTime())
    fs_webauthn_user_handle = db.Column(db.String(64), unique=True, nullable=True)

    roles = db.relationship('Role',
                            secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))

    @declared_attr
    def webauthn_relations(cls):
        return db.relationship("WebAuthn",
                               primaryjoin="User.id == foreign(WebAuthn.user_id)",
                               secondary="WebAuthn",
                               secondaryjoin="User.id == foreign(WebAuthn.user_id)",
                               backref=db.backref('users', lazy='dynamic'),
                               cascade="all, delete")

    def __repr__(self):
        return self.email


class WebAuthn(db.Model):
    __tablename__ = 'WebAuthn'

    id = db.Column(db.Integer(), primary_key=True)
    credential_id = db.Column(db.LargeBinary(1024))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    public_key = db.Column(db.LargeBinary(1024))
    sign_count = db.Column(db.Integer())
    transports = db.Column(StringListColumn)
    extensions = db.Column(db.String(255))
    lastuse_datetime = db.Column(db.DateTime())
    name = db.Column(db.String(64))
    usage = db.Column(db.String(64))
    backup_state = db.Column(db.Boolean())
    device_type = db.Column(db.String(64))

    user_relation = db.relationship("User", backref="webauthn", foreign_keys=[user_id])

    def get_user_mapping(self):
        return {'id': self.user_id}
