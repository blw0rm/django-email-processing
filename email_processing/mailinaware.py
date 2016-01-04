##############################################################################
"""

$Id$
"""
import copy
from email.Utils import parseaddr
from django.utils.translation import ugettext as _
from django.conf import settings
from utils import log_exc
from exceptions import MailInException

def UserModel():
    try:
        from django.contrib.auth import get_user_model
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        return User

registry = {}


class MailInAwareDestination(object):

    def __init__(self, address):
        self.address = address

    def register(self):
        if not self.address:
            return

        if registry.get(self.address) is not None:
            raise MailInException(
                'Mail-in email address already in use: %s'%self.address)
        registry[self.address] = self

    def unregister(self):
        del registry[self.address]

    @property
    def enabled(self):
        return self.__dict__.get('enabled', False)

    @enabled.setter
    def enabled(self, value):
        if value:
            self.register()
        else:
            self.unregister()

        self.__dict__['enabled'] = value

    @property
    def address(self):
        return self.__dict__.get('address', u'')

    @address.setter
    def address(self, value):
        if self.enabled:
            self.unregister()
            self.__dict__['address'] = value
            self.register()
        else:
            self.__dict__['address'] = value

    def process(self, message):
        # find principal
        from_hdr = parseaddr(message['From'])[1].lower()
        try:
            principal = UserModel().objects.get(email=from_hdr)
        except UserModel().DoesNotExist:
            # member not found
            raise MailInException('Member not found: %s'%from_hdr)

        # deliver message
        try:
            self.processRecipient(principal, message)
        except Exception, e:
            log_exc()
            raise MailInException(e)

    def processRecipient(self, principal, message):
        raise NotImplementedError()
