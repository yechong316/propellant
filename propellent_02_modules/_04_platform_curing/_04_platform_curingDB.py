#-*-coding: UTF-8-*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _04_platform_curingDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe-\xb9\xcc\xbb\xaf\xb9\xa4\xd2\xd5',
            self.OK|self.APPLY|self.CANCEL|self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR|DATADIALOG_BAILOUT)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('\xc8\xb7\xb6\xa8')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')
            
        l = FXLabel(p=self, text='\xb1\xbe\xb2\xe5\xbc\xfe\xd6\xbc\xd4\xda\xb6\xa8\xb9\xcc\xbb\xaf\xb9\xa4\xd2\xd5\xcf\xe0\xb9\xd8\xb5\xc4\xb7\xc2\xd5\xe6\xb2\xce\xca\xfd', opts=JUSTIFY_LEFT)
        HFrame_13 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_6 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_6, ncols=12, labelText='\xb9\xb9\xbc\xfe\xb3\xf5\xca\xbc\xce\xc2\xb6\xc8\xa3\xba', tgt=form.intialtempKw, sel=0)
        AFXTextField(p=HFrame_6, ncols=12, labelText='\xb9\xcc\xbb\xaf\xca\xb1\xb3\xa4\xa3\xa8\xd2\xd4\xc3\xeb\xce\xaa\xb5\xa5\xce\xbb\xa3\xa9\xa3\xba', tgt=form.timePeriod1Kw, sel=0)
        HFrame_10 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        pickHf = FXHorizontalFrame(p=HFrame_10, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xbf\xc7\xcc\xe5\xcd\xe2\xb1\xed\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _04_platform_curingDBPickHandler(form, form.Composite_outfaceKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        l = FXLabel(p=HFrame_10, text='\xd7\xa2\xd2\xe2\xa3\xba\xc7\xeb\xd1\xa1\xd4\xf1\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xbf\xc7\xcc\xe5\xc9\xcf\xb5\xc4\xc4\xb3\xd2\xbb\xb8\xf6\xc3\xe6\xa3\xac\xb7\xf1\xd4\xf2\xb1\xa8\xb4\xed\xa3\xa1\xa3\xa1\xa3\xa1', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=self, text='\xcc\xe1\xbd\xbb\xbc\xc6\xcb\xe3:', opts=JUSTIFY_LEFT)
        HFrame_11 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_11, ncols=12, labelText='\xb5\xf7\xd3\xc3CPU\xba\xcb\xca\xfd:', tgt=form.Cpu_numKw, sel=0)
        vf = FXVerticalFrame(self, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        vf.setSelector(99)
        table = AFXTable(vf, 7, 3, 10, 3, form.table_listKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_CUT|AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS|AFXTable.POPUP_READ_FROM_FILE|AFXTable.POPUP_WRITE_TO_FILE)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 100)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 100)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('\xca\xb1\xbc\xe4\xa3\xa8\xb5\xa5\xce\xbb\xce\xaas\xa3\xa9\t\xce\xc2\xb6\xc8\xa3\xa8\xd2\xd4\xb9\xfa\xbc\xca\xce\xc2\xb1\xea\xce\xaa\xd7\xbc\xa3\xac\xb5\xa5\xce\xbb\xce\xaaK\xa3\xa9')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        # 2019年2月22日09:30:24 新增列表显示默认值
        # 跟据执行文件中的代码，依次生成下列两个label之间的参数，使其界面显示参数值
        # table_start
        table.setItemFloatValue(1, 1, 0)
        table.setItemFloatValue(1, 2, 297)
        table.setItemFloatValue(2, 1, 20)
        table.setItemFloatValue(2, 2, 232)
        table.setItemFloatValue(3, 1, 740)
        table.setItemFloatValue(3, 2, 232)
        table.setItemFloatValue(4, 1, 741)
        table.setItemFloatValue(4, 2, 322)
        table.setItemFloatValue(5, 1, 1460)
        table.setItemFloatValue(5, 2, 322)
        table.setItemFloatValue(6, 1, 1461)
        table.setItemFloatValue(6, 2, 297)
        # table_end
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
        fileHandler_input = _04_platform_curingDBFileHandler(form, 'inputfile', 'txt(*.txt)')
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


###########################################################################
# Class definition
###########################################################################

class _04_platform_curingDBPickHandler(AFXProcedure):

        count = 0

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def __init__(self, form, keyword, prompt, entitiesToPick, numberToPick, label):

                self.form = form
                self.keyword = keyword
                self.prompt = prompt
                self.entitiesToPick = entitiesToPick # Enum value
                self.numberToPick = numberToPick # Enum value
                self.label = label
                self.labelText = label.getText()

                AFXProcedure.__init__(self, form.getOwner())

                _04_platform_curingDBPickHandler.count += 1
                self.setModeName('_04_platform_curingDBPickHandler%d' % (_04_platform_curingDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('None', 'Picked') )
                return None


###########################################################################
# Class definition
###########################################################################

class _04_platform_curingDBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, _04_platform_curingDBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
