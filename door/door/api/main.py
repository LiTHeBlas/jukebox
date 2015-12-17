from __future__ import absolute_import, unicode_literals
import logging

from flask import Flask, abort
from flask_restful import Api, Resource, reqparse

from ..lib import get_closed, get_locked, unlock
from .auth import TokenAuth

logger = logging.getLogger(__name__)

app = Flask(__name__)
auth = TokenAuth()
api = Api(app)


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
