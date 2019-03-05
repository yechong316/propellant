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

class _02_platform_tieDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe-\xb0\xf3\xb6\xa8\xb9\xd8\xcf\xb5',
            self.OK|self.APPLY|self.CANCEL|self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR| DATADIALOG_BAILOUT)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText(b'\xc8\xb7\xb6\xa8')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')
            
        l = FXLabel(p=self, text='\xb1\xbe\xb2\xe5\xbc\xfe\xd6\xbc\xd4\xda\xb6\xa8\xd2\xe54\xb8\xf6\xb9\xb9\xbc\xfe\xd6\xae\xbc\xe4\xb5\xc4\xb0\xf3\xb6\xa8\xb9\xd8\xcf\xb5', opts=JUSTIFY_LEFT)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=self, text='\xd7\xa2\xd2\xe2\xa3\xba\xd6\xf7\xb4\xd3\xc3\xe6\xb5\xc4\xd1\xa1\xd4\xf1\xca\xc7\xd3\xd0\xcb\xb3\xd0\xf2\xb5\xc4\xa3\xac\xbe\xd9\xc0\xfd\xa3\xba\xc8\xf4\xc4\xfa\xd0\xe8\xd2\xaa\xb6\xa8\xd2\xe5\xa1\xae\xb0\xfc\xb8\xb2\xb2\xe3-\xb7\xe2\xcd\xb7\xa1\xaf\xa3\xac\xd6\xf7\xc3\xe6\xb1\xd8\xd0\xeb\xd1\xa1\xd4\xf1\xb0\xfc\xb8\xb2\xb2\xe3\xc9\xcf\xb5\xc4\xc4\xb3\xb8\xf6\xc3\xe6', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        l = FXLabel(p=self, text='\xb4\xd3\xc3\xe6\xd1\xa1\xd4\xf1\xb7\xe2\xcd\xb7\xc9\xcf\xc4\xb3\xb8\xf6\xc3\xe6\xa3\xac\xcb\xb3\xd0\xf2\xb2\xbb\xbf\xc9\xb5\xdf\xb5\xb9\xa3\xa1\xd2\xbb\xb6\xa8\xb2\xbb\xc4\xdc\xb8\xe3\xbb\xec\xcb\xb3\xd0\xf2\xbb\xf2\xd5\xdf\xd1\xa1\xd4\xf1\xc6\xe4\xcb\xfb\xb9\xb9\xbc\xfe\xa3\xac\xb7\xf1\xd4\xf2\xbc\xc6\xcb\xe3\xbd\xe1\xb9\xfb\xb4\xed\xce\xf3\xa3\xa1\xa3\xa1\xa3\xa1', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        l = FXLabel(p=self, text='\xb6\xa8\xd2\xe5\xb0\xf3\xb6\xa8\xb9\xd8\xcf\xb5:', opts=JUSTIFY_LEFT)
        HFrame_1 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_1, text='\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xbf\xc7\xcc\xe5-\xb0\xfc\xb8\xb2\xb2\xe3\xa3\xba', opts=JUSTIFY_LEFT)
        pickHf = FXHorizontalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xd6\xf7\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Master_cbKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        pickHf = FXHorizontalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb4\xd3\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Slave_cbKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        AFXTextField(p=HFrame_1, ncols=7, labelText='\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xa3\xba', tgt=form.Position_cbKw, sel=0)
        FXCheckButton(p=HFrame_1, text='\xc7\xd0\xbb\xbb\xd6\xf7\xb4\xd3\xc3\xe6', tgt=form.var_cbKw, sel=0)
        HFrame_3 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_3, text='\xb0\xfc\xb8\xb2\xb2\xe3-\xb7\xe2\xcd\xb7\xa3\xba', opts=JUSTIFY_LEFT)
        pickHf = FXHorizontalFrame(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xd6\xf7\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Master_bfKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        pickHf = FXHorizontalFrame(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb4\xd3\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Slave_bfKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        AFXTextField(p=HFrame_3, ncols=12, labelText='\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xa3\xba', tgt=form.Position_bfKw, sel=0)
        FXCheckButton(p=HFrame_3, text='\xc7\xd0\xbb\xbb\xd6\xf7\xb4\xd3\xc3\xe6', tgt=form.var_bfKw, sel=0)
        HFrame_4 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_4, text='\xb0\xfc\xb8\xb2\xb2\xe3-\xcd\xc6\xbd\xf8\xbc\xc1\xa3\xba', opts=JUSTIFY_LEFT)
        pickHf = FXHorizontalFrame(p=HFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xd6\xf7\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Master_bhKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        pickHf = FXHorizontalFrame(p=HFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb4\xd3\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Slave_bhKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        AFXTextField(p=HFrame_4, ncols=12, labelText='\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xa3\xba', tgt=form.Position_bhKw, sel=0)
        FXCheckButton(p=HFrame_4, text='\xc7\xd0\xbb\xbb\xd6\xf7\xb4\xd3\xc3\xe6', tgt=form.var_bhKw, sel=0)
        HFrame_5 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_5, text='\xcd\xc6\xbd\xf8\xbc\xc1-\xb7\xe2\xcd\xb7\xa3\xba', opts=JUSTIFY_LEFT)
        pickHf = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xd6\xf7\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Master_hfKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        pickHf = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='\xb4\xd3\xc3\xe6' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = _02_platform_tieDBPickHandler(form, form.Slave_hfKw, 'Pick an entity', FACES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        AFXTextField(p=HFrame_5, ncols=12, labelText='\xce\xbb\xd6\xc3\xc8\xdd\xb2\xee\xa3\xba', tgt=form.Position_hfKw, sel=0)
        FXCheckButton(p=HFrame_5, text='\xc7\xd0\xbb\xbb\xd6\xf7\xb4\xd3\xc3\xe6', tgt=form.var_hfKw, sel=0)
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
        fileHandler_input = Tie_DBFileHandler(form, 'inputfile', 'txt(*.txt)')
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

class _02_platform_tieDBPickHandler(AFXProcedure):

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

                _02_platform_tieDBPickHandler.count += 1
                self.setModeName('_02_platform_tieDBPickHandler%d' % (_02_platform_tieDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('None', 'Picked') )
                return None


class Tie_DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*.txt'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, Tie_DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
