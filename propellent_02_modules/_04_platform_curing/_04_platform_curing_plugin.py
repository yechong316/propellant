# -- encoding:utf-8 --
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

from propellent_07_job.curing_parameter_GUI_file import *
data_path = os.path.abspath(os.path.join(os.getcwd(), "...")) + '\\abaqus_plugins\\propellant\\propellent_04_data\\'

if var_data().extract_var == 'GUI':
    data_time = Data_GUI().time
    data_init_temp = Data_GUI().init_temp
    data_CPUnum = Data_GUI().CPUnum
elif var_data().extract_var == 'file':
#
    data_time = Data_file().time
    data_init_temp = Data_file().init_temp
    data_CPUnum = Data_file().CPUnum
###########################################################################
# Class definition
###########################################################################

class _04_platform_curing_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='curing_input',
            objectName='propellent_02_modules._04_platform_curing.curing_kernel', registerQuery=False)
        pickedDefault = ''
        self.intialtempKw = AFXFloatKeyword(self.cmd, 'intialtemp', True, data_init_temp)
        self.timePeriod1Kw = AFXFloatKeyword(self.cmd, 'timePeriod1', True, data_time)
        self.Composite_outfaceKw = AFXObjectKeyword(self.cmd, 'Composite_outface', TRUE, pickedDefault)
        self.Cpu_numKw = AFXFloatKeyword(self.cmd, 'Cpu_num', True, data_CPUnum)
        self.table_listKw = AFXTableKeyword(self.cmd, 'table_list', True)
        self.table_listKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table_listKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.var_exportKw = AFXBoolKeyword(self.cmd, 'var_export', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.var_inputKw = AFXBoolKeyword(self.cmd, 'var_input', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, data_path + 'Curing_v2019-03-07_10-55-14.txt')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _04_platform_curingDB
        return _04_platform_curingDB._04_platform_curingDB(self)

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
                               # '固化反应时间必须为正数!'
                               b'\xb9\xcc\xbb\xaf\xb7\xb4\xd3\xa6\xca\xb1\xbc\xe4\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
