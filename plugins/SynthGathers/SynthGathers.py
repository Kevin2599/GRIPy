from om.Manager import ObjectManager
from plugins import SimpleDialogPlugin


class SynthGathers(SimpleDialogPlugin):

    def __init__(self):
        super(SynthGathers, self).__init__()
        #self._OM = ObjectManager(self)

    def run(self, uiparent):
        print 'uiparent:', uiparent