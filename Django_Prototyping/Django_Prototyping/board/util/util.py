# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 31.

@author: je-ho.han
'''
class pagingHelper:
    "paging helper class"
    def getTotalPageList(self, total_cnt, rowsPerPage):               
        if ((total_cnt % rowsPerPage) == 0):
            self.total_pages = total_cnt / rowsPerPage;
            print 'getTotalPage #1'
        else:
            self.total_pages = (total_cnt / rowsPerPage) + 1;
            print 'getTotalPage #2'
               
        self.totalPageList = []
        for j in range( self.total_pages ):
            self.totalPageList.append(j+1)
                
        return self.totalPageList        

    def __init__(self ):
        self.total_pages = 0
        self.totalPageList  = 0