
import sys
import copy

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast

import pycparser

import yacctab

print(yacctab)

if __name__ == "__main__":
    _code = '''

    struct _struct {
    };

    typedef struct _struct my_struct;

    void func_d() {}

    1;
    1+1;
    (int*)d1;

    ((void*)d1 * 1);

    int* (*dd)(void, void);

    void main() {
    }

    '''
    # int d1 = 1;

    parser = c_parser.CParser(yacctab=yacctab)

    node_ast = parser.parse(_code, filename='<none>', debug=False) # debug=True

    node_ast.show()
    # print(node_ast)

