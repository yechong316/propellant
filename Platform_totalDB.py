# -*- coding: utf-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os, sys



thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

print(os.path.abspath(os.path.join(os.getcwd(), ".")))

# 导入5个启动插件的包，注意是plugin文件
from propellent_02_modules._01_platform_Part.Part_wcm_plugin import Part_wcm_plugin
from propellent_02_modules._02_platform_tie._02_platform_tie_plugin import _02_platform_tie_plugin
from propellent_02_modules._03_platform_thermal._03_platform_thermal_plugin import _03_platform_thermal_plugin
from propellent_02_modules._04_platform_curing._04_platform_curing_plugin import _04_platform_curing_plugin
from propellent_02_modules._05_platform_warp._05_platform_warp_plugin import _05_platform_warp_plugin

###########################################################################
# Class definition
###########################################################################

class Platform_totalDB(AFXDataDialog):

    [ID_1, ID_2, ID_3, ID_4, ID_5] = range(AFXDataDialog.ID_LAST, AFXDataDialog.ID_LAST + 5)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #写入5个插件的plugin文件
        self.Part_wcm_plugin              = Part_wcm_plugin(form.getOwner())
        self._02_platform_tie_plugin      = _02_platform_tie_plugin(form.getOwner())
        self._03_platform_thermal_plugin  = _03_platform_thermal_plugin(form.getOwner())
        self._04_platform_curing_plugin   = _04_platform_curing_plugin(form.getOwner())
        self._05_platform_warp_plugin     = _05_platform_warp_plugin(form.getOwner())


        AFXDataDialog.__init__(self, form, '\xb9\xcc\xcc\xe5\xb7\xa2\xb6\xaf\xbb\xfa\xb1\xbe\xd6\xca\xcc\xd8\xd0\xd4\xb7\xd6\xce\xf6\xc8\xed\xbc\xfe',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('\xc8\xb7\xb6\xa8')
            
        HFrame_1 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)

        #第一步
        GroupBox_1 = FXGroupBox(p=HFrame_1, text='\xb5\xda\xd2\xbb\xb2\xbd:', opts=FRAME_GROOVE)
        #l = FXLabel(p=GroupBox_1, text='\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe', opts=JUSTIFY_LEFT)

        #第二步
        GroupBox_2 = FXGroupBox(p=HFrame_1, text='\xb5\xda\xb6\xfe\xb2\xbd:', opts=FRAME_GROOVE)
        #l = FXLabel(p=GroupBox_1, text='\xb5\xbc\xc8\xeb\xb9\xb9\xbc\xfe', opts=JUSTIFY_LEFT)

        #第三步
        GroupBox_3 = FXGroupBox(p=HFrame_1,text=b'\xb5\xda\xc8\xfd\xb2\xbd:', opts=FRAME_GROOVE)
        #l = FXLabel(p=GroupBox_3, text='loadcase', opts=JUSTIFY_LEFT)

        #定义选择，供用户选择工艺类型，下面3个依次为温度冲击，固化工艺，缠绕工艺
        #self.FXCheckButton1 = FXCheckButton(p=GroupBox_3, text='\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7', tgt=form.keyword01Kw, sel=0)
        #self.FXCheckButton2 = FXCheckButton(p=GroupBox_3, text='\xb9\xcc\xbb\xaf\xb9\xa4\xd2\xd5', tgt=form.keyword02Kw, sel=0)
        #self.FXCheckButton3 = FXCheckButton(p=GroupBox_3, text='\xb2\xf8\xc8\xc6\xb9\xa4\xd2\xd5', tgt=form.keyword03Kw, sel=0)



        # 新增WCM插件后，首先建立一个message 映射---插件1
        FXMAPFUNC(self, SEL_COMMAND, self.ID_1, Platform_totalDB.onCmdID_1)
        # 定义一个启动的button---插件1
        FXButton(p=GroupBox_1, text='\xc7\xb0\xc6\xda\xd4\xa4\xb4\xa6\xc0\xed'  # 输入导入构件
        , ic=None, tgt=self, sel=self.ID_1,opts=BUTTON_NORMAL, x=0, y=0, w=5, h=1, pl=0)
        
        # 新增WCM插件后，首先建立一个message 映射---插件2
        FXMAPFUNC(self, SEL_COMMAND, self.ID_2, Platform_totalDB.onCmdID_2)
        # 定义一个启动的button---插件2

        FXButton(p=GroupBox_2, text='\xb0\xf3\xb6\xa8\xb9\xd8\xcf\xb5'  # 输入绑定关系
        , ic=None, tgt=self, sel=self.ID_2,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)
       
       #初始化buttton 
        # FXButton(p=GroupBox_3, text='initial'  # 初始化buttton
        # , ic=None, tgt=self, sel=self.ID_2,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)  
        # 新增WCM插件后，首先建立一个message 映射---插件3
        m = FXMatrix(GroupBox_3, 1)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_3, Platform_totalDB.onCmdID_3)
        # 定义一个启动的button---插件3
        self.FXButton1 = FXButton(p=m, text='\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7'  # 输入温度冲击
        , ic=None, tgt=self, sel=self.ID_3,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)

        # 新增WCM插件后，首先建立一个message 映射---插件4
        FXMAPFUNC(self, SEL_COMMAND, self.ID_4, Platform_totalDB.onCmdID_4)
        # 定义一个启动的button---ID_4
        self.FXButton2 = FXButton(p=m, text='\xb9\xcc\xbb\xaf\xb9\xa4\xd2\xd5'  # 输入固化工艺
        , ic=None, tgt=self, sel=self.ID_4,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)
        
        # 新增WCM插件后，首先建立一个message 映射---插件5
        FXMAPFUNC(self, SEL_COMMAND, self.ID_5, Platform_totalDB.onCmdID_5)
        # 定义一个启动的button---ID_5
        self.FXButton3 = FXButton(p=m, text='\xb2\xf8\xc8\xc6\xb9\xa4\xd2\xd5'  # 输入缠绕工艺
        , ic=None, tgt=self, sel=self.ID_5,opts=BUTTON_NORMAL, x=0, y=0, w=0, h=0, pl=0)

        self.form = form
  
  # 定义插件的状态
    #def processUpdates(self):
        # if self.form.keyword01Kw.getValue() == True and self.form.keyword02Kw.getValue() == False and self.form.keyword03Kw.getValue() == False:
        # #if '\xce\xc2\xb6\xc8\xb3\xe5\xbb\xf7' == True:
        #     self.FXButton1.setButtonStyle(BUTTON_NORMAL)
        #     self.FXButton2.setButtonStyle(BUTTON_AUTOGRAY)
        #     self.FXButton3.setButtonStyle(BUTTON_AUTOGRAY)
        #     #self.FXCheckButton1.enable()
        #     #self.FXCheckButton2.disable()
        #     # self.FXCheckButton3.disable()

        # elif self.form.keyword01Kw.getValue() == False and self.form.keyword02Kw.getValue() == True and self.form.keyword03Kw.getValue() == False:
        #     self.FXButton2.setButtonStyle(BUTTON_NORMAL)
        #     self.FXButton1.setButtonStyle(BUTTON_AUTOGRAY)
        #     self.FXButton3.setButtonStyle(BUTTON_AUTOGRAY)
        #     self.FXCheckButton2.enable()
        #     self.FXCheckButton1.disable()
        #     self.FXCheckButton3.disable()
        # elif self.form.keyword01Kw.getValue() == False and self.form.keyword02Kw.getValue() == False and self.form.keyword03Kw.getValue() == True:
        #     self.FXButton3.setButtonStyle(BUTTON_NORMAL)
        #     self.FXButton1.setButtonStyle(BUTTON_AUTOGRAY)
        #     self.FXButton2.setButtonStyle(BUTTON_AUTOGRAY)
        #     self.FXCheckButton3.enable()
        #     self.FXCheckButton2.disable()
        #     self.FXCheckButton1.disable()
        # else:
        #     self.FXButton3.setButtonStyle(BUTTON_NORMAL)
        #     self.FXButton1.setButtonStyle(BUTTON_NORMAL)
        #     self.FXButton2.setButtonStyle(BUTTON_NORMAL)
        #     self.FXCheckButton3.enable()
        #     self.FXCheckButton2.enable()
        #     self.FXCheckButton1.enable()
#定义插件 1 的启动方法
    def onCmdID_1(self, sender, sel, ptr):
        if SELID(sel) == self.ID_1:
            # 激活窗口
            self.Part_wcm_plugin.activate()
        return 1


    #定义插件 2 的启动方法
    def onCmdID_2(self, sender, sel, ptr):
        if SELID(sel) == self.ID_2:
            # 激活窗口
            self._02_platform_tie_plugin.activate()
        return 1

    #定义插件 3 的启动方法
    def onCmdID_3(self, sender, sel, ptr):
        if SELID(sel) == self.ID_3:
            # 激活窗口
            self._03_platform_thermal_plugin.activate()
        return 1

    #定义插件 4 的启动方法
    def onCmdID_4(self, sender, sel, ptr):
        if SELID(sel) == self.ID_4:
            # 激活窗口
            self._04_platform_curing_plugin.activate()
        return 1

    #定义插件 5 的启动方法
    def onCmdID_5(self, sender, sel, ptr):
        if SELID(sel) == self.ID_5:
            # 激活窗口
            self._05_platform_warp_plugin.activate()
        return 1