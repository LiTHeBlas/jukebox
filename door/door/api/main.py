from __future__ import absolute_import, unicode_literals
import logging

from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse

from opbeat.contrib.flask import Opbeat

from .. import settings
from ..lib import get_closed, get_locked, unlock
from .auth import TokenAuth

logger = logging.getLogger(__name__)

app = Flask(__name__)
auth = TokenAuth()
api = Api(app)
opbeat = Opbeat(app)


@app.before_request
def allow_only_allowed_ips():
    if settings.ALLOWED_IPS and request.remote_addr not in settings.ALLOWED_IPS:
        abort(403)


class Action(Resource):
    decorators = [auth.login_required]

    def get(self, action):
        if action == 'check':
            return {
                'locked': get_locked(),
                'closed': get_closed()
            }
        else:
            abort(400)

    def post(self, action):
        if action == 'unlock':
            unlock()
            return self.get('check')
        else:
            abort(400)

api.add_resource(Action, '/actions/<action>/')
