import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import pydb_sql.compare_structured_str as cmpss

target = [('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('test',),('test2','test2_2')]

def test_contain_case01_S():
    
    search_word = 'information_schema'
    
    assert(cmpss.contain(target, search_word)) # test this line

def test_contain_case01_F():
    
    search_word = 'Not_existing_word'
    
    assert(cmpss.contain(target, search_word)==False) # test this line

def test_contain_case01_S_02():
    
    search_word = 'test2'
    
    assert(cmpss.contain(target, search_word)) # test this line

def test_contain_case02_S():
    
    search_word = 'test2_2'
    
    assert(cmpss.contain(target, search_word)) # test this line

