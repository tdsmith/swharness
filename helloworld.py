#!/usr/bin/python

import win32com.client
import sldworks, swcommands, swconst
from random import random
from math import sin, cos, sqrt, pi

class Cell:
    RADIUS = 0.025
    def __init__(self, com=None, angle=None, sketchpoints=None, featurepoints=None):
        self.com = com
        self.angle = angle
        self.sketchpoints = sketchpoints or []
        self.featurepoints = featurepoints or []
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

def main():
    cells = decorate()

if __name__ == '__main__': print main()

