# -*- coding: utf-8 -*-

import os
import logging
import weakref
from OM.Manager import ObjectManager
from UI.uimanager import UIManager
from FileIO.utils import AsciiFile


class GripyController(object):
    _OM_file = None
        
    def __init__(self, owner):
        try:
            owner_str = owner.name
        except AttributeError:
            owner_str = owner.__class__.__name__
        msg = owner_str + ' calls for a new ' + self.__class__.__name__ + ' instance.'    
        logging.info(msg)
        
        self._ownerref = weakref.ref(owner)
        self._OM = ObjectManager(owner)
        self._UIM = UIManager()
        self._OM_file = GripyController._OM_file
        #self.PM = Plugins.PluginManager.get()
        #self.dir_name = wx.EmptyString
        #self.file_name = wx.EmptyString
        msg = owner_str + ' created sucessfully a new ' + self.__class__.__name__ + ' instance.'    
        logging.info(msg)        


    def load_project(self, dirname, filename):
        self._OM_file = os.path.join(dirname, filename)
        self._OM.load(self._OM_file)
        mwc = self._UIM.list('main_window_controller')[0]
        tree_ctrl = self._UIM.list('tree_controller', mwc.uid)[0]
        if tree_ctrl:        
            tree_ctrl.set_project_name(filename)
                  
                  
    def save_project(self):
        if self._OM_file:
            self._OM.save(self._OM_file)
        
    
    def create(self, controller_tid, parent_uid=None, **base_state):
        obj = None
        try:
            obj = self._UIM.create(controller_tid, parent_uid, **base_state)   
        except Exception:
            logging.exception('')
        return obj
        
    def save_UI_state(self, filename):
        try:
            _state = self._UIM._getstate()
        except Exception:
            _state = None
            msg = 'ERROR: UI State cannot be gotten from UI Manager.' 
            logging.exception(msg)
        if _state is not None: 
            try:
                AsciiFile.write_json_file(_state, filename)
                msg = 'UI state successfully saved to file ' + filename 
                logging.info(msg)
            except Exception:
                raise
        
  
    @staticmethod    
    def get_event_controllers(event):
        try:
            _UIM = UIManager()
            _controller = _UIM.get(event.GetEventObject()._controller_uid)
            _root_controller = _controller.get_root_controller()          
            return _controller, _root_controller
        except Exception:
            return None
        

        
        