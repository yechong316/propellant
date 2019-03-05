# -- encoding:utf-8 --
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _05_platform_warpDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe-\xb2\xf8\xc8\xc6\xb9\xa4\xd2\xd5',
            self.OK | self.APPLY | self.CANCEL | self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR | DATADIALOG_BAILOUT)

            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText(b'\xc8\xb7\xb6\xa8')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')
            
        l = FXLabel(p=self, text='\xb1\xbe\xb2\xe5\xbc\xfe\xd3\xc3\xd3\xda\xb2\xf8\xc8\xc6\xb9\xa4\xd2\xd5\xb7\xc2\xd5\xe6', opts=JUSTIFY_LEFT)
        l = FXLabel(p=self, text='\xd4\xd8\xba\xc9:', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        HFrame_6 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_6, ncols=12, labelText='\xc7\xeb\xca\xe4\xc8\xeb\xd4\xa4\xbd\xf4\xc1\xa6\xa3\xba', tgt=form.FKw, sel=0)
        HFrame_4 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_4, ncols=12, labelText='\xcf\xcb\xce\xac\xc6\xcc\xb2\xe3\xba\xf1\xb6\xc8\xa3\xba', tgt=form.thicknessKw, sel=0)
        AFXTextField(p=HFrame_4, ncols=12, labelText='\xcf\xcb\xce\xac\xbf\xed\xb6\xc8\xa3\xba', tgt=form.widthKw, sel=0)
        l = FXLabel(p=self, text='\xcc\xe1\xbd\xbb\xbc\xc6\xcb\xe3\xa3\xba', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        HFrame_5 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_5, ncols=12, labelText='\xb5\xf7\xd3\xc3CPU\xba\xcb\xca\xfd:', tgt=form.Cpu_numKw, sel=0)
        # 2019年1月26日17:31:39 应主任要求，建立两个控件，读取数据和导出数据
        # 建立一个平行控制栏，令两个控件的位置平行
        HFrame_data_in_out = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        # 新增一个检查框，是否导出数据
        FXCheckButton(p=HFrame_data_in_out, text=
        b'\xb5\xbc\xb3\xf6\xbd\xe7\xc3\xe6\xb2\xce\xca\xfd'
                      , tgt=form.var_exportKw, sel=0)
        # 新增一个检查框，是否读取数据
        self.var_input_data = FXCheckButton(p=HFrame_data_in_out, text=
        b'\xb6\xc1\xc8\xa1\xd2\xd1\xd3\xd0\xce\xc4\xbc\xfe\xca\xfd\xbe\xdd'
                                            , tgt=form.var_inputKw, sel=0)
        # 建立读取数据的框
        fileHandler_input = Warp_DBFileHandler(form, 'inputfile', 'txt(*.txt)')
        fileTextHf = FXHorizontalFrame(p=HFrame_data_in_out, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        fileTextHf.setSelector(99)
        self.input_data = AFXTextField(p=fileTextHf, ncols=12, labelText=
        b'\xce\xc4\xbc\xfe\xc2\xb7\xbe\xb6:'
                                       , tgt=form.inputfileKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        self.read_out_data = FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler_input, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        self.form = form



class Warp_DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*.txt'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, Warp_DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
