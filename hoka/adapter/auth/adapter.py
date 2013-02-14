from hoka.adapter.base import *
from AccessControl import getSecurityManager

class IAuth(Interface):
    pass

class Adapter(BaseAdapter):

    def __call__(self):
        """Return the current authenticated user"""
        return getSecurityManager().getUser()