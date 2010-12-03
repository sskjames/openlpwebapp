'''
Created on Dec 3, 2010

@author: james
'''

from django.conf import settings

def constants(request):
    return {'SITE_NAME': settings.SITE_NAME}