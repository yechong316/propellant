# -*- coding: utf-8 -*-
#!/usr/bin/python3
# propellant_v0125-1100 
# Authorn:Jaime Lannister
# Time:2019/2/28-11:49 

from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

class Composite_plugin(AFXForm):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, owner):
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd_composite = AFXGuiCommand(mode=self, method='orthotropic_mat',
        objectName='propellent_02_modules._01_platform_Part.Part_wcm_kernel',
        registerQuery=False)
        pickedDefault = ''

        # 定义专属复合材料的属性

        self.nameKw = AFXStringKeyword(self.cmd_composite, 'name', True, 'T700')

        # 密度
        self.desityKw = AFXFloatKeyword(self.cmd_composite, 'desity', True, 0.056)

        # 弹性模量
        self.elasticKw = AFXTableKeyword(self.cmd_composite, 'elastic', True)
        self.elasticKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(2, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(3, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(4, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(5, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(6, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(7, AFXTABLE_TYPE_FLOAT)
        self.elasticKw.setColumnType(8, AFXTABLE_TYPE_FLOAT)

        # 热传导
        self.conductivityKw = AFXTableKeyword(self.cmd_composite, 'conductivity', True)
        self.conductivityKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.conductivityKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)

        # 热膨胀
        self.expansionKw = AFXTableKeyword(self.cmd_composite, 'expansion', True)
        self.expansionKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.expansionKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)

        # 比热容
        self.specificKw = AFXFloatKeyword(self.cmd_composite, 'specific', True, 0.1)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import compositeDB
        return compositeDB.CompositeDB(self)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1, kw2, d in self.radioButtonGroups.values():
            try:
                value = d[kw1.getValue()]
                kw2.setValue(value)
            except:
                pass
        return True

    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

    def onCmdWarning(self, sender, sel, ptr):
        # print 'haha'
        if sender.getPressedButtonId() == \
                AFXDialog.ID_CLICKED_YES:
            self.issueCommands()
        elif sender.getPressedButtonId() == \
                AFXDialog.ID_CLICKED_NO:
            self.deactivate()


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





