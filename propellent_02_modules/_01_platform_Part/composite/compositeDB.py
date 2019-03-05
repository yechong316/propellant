# -*- coding: utf-8 -*-
#!/usr/bin/python3
# propellant_v0125-1100 
# Authorn:Jaime Lannister
# Time:2019/2/28-11:56 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

class CompositeDB(AFXDataDialog):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):
        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xb2\xc4\xc1\xcf\xca\xf4\xd0\xd4',
         self.OK | self.APPLY|self.CANCEL|self.DEFAULTS, DIALOG_ACTIONS_SEPARATOR| DATADIALOG_BAILOUT)

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText(b'\xc8\xb7\xb6\xa8')



        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('\xd3\xa6\xd3\xc3')

        DEFAULTSBtn = self.getActionButton(self.ID_CLICKED_DEFAULTS)
        DEFAULTSBtn.setText(b'\xc4\xac\xc8\xcf')


        GroupBox_1 = FXGroupBox(p=self, text='\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf', opts=FRAME_GROOVE)
        HFrame_1 = FXHorizontalFrame(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
                                     pl=0, pr=0, pt=0, pb=0)

        # 材料名称
        AFXTextField(p=HFrame_1, ncols=12, labelText='\xb2\xc4\xc1\xcf\xc3\xfb\xb3\xc6:', tgt=form.nameKw, sel=0)
        vf = FXVerticalFrame(GroupBox_1, FRAME_SUNKEN | FRAME_THICK | LAYOUT_FILL_X,
                             0, 0, 0, 0, 0, 0, 0, 0)
        vf.setSelector(99)

        HFrame_11 = FXHorizontalFrame(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
                                      pl=0, pr=0, pt=0, pb=0)

        # 密度
        AFXTextField(p=HFrame_11, ncols=12, labelText='\xc3\xdc\xb6\xc8:', tgt=form.desityKw, sel=0)

        # 比热容
        AFXTextField(p=HFrame_11, ncols=12, labelText='\xb1\xc8\xc8\xc8\xc8\xdd\xcf\xb5\xca\xfd:', tgt=form.specificKw,
                     sel=0)

        # 弹性模量
        l = FXLabel(p=GroupBox_1, text='\xb5\xaf\xd0\xd4:', opts=JUSTIFY_LEFT)

        vf = FXVerticalFrame(GroupBox_1, FRAME_SUNKEN | FRAME_THICK | LAYOUT_FILL_X,
                             0, 0, 0, 0, 0, 0, 0, 0)
        vf.setSelector(99)
        table_e = AFXTable(vf, 2, 10, 2, 10, form.elasticKw, 0, AFXTABLE_EDITABLE | LAYOUT_FILL_X)
        table_e.setLeadingRows(1)
        table_e.setLeadingColumns(1)
        table_e.setColumnWidth(1, 100)
        table_e.setColumnType(1, AFXTable.FLOAT)
        table_e.setColumnWidth(2, 100)
        table_e.setColumnType(2, AFXTable.FLOAT)
        table_e.setColumnWidth(3, 100)
        table_e.setColumnType(3, AFXTable.FLOAT)
        table_e.setColumnWidth(4, 100)
        table_e.setColumnType(4, AFXTable.FLOAT)
        table_e.setColumnWidth(5, 100)
        table_e.setColumnType(5, AFXTable.FLOAT)
        table_e.setColumnWidth(6, 100)
        table_e.setColumnType(6, AFXTable.FLOAT)
        table_e.setColumnWidth(7, 100)
        table_e.setColumnType(7, AFXTable.FLOAT)
        table_e.setColumnWidth(8, 100)
        table_e.setColumnType(8, AFXTable.FLOAT)
        table_e.setColumnWidth(9, 100)
        table_e.setColumnType(9, AFXTable.FLOAT)
        table_e.setLeadingRowLabels('E1\tE2\tE3\tNu12\tNu13\tN23\tG12\tG13\tG23')
        table_e.setStretchableColumn(table_e.getNumColumns() - 1)
        table_e.showHorizontalGrid(True)
        table_e.showVerticalGrid(True)
        table_e.setItemFloatValue(1, 1, 21500000)
        table_e.setItemFloatValue(1, 2, 227000)
        table_e.setItemFloatValue(1, 3, 227000)
        table_e.setItemFloatValue(1, 4, 0.28)
        table_e.setItemFloatValue(1, 5, 0.28)
        table_e.setItemFloatValue(1, 6, 0.305)
        table_e.setItemFloatValue(1, 7, 212000)
        table_e.setItemFloatValue(1, 8, 212000)
        table_e.setItemFloatValue(1, 9, 86973)
        table_e.setPopupOptions(
        AFXTable.POPUP_CUT | AFXTable.POPUP_COPY | AFXTable.POPUP_PASTE | AFXTable.POPUP_INSERT_ROW | AFXTable.POPUP_DELETE_ROW | AFXTable.POPUP_CLEAR_CONTENTS | AFXTable.POPUP_READ_FROM_FILE | AFXTable.POPUP_WRITE_TO_FILE)

        # 热传导
        l = FXLabel(p=GroupBox_1, text='\xc8\xc8\xb4\xab\xb5\xbc:', opts=JUSTIFY_LEFT)
        vf = FXVerticalFrame(GroupBox_1, FRAME_SUNKEN | FRAME_THICK | LAYOUT_FILL_X,
                             0, 0, 0, 0, 0, 0, 0, 0)
        vf.setSelector(99)
        table_c = AFXTable(vf, 2, 4, 2, 4, form.conductivityKw, 0, AFXTABLE_EDITABLE | LAYOUT_FILL_X)
        table_c.setLeadingRows(1)
        table_c.setLeadingColumns(1)
        table_c.setColumnWidth(1, 100)
        table_c.setColumnType(1, AFXTable.FLOAT)
        table_c.setColumnWidth(2, 100)
        table_c.setColumnType(2, AFXTable.FLOAT)
        table_c.setLeadingRowLabels('k11\tk22\tk33')
        table_c.setStretchableColumn(table_c.getNumColumns() - 1)
        table_c.showHorizontalGrid(True)
        table_c.showVerticalGrid(True)
        table_c.setItemFloatValue(1, 1, 0.0001)
        table_c.setItemFloatValue(1, 2, 0.0005)
        table_c.setItemFloatValue(1, 3, 0.0005)
        table_c.setPopupOptions(
            AFXTable.POPUP_CUT | AFXTable.POPUP_COPY | AFXTable.POPUP_PASTE | AFXTable.POPUP_INSERT_ROW | AFXTable.POPUP_DELETE_ROW | AFXTable.POPUP_CLEAR_CONTENTS | AFXTable.POPUP_READ_FROM_FILE | AFXTable.POPUP_WRITE_TO_FILE)

        # 热膨胀
        l = FXLabel(p=GroupBox_1, text='\xc8\xc8\xc5\xf2\xd5\xcd:', opts=JUSTIFY_LEFT)
        vf = FXVerticalFrame(GroupBox_1, FRAME_SUNKEN | FRAME_THICK | LAYOUT_FILL_X,
                             0, 0, 0, 0, 0, 0, 0, 0)
        vf.setSelector(99)
        table_ex = AFXTable(vf, 2, 4, 2, 4, form.expansionKw, 0, AFXTABLE_EDITABLE | LAYOUT_FILL_X)
        table_ex.setLeadingRows(1)
        table_ex.setLeadingColumns(1)
        table_ex.setColumnWidth(1, 100)
        table_ex.setColumnType(1, AFXTable.FLOAT)
        table_ex.setColumnWidth(2, 100)
        table_ex.setColumnType(2, AFXTable.FLOAT)
        table_ex.setLeadingRowLabels('alpha11\talpha22\talpha33')
        table_ex.setStretchableColumn(table_ex.getNumColumns() - 1)
        table_ex.showHorizontalGrid(True)
        table_ex.showVerticalGrid(True)
        table_ex.setItemFloatValue(1, 1, 1.4E-007)
        table_ex.setItemFloatValue(1, 2, 1.35E-005)
        table_ex.setItemFloatValue(1, 3, 1.35E-005)
        table_ex.setPopupOptions(
        AFXTable.POPUP_CUT | AFXTable.POPUP_COPY | AFXTable.POPUP_PASTE | AFXTable.POPUP_INSERT_ROW | AFXTable.POPUP_DELETE_ROW | AFXTable.POPUP_CLEAR_CONTENTS | AFXTable.POPUP_READ_FROM_FILE | AFXTable.POPUP_WRITE_TO_FILE)

