#!/usr/bin/python

import win32com.client
import sldworks, swcommands, swconst
from random import random

def get_equation_values(model, names):
    # model is an instance of sldworks.IModelDoc2 (like from ActiveDoc)
    # names is a list of strings containing the names of equation constants
    # returns a dictionary d[names[0]] = numeric value
    eqm = model.GetEquationMgr
    d = dict(zip(names, [None]*len(names)))
    for i in xrange(eqm.GetCount):
        for key in d:
            if eqm.equation(i).startswith('"%s"=' % key): d[key] = eqm.value(i)
    return d

def decorate(n=5):
    # connect to SolidWorks and set up objects
    swApp = sldworks.SldWorks()
    swApp.Visible = True
    model = swApp.ActiveDoc
    part = sldworks.PartDoc(model)
    selmgr = model.SelectionManager
    skmgr = model.SketchManager
    featmgr = model.FeatureManager

    # read the part geometry from the equations defined in the document
    geometry = get_equation_values(model, ['beam_length', 'beam_width', 'beam_height', 'base_extent'])
    for (key,value) in geometry.iteritems(): geometry[key] = value/1000.0 # the API insists on taking values in meters

    # select the face of the beam and create a sketch on it
    beamface = part.GetEntityByName('beamface', swconst.constants.swSelFACES).GetSafeEntity
    seldata = selmgr.CreateSelectData
    beamface.Select4(False, seldata)
    skmgr.InsertSketch(False)

    # add each of the new points and then close the sketch
    newpoints = []
    for i in xrange(n): newpoints.append(skmgr.CreatePoint(geometry['beam_width']*random(), -geometry['beam_length']*random(),0))
    skmgr.InsertSketch(True)

    # convert the sketch point into a reference geometry feature by projecting it onto the face beneath
    refpoints = []
    for newpoint in newpoints:
        beamface.Select4(False, seldata)
        newpoint.Select4(True, seldata)
        refpoints.append(featmgr.InsertReferencePoint(swconst.constants.swRefPointFaceVertexProjection, 0, 0, 1))
    
    return refpoints

def main():
    return decorate()

if __name__ == '__main__': print main()

