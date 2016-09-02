# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 31.

@author: je-ho.han
'''
from django.shortcuts import render_to_response
from board.model.models import DjangoBoard
from board.util.util import pagingHelper
from board.util import Const

def showList(request):    
    searchStr = ""
    totalCnt = 0
    current_page = 1
    if request.GET.__contains__("searchStr"):
        searchStr = request.GET['searchStr']
        totalCnt = DjangoBoard.objects.filter(subject__contains=searchStr).count()
    else:
        totalCnt = DjangoBoard.objects.all().count()    
    
    if request.GET.__contains__("current_page"):
        current_page = request.GET['current_page']
    
    sqlParameter = []   
    sqlParameter.append(Const.rowsPerPage)   
    sql = """   
            SELECT Z.* 
            FROM (
                    SELECT X.*, ceil(rownum / %s) as page
                    FROM ( 
                            SELECT ID,SUBJECT,NAME,CREATED_DATE,MAIL,MEMO,HITS 
                            FROM BOARD_DJANGOBOARD"""
    if searchStr is not None and searchStr != "":
        sql += "            WHERE SUBJECT LIKE '%%'||%s||'%%'"
        sqlParameter.append(searchStr)  
    
    sql +="""               ORDER BY ID DESC
                        ) X 
                 ) Z 
                WHERE page = %s"""
    sqlParameter.append(current_page) 
    
    boardList = DjangoBoard.objects.raw(sql,sqlParameter)    
    
    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, Const.rowsPerPage)
    
    return render_to_response('list.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                            'current_page':current_page ,'totalPageList':totalPageList,'searchStr':searchStr} )
