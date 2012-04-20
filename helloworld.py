#!/usr/bin/python

import win32com.client
import sldworks, swcommands, swconst

def helloworld():
    swApp = sldworks.SldWorks()
    swApp.Visible = True
    model = swApp.ActiveDoc2
    skm = model.SketchManager
    eqm = model.EquationManager
    
    