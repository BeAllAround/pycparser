import sys

sys.path.append('./')

import yacctab

print(__name__, yacctab)

'''
_module = 'pycparser.yacctab'
exec('import %s' % _module)
yacctab = sys.modules[_module]
'''

print(__name__, yacctab)

external_6 = yacctab._lr_action.get(0)


print(external_6)


external_0 = {'$end': -346, 'SEMI': 10, 'PPHASH': 21, 'PPPRAGMA': 22, '_PRAGMA': 23, '_STATIC_ASSERT': 26, 'ID': 27, 'CASE': 28, 'DEFAULT': 29, 'IF': 32, 'SWITCH': 34, 'WHILE': 35, 'DO': 36, 'FOR': 37, 'GOTO': 38, 'BREAK': 39, 'CONTINUE': 40, 'RETURN': 41, 'LBRACE': 51, 'LPAREN': 24, 'TIMES': 54, 'TYPEID': 59, 'ENUM': 60, 'VOID': 62, '_BOOL': 63, 'CHAR': 64, 'SHORT': 65, 'INT': 66, 'LONG': 67, 'FLOAT': 68, 'DOUBLE': 69, '_COMPLEX': 70, 'SIGNED': 71, 'UNSIGNED': 72, '__INT128': 73, '_ATOMIC': 74, 'CONST': 75, 'RESTRICT': 76, 'VOLATILE': 77, 'AUTO': 78, 'REGISTER': 79, 'STATIC': 52, 'EXTERN': 80, 'TYPEDEF': 81, '_THREAD_LOCAL': 82, 'INLINE': 83, '_NORETURN': 84, '_ALIGNAS': 85, 'STRUCT': 88, 'UNION': 89, 'PLUSPLUS': 92, 'MINUSMINUS': 93, 'SIZEOF': 96, '_ALIGNOF': 97, 'AND': 100, 'PLUS': 98, 'MINUS': 99, 'NOT': 102, 'LNOT': 103, 'OFFSETOF': 107, 'INT_CONST_DEC': 108, 'INT_CONST_OCT': 109, 'INT_CONST_HEX': 110, 'INT_CONST_BIN': 111, 'INT_CONST_CHAR': 112, 'FLOAT_CONST': 113, 'HEX_FLOAT_CONST': 114, 'CHAR_CONST': 115, 'WCHAR_CONST': 116, 'U8CHAR_CONST': 117, 'U16CHAR_CONST': 118, 'U32CHAR_CONST': 119, 'STRING_LITERAL': 120, 'WSTRING_LITERAL': 121, 'U8STRING_LITERAL': 122, 'U16STRING_LITERAL': 123, 'U32STRING_LITERAL': 124}


print(external_0)
