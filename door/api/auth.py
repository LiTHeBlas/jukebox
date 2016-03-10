from __future__ import absolute_import, unicode_literals
import logging

from flask_httpauth import HTTPBasicAuth
from itsdangerous import URLSafeSerializer, BadSignature

from .. import settings

logger = logging.getLogger(__name__)


def get_serializer():
    return URLSafeSerializer(settings.SECRET_KEY)


def generate_token(name):
    assert isinstance(name, str)
    serializer = get_serializer()
    return serializer.dumps(name)


def verify_token(token):
    serializer = get_serializer()
    return serializer.loads(token)


def verify_password(username, password):
    try:
        return username == verify_token(password)
    except BadSignature:
        return False


class TokenAuth(HTTPBasicAuth):
    def __init__(self):
        super(TokenAuth, self).__init__()
        self.verify_password(verify_password)
