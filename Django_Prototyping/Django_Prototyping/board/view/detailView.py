# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 31.

@author: je-ho.han
'''
from django.shortcuts import render_to_response
from board.model.models import DjangoBoard

def showView(request):
    pk= request.GET['memo_id']
    boardData = DjangoBoard.objects.get(id=pk)

    
    # 조회수를 늘린다.    
    DjangoBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)

    
    return render_to_response('view.html', {'memo_id': request.GET['memo_id'],
                                            'current_page':request.GET['current_page'],
                                            'searchStr': request.GET['searchStr'],
                                            'boardData': boardData } )

