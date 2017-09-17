#***************************************************************************
#*                                                                         *
#*  This file is part of the Open Source Ecology D3D 3D Printer Workbench  *
#*  for FreeCAD.                                                           *
#*                                                                         *
#*  Copyright (C) 2017                                                     *
#*  Open Source Ecology <info|at|opensourceecology.org>                    *
#*                                                                         *
#*  This library is free software; you can redistribute it and/or          *
#*  modify it under the terms of the GNU Lesser General Public             *
#*  License as published by the Free Software Foundation; either           *
#*  version 2 of the License, or (at your option) any later version.       *
#*                                                                         *            
#*  This library is distributed in the hope that it will be useful,        *
#*  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU      *
#*  Lesser General Public License for more details.                        *
#*                                                                         *
#*  You should have received a copy of the GNU Lesser General Public       *
#*  License along with this library; if not, If not, see                   *
#*  <http://www.gnu.org/licenses/>.                                        *
#*                                                                         *
#*                                                                         *
#***************************************************************************


import FreeCAD, Part, D3DInit
from FreeCAD import Gui

class D3D_AddFrameClass():
    """Command to add the printer frame"""

    def GetResources(self):
        return {'Pixmap'  : D3DInit.ICON_PATH + '/DrawStyleWireFrame.svg', # the name of a svg file available in the resources
                'Accel' : "Shift+S", # a default shortcut (optional)
                'MenuText': "Add a frame",
                'ToolTip' : "Adds a D3D printer frame"}

    def Activated(self):
        "Do something here"
        # See here for opening dialog to choose part to import 
        # https://github.com/hamish2014/FreeCAD_assembly2/blob/master/importPart.py#L125
        FreeCAD.Console.PrintMessage("D3D Printer workbench is working!")
        if Gui.ActiveDocument == None:
            FreeCAD.newDocument()
#        view = Gui.activeDocument().activeView()
        doc=FreeCAD.activeDocument()
        n=list()
        c = Part.Circle() 
        c.Radius=2.0
        f = doc.addObject("Part::Feature", "Circle") # create a document with a circle feature
        f.Shape = c.toShape() # Assign the circle shape to the shape property
        doc.recompute()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

Gui.addCommand('D3D_AddFrame', D3D_AddFrameClass()) 
