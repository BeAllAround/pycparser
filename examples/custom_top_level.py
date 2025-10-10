
import sys
import copy

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_generator, c_ast



import pycparser

import yacctab

print(yacctab)


class Transform:
    def __init__(self):
        self.ref_ids = dict()

        # If we have origin, we will have dest_stack
        self.dest_stack = list()
        self.ptr_decl_stack = list()

        self.decl_name = ''

    def get_decl_name(self):
        decl_name = self.decl_name
        self.decl_name = ''
        return decl_name

    def clear_stack(self):
        self.dest_stack.clear()
        self.ptr_decl_stack.clear()

    # extracting type that is essentially a cast in plain source
    def extract_cast(self, node, origin = c_ast.Decl):
        _type = type(node)

        s_type = '' # type as string

        if(_type == c_ast.Decl):
            return self.extract_cast(node.type)
        if(_type == c_ast.FuncDecl):
            signature = self.extract_cast(node.type)

            if(origin == c_ast.PtrDecl):
                func_cast = '('
                # print(self.ptr_decl_stack)
                while(len(self.ptr_decl_stack) != 0):
                    func_cast += self.ptr_decl_stack.pop()
                func_cast += ')'
                signature += func_cast

            # print(signature)

            param_types = list()
            for param in node.args.params:
                param_types.append(
                        self.extract_cast(param)
                )
            signature += '(' + ', '.join(param_types) + ')'

            # Can now return to its origin call: PtrDecl
            # This is somewhat equivalent to (return (signature, c_ast.FuncDecl)) since c_ast.PtrDecl takes priority in the node tree
            self.dest_stack.append(c_ast.FuncDecl) 

            return signature

        elif(_type == c_ast.PtrDecl):
            # Other declaration types come first in order to extract the cast
            self.ptr_decl_stack.append('*')
            s_type += self.extract_cast(node.type, c_ast.PtrDecl)

            # print(_type, self.dest_stack)
            if(len(self.dest_stack) != 0 and (self.dest_stack[-1] == c_ast.FuncDecl)):
                self.dest_stack.pop()
                self.dest_stack.append(c_ast.FuncDecl) # keep the dest of the return. Similar to (return (signature, c_ast.FuncDecl)) to keep the origin if the inner node is FuncDecl
            else:
                len(self.ptr_decl_stack) != 0 and self.ptr_decl_stack.pop()
                s_type += '*'

        elif(_type == c_ast.TypeDecl):
            if(len(self.decl_name) == 0 and node.declname != None): # First TypeDecl in the node tree represents the declaration name
                self.decl_name = node.declname
            s_type += self.extract_cast(node.type)

        elif(_type == c_ast.IdentifierType):
            id_type = ''
            # while(len(self.ptr_decl_stack) != 0):
            #    id_type += self.ptr_decl_stack.pop()

            for name in node.names:
                id_type += name
            s_type += id_type

        elif(_type == c_ast.Typename):
            return self.extract_cast(node.type)
        else:
            pass


        return s_type


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

    '''
    # void main() {}
    # int d1 = 1;

    generator = c_generator.CGenerator()

    parser = c_parser.CParser(yacctab=yacctab)


    _code = '''const int* (*dd)(void, void);'''
    # _code = '''const int* (***dd)(void, void);'''
    # _code = '''const int (*dd)(void, void);'''
    # _code = '''const int*** (*dd)(void, void);'''
    # _code = '''const int** (*dd)(void v0, void v1);'''
    # _code = '''int** (*dd)(int* (*d1)(void v0, void v1), void v2);'''
    # _code = '''int** (*dd)(int* (*)(void, void), void);'''
    # _code = 'int* d;';
    # _code = 'int d;';
    # _code = "int (*dd);"
    # _code = "int (**dd1);"
    # _code = "int _num = 1;"
    node_ast = parser.parse(_code, filename='<none>', debug=False) # debug=True

    print(dir(c_ast))

    trans = Transform()
    for ext in node_ast.ext:
        t = type(ext)
        print(t, ext)
        if(t == c_ast.Decl):
            print(trans.extract_cast(ext))
            print(trans.get_decl_name())


    

    # print(ext)
    # print('c_source:', generator.visit(ext) + ';')

    # node_ast.show()
    # print(node_ast)

