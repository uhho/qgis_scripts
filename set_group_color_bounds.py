from qgis.core import *

def set_color_bounds(group_name, red_min_max, green_min_max, blue_min_max):
    root = QgsProject.instance().layerTreeRoot()
    mygroup = root.findGroup(group_name)

    for child in mygroup.children():
        layer = child.layer()
        
        myRedBand = layer.renderer().redBand()
        myRedType = layer.renderer().dataType(myRedBand)
        myRedEnhancement = QgsContrastEnhancement(myRedType)
       
        myGreenBand = layer.renderer().greenBand()
        myGreenType = layer.renderer().dataType(myGreenBand)
        myGreenEnhancement = QgsContrastEnhancement(myGreenType)
        
        myBlueBand = layer.renderer().blueBand()
        myBlueType = layer.renderer().dataType(myBlueBand)
        myBlueEnhancement = QgsContrastEnhancement(myBlueType)
        
        ContrastEnhancement = QgsContrastEnhancement.StretchToMinimumMaximum
        myRedEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement, True)
        myRedEnhancement.setMinimumValue(red_min_max[0])
        myRedEnhancement.setMaximumValue(red_min_max[1])
        layer.renderer().setRedContrastEnhancement(myRedEnhancement)
        
        myGreenEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement, True)
        myGreenEnhancement.setMinimumValue(green_min_max[0])
        myGreenEnhancement.setMaximumValue(green_min_max[1])
        layer.renderer().setGreenContrastEnhancement(myGreenEnhancement)
        
        myBlueEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement, True)
        myBlueEnhancement.setMinimumValue(blue_min_max[0])
        myBlueEnhancement.setMaximumValue(blue_min_max[1])
        layer.renderer().setBlueContrastEnhancement(myBlueEnhancement)
        
        layer.triggerRepaint()


set_color_bounds(group_name='group1',
        red_min_max=[100, 3000], 
        green_min_max=[100, 3000], 
        blue_min_max=[100, 3000])
