"""

$Id$
"""
from email import message_from_string

from utils import log, log_exc
from exceptions import MailInException
from config import config_instance
from django.shortcuts import render_to_response
from django.http import HttpResponse


class MailInTransport(object):

    def __call__(self, request, *args, **kw):
        mail = request.POST.get('mail') or request.GET.get('mail')
        if not mail:
            return HttpResponse('failed', status=500)

        # convert mail
        try:
            msg = message_from_string(mail.encode('utf-8'))
        except:
            log_exc('Error parsing email')
            return HttpResponse('failed on parsing', status=500)

        # check message for loops, wrong mta hosts, etc
        try:
            config_instance.checkMessage(msg, mail, request)
        except MailInException, msg:
            log(str(msg))
            return HttpResponse('failed on checking', status=500)

        # process message
        try:
            config_instance.process(msg)
        except MailInException, msg:
            log_exc('Error processing email')
            return HttpResponse('failed on processing', status=500)

        return HttpResponse('success')


transport = MailInTransport()
