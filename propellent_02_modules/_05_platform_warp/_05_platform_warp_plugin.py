# -- encoding:utf-8 --
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

from propellent_07_job.warp_parameter_GUI_file import *
data_path = os.path.abspath(os.path.join(os.getcwd(), "...")) + '\\abaqus_plugins\\propellant\\propellent_04_data\\'

if var_data().extract_var == 'GUI':
    data_Force = Data_GUI().Force
    data_Thickness = Data_GUI().Thickness
    data_Width = Data_GUI().Width
    data_CPUnum = Data_GUI().CPUnum
elif var_data().extract_var == 'file':

    data_Force = Data_file().Force
    data_Thickness = Data_file().Thickness
    data_Width = Data_file().Width
    data_CPUnum = Data_file().CPUnum


###########################################################################
# Class definition
###########################################################################

class _05_platform_warp_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='warp',
            objectName='propellent_02_modules._05_platform_warp.warp_kernel', registerQuery=False)
        pickedDefault = ''
        self.FKw = AFXFloatKeyword(self.cmd, 'F', True, data_Force)
        self.thicknessKw = AFXFloatKeyword(self.cmd, 'thickness', True, data_Thickness)
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True, data_Width)
        self.Cpu_numKw = AFXFloatKeyword(self.cmd, 'Cpu_num', True, data_CPUnum)
        self.var_exportKw = AFXBoolKeyword(self.cmd, 'var_export', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.var_inputKw = AFXBoolKeyword(self.cmd, 'var_input', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, data_path + 'Warp_v2019-01-27_23-08-18.txt')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _05_platform_warpDB
        return _05_platform_warpDB._05_platform_warpDB(self)

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
        if self.FKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xd4\xa4\xbd\xf4\xc1\xa6\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.thicknessKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层尺寸必须为正数，请重新输入！'
                               b'\xcf\xcb\xce\xac\xba\xf1\xb6\xc8\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.widthKw.getValue() <= 0:
            # Force must be da yu 0
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xcf\xcb\xce\xac\xbf\xed\xb6\xc8\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.Cpu_numKw.getValue() <= 0:
            # xianwei must be da yu 0
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'CPU\xba\xcb\xca\xfd\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        else:
            return True
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
