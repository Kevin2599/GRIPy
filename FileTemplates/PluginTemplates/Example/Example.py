# -*- coding: utf-8 -*-

from plugins import DefaultPlugin
from plugins.Example import core
from om.Manager import ObjectManager

class ExamplePlugin(DefaultPlugin):

    def __init__(self):
        super(ExamplePlugin, self).__init__()
        self._OM = ObjectManager(self)
        self.input = {}
        self.output = {}

    @classmethod
    def reloadcore(cls):
        reload(core)
        setattr(cls, 'doinput', core.doinput)
        setattr(cls, 'dojob', core.dojob)
        setattr(cls, 'dooutput', core.dooutput)
    
    def run(self):
        output = self.dojob(**self.input)
        if output:
            self.output = output
        else:
            self.output = {}
    
    
ExamplePlugin.reloadcore()
