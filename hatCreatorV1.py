import maya.cmds as cmds
import random


"""
A script to 
cmds documentation: http://help.autodesk.com/cloudhelp/2018/CHS/Maya-Tech-Docs/CommandsPython/

Lines to put in the python section of the script editor:
import hatCreator
reload(hatCreator)
hatCreator.createHat()


"""

def createHat(cone_colour=None, pompom_colour=None):
    # Create the cone and pompom
    cone_obj, cone_node = cmds.polyCone()
    pompom_obj, pompom_node = cmds.polySphere(r=0.25)
    #move the pompom to the right spot on the hat cone while it's still selected
    cmds.move(0, 1.06, 0)

    change_colour(cone_obj, 'blinn', cone_colour)
    change_colour(pompom_obj, 'lambert', pompom_colour)
    # merge them into one shape (polyUnite)
    cmds.polyUnite(cone_obj, pompom_obj, n='hat')



def change_colour(object, material, colour):
    # use lambert as the default for the pompom s it looks a bit different from the cone
    cmds.sets(name=material+'MaterialGroup', renderable=True, empty=True)
    cmds.shadingNode(material, name=material+'Shader', asShader=True)

    if not colour:
        # randomly generate a colour   0 to 1 on each axis   r g b
        red = random.random()
        green = random.random()
        blue = random.random()
        cmds.setAttr(material+'Shader.color', red, green, blue, type='double3')

    else:
        # we should add some error catching here
        red = colour[0]
        green = colour[1]
        blue = colour[2]
        cmds.setAttr(material+'Shader.color', red, green, blue, type='double3')

    cmds.surfaceShaderList(material+'Shader', add=material+'MaterialGroup')
    cmds.sets(object, e=True, forceElement=material+'MaterialGroup')

