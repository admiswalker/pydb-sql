import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import pydb_sql.compare_structured_str as cmpss

TARGET_SHARE = [('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('test',),('test2','test2_2')]

def test_contain_case01_S():
    
    search_word = 'information_schema'
    
    assert(cmpss.contain(TARGET_SHARE, search_word)) # test this line

def test_contain_case01_F():
    
    search_word = 'Not_existing_word'
    
    assert(cmpss.contain(TARGET_SHARE, search_word)==False) # test this line

def test_contain_case01_S_02():
    
    search_word = 'test2'
    
    assert(cmpss.contain(TARGET_SHARE, search_word)) # test this line

def test_contain_case02_S():
    
    search_word = 'test2_2'
    
    assert(cmpss.contain(TARGET_SHARE, search_word)) # test this line

def test_contain_case03_S():

    target = 'abcdefg'
    search_word = 'cde'
    
    assert(cmpss.contain(target, search_word)) # test this line

def test_contain_case04_S():

    target = "[Table Create Error] 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'illegal query' at line 1"
    search_word = 'You have an error in your SQL syntax;'
    
    assert(cmpss.contain(target, search_word)) # test this line

