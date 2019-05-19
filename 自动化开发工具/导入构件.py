from abaqus import *
from abaqusConstants import *


def input_part(name, filepath):
    # assert os.path.exists(filepath), '{} not exists'.format(filepath)
    print('filepath IS :', filepath)
    acis = mdb.openAcis(filepath, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name=name, geometryFile=acis,
                                               combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    print('   - {} BEEN IMPORTED TO CAE ...'.format(self.name))

