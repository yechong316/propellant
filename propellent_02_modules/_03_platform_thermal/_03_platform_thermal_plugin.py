# coding:utf-8
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

from propellent_07_job.thermal_parameter_GUI_file import *

if var_data().extract_var == 'GUI':
    data_time = Data_GUI().time
    data_init_temp = Data_GUI().init_temp
    data_CPUnum = Data_GUI().CPUnum
elif var_data().extract_var == 'file':

    data_time = Data_file().time
    data_init_temp = Data_file().init_temp
    data_CPUnum = Data_file().CPUnum
###########################################################################
# Class definition
###########################################################################

class _03_platform_thermal_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='temprature_shock_input',
            objectName='propellent_02_modules._03_platform_thermal.temprature_shock_kernel', registerQuery=False)
        pickedDefault = ''
        self.timePeriod1Kw = AFXFloatKeyword(self.cmd, 'timePeriod1', True, data_time)
        print(self.timePeriod1Kw)
        self.intialtempKw = AFXFloatKeyword(self.cmd, 'intialtemp', True, data_init_temp)

        self.hermal_zaihe_listKw = AFXTableKeyword(self.cmd, 'hermal_zaihe_list', True)
        self.hermal_zaihe_listKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.hermal_zaihe_listKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        # self.hermal_zaihe_listKw.setItemText(1, 2,100)

        # setDefaultFloatValue
        self.Composite_outfaceKw = AFXObjectKeyword(self.cmd, 'Composite_outface', TRUE, pickedDefault)
        self.Cpu_numKw = AFXFloatKeyword(self.cmd, 'Cpu_num', True, data_CPUnum)
        self.var_exportKw = AFXBoolKeyword(self.cmd, 'var_export', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.var_inputKw = AFXBoolKeyword(self.cmd, 'var_input', AFXBoolKeyword.TRUE_FALSE,True, False)
        self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, None)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _03_platform_thermalDB
        return _03_platform_thermalDB._03_platform_thermalDB(self)

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
        if self.timePeriod1Kw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '温度冲击试验时间必须为正数!'
                               b'\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7\xca\xd4\xd1\xe9\xca\xb1\xbc\xe4\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.intialtempKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '初始温度必须为正数!'
                               b'\xb3\xf5\xca\xbc\xce\xc2\xb6\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.Cpu_numKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # 'CPU核数必须为正数!'
                               b'CPU\xba\xcb\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd!'
                               )
            return False
        else:
            return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

