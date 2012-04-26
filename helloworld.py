#!/usr/bin/python

import win32com.client
import pythoncom
import sldworks, swcommands, swconst, cosworks
from random import random
from math import sin, cos, sqrt, pi

class Cell:
    RADIUS = 0.025
    def __init__(self, com=None, angle=None, sketchpoints=None, featurepoints=None, spring=None):
        self.com = com
        self.angle = angle
        self.sketchpoints = sketchpoints or []
        self.featurepoints = featurepoints or []
        self.spring = spring
    def get_point_locations(self):
        return [(self.com[0]+Cell.RADIUS*cos(self.angle), self.com[1]+Cell.RADIUS*sin(self.angle)),
                (self.com[0]+Cell.RADIUS*cos(pi+self.angle), self.com[1]+Cell.RADIUS*sin(pi+self.angle))]
    def __repr__(self):
        return 'Cell(%s, %s, %s, %s)' % tuple([repr(i) for i in [self.com, self.angle, self.sketchpoints, self.featurepoints]])

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

def decorate(swApp, n=5):
    # connect to SolidWorks and set up objects
    model = swApp.ActiveDoc
    part = sldworks.PartDoc(model)
    selmgr = model.SelectionManager
    skmgr = model.SketchManager
    featmgr = model.FeatureManager

    # read the part geometry from the equations defined in the document
    geometry = get_equation_values(model, ['beam_length', 'beam_width', 'beam_height', 'base_extent'])
    for (key,value) in geometry.iteritems(): geometry[key] = value

    # figure where to put cells
    cells = []
    for i in xrange(n):
        success = False
        while not success:
            # choose a center of mass
            newcom = ((geometry['beam_width']-2*Cell.RADIUS)*random()+Cell.RADIUS,
                       (geometry['beam_length']-2*Cell.RADIUS)*random()+Cell.RADIUS)
            success = True
            for othercell in cells:
                distance = lambda p1, p2: sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
                if distance(newcom, othercell.com) <= 2*Cell.RADIUS: success = False
        cells.append(Cell(newcom, random()*pi))

    # select the face of the beam and create a sketch on it
    beamface = part.GetEntityByName('beamface', swconst.constants.swSelFACES).GetSafeEntity
    seldata = selmgr.CreateSelectData
    beamface.Select4(False, seldata)
    skmgr.InsertSketch(False)
    
    # add each of the new points and then close the sketch
    for cell in cells:
        for point in cell.get_point_locations():
            x, y = point
            cell.sketchpoints.append(skmgr.CreatePoint(x/1000., -y/1000., 0)) # convert to meters

    skmgr.InsertSketch(True)

    # convert the sketch point into a reference geometry feature by projecting it onto the face beneath
    refpoints = []
    for cell in cells:
        for sketchpoint in cell.sketchpoints:
            beamface.Select4(False, seldata)
            sketchpoint.Select4(True, seldata)
            cell.featurepoints.append(featmgr.InsertReferencePoint(swconst.constants.swRefPointFaceVertexProjection, 0, 0, 1))
        
    return cells

def springify(cw, cells):
    cwdoc = cw.ActiveDoc
    studymgr = cwdoc.StudyManager
    study = None
    for i in xrange(studymgr.StudyCount):
        temp = studymgr.GetStudy(i)
        if temp.Name.startswith('One-spring'):
            study = temp
            break
    # force using the makepy script to handle the weird reference
    lrm = cosworks.ICWLoadsAndRestraintsManager(study.LoadsAndRestraintsManager)
    springtype = cosworks.constants.swsSpringConnectoryTypeBetweenVertices
    for cell in cells:
        errorcode = 0
        p1, p2 = cell.featurepoints
        cell.spring = lrm.AddSpringConnector(springtype, [p1], [p2], errorcode)
        print type(cell.spring)
        print type(cell.spring.SpringConnectorBeginEdit)
        print type(cell.spring._oleobj_), cell.spring._oleobj_
        print type(lrm._oleobj_), lrm._oleobj_
        cell.spring.SpringConnectorBeginEdit()
        cell.spring.PreLoadForceType = cosworks.constants.swsPreLoadForceTypeCompression
        cell.spring.PreLoadForceValue = 1e-6
        cell.spring.NormalRadialStiffnessValue = 10
        cell.spring.SpringConnectorEndEdit
        
    return cells

def main():
    swApp = sldworks.SldWorks()
    swApp.Visible = True
    cw = swApp.GetAddInObject("SldWorks.Simulation").COSMOSWORKS
    
    cells = decorate(swApp)
    springify(cw, cells)
    return cells

if __name__ == '__main__': print main()

