from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declared_attr, relationship

from app.app import db
from flask_security.models import fsqla_v2


class Role(db.Model, fsqla_v2.FsRoleMixin):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return self.name


class User(db.Model, fsqla_v2.FsUserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    @declared_attr
    def webauthn(cls):
        return relationship("WebAuthn", backref="users", cascade="all, delete")

    def __repr__(self):
        return self.email

    def __iter__(self):
        values = vars(self)
        for attr in self.__mapper__.columns.keys():
            if attr in values:
                yield attr, values[attr]


class WebAuthn(db.Model, fsqla_v2.FsUserMixin):
    __tablename__ = 'WebAuthn'
    __table_args__ = {'extend_existing': True}

    @declared_attr
    def user_id(cls):
        return Column(
            Integer,
            ForeignKey("user.id", ondelete="CASCADE"),
            nullable=False,
        )
