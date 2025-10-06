import sys

sys.path.append('./')

import yacctab

print(yacctab)

'''
_module = 'pycparser.yacctab'
exec('import %s' % _module)
yacctab = sys.modules[_module]
'''

print(yacctab)

print(yacctab._lr_action.get(0))
