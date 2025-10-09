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

print(yacctab._lr_action.get(0))
