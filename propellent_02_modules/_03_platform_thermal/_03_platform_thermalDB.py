# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _03_platform_thermalDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7',
            self.OK|self.APPLY|self.CANCEL|self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR| DATADIALOG_BAILOUT)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('\xc8\xb7\xb6\xa8')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')
            
        l = FXLabel(p=self, text='\xb1\xbe\xb2\xe5\xbc\xfe\xd6\xbc\xd4\xda\xb6\xa8\xd2\xe5\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7\xca\xd4\xd1\xe9\xb5\xc4\xc9\xfd\xbd\xb5\xce\xc2\xc7\xfa\xcf\xdf\xd2\xd4\xbc\xb0\xcc\xe1\xbd\xbb\xbc\xc6\xcb\xe3', opts=JUSTIFY_LEFT)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        HFrame_9 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_9, ncols=12, labelText='\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7\xca\xd4\xd1\xe9\xd7\xdc\xca\xb1\xbc\xe4\xa3\xba', tgt=form.timePeriod1Kw, sel=0)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=self, text='\xd4\xd8\xba\xc9:', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        AFXTextField(p=self, ncols=12, labelText='\xb9\xb9\xbc\xfe\xb3\xf5\xca\xbc\xce\xc2\xb6\xc8\xa3\xa8\xb5\xa5\xce\xbb\xce\xaa\xc3\xeb\xa3\xa9\xa3\xba', tgt=form.intialtempKw, sel=0)
        HFrame_6 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=self, text='\xb6\xa8\xd2\xe5\xc9\xfd\xbd\xb5\xce\xc2\xc7\xfa\xcf\xdf:', opts=JUSTIFY_LEFT)
        vf = FXVerticalFrame(self, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 7, 3, 10, 3, form.hermal_zaihe_listKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
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
        # table.setItemFloatValue(1, 2, 100)
        HFrame_10 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        pickHf = FXHorizontalFrame(p=HFrame_10, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xbf\xc7\xcc\xe5\xcd\xe2\xb1\xed\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _03_platform_thermalDBPickHandler(form, form.Composite_outfaceKw, 'Pick an entity', FACES, MANY, label)
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
        AFXTextField(p=HFrame_11, ncols=12, labelText='CPU\xca\xfd\xc1\xbf\xa3\xba:', tgt=form.Cpu_numKw, sel=0)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        # 2019��1��26��17:31:39 Ӧ����Ҫ�󣬽��������ؼ�����ȡ���ݺ͵�������
        # ����һ��ƽ�п��������������ؼ���λ��ƽ��
        HFrame_data_in_out = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        # ����һ�������Ƿ񵼳�����
        FXCheckButton(p=HFrame_data_in_out, text=
        b'\xb5\xbc\xb3\xf6\xbd\xe7\xc3\xe6\xb2\xce\xca\xfd'
                      , tgt=form.var_exportKw, sel=0)
        # ����һ�������Ƿ��ȡ����?
        self.var_input_data = FXCheckButton(p=HFrame_data_in_out, text=
        b'\xb6\xc1\xc8\xa1\xd2\xd1\xd3\xd0\xce\xc4\xbc\xfe\xca\xfd\xbe\xdd'
                                            , tgt=form.var_inputKw, sel=0)
        # ������ȡ���ݵĿ�
        fileHandler_input = Thermal_DBFileHandler(form, 'inputfile', 'txt(*.txt)')
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

class _03_platform_thermalDBPickHandler(AFXProcedure):

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

                _03_platform_thermalDBPickHandler.count += 1
                self.setModeName('_03_platform_thermalDBPickHandler%d' % (_03_platform_thermalDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('None', 'Picked') )
                return None


class Thermal_DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*.txt'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, Thermal_DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
