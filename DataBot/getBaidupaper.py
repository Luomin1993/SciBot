#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://xueshu.baidu.com/s?wd=paperuri%3A%28d3cfdf816a9ab6c61b0d2c00b3f082af%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fadsabs.harvard.edu%2Fcgi-bin%2Fnph-data_query%3Fbibcode%3D1989gaso.book.....G%26amp%3Bdb_key%3DAST%26amp%3Blink_type%3DABSTRACT&ie=utf-8&sc_us=1062315178241084878
#http://xueshu.baidu.com/s?wd=paperuri%3A%28d3cfdf816a9ab6c61b0d2c00b3f082af%29&amp;filter=sc_long_sign&amp;sc_ks_para=q%3DGenetic%20Algorithms%20in%20Search%2C%20Optimization%20and%20Machine%20Learning&amp;sc_us=1062315178241084878&amp;tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8
#http://xueshu.baidu.com/s?wd=paperuri%3A%28d3cfdf816a9ab6c61b0d2c00b3f082af%29&    filter=sc_long_sign&    sc_ks_para=q%3DGenetic%20Algorithms%20in%20Search%2C%20Optimization%20and%20Machine%20Learning&    sc_us=1062315178241084878&    tn=SE_baiduxueshu_c1gjeupa&    ie=utf-8
#http://xueshu.baidu.com/s?wd=paperuri%3A%282e123e324930ddb256896e1b9c8d5cf4%29&filter=sc_long_sign&sc_ks_para=q%3DMachine%20learning.&sc_us=14339372554542024416&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8

import spider
import re
import sys

__author__ = 'hanss401'


def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 

#-----------------get urls of searched paper-------------------------------
def get_urls_of_searched_paper(words):
    #http://xueshu.baidu.com/s?wd=machine+learning&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=3&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsp=0
    #http://xueshu.baidu.com/s?wd=machine+learning&pn=10&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&f=3&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1
    search_url = 'http://xueshu.baidu.com/s?wd='+ words.replace(' ','+') +'&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=3&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsp=0'
    content = spider.url_get(search_url,"gb2312")
    #save('xueshu.baidu',str(content))
    papers_urls_r = re.compile(r's?wd=paperuri(.*)tn=SE_baiduxueshu_c1gjeupa&ie=utf-8')
    papers_urls   = papers_urls_r.findall(content)
    for i in range(len(papers_urls)):
    	papers_urls[i] = ('http://xueshu.baidu.com/s?wd=paperuri'+ papers_urls[i] +'tn=SE_baiduxueshu_c1gjeupa&amp;ie=utf-8').replace('amp;','')
    return papers_urls	

def TEST_urls_of_searched_paper():
    print len(get_urls_of_searched_paper('machine learning'))    	


#-------------get



if __name__ == '__main__':
    TEST_urls_of_searched_paper()    