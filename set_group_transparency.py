from qgis.core import *

def set_transparency(group_name, transparency):
    root = QgsProject.instance().layerTreeRoot()
    mygroup = root.findGroup(group_name)
    for child in mygroup.children():
        if isinstance(child, QgsLayerTreeLayer):
            layer = child.layer()
            layer.renderer().setOpacity(transparency)
            layer.triggerRepaint()


set_transparency(group_name='group1', transparency=0.5)
