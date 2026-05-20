# -*- coding: utf-8 -*-
from cuckoo.common.abstracts import Machinery

class Physical(Machinery):
    def _initialize(self, machine_dict):
        super(Physical, self)._initialize(machine_dict)

    def _status(self, machine_name):
        return self.MACHINERY_RUNNING

    def start(self, label, task=None):
        pass

    def stop(self, label):
        pass

    def _list(self):
        return self.machines()
