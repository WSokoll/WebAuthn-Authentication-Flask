import base64
import typing as t

from flask_security import WebAuthnSigninResponseForm


class CustomWebAuthnSigninResponseForm(WebAuthnSigninResponseForm):
    def validate(self, **kwargs: t.Any):
        pre_validate = super(CustomWebAuthnSigninResponseForm, self).validate()

        if pre_validate is False and self.user is not None:
            self.user.fs_webauthn_user_handle = base64\
                .b64encode(self.user.fs_webauthn_user_handle.encode('utf-8'))\
                .decode('utf8')

            return super(CustomWebAuthnSigninResponseForm, self).validate()

        return pre_validate
