# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 31.

@author: je-ho.han
'''
from django.shortcuts import render_to_response
from board.model.models import DjangoBoard
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def showWrite(request):
    return render_to_response('write.html')

@csrf_exempt
def doWrite(request):
    br = DjangoBoard (subject = request.POST['subject'],
                      name = request.POST['name'],
                      mail = request.POST['email'],
                      memo = request.POST['memo'],
                      created_date = timezone.now(),
                      hits = 0
                     )
    br.save()
    
    url = '/showList?current_page=1'
    return HttpResponseRedirect(url)