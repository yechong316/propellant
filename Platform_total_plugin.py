# -*- coding: utf-8 -*-
# from abaqusGui import *
# from abaqusConstants import ALL
# import osutils, os, sys
import abaqus_gui


reload(sys)
sys.setdefaultencoding('utf-8')


###########################################################################
# Class definition
###########################################################################

class Platform_total_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='',
            objectName='', registerQuery=False)
        pickedDefault = ''
        self.keyword01Kw = AFXBoolKeyword(self.cmd, 'keyword01', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.keyword02Kw = AFXBoolKeyword(self.cmd, 'keyword02', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.keyword03Kw = AFXBoolKeyword(self.cmd, 'keyword03', AFXBoolKeyword.TRUE_FALSE, True, False)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import Platform_totalDB
        return Platform_totalDB.Platform_totalDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #

        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe', 
    #buttonText='固体发动机本质特性分析软件', 

    object=Platform_total_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import propellent_02_modules._01_platform_Part.Part_wcm_kernel\
 ,propellent_02_modules._02_platform_tie.tie_kernel\
 ,propellent_02_modules._03_platform_thermal.temprature_shock_kernel\
 ,propellent_02_modules._04_platform_curing.curing_kernel\
 ,propellent_02_modules._05_platform_warp.warp_kernel',
    applicableModules=ALL,     
    version='N/A',           
    author='N/A',              
    description='N/A',         
    helpUrl='N/A'
)
