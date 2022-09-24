import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import pydb_sql.type_conversion as cnv

def test_LT2L():
    LT_in = [('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('test',)]
    L_ans = ['information_schema', 'mysql', 'performance_schema', 'sys', 'test']
    
    L = cnv.LT2L(LT_in) # test this line
    
    assert(L==L_ans)

