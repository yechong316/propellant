#!/usr/bin/python
#-*-coding: UTF-8-*-
# -*- coding: mbcs -*-  
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

from propellent_07_job.tie_parameter_GUI_file import *

if var_data().extract_var == 'GUI':
    data_c_b_position = Data_GUI().c_b_position
    data_c_b_var = Data_GUI().c_b_var
    data_b_f_position = Data_GUI().b_f_position
    data_b_f_var = Data_GUI().b_f_var
    data_b_h_position = Data_GUI().b_h_position
    data_b_h_var = Data_GUI().b_h_var
    data_h_f_position = Data_GUI().h_f_position
    data_h_f_var = Data_GUI().h_f_var
elif var_data().extract_var == 'file':
#
    data_c_b_position = Data_file().c_b_position
    data_c_b_var = Data_file().c_b_var
    data_b_f_position = Data_file().b_f_position
    data_b_f_var = Data_file().b_f_var
    data_b_h_position = Data_file().b_h_position
    data_b_h_var = Data_file().b_h_var
    data_h_f_position = Data_file().h_f_position
    data_h_f_var = Data_file().h_f_var
data_path = os.path.abspath(os.path.join(os.getcwd(), "...")) + '\\abaqus_plugins\\propellant\\propellent_04_data\\'
###########################################################################
# Class definition
###########################################################################

class _02_platform_tie_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='tie_input',
            objectName='propellent_02_modules._02_platform_tie.tie_kernel', registerQuery=False)
        pickedDefault = ''
        self.Master_cbKw = AFXObjectKeyword(self.cmd, 'Master_cb', TRUE, pickedDefault)
        self.Slave_cbKw = AFXObjectKeyword(self.cmd, 'Slave_cb', TRUE, pickedDefault)
        self.Position_cbKw = AFXFloatKeyword(self.cmd, 'Position_cb', True, data_c_b_position)
        self.var_cbKw = AFXBoolKeyword(self.cmd, 'var_cb', AFXBoolKeyword.TRUE_FALSE, True, data_c_b_var)
        self.Master_bfKw = AFXObjectKeyword(self.cmd, 'Master_bf', TRUE, pickedDefault)
        self.Slave_bfKw = AFXObjectKeyword(self.cmd, 'Slave_bf', TRUE, pickedDefault)
        self.Position_bfKw = AFXFloatKeyword(self.cmd, 'Position_bf', True, data_b_f_position)
        self.var_bfKw = AFXBoolKeyword(self.cmd, 'var_bf', AFXBoolKeyword.TRUE_FALSE, True, data_b_f_var)
        self.Master_bhKw = AFXObjectKeyword(self.cmd, 'Master_bh', TRUE, pickedDefault)
        self.Slave_bhKw = AFXObjectKeyword(self.cmd, 'Slave_bh', TRUE, pickedDefault)
        self.Position_bhKw = AFXFloatKeyword(self.cmd, 'Position_bh', True, data_b_h_position)
        self.var_bhKw = AFXBoolKeyword(self.cmd, 'var_bh', AFXBoolKeyword.TRUE_FALSE, True, data_b_h_var)
        self.Master_hfKw = AFXObjectKeyword(self.cmd, 'Master_hf', TRUE, pickedDefault)
        self.Slave_hfKw = AFXObjectKeyword(self.cmd, 'Slave_hf', TRUE, pickedDefault)
        self.Position_hfKw = AFXFloatKeyword(self.cmd, 'Position_hf', True, data_h_f_position)
        self.var_hfKw = AFXBoolKeyword(self.cmd, 'var_hf', AFXBoolKeyword.TRUE_FALSE, True, data_h_f_var)
        self.var_exportKw = AFXBoolKeyword(self.cmd, 'var_export', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.var_inputKw = AFXBoolKeyword(self.cmd, 'var_input', AFXBoolKeyword.TRUE_FALSE,True, True)
        self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, data_path + 'Tie_v2019-03-06_14-36-51.txt')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _02_platform_tieDB
        return _02_platform_tieDB._02_platform_tieDB(self)

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
            # 当用户选择到错误实体上的面，弹出错误
        # 撰写位置容差的警告提示
        # 4组容差警告提示
        if self.Position_cbKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xbf\xc7\xcc\xe5\xd3\xeb\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.Position_bfKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层尺寸必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xd3\xeb\xb7\xe2\xcd\xb7\xb5\xc4\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.Position_bhKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xd3\xeb\xcd\xc6\xbd\xf8\xbc\xc1\xb5\xc4\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
                               )
            return False
        elif self.Position_hfKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xcd\xc6\xbd\xf8\xbc\xc1\xd3\xeb\xb7\xe2\xcd\xb7\xb5\xc4\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xb1\xd8\xd0\xeb\xca\xc7\xd5\xfd\xca\xfd!'
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

