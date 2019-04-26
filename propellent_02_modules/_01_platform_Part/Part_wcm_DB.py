# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session

# 导入复合材料的专属材料属性窗口
from composite.composite_plugin import Composite_plugin
import os

'''
建立是否启用方框方法是：
   ---》定义一个processUpdates(self)函数
   ---》定义self.XX = 你想要控制的控件
   self.input_data = AFXTextField(p=fileTextHf, ncols=12, labelText=
        '\xb6\xc1\xc8\xa1\xce\xc4\xbc\xfe:'
                     , tgt=form.inputfileKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
   ---》当关键词等于XXX时，
   if self.form.var_inputKw.getValue() == True:
    self.input_data.enable()
    否则
    self.input_data.disable()
   ---》当
'''
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class Part_wcm_DB(AFXDataDialog):
    [ID_Mybutton, ID_composite] = [AFXDataDialog.ID_LAST, AFXDataDialog.ID_LAST + 2]          #分配ID


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #
        # 定义弹出窗口的plugin
        self.composite_plugin = Composite_plugin(form.getOwner())


        AFXDataDialog.__init__(self, form,
'\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe-\xc7\xb0\xc6\xda\xd4\xa4\xb4\xa6\xc0\xed',
            self.OK|self.APPLY|self.CANCEL|self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR| DATADIALOG_BAILOUT)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText(b'\xc8\xb7\xb6\xa8')

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')
            
        l = FXLabel(p=self, text='\xb1\xbe\xb2\xe5\xbc\xfe\xd6\xbc\xd4\xda\xcd\xea\xb3\xc9\xb5\xbc\xc8\xeb\xc4\xa3\xd0\xcd\xa1\xa2\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xb8\xb3\xd3\xe8\xd2\xd4\xbc\xb0\xcd\xf8\xb8\xf1\xbb\xae\xb7\xd6\xb9\xa4\xd7\xf7;', opts=JUSTIFY_LEFT)
        l = FXLabel(p=self, text='\xb8\xc3\xd7\xb0\xc5\xe4\xcc\xe5\xd3\xd0\xb6\xe0\xc9\xd9\xb8\xf6\xb9\xb9\xbc\xfe\xa3\xac\xbe\xcd\xb1\xd8\xd0\xeb\xd3\xd0\xb6\xe0\xc9\xd9\xb8\xf6\xce\xc4\xbc\xfe\xa3\xac\xce\xde\xd0\xe8\xc8\xce\xba\xce\xc6\xca\xb7\xd6\xb2\xd9\xd7\xf7\xa1\xa3', opts=JUSTIFY_LEFT)

        # 新增WCM插件后，首先建立一个message 映射
        FXMAPFUNC(self, SEL_COMMAND, self.ID_composite, Part_wcm_DB.onCmdComposite)

        # 定义一个启动的button
        hf = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.composite_wcm = FXButton(p=hf, text='\xca\xe4\xc8\xeb\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4'  # 输入复合材料属性
        , ic=None, tgt=self, sel=self.ID_composite,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)
        # 新增一个检查框，是否使用WCM插件
        # FXCheckButton(p=hf,
        # text='WCM plugin', tgt=form.var_WCMKw, sel=0, opts=CHECKBUTTON_NORMAL,
        #          x=0, y=0, w=0, h=0, pl=DEFAULT_PAD, pr=DEFAULT_PAD, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        FXCheckButton(p=hf,
        text=b'\xca\xb9\xd3\xc3WCM\xb2\xe5\xbc\xfe', tgt=form.var_WCMKw, sel=0)
        # 这里需增加一个复合材料专属控件


        # 2019年2月28日10:23:40 原始版本的插件，
        l = FXLabel(p=self, text='\xd7\xa2\xd2\xe2\xa3\xba\xc7\xeb\xcf\xc8\xd4\xdaUG\xd6\xd0\xd7\xb0\xc5\xe4\xcd\xea\xb1\xcf\xba\xf3\xbd\xf8\xd0\xd0\xcf\xc2\xca\xf6\xb2\xd9\xd7\xf7\xa1\xa3', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )

        # 创建一个table主程序
        TabBook_1 = FXTabBook(p=self, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        # 创建子标签页的属性TabItem_3
        # 插件的层级为，TabBook_1 -》 TabItem_3 -》FXLabel

        # 包覆层
        tabItem = FXTabItem(p=TabBook_1, text='\xb0\xfc\xb8\xb2\xb2\xe3', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_3, text='\xc7\xeb\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe\xa3\xba', opts=JUSTIFY_LEFT)
        HFrame_5 = FXHorizontalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        fileHandler = part_DBFileHandler(form, 'filepath_b', 'ACIS SAT(*.sat*)')
        fileTextHf = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=12, labelText='\xb0\xfc\xb8\xb2\xb2\xe3\xc4\xa3\xd0\xcd\xc2\xb7\xbe\xb6\xa3\xa8\xbd\xf6\xd6\xa7\xb3\xd6SAT\xb8\xf1\xca\xbd\xce\xc4\xbc\xfe\xa3\xa9:', tgt=form.filepath_bKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        if isinstance(TabItem_3, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_3, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_3, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_3, text='\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xb8\xb3\xd3\xe8', opts=JUSTIFY_LEFT)
        HFrame_6 = FXHorizontalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.db = AFXTextField(p=HFrame_6, ncols=12, labelText='\xc3\xdc\xb6\xc8:', tgt=form.desity_bKw, sel=0)
        self.eb = AFXTextField(p=HFrame_6, ncols=11, labelText='\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf:', tgt=form.Elastic_bKw, sel=0)
        self.pb = AFXTextField(p=HFrame_6, ncols=12, labelText='\xb2\xb4\xcb\xc9\xb1\xc8:', tgt=form.Poisson_bKw, sel=0)
        HFrame_7 = FXHorizontalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.cb = AFXTextField(p=HFrame_7, ncols=12, labelText='\xc8\xc8\xb4\xab\xb5\xbc\xc2\xca\xcf\xb5\xca\xfd:', tgt=form.Conductivity_bKw, sel=0)
        self.sb = AFXTextField(p=HFrame_7, ncols=12, labelText='\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd:', tgt=form.SpecificHeat_bKw, sel=0)
        self.exb = AFXTextField(p=HFrame_7, ncols=12, labelText='\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd:', tgt=form.Expansion_bKw, sel=0)
        if isinstance(TabItem_3, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_3, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_3, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_3, text='\xcd\xf8\xb8\xf1\xbb\xae\xb7\xd6', opts=JUSTIFY_LEFT)
        self.mb = AFXTextField(p=TabItem_3, ncols=12, labelText='\xc8\xab\xbe\xd6\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7:', tgt=form.size_bKw, sel=0)

        # 封头
        tabItem = FXTabItem(p=TabBook_1, text='\xb7\xe2\xcd\xb7', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_4, text='\xc7\xeb\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe\xa3\xba', opts=JUSTIFY_LEFT)
        fileHandler = part_DBFileHandler(form, 'filepath_f', 'ACIS SAT(*.sat*)')
        fileTextHf = FXHorizontalFrame(p=TabItem_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=12, labelText='\xb7\xe2\xcd\xb7\xc4\xa3\xd0\xcd\xc2\xb7\xbe\xb6\xa3\xa8\xbd\xf6\xd6\xa7\xb3\xd6SAT\xb8\xf1\xca\xbd\xce\xc4\xbc\xfe\xa3\xa9:', tgt=form.filepath_fKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        if isinstance(TabItem_4, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_4, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_4, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_4, text='\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xb8\xb3\xd3\xe8', opts=JUSTIFY_LEFT)
        HFrame_8 = FXHorizontalFrame(p=TabItem_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.df =AFXTextField(p=HFrame_8, ncols=12, labelText='\xc3\xdc\xb6\xc8:', tgt=form.desity_fKw, sel=0)
        self.ef =AFXTextField(p=HFrame_8, ncols=10, labelText='\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf:', tgt=form.Elastic_fKw, sel=0)
        self.pf =AFXTextField(p=HFrame_8, ncols=12, labelText='\xb2\xb4\xcb\xc9\xb1\xc8:', tgt=form.Poisson_fKw, sel=0)
        HFrame_9 = FXHorizontalFrame(p=TabItem_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.cf = AFXTextField(p=HFrame_9, ncols=12, labelText='\xc8\xc8\xb4\xab\xb5\xbc\xc2\xca\xcf\xb5\xca\xfd:', tgt=form.Conductivity_fKw, sel=0)
        self.sf = AFXTextField(p=HFrame_9, ncols=12, labelText='\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd:', tgt=form.SpecificHeat_fKw, sel=0)
        self.exf =AFXTextField(p=HFrame_9, ncols=12, labelText='\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd:', tgt=form.Expansion_fKw, sel=0)
        if isinstance(TabItem_4, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_4, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_4, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_4, text='\xcd\xf8\xb8\xf1\xbb\xae\xb7\xd6', opts=JUSTIFY_LEFT)
        self.mf = AFXTextField(p=TabItem_4, ncols=12, labelText='\xc8\xab\xbe\xd6\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7:', tgt=form.size_fKw, sel=0)

        # 推进剂
        tabItem = FXTabItem(p=TabBook_1, text='\xcd\xc6\xbd\xf8\xbc\xc1', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_2, text='\xc7\xeb\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe\xa3\xba', opts=JUSTIFY_LEFT)
        fileHandler = part_DBFileHandler(form, 'filepath_h', 'ACIS SAT(*.sat*)')
        fileTextHf = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=12, labelText='\xcd\xc6\xbd\xf8\xbc\xc1\xc4\xa3\xd0\xcd\xc2\xb7\xbe\xb6\xa3\xa8\xbd\xf6\xd6\xa7\xb3\xd6SAT\xb8\xf1\xca\xbd\xce\xc4\xbc\xfe\xa3\xa9:', tgt=form.filepath_hKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        if isinstance(TabItem_2, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_2, text='\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xb8\xb3\xd3\xe8', opts=JUSTIFY_LEFT)
        HFrame_10 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.dh =AFXTextField(p=HFrame_10, ncols=12, labelText='\xc3\xdc\xb6\xc8:', tgt=form.desity_hKw, sel=0)
        self.eh =AFXTextField(p=HFrame_10, ncols=10, labelText='\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf:', tgt=form.Elastic_hKw, sel=0)
        self.ph =AFXTextField(p=HFrame_10, ncols=12, labelText='\xb2\xb4\xcb\xc9\xb1\xc8:', tgt=form.Poisson_hKw, sel=0)
        l = FXLabel(p=HFrame_10, text=
        '\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf'
                    , opts=JUSTIFY_LEFT)
        
        vf1 = FXVerticalFrame(HFrame_10, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        vf1.setSelector(99)


        # self.eh =AFXTextField(p=HFrame_10, ncols=12, labelText='\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf:', tgt=form.Elastic_hKw, sel=0)
        # self.ph =AFXTextField(p=HFrame_10, ncols=12, labelText='\xb2\xb4\xcb\xc9\xb1\xc8:', tgt=form.Poisson_hKw, sel=0)
        HFrame_11 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.ch = AFXTextField(p=HFrame_11, ncols=12, labelText='\xc8\xc8\xb4\xab\xb5\xbc\xc2\xca\xcf\xb5\xca\xfd:', tgt=form.Conductivity_hKw, sel=0)
        self.sh = AFXTextField(p=HFrame_11, ncols=12, labelText='\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd:', tgt=form.SpecificHeat_hKw, sel=0)
        self.exh = AFXTextField(p=HFrame_11, ncols=12, labelText='\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd:', tgt=form.Expansion_hKw, sel=0)
        if isinstance(TabItem_2, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_2, text='\xcd\xf8\xb8\xf1\xbb\xae\xb7\xd6', opts=JUSTIFY_LEFT)
        self.mh = AFXTextField(p=TabItem_2, ncols=12, labelText='\xc8\xab\xbe\xd6\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7:', tgt=form.size_hKw, sel=0)

        # 推进剂外壳
        tabItem = FXTabItem(p=TabBook_1, text='\xcd\xe2\xbf\xc7', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # l = FXLabel(p=TabItem_2, text='shell text', opts=JUSTIFY_LEFT)
        l = FXLabel(p=TabItem_2, text='\xc7\xeb\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe\xa3\xba', opts=JUSTIFY_LEFT)
        fileHandler = part_DBFileHandler(form, 'filepath_c', 'ACIS SAT(*.sat*)')
        fileTextHf = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
                                       pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=12,
                     labelText='\xcd\xc6\xbd\xf8\xbc\xc1\xc4\xa3\xd0\xcd\xc2\xb7\xbe\xb6\xa3\xa8\xbd\xf6\xd6\xa7\xb3\xd6SAT\xb8\xf1\xca\xbd\xce\xc4\xbc\xfe\xa3\xa9:',
                     tgt=form.filepath_cKw, sel=0,
                     opts=AFXTEXTFIELD_STRING | LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL)
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
                 opts=BUTTON_NORMAL | LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        if isinstance(TabItem_2, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_2, text='\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xb8\xb3\xd3\xe8', opts=JUSTIFY_LEFT)
        HFrame_10 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
                                      pl=0, pr=0, pt=0, pb=0)
        self.dc = AFXTextField(p=HFrame_10, ncols=12, labelText='\xc3\xdc\xb6\xc8:', tgt=form.desity_cKw, sel=0)
        self.ec = AFXTextField(p=HFrame_10, ncols=12, labelText='\xb5\xaf\xd0\xd4\xc4\xa3\xc1\xbf:',
                               tgt=form.Elastic_cKw, sel=0)
        self.pc = AFXTextField(p=HFrame_10, ncols=12, labelText='\xb2\xb4\xcb\xc9\xb1\xc8:', tgt=form.Poisson_cKw,
                               sel=0)
        HFrame_11 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
                                      pl=0, pr=0, pt=0, pb=0)
        self.cc = AFXTextField(p=HFrame_11, ncols=12, labelText='\xc8\xc8\xb4\xab\xb5\xbc\xc2\xca\xcf\xb5\xca\xfd:',
                               tgt=form.Conductivity_cKw, sel=0)
        self.sc = AFXTextField(p=HFrame_11, ncols=12, labelText='\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd:',
                               tgt=form.SpecificHeat_cKw, sel=0)
        self.exc = AFXTextField(p=HFrame_11, ncols=12, labelText='\xc8\xc8\xc5\xf2\xd5\xcd\xcf\xb5\xca\xfd:',
                                tgt=form.Expansion_cKw, sel=0)
        if isinstance(TabItem_2, FXHorizontalFrame):
            FXVerticalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=TabItem_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=TabItem_2, text='\xcd\xf8\xb8\xf1\xbb\xae\xb7\xd6', opts=JUSTIFY_LEFT)
        self.mc = AFXTextField(p=TabItem_2, ncols=12, labelText='\xc8\xab\xbe\xd6\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7:',
                               tgt=form.size_cKw, sel=0)

        # table 分页完毕
        l = FXLabel(p=self, text=
        '\xb1\xd8\xd0\xeb\xbd\xab4\xb8\xf6\xb9\xb9\xbc\xfe\xb5\xc4\xc2\xb7\xbe\xb6\xa3\xac\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4\xa3\xac\xcd\xf8\xb8\xf1\xb3\xdf\xb4\xe7\xa3\xac\xcb\xf9\xd3\xd0\xca\xf4\xd0\xd4\xca\xe4\xc8\xeb\xcd\xea\xb1\xcf\xb2\xc5\xbf\xc9\xd2\xd4\xb5\xe3\xbb\xf7\xc8\xb7\xb6\xa8\xbb\xf2\xd5\xdf\xd3\xa6\xd3\xc3'
                    , opts=JUSTIFY_LEFT)

        # 2019年1月25日10:11:42 应主任要求，建立两个控件，读取数据和导出数据
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
        fileHandler_input = part_DBFileHandler(form, 'inputfile', 'txt(*.txt)')
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

        # 建立读取数据的框
        self.form = form

#         开始定义当开关启用时，读取文件控件高亮，材料参数变灰，关闭开关，文件控件变灰，材料参数高亮
    def processUpdates(self):
        if self.form.var_inputKw.getValue() == True:
            self.input_data.enable()
            self.read_out_data.enable()
            self.db.disable()
            self.eb.disable()
            self.pb.disable()
            self.cb.disable()
            self.sb.disable()
            self.exb.disable()
            self.mb.disable()
            self.df.disable()
            self.ef.disable()
            self.pf.disable()
            self.cf.disable()
            self.sf.disable()
            self.exf.disable()
            self.mf.disable()
            self.dh.disable()
            # self.eh.disable()
            # self.ph.disable()
            self.ch.disable()
            self.sh.disable()
            self.exh.disable()
            self.mh.disable()
            # self.mh.hide()

        else:
            self.input_data.disable()
            self.read_out_data.disable()
            self.db.enable()
            self.eb.enable()
            self.pb.enable()
            self.cb.enable()
            self.sb.enable()
            self.exb.enable()
            self.mb.enable()
            self.df.enable()
            self.ef.enable()
            self.pf.enable()
            self.cf.enable()
            self.sf.enable()
            self.exf.enable()
            self.mf.enable()
            self.dh.enable()
            # self.eh.enable()
            # self.ph.enable()
            self.ch.enable()
            self.sh.enable()
            self.exh.enable()
            self.mh.enable()
            # self.mh.show()

    # def processUpdates(self):
    #     if  self.var_WCM_data.getValue() == True:
    #         self.composite_wcm.enable()
    #     else:
    #         self.composite_wcm.disable()
    # # elif
    # self.
#     自定义执行方法
    def onCmdComposite(self, sender, sel, ptr):
        if SELID(sel) ==self.ID_composite:
            # 激活窗口
            self.composite_plugin.activate()
        return 1





###########################################################################
# Class definition
###########################################################################

class part_DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*.sta'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, part_DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
