import unittest
from hoka.adapter.base import BaseAdapter
from OFS.Application import Application
from zope.configuration import xmlconfig

import hoka.patches.get_adapter
import hoka.adapter.auth
import zope.component
import z3c.autoinclude
context = xmlconfig.file('meta.zcml', zope.component)
xmlconfig.file('meta.zcml', z3c.autoinclude, context=context)
xmlconfig.file('configure.zcml', hoka.patches.get_adapter, context=context)
xmlconfig.file('configure.zcml', hoka.adapter.auth, context=context)


def makeConnection():
    import ZODB
    from ZODB.DemoStorage import DemoStorage

    s = DemoStorage()
    return ZODB.DB( s ).open()

class TestBase(unittest.TestCase):

    def setUp( self ):
        self.connection = makeConnection()
        r = self.connection.root()
        a = Application()
        r['Application'] = a
        self.root = a

    def test_auth(self):
        self.root.get_adapter('auth')()

if __name__ == '__main__':
    unittest.main()
