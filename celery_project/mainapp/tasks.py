
from celery import shared_task
'''
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import BroadcastNotification
import json
from celery import Celery, states
from celery.exceptions import Ignore
import asyncio
'''

@shared_task(bind = True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"