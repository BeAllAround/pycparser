import sys
import copy

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_generator, c_ast



import pycparser

import yacctab

print(yacctab)


if __name__ == "__main__":
    _code = '''

    struct _struct {
    };

    typedef struct _struct my_struct;1;1+1;

    (int*)(d1 + 1);

    ((void*)d1 * 1);

    int* (*dd)(void, void);


    int d;
    d;

    d = 44;

    void func_d() { aaaaa; printf("AA", a); }

    int bb = 1 + 1;


    int (*(*f13(void))(void *))( int );
    int* (*(*f13(int d))(void *n))(int fd, int(*d)() );

    int* (**(***f13(int d))(void *n))(int fd, int(*d)() );

    '''
    # const char* _string = "AAA";
    # void main() {}
    # int d1 = 1;

    generator = c_generator.CGenerator()

    parser = c_parser.CParser(yacctab=yacctab)
    
    node_ast = parser.parse(_code, filename='<none>', debug=False) # debug=True
    
    assert node_ast != None

    print(node_ast.ext[-1])
    print(generator.visit(node_ast.ext[-1].type))
    print(generator._generate_type(node_ast.ext[-1].type))
    print(generator._type_of(node_ast.ext[-1].type))
    
    # node_ast.show()

    # print(ext)
    # print('c_source:', generator.visit(ext) + ';')

    # node_ast.show()
    # print(node_ast)

