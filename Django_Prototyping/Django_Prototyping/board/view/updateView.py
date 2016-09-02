# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 31.

@author: je-ho.han
'''
from django.shortcuts import render_to_response
from board.model.models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect
from board.util.util import pagingHelper
from board.util import Const

def showUpdate(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']
    boardData = DjangoBoard.objects.get(id=memo_id)
    return render_to_response('update.html', {'memo_id': memo_id,
                                              'current_page':current_page,
                                              'searchStr': searchStr,
                                              'boardData': boardData } )

@csrf_exempt
def doUpdate(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']

    DjangoBoard.objects.filter(id=memo_id).update(
                                                  mail= request.POST['mail'],
                                                  subject= request.POST['subject'],
                                                  memo= memo_id
                                                  )

    url = '/showList?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

@csrf_exempt
def doDelete(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']

    p = DjangoBoard.objects.get(id=memo_id)
    p.delete()
    
    totalCnt = DjangoBoard.objects.all().count()
    pagingHelperIns = pagingHelper();

    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, Const.rowsPerPage)

    if int(current_page) in totalPageList:
        current_page=current_page
    else:
        current_page= int(current_page)-1
        
    url = '/showList?current_page=' + str(current_page)
    return HttpResponseRedirect(url)


