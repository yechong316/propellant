# -* - coding:UTF-8 -*-
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


#assert os.path.abspath(os.path.join(os.getcwd(), ".")) == "C:\Users\yanguowei\abaqus_plugins\e", 'current path is not "C:\Users\yanguowei\abaqus_plugins\e"'

from propellent_07_job.part_parameter_GUI_file import *

# 2019年2月14日22:23:58
if var_data().extract_var == 'GUI':

    # 读取界面默认数据
    data_b_d = Data_GUI().b_d
    data_b_e = Data_GUI().b_e
    data_b_p = Data_GUI().b_p
    data_b_c = Data_GUI().b_c
    data_b_s = Data_GUI().b_s
    data_b_ep = Data_GUI().b_ep
    data_b_mesh_size = Data_GUI().b_mesh_size
    data_f_d = Data_GUI().f_d
    data_f_e = Data_GUI().f_e
    data_f_p = Data_GUI().f_p
    data_f_c = Data_GUI().f_c
    data_f_s = Data_GUI().f_s
    data_f_ep = Data_GUI().f_ep
    data_f_mesh_size = Data_GUI().f_mesh_size
    data_h_d = Data_GUI().h_d
    data_h_e = Data_GUI().h_e
    data_h_p = Data_GUI().h_p
    data_h_c = Data_GUI().h_c
    data_h_s = Data_GUI().h_s
    data_h_ep = Data_GUI().h_ep
    data_h_mesh_size = Data_GUI().h_mesh_size

# 此时读取file数据
elif var_data().extract_var == 'file':
    data_b_d = Data_file().b_d
    data_b_e = Data_file().b_e
    data_b_p = Data_file().b_p
    data_b_c = Data_file().b_c
    data_b_s = Data_file().b_s
    data_b_ep = Data_file().b_ep
    data_b_mesh_size = Data_file().b_mesh_size
    data_f_d = Data_file().f_d
    data_f_e = Data_file().f_e
    data_f_p = Data_file().f_p
    data_f_c = Data_file().f_c
    data_f_s = Data_file().f_s
    data_f_ep = Data_file().f_ep
    data_f_mesh_size = Data_file().f_mesh_size
    data_h_d = Data_file().h_d
    data_h_e = Data_file().h_e
    data_h_p = Data_file().h_p
    data_h_c = Data_file().h_c
    data_h_s = Data_file().h_s
    data_h_ep = Data_file().h_ep
    data_h_mesh_size = Data_file().h_mesh_size
# '''
# 2019年2月14日00:00:22  经测试，以上方法可行，设置开关，根据是否导入文件数据，在界面上显示不同来源的数据
# '''part_wcm_plugin.py


CAD_path = os.path.abspath(os.path.join(os.getcwd(), "...")) + '\\abaqus_plugins\\propellant\\propellent_06_CAD\\' 


###########################################################################
# Class definition
###########################################################################

class Part_wcm_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        # AFXForm.__init__(self, owner)

        self.radioButtonGroups = {}

        # 2019年2月27日17:53:51 定义原始的版本
        self.cmd = AFXGuiCommand(mode=self, method='part_var',
            objectName='propellent_02_modules._01_platform_Part.Part_wcm_kernel', registerQuery=False)
        pickedDefault = ''

        # 复合材料
        self.filepath_cKw = AFXStringKeyword(self.cmd, 'filepath_c', True, CAD_path + 'composite.sat')
        self.desity_cKw = AFXFloatKeyword(self.cmd, 'desity_c', True, 1.23E-006)
        self.Elastic_cKw = AFXFloatKeyword(self.cmd, 'Elastic_c', True, 235000)
        self.Poisson_cKw = AFXFloatKeyword(self.cmd, 'Poisson_c', True, 0.33)
        self.Conductivity_cKw = AFXFloatKeyword(self.cmd, 'Conductivity_c', True, 0.00043)
        self.SpecificHeat_cKw = AFXFloatKeyword(self.cmd, 'SpecificHeat_c', True, 826)
        self.Expansion_cKw = AFXFloatKeyword(self.cmd, 'Expansion_c', True, 0.00143)
        self.size_cKw = AFXFloatKeyword(self.cmd, 'size_c', True, 5)

        # 包覆层
        self.filepath_bKw = AFXStringKeyword(self.cmd, 'filepath_b', True, CAD_path + 'bfc.sat')
        self.desity_bKw = AFXFloatKeyword(self.cmd, 'desity_b', True, data_b_d)
        self.Elastic_bKw = AFXFloatKeyword(self.cmd, 'Elastic_b', True, data_b_e)
        self.Poisson_bKw = AFXFloatKeyword(self.cmd, 'Poisson_b', True, data_b_p)
        self.Conductivity_bKw = AFXFloatKeyword(self.cmd, 'Conductivity_b', True, data_b_c)
        self.SpecificHeat_bKw = AFXFloatKeyword(self.cmd, 'SpecificHeat_b', True, data_b_s)
        self.Expansion_bKw = AFXFloatKeyword(self.cmd, 'Expansion_b', True, data_b_ep)
        self.size_bKw = AFXFloatKeyword(self.cmd, 'size_b', True, data_b_mesh_size)

        # 封头
        self.filepath_fKw = AFXStringKeyword(self.cmd, 'filepath_f', True, CAD_path + 'fengtou.sat')
        self.desity_fKw = AFXFloatKeyword(self.cmd, 'desity_f', True, data_f_d)
        self.Elastic_fKw = AFXFloatKeyword(self.cmd, 'Elastic_f', True, data_f_e)
        self.Poisson_fKw = AFXFloatKeyword(self.cmd, 'Poisson_f', True, data_f_p)
        self.Conductivity_fKw = AFXFloatKeyword(self.cmd, 'Conductivity_f', True, data_f_c)
        self.SpecificHeat_fKw = AFXFloatKeyword(self.cmd, 'SpecificHeat_f', True, data_f_s)
        self.Expansion_fKw = AFXFloatKeyword(self.cmd, 'Expansion_f', True, data_f_ep)
        self.size_fKw = AFXFloatKeyword(self.cmd, 'size_f', True, data_f_mesh_size)

        # 推进剂
        self.filepath_hKw = AFXStringKeyword(self.cmd, 'filepath_h', True, CAD_path + 'propeller.sat')
        self.desity_hKw = AFXFloatKeyword(self.cmd, 'desity_h', True, data_h_d)
        self.Elastic_hKw = AFXFloatKeyword(self.cmd, 'Elastic_h', True, data_h_e)
        self.Poisson_hKw = AFXFloatKeyword(self.cmd, 'Poisson_h', True, data_h_p)
        self.Conductivity_hKw = AFXFloatKeyword(self.cmd, 'Conductivity_h', True, data_h_c)
        self.SpecificHeat_hKw = AFXFloatKeyword(self.cmd, 'SpecificHeat_h', True, data_h_s)
        self.Expansion_hKw = AFXFloatKeyword(self.cmd, 'Expansion_h', True, data_h_ep)
        self.size_hKw = AFXFloatKeyword(self.cmd, 'size_h', True, data_h_mesh_size)

        # 开关函数
        self.var_exportKw = AFXBoolKeyword(self.cmd, 'var_export', AFXBoolKeyword.TRUE_FALSE,True, False)
        self.var_inputKw = AFXBoolKeyword(self.cmd, 'var_input', AFXBoolKeyword.TRUE_FALSE,True, False)
        self.inputfileKw = AFXStringKeyword(self.cmd, 'inputfile', True, None)
        self.var_WCMKw = AFXBoolKeyword(self.cmd, 'var_WCM', AFXBoolKeyword.TRUE_FALSE, True, False)
        



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import Part_wcm_DB
        return Part_wcm_DB.Part_wcm_DB(self)


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
    def doCustomChecks(self):
        '''
        本部分为复合材料部分的所有参数警告，当输入为0
        :param self:
        :return:
        '''
        # 4个构件文件路径警告提示
        if self.filepath_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层尺寸必须为正数，请重新输入！'
                               b'\xc7\xeb\xb5\xbc\xc8\xeb\xb0\xfc\xb8\xb2\xb2\xe3CAD\xcd\xbc'
                               )
            return False
        elif self.filepath_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xc7\xeb\xb5\xbc\xc8\xeb\xb7\xe2\xcd\xb7CAD\xcd\xbc'
                               )

            return False
        elif self.filepath_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               b'\xc7\xeb\xb5\xbc\xc8\xeb\xcd\xc6\xbd\xf8\xbc\xc1CAD\xcd\xbc'
                               )
        # 构件网格尺寸警告提示
        elif self.size_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层尺寸必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )
            return False
        elif self.size_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '封头尺寸必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )

            return False
        elif self.size_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '火药尺寸必须为正数，请重新输入！'
                               b'\xcd\xc6\xbd\xf8\xbc\xc1\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )
        # 4个构件密度警告提示
        elif self.desity_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层密度必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xc3\xdc\xb6\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1')
            return False
        elif self.desity_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '封头密度必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xc3\xdc\xb6\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )
            return False
        elif self.desity_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '火药密度必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xc3\xdc\xb6\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )
            return False
        # 4个构件弹性模量警告提示
        elif self.Elastic_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层弹性模量必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1'
                               )
            return False
        elif self.Elastic_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '封头弹性模量必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xb5\xc4\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1')
            return False
        elif self.Elastic_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '火药弹性模量必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xb5\xc4\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd\xa3\xac\xc7\xeb\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xa3\xa1')
            return False
        # 4个构件泊松比警告提示
        elif self.Poisson_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层的泊松比必须为正数'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xb2\xb4\xcb\xc9\xb1\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Poisson_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xb5\xc4\xb2\xb4\xcb\xc9\xb1\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Poisson_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '火药的泊松比必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xb5\xc4\xb2\xb4\xcb\xc9\xb1\xc8\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        # 4个构件热传导警告提示
        elif self.Conductivity_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '包覆层的热传导系数必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xc8\xc8\xb4\xab\xb5\xbc\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Conductivity_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '封头的热传导系数必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xb5\xc4\xc8\xc8\xb4\xab\xb5\xbc\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Conductivity_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xb5\xc4\xc8\xc8\xb4\xab\xb5\xbc\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        # 4个构件比热容警告提示
        elif self.SpecificHeat_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.SpecificHeat_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xb5\xc4\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.SpecificHeat_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xb5\xc4\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        # 4个构件热膨胀警告提示
        elif self.Expansion_bKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xb0\xfc\xb8\xb2\xb2\xe3\xb5\xc4\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Expansion_fKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xb7\xe2\xcd\xb7\xb5\xc4\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        elif self.Expansion_hKw.getValue() <= 0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                               # '复合材料尺寸必须为正数，请重新输入！'
                               b'\xbb\xf0\xd2\xa9\xb5\xc4\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd\xb1\xd8\xd0\xeb\xce\xaa\xd5\xfd\xca\xfd'
                               )
            return False
        else:
            return True

    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
    def onCmdWarning(self, sender, sel, ptr):
        #print 'haha'
        if sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_YES:
                self.issueCommands()
        elif sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_NO:
                self.deactivate() 
