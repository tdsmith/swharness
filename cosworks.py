# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)]
# From type library 'cosworks.tlb'
# On Fri Apr 20 11:32:28 2012
"""SolidWorks Simulation 2011 type library"""
makepy_version = '0.5.00'
python_version = 0x20702f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{502B0223-5406-4829-84BE-1111B8661D5F}')
MajorVersion = 3
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	swsAnalysisStudyTypeBuckling  =2          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeDropTest  =6          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeFatigue   =7          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeFrequency =1          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeNonlinear =5          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeOptimization=4          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeStatic    =0          # from enum swsAnalysisStudyType_e
	swsAnalysisStudyTypeThermal   =3          # from enum swsAnalysisStudyType_e
	swsBeamBodyConnectionManual   =3          # from enum swsBeamBodyConnectionType_e
	swsBeamBodyConnectionPin      =1          # from enum swsBeamBodyConnectionType_e
	swsBeamBodyConnectionRigid    =0          # from enum swsBeamBodyConnectionType_e
	swsBeamBodyConnectionSlide    =2          # from enum swsBeamBodyConnectionType_e
	swsBeamBodyManualConnectionHinge1stDirection=0          # from enum swsBeamBodyManualConnectionType_e
	swsBeamBodyManualConnectionHinge2ndDirection=1          # from enum swsBeamBodyManualConnectionType_e
	swsBeamBodyManualConnectionHingeAlongBeam=2          # from enum swsBeamBodyManualConnectionType_e
	swsBeamBodyManualConnectionSlide1stDireciton=3          # from enum swsBeamBodyManualConnectionType_e
	swsBeamBodyManualConnectionSlide2ndDirection=4          # from enum swsBeamBodyManualConnectionType_e
	swsBeamBodyManualConnectionSlideAlongBeam=5          # from enum swsBeamBodyManualConnectionType_e
	swsBeamForceAxial             =0          # from enum swsBeamForceType_e
	swsBeamForceMomentDirection1  =3          # from enum swsBeamForceType_e
	swsBeamForceMomentDirection2  =4          # from enum swsBeamForceType_e
	swsBeamForceShearDirection1   =1          # from enum swsBeamForceType_e
	swsBeamForceShearDirection2   =2          # from enum swsBeamForceType_e
	swsBeamForceTorque            =5          # from enum swsBeamForceType_e
	swsCentralLoad                =1          # from enum swsBeamNonUniformLoadDef_e
	swsTableDrivenLoad            =2          # from enum swsBeamNonUniformLoadDef_e
	swsTotalLoad                  =0          # from enum swsBeamNonUniformLoadDef_e
	swsEllipticalLoad             =2          # from enum swsBeamNonUniformLoadType_e
	swsParabolicLoad              =1          # from enum swsBeamNonUniformLoadType_e
	swsTriangularLoad             =0          # from enum swsBeamNonUniformLoadType_e
	swsBeamStressComponentAxial   =0          # from enum swsBeamStressComponent_e
	swsBeamStressComponentBendingLocalDir1=1          # from enum swsBeamStressComponent_e
	swsBeamStressComponentBendingLocalDir2=2          # from enum swsBeamStressComponent_e
	swsBeamStressComponentWorstCase=3          # from enum swsBeamStressComponent_e
	swsBeamStressAxial            =0          # from enum swsBeamStressType_e
	swsBeamStressBendingDirection1=1          # from enum swsBeamStressType_e
	swsBeamStressBendingDirection2=2          # from enum swsBeamStressType_e
	swsBeamStressTorsional        =3          # from enum swsBeamStressType_e
	swsBeamStressWorstCase        =4          # from enum swsBeamStressType_e
	swsBeamTypeBeam               =0          # from enum swsBeamType_e
	swsBeamTypeTruss              =1          # from enum swsBeamType_e
	swsBearingLoadEndEditErrorBodyExcludedFromAnalysis=17         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorCoordinateSystemCylindricalFaces=1          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorEntityExists=3          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorHasBeamBody=9          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorHasMassElement=8          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorIncorrectOrNullEntity=2          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorIndexExceedsNumberOfEntities=10         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorNoEntity=11         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorNoEntityAtIndex=5          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorNullEntity=16         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSelectFace=4          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSelectFaceWithCylindricalSurface=7          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSelectForceDirection=13         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSelectOneForceDirection=12         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSetXDirection=14         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSetYDirection=15         # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSpecifyValue=6          # from enum swsBearingLoadEndEditError_e
	swsBearingLoadEndEditErrorSuccessful=0          # from enum swsBearingLoadEndEditError_e
	swsBoltConnectorEndEditErrorBodyExcludedFromAnalysis=40         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorBodyHasBeamElement=42         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorBodyHasMassElement=39         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorBoltDiameterBiggerShankContactFaceDiameter=25         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorDefineMaterial=13         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorDocumentIsPart=30         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorEntityAlreadyExits=27         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorEntitySelectionBoxesEmpty=34         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorIncorrectHeadDiameter=3          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorIncorrectNutDiameter=29         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorIncorrectShankDiameter=7          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorNoEntity=28         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorNoMultiBoltSelected=38         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorNoObjectAtIndex=33         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorNoShearEffectSelected=37         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorNullEntity=41         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectBoltHeadAndNut=17         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectBoltNut=26         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectCircularEdge=5          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectCoaxialCylindricalSurfaces=23         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectConcentricCylindricalFaces=24         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectConcentricEntities=9          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectConicalFaceAndBoltNut=19         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectConicalFaceAndFaceForThread=20         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectConicalSurface=2          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectCylindricalThreadFace=6          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectEdge=4          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectEdgesOnShells=32         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectFace=1          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectFaceForHeadNutFaceForThread=18         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectFacesFromMultilayerBolt=22         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectMass=8          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectNutOrHead=31         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectOneEntity=35         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectPlanarFace=16         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSelectReferencePlane=21         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSpecifyFrictionValue=15         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSpecifyPoissonsRatio=12         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSpecifyPreloadValue=14         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSpecifyTemperatureCoefficient=11         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSpecifyYoungModulus=10         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorSuccessful=0          # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorEndEditErrorTooManyEntities=36         # from enum swsBoltConnectorEndEditError_e
	swsBoltConnectorErrorArrayEmpty=17         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorBodyExcludedFromAnalysis=20         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorBoltDiameterTooLarge=19         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorInvalidMesh=1          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorInvalidStudy=3          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorNoObjectForNutOrHead=15         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorNonLinearStudyAndPartDocument=2          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSameEntityHeadAndNut=13         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectAssemblyDocument=14         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectCircularEdgeOnShells=18         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectConcentricEntities=9          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectCylindricalThreadFace=8          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectDatumPlane=10         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectEdge=11         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectEdgeWithCircularLine=6          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectEntity=4          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectFace=12         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectFaceWithConicalSurface=5          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectFaceWithCylindricalSurface=7          # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSelectNutOrHead=16         # from enum swsBoltConnectorError_e
	swsBoltConnectorErrorSuccessful=0          # from enum swsBoltConnectorError_e
	swsBoltMaterialSourceCustomDefined=1          # from enum swsBoltMaterialSource_e
	swsBoltMaterialSourceLibraryFiles=2          # from enum swsBoltMaterialSource_e
	swsBoltMaterialSourceSolidWorks=0          # from enum swsBoltMaterialSource_e
	swsBoltMaterialTypeCustom     =0          # from enum swsBoltMaterialType_e
	swsBoltMaterialTypeLibrary    =1          # from enum swsBoltMaterialType_e
	swBoltTypeCountersinkWithNut  =1          # from enum swsBoltType_e
	swsBoltTypeCountersinkScrew   =3          # from enum swsBoltType_e
	swsBoltTypeFoundationBolt     =4          # from enum swsBoltType_e
	swsBoltTypeStandardOrCounterboreNut=0          # from enum swsBoltType_e
	swsBoltTypeStandardOrCounterboreScrew=2          # from enum swsBoltType_e
	swsCentrifugalForceEndEditErrorSuccessful=0          # from enum swsCentrifugalForceEndEditError_e
	wsCentrifugalForceEndEditErrorSpecifyAxisEdgeOrCylindricalFace=1          # from enum swsCentrifugalForceEndEditError_e
	swsCentrifugalForceErrorAlreadyDefined=4          # from enum swsCentrifugalForceError_e
	swsCentrifugalForceErrorEdgeNotLinear=3          # from enum swsCentrifugalForceError_e
	swsCentrifugalForceErrorFaceNotCylindrical=2          # from enum swsCentrifugalForceError_e
	swsCentrifugalForceErrorInvalidStudyType=5          # from enum swsCentrifugalForceError_e
	swsCentrifugalForceErrorSelectAxisEdgeOrCylindricalFace=1          # from enum swsCentrifugalForceError_e
	swsCentrifugalForceErrorSuccessful=0          # from enum swsCentrifugalForceError_e
	swsConnectAnalysisDatabaseErrorFailed=1          # from enum swsConnectAnalysisDatabaseError_e
	swsConnectAnalysisDatabaseErrorInvalidPath=2          # from enum swsConnectAnalysisDatabaseError_e
	swsConnectAnalysisDatabaseErrorInvalidResults=3          # from enum swsConnectAnalysisDatabaseError_e
	swsConnectAnalysisDatabaseErrorSuccess=0          # from enum swsConnectAnalysisDatabaseError_e
	swsContactComponentEndEditErrorBodiesNotTouchingBodies=8          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorCannotSpecifyFreeContact=7          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorContactComponentCannotBeCreated=1          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorIncorrectCoefficientOfFriction=4          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorInvalidContactType=2          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorSelectComponentOrBody=3          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorSelectSolidBodyOrComponent=5          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorSuccessful=0          # from enum swsContactComponentEndEditError_e
	swsContactComponentEndEditErrorTooManyBodiesOrComponents=6          # from enum swsContactComponentEndEditError_e
	swsContactSetEndEditErrorBondTouchingFacesInDropTestStudies=15         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorContactSetsMustBeUnique=13         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorEntityAlreadySpecified=2          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorIncorrectCoefficientFriction=10         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorInvalidContactSetType=3          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorInvalidOption=4          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorNoEntityAtIndex=1          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorNodeToNodeContactAndSourceTargetFaces=14         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorOnlyFacesAllowedForTarget=7          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorShrinkFitAndnterferingSourceTargetBodies=16         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorSpecifyFacesEdgesOrVerticesForSource=5          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorSpecifyOneTargetPlaneForVirtualWall=6          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorStiffnessCannotBeNegative=8          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorStiffnessMustBePositive=9          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorSuccessful=0          # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorThermalResistanceMustBePositive=12         # from enum swsContactSetEndEditError_e
	swsContactSetEndEditErrorVerticesAndEdgesForBondingAndSurfaceContacts=11         # from enum swsContactSetEndEditError_e
	swsContactSetErrorBondedContactForTouchingFaces=10         # from enum swsContactSetError_e
	swsContactSetErrorCannotCreateContactPair=12         # from enum swsContactSetError_e
	swsContactSetErrorFaceForSourceAndTarget=7          # from enum swsContactSetError_e
	swsContactSetErrorInvalidArray=1          # from enum swsContactSetError_e
	swsContactSetErrorInvalidType =3          # from enum swsContactSetError_e
	swsContactSetErrorNoEntities  =2          # from enum swsContactSetError_e
	swsContactSetErrorSelectOneTargetPlane=5          # from enum swsContactSetError_e
	swsContactSetErrorSelectOnlyFaces=6          # from enum swsContactSetError_e
	swsContactSetErrorShrinkFitNeedsIntereference=11         # from enum swsContactSetError_e
	swsContactSetErrorSourceTargetFacesMustTouch=9          # from enum swsContactSetError_e
	swsContactSetErrorSpecifyFacesEdgesOrVertices=4          # from enum swsContactSetError_e
	swsContactSetErrorSuccess     =0          # from enum swsContactSetError_e
	swsContactSetErrorVerticesEdgesForBondingSurfaceContacts=8          # from enum swsContactSetError_e
	swsContactSetTypeStaticNonLinearBonded=1          # from enum swsContactSetTypeStaticNonLinear_e
	swsContactSetTypeStaticNonLinearFree=3          # from enum swsContactSetTypeStaticNonLinear_e
	swsContactSetTypeStaticNonLinearNoPrenetration=0          # from enum swsContactSetTypeStaticNonLinear_e
	swsContactSetTypeStaticNonLinearShrinkFit=2          # from enum swsContactSetTypeStaticNonLinear_e
	swsContactSetTypeStaticNonLinearVirtualWall=4          # from enum swsContactSetTypeStaticNonLinear_e
	swsContactSetTypeThermalBonded=1          # from enum swsContactSetTypeThermal_e
	swsContactSetTypeThermalInsulated=2          # from enum swsContactSetTypeThermal_e
	swsContactSetTypeThermalResistance=0          # from enum swsContactSetTypeThermal_e
	swsContactTypeBonded          =0          # from enum swsContactType_e
	swsContactTypeFreeOrInsulated =1          # from enum swsContactType_e
	swsContactTypeStaticNoPenetration=2          # from enum swsContactType_e
	swsConvectionEndEditErrorEntityAlreadyAdded=2          # from enum swsConvectionEndEditError_e
	swsConvectionEndEditErrorNoEntityAtIndex=1          # from enum swsConvectionEndEditError_e
	swsConvectionEndEditErrorNoEntitySelected=3          # from enum swsConvectionEndEditError_e
	swsConvectionEndEditErrorSelectFace=4          # from enum swsConvectionEndEditError_e
	swsConvectionEndEditErrorSelectFaceOrEdge=5          # from enum swsConvectionEndEditError_e
	swsConvectionEndEditErrorSuccessful=0          # from enum swsConvectionEndEditError_e
	swsConvectionErrorEmptyArray  =5          # from enum swsConvectionError_e
	swsConvectionErrorFacesAndShellEdgesAllowed=1          # from enum swsConvectionError_e
	swsConvectionErrorInvalidArray=4          # from enum swsConvectionError_e
	swsConvectionErrorInvalidStudyType=3          # from enum swsConvectionError_e
	swsConvectionErrorSelectFacesOrShellEdge=2          # from enum swsConvectionError_e
	swsConvectionErrorSuccessful  =0          # from enum swsConvectionError_e
	swsCoordinateTypeCartesian    =1          # from enum swsCoordinateType_e
	swsCoordinateTypeCylindrical  =3          # from enum swsCoordinateType_e
	swsCoordinateTypeSpherical    =2          # from enum swsCoordinateType_e
	swsCreateAnalysisDBAuthorizationFailed=22         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBDefineInitialTemperature=3          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBDefineRigidVirtualWallContact=2          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBEXMaterialPropertyNotDefined=13         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBEXValue    =14         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBFailed     =24         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMaterialNotDefined=19         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMaterialNotDefinedForComponents=20         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMaterialNotDefinedForShells=18         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMeshFailed =23         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMeshNotIdentical=11         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBMultipleLoadsUseSameTimeCurve=4          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBNeedOneOrMoreStaticStudies=6          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBNoFatigueEvent=7          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBNoSNCurve  =9          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBNoSolidBody=21         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBNoValidShell=12         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBPoissonsRatio=15         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBRemoveOrChangeCreep=17         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBSetUpDropTestStudy=5          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBSuccessful =0          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBThermalConductivityNotDefined=16         # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBTimeDependentOrAmplitideOnlyLoads=8          # from enum swsCreateAnalysisDatabaseError_e
	swsCreateAnalysisDBUseHighQualityMesh=1          # from enum swsCreateAnalysisDatabaseError_e
	swsDisplacementComponentRFRES =7          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRFX   =4          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRFY   =5          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRFZ   =6          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRMRES =14         # from enum swsDisplacementComponent_e
	swsDisplacementComponentRMX   =11         # from enum swsDisplacementComponent_e
	swsDisplacementComponentRMY   =12         # from enum swsDisplacementComponent_e
	swsDisplacementComponentRMZ   =13         # from enum swsDisplacementComponent_e
	swsDisplacementComponentRX    =8          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRY    =9          # from enum swsDisplacementComponent_e
	swsDisplacementComponentRZ    =10         # from enum swsDisplacementComponent_e
	swsDisplacementComponentURES  =3          # from enum swsDisplacementComponent_e
	swsDisplacementComponentUX    =0          # from enum swsDisplacementComponent_e
	swsDisplacementComponentUY    =1          # from enum swsDisplacementComponent_e
	swsDisplacementComponentUZ    =2          # from enum swsDisplacementComponent_e
	swsElasticConnectorEndEditErrorBodyExcludedFromAnalysis=10         # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorEntityAlreadyAdded=2          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorHasBeamBody=8          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorHasMassElement=9          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorNoEntityAtIndex=1          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorNullEntity=11         # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSelectEntity=7          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSelectFace=3          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSelectNonNegativeValueForNormalOrShearStiffness=5          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSelectNonZeroValueForNormalOrShearStiffness=6          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSelectPlanarFace=4          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorEndEditErrorSuccessful=0          # from enum swsElasticConnectorEndEditError_e
	swsElasticConnectorErrorBodyExcludedFromAnalysis=10         # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorFaceHasRemoteMassOrBeamBody=9          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorInvalidArray=4          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorInvalidMesh=1          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorInvalidStudy=3          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorNoEntityNoObject=7          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorNonlinearStudyAndPartDocument=2          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorNullOrEmptyArray=8          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorSelectFace=5          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorSelectPlanarFace=6          # from enum swsElasticConnectorError_e
	swsElasticConnectorErrorSuccessful=0          # from enum swsElasticConnectorError_e
	swsForceEndEditErrorEntityAlreadyExists=2          # from enum swsForceEndEditError_e
	swsForceEndEditErrorMagnitudeForceMustBeLargerZero=11         # from enum swsForceEndEditError_e
	swsForceEndEditErrorNoEntitiesSelected=3          # from enum swsForceEndEditError_e
	swsForceEndEditErrorNoEntityAtIndex=1          # from enum swsForceEndEditError_e
	swsForceEndEditErrorReferenceGeometryEntityNotSelected=5          # from enum swsForceEndEditError_e
	swsForceEndEditErrorSelectCoordinateSystem=8          # from enum swsForceEndEditError_e
	swsForceEndEditErrorSelectFace=7          # from enum swsForceEndEditError_e
	swsForceEndEditErrorSelectFaceEdgeOrVertex=4          # from enum swsForceEndEditError_e
	swsForceEndEditErrorSelectFaceEdgePlaneOrAxisForReferenceGeometry=6          # from enum swsForceEndEditError_e
	swsForceEndEditErrorSelectReferenceAxisOrCylindricalFaceForTorque=10         # from enum swsForceEndEditError_e
	swsForceEndEditErrorSuccessful=0          # from enum swsForceEndEditError_e
	swsForceEndEditErrorVariableForceCannotBeAppliedToVertices=12         # from enum swsForceEndEditError_e
	swsForceEndEditErrorVariableForceCannotBeAppliedToVerticesOrEdges=9          # from enum swsForceEndEditError_e
	swsForceErrorApplyNormalForceToFacesAndShellEdges=3          # from enum swsForceError_e
	swsForceErrorCannotApplyForce =10         # from enum swsForceError_e
	swsForceErrorCannotApplyNonuniformForce=9          # from enum swsForceError_e
	swsForceErrorCannotApplyNonuniformLoadOnMultipleBeam=18         # from enum swsForceError_e
	swsForceErrorCannotApplyZeroLoading=19         # from enum swsForceError_e
	swsForceErrorInvalidArray     =6          # from enum swsForceError_e
	swsForceErrorInvalidForceType =7          # from enum swsForceError_e
	swsForceErrorInvalidSelectionType=20         # from enum swsForceError_e
	swsForceErrorInvalidStudyType =5          # from enum swsForceError_e
	swsForceErrorNoEntities       =8          # from enum swsForceError_e
	swsForceErrorNonUniformBeamLoadInvalidTableData=21         # from enum swsForceError_e
	swsForceErrorNonUniformBeamLoadInvalidTableDistData=22         # from enum swsForceError_e
	swsForceErrorSelectFaceEdgePlaneOrAxis=2          # from enum swsForceError_e
	swsForceErrorSelectFacesEdgesVerticesOrPoints=1          # from enum swsForceError_e
	swsForceErrorSelectReferenceAxisOrCylindricalFace=4          # from enum swsForceError_e
	swsForceErrorSuccessful       =0          # from enum swsForceError_e
	swsForceTypeForceOrMoment     =0          # from enum swsForceType_e
	swsForceTypeNormal            =1          # from enum swsForceType_e
	swsForceTypeTorque            =2          # from enum swsForceType_e
	swsForceUnitNOrNm             =0          # from enum swsForceUnit_e
	swsForceUnitkgfOrkgfcm        =2          # from enum swsForceUnit_e
	swsForceUnitlbOrlbin          =1          # from enum swsForceUnit_e
	swsFrequencyStudyOptionNumberFrequencies=0          # from enum swsFrequencyStudyOption_e
	swsFrequencyStudyOptionUseUpperBoundFrequency=1          # from enum swsFrequencyStudyOption_e
	swsGapTypeAlwaysIgnoreClearance=0          # from enum swsGapType_e
	swsGapTypeIgnoreIfSmallerThanSpecifiedClearance=1          # from enum swsGapType_e
	swsGravityEndEditErrorSpecifyReferencePlaneFaceOrEdge=1          # from enum swsGravityEndEditError_e
	swsGravityEndEditErrorSuccessful=0          # from enum swsGravityEndEditError_e
	swsGravityEndEditErrorValuesCannotBeZeros=2          # from enum swsGravityEndEditError_e
	swsGravityErrorEdgeNotStraight=3          # from enum swsGravityError_e
	swsGravityErrorFaceNotPlanar  =2          # from enum swsGravityError_e
	swsGravityErrorGravityAlreadyDefined=4          # from enum swsGravityError_e
	swsGravityErrorInvalidStudy   =5          # from enum swsGravityError_e
	swsGravityErrorSelectFaceEdgeOrPlane=1          # from enum swsGravityError_e
	swsGravityErrorSuccessful     =0          # from enum swsGravityError_e
	swsHeatFluxEndEditErrorEntityAlreadyExists=2          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorLowerboundTemperatureHigherThanUpperbound=7          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorNoEntities=3          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorNoEntityAtIndex=1          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorSelectFace=4          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorSelectFacesOrShellEdge=5          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorSelectrVertexForSensorLocation=6          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorSuccessful=0          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxEndEditErrorThermostatForTransientStudiesOnly=8          # from enum swsHeatFluxEndEditError_e
	swsHeatFluxErrorInvalidArray  =4          # from enum swsHeatFluxError_e
	swsHeatFluxErrorInvalidStudy  =3          # from enum swsHeatFluxError_e
	swsHeatFluxErrorNoEntities    =5          # from enum swsHeatFluxError_e
	swsHeatFluxErrorNoFaces       =1          # from enum swsHeatFluxError_e
	swsHeatFluxErrorNoFacesOrShellEdges=2          # from enum swsHeatFluxError_e
	swsHeatFluxErrorSuccessful    =0          # from enum swsHeatFluxError_e
	swsHeatPowerEndEditErrorEntityAlreadyExists=2          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorLowerboundTemperatureHigherThanUpperbound=7          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorNoEntitiesSelected=3          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorNoEntityAtIndex=1          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorNotValidForSteadyStateAnalysis=8          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorSelectFaceEdgeOrVertex=5          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorSelectVertexForThermostatLocation=6          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies=4          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorSuccessful=0          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerEndEditErrorVertexCannotBeUsedForSensorLocation=9          # from enum swsHeatPowerEndEditError_e
	swsHeatPowerErrorInvalidArray =4          # from enum swsHeatPowerError_e
	swsHeatPowerErrorInvalidStudy =3          # from enum swsHeatPowerError_e
	swsHeatPowerErrorNoEntities   =5          # from enum swsHeatPowerError_e
	swsHeatPowerErrorSelectFaceEdgeVertexComponentOrBody=1          # from enum swsHeatPowerError_e
	swsHeatPowerErrorSelectFacesEdgesOrVertices=2          # from enum swsHeatPowerError_e
	swsHeatPowerErrorSuccessful   =0          # from enum swsHeatPowerError_e
	swsLinearUnitCentimeters      =1          # from enum swsLinearUnit_e
	swsLinearUnitFeet             =4          # from enum swsLinearUnit_e
	swsLinearUnitFeetInches       =5          # from enum swsLinearUnit_e
	swsLinearUnitInches           =3          # from enum swsLinearUnit_e
	swsLinearUnitMeters           =2          # from enum swsLinearUnit_e
	swsLinearUnitMillimeters      =0          # from enum swsLinearUnit_e
	swsLinkConnectorEndEditErrorBodyExcludedFromAnalysis=7          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorEntityAlreadyExists=1          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorHasBeamBody=5          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorHasMassElement=6          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorNullEntity=4          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorSelectDatumPointOrVertices=2          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorSelectEntity=3          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorEndEditErrorSuccessful=0          # from enum swsLinkConnectorEndEditError_e
	swsLinkConnectorErrorBodyExcludedFromAnalysis=8          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorEmptyEntity=5          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorHasRemoteMassOrBeamBody=7          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorInvalidMesh=1          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorInvalidStudy=3          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorNonlinearStudyPartDocument=2          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorSelectAssemblyDocument=4          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorSelectVertexOrDatumPoint=6          # from enum swsLinkConnectorError_e
	swsLinkConnectorErrorSuccessful=0          # from enum swsLinkConnectorError_e
	swsLoadsAndRestraintsErrorNotFoundAtIndex=1          # from enum swsLoadsAndRestraintsError_e
	swsLoadsAndRestraintsErrorSuccessful=0          # from enum swsLoadsAndRestraintsError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorBodyExcludedFromAnalysis=9          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemAndCylindricalFaces=6          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemEmpty=3          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorInvalidArray=1          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorInvalidMesh=7          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorInvalidStudy=8          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorNoObjectForFace=2          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorSelectCoordinateSystem=5          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorSelectFace=4          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsManagerBearingLoadErrorSuccessful=0          # from enum swsLoadsAndRestraintsManagerBearingLoadError_e
	swsLoadsAndRestraintsTypeBearingLoads=13         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeCentrifugal=5          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeConnectors=12         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeConvection=7          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeForce=3          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeGravity=4          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeHeatFlux=9          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeHeatPower=8          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeMeshControl=21         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypePressure=1          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeRadiation=10         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeRemoteLoad=11         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeRemoteMass=31         # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeRestraint=2          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeTemperature=6          # from enum swsLoadsAndRestraintsType_e
	swsLoadsAndRestraintsTypeVelocity=14         # from enum swsLoadsAndRestraintsType_e
	swsMaterialDataCurveErrorCannotBeDefined=1          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorIndexForMooneyRivlinAndOgeden=3          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorIndexForViscoElastic=4          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorIndexValues=2          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorInvalidArray=5          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorNeedDataPoints=7          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorSuccessful=0          # from enum swsMaterialDataCurveError_e
	swsMaterialDataCurveErrorTemperatures=6          # from enum swsMaterialDataCurveError_e
	swsMaterialErrorWarningCreepWithForceControl=24         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningDefineCurveForEx=10         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningDefinePointForStressStrainCurve=16         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningDefineProperty=6          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningDefineStressStrainCurve=15         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningDensityNotDefined=13         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningEXNotDefined=8          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningEXValue=9          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningFatigueSNCurvesCycles=3          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningInvalidLinearElasticAnisotropicMaterialModel=1          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningInvalidMaterialModel=2          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningMaterialPropertyValue=7          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningMaterialTemperatureCurveForNitinol=11         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningMaterialTemperatureDependencyIgnored=30         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningNUXYNotDefined=32         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningNUXYValue=12         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningOnlyBilinearPlasticityForDropTestStudies=31         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGC_F2LessThanSIGC_S2=23         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGC_S1LessThanSIGC_F1=21         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGC_S2LessThanSIGC_F1=22         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGT_F2LessThanSIGT_S2=20         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGT_S1LessThanSIGT_F1=18         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGT_S1_F1_S2_F2Values=17         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSIGT_S2LessThanSIGT_F1=19         # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningSuccessful=0          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningTooManyPointsSNCurve=5          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningUniqueStressRatioForEachSNCurve=4          # from enum swsMaterialErrorWarning_e
	swsMaterialErrorWarningrKXNotDefined=14         # from enum swsMaterialErrorWarning_e
	swsMaterialFatigueSNCurveErrorCurveDataPoints=4          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialFatigueSNCurveErrorCycles=3          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialFatigueSNCurveErrorIndexValues=1          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialFatigueSNCurveErrorInvalidArray=2          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialFatigueSNCurveErrorStressValuesMustBeUnique=5          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialFatigueSNCurveErrorSuccessful=0          # from enum swsMaterialFatigueSNCurveError_e
	swsMaterialModelTypeCreepExponential=12         # from enum swsMaterialModelType_e
	swsMaterialModelTypeElastoPlasticDruckerPrager=6          # from enum swsMaterialModelType_e
	swsMaterialModelTypeElastoPlasticTrescaKinematic=5          # from enum swsMaterialModelType_e
	swsMaterialModelTypeElastoPlasticvonMisesKinematic=4          # from enum swsMaterialModelType_e
	swsMaterialModelTypeHyperElasticBlatzko=9          # from enum swsMaterialModelType_e
	swsMaterialModelTypeHyperElasticMooneyRivlin=7          # from enum swsMaterialModelType_e
	swsMaterialModelTypeHyperElasticOgden=8          # from enum swsMaterialModelType_e
	swsMaterialModelTypeLinearElasticAnisotropic=2          # from enum swsMaterialModelType_e
	swsMaterialModelTypeLinearElasticIsotropic=0          # from enum swsMaterialModelType_e
	swsMaterialModelTypeLinearElasticOrthtropic=1          # from enum swsMaterialModelType_e
	swsMaterialModelTypeNitinol   =11         # from enum swsMaterialModelType_e
	swsMaterialModelTypeNonlinearElastic=3          # from enum swsMaterialModelType_e
	swsMaterialModelTypeViscoElastic=10         # from enum swsMaterialModelType_e
	swsMaterialReferencePlaneErrorSpecifyPlaneOrAxis=1          # from enum swsMaterialReferencePlaneError_e
	swsMaterialReferencePlaneErrorSuccessful=0          # from enum swsMaterialReferencePlaneError_e
	swsMaterialSNCurveSourceASMEAustenticSteel=1          # from enum swsMaterialSNCurveSource_e
	swsMaterialSNCurveSourceASMECarbonSteel=2          # from enum swsMaterialSNCurveSource_e
	swsMaterialSNCurveSourceUserDefined=0          # from enum swsMaterialSNCurveSource_e
	swsMaterialSourceCentorLibrary=2          # from enum swsMaterialSource_e
	swsMaterialSourceCustomDefined=1          # from enum swsMaterialSource_e
	swsMaterialSourceLibraryFiles =3          # from enum swsMaterialSource_e
	swsMaterialSourceSolidWorks   =0          # from enum swsMaterialSource_e
	swsMaterialStressStrainCurveErrorInvalidArray=2          # from enum swsMaterialStressStrainCurveError_e
	swsMaterialStressStrainCurveErrorInvalidForMaterial=1          # from enum swsMaterialStressStrainCurveError_e
	swsMaterialStressStrainCurveErrorNeedDataPoints=4          # from enum swsMaterialStressStrainCurveError_e
	swsMaterialStressStrainCurveErrorSuccessful=0          # from enum swsMaterialStressStrainCurveError_e
	swsMaterialStressStrainCurveErrorTemperatures=3          # from enum swsMaterialStressStrainCurveError_e
	swsMaterialTemperatureCurveForPropertyErrorInvalidArray=4          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorNeedDataPoints=5          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorNotAllowed=3          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorNotApplicable=2          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorPropertyNotDefined=1          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorSuccessful=0          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureCurveForPropertyErrorTermperatures=6          # from enum swsMaterialTemperatureCurveForPropertyError_e
	swsMaterialTemperatureDependent=0          # from enum swsMaterialTemperature_e
	swsMaterialTemperatureNotDependent=1          # from enum swsMaterialTemperature_e
	swsMeshCompatibilityCompatible=0          # from enum swsMeshCompatibility_e
	swsMeshCompatibiltyIncompatible=1          # from enum swsMeshCompatibility_e
	swsMeshControlErrorElementSize=6          # from enum swsMeshControlError_e
	swsMeshControlErrorEntityAlreadyExists=2          # from enum swsMeshControlError_e
	swsMeshControlErrorNoEntities =3          # from enum swsMeshControlError_e
	swsMeshControlErrorNoEntityAtIndex=1          # from enum swsMeshControlError_e
	swsMeshControlErrorNumberOfLayers=7          # from enum swsMeshControlError_e
	swsMeshControlErrorSelectFaceEdgeOrVertex=5          # from enum swsMeshControlError_e
	swsMeshControlErrorSelectVerticesEdgesFacesBodiesOrComponents=4          # from enum swsMeshControlError_e
	swsMeshControlErrorSuccessful =0          # from enum swsMeshControlError_e
	swsMeshControlWeightFactorDefault=0          # from enum swsMeshControlWeightFactor_e
	swsMeshControlWeightFactorHighest=1          # from enum swsMeshControlWeightFactor_e
	swsMeshElementNodeLocationNoElement=2          # from enum swsMeshElementNodeLocation_e
	swsMeshElementNodeLocationNoNode=1          # from enum swsMeshElementNodeLocation_e
	swsMeshElementNodeLocationSuccessful=0          # from enum swsMeshElementNodeLocation_e
	swsMeshFlipShellErrorEmptyArray=2          # from enum swsMeshFlipShellError_e
	swsMeshFlipShellErrorInvalidArray=1          # from enum swsMeshFlipShellError_e
	swsMeshFlipShellErrorMeshInformationNotFound=5          # from enum swsMeshFlipShellError_e
	swsMeshFlipShellErrorNotShell =3          # from enum swsMeshFlipShellError_e
	swsMeshFlipShellErrorSelectFaces=4          # from enum swsMeshFlipShellError_e
	swsMeshFlipShellErrorSuccessful=0          # from enum swsMeshFlipShellError_e
	swsMeshQualityDraft           =0          # from enum swsMeshQuality_e
	swsMeshQualityHigh            =1          # from enum swsMeshQuality_e
	swsMeshShellNormalBottomFace  =1          # from enum swsMeshShellNormal_e
	swsMeshShellNormalNotFoundOrFaceNotSelected=-1         # from enum swsMeshShellNormal_e
	swsMeshShellNormalTopFace     =0          # from enum swsMeshShellNormal_e
	swsMeshStateExistsAndCurrent  =1          # from enum swsMeshState_e
	swsMeshStateExistsAndNotCurrent=2          # from enum swsMeshState_e
	swsMeshStateFailed            =3          # from enum swsMeshState_e
	swsMeshStateInterrupted       =4          # from enum swsMeshState_e
	swsMeshStateNoMesh            =0          # from enum swsMeshState_e
	swsMeshTypeBeam               =4          # from enum swsMeshType_e
	swsMeshTypeMidSurface         =1          # from enum swsMeshType_e
	swsMeshTypeMixed              =3          # from enum swsMeshType_e
	swsMeshTypeSolid              =0          # from enum swsMeshType_e
	swsMeshTypeSurfaces           =2          # from enum swsMeshType_e
	swsMesherTypeAlternate        =1          # from enum swsMesherType_e
	swsMesherTypeStandard         =0          # from enum swsMesherType_e
	swsNoPenetrationOptionNodeToNode=0          # from enum swsNoPenetrationOption_e
	swsNoPenetrationOptionNodeToSurface=1          # from enum swsNoPenetrationOption_e
	swsNoPenetrationOptionSurfaceToSurface=2          # from enum swsNoPenetrationOption_e
	swsNonLinearControl_ArcLength =2          # from enum swsNonLinearOptionControlMethodType_e
	swsNonLinearControl_Displacement=1          # from enum swsNonLinearOptionControlMethodType_e
	swsNonLinearControl_Force     =0          # from enum swsNonLinearOptionControlMethodType_e
	swsNonLinearIntegration_CentralDifference=2          # from enum swsNonLinearOptionIntegrationMethodType_e
	swsNonLinearIntegration_Newmark=0          # from enum swsNonLinearOptionIntegrationMethodType_e
	swsNonLinearIntegration_WilsonTheta=1          # from enum swsNonLinearOptionIntegrationMethodType_e
	swsNonLinearIterative_ModifiedNewtonRaphson=0          # from enum swsNonLinearOptionIterativeMethodType_e
	swsNonLinearIterative_NewtonRaphson=1          # from enum swsNonLinearOptionIterativeMethodType_e
	swsNonLinearStudyInvalidArcLengthMaximumDisplacementValue=17         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidArcLengthMaximumLoadValue=18         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidArcLengthMultiplierValue=16         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidArcLengthStepsValue=19         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidDisplaceComponentUnitValue=15         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidDisplaceComponentValue=14         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyInvalidSingularityEliminationfactorValue=20         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorAutoSteppingParameters=2          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorEmptyDispatch=12         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectArcLengthControlType=7          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectDirectSolver=9          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectDisplacementControlType=6          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectForceControl=10         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectTimeCurve=8          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSelectVerticesOrDatumPoint=5          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSolutionSteps=4          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorStartEndStepsAndIncrement=1          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorStartTimeLessThanEndTime=3          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorSuccessful=0          # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyOptionsErrorWrongArcLengthUnit=11         # from enum swsNonLinearStudyOptionsError_e
	swsNonLinearStudyTimeCurveErrorInvalidStudyType=13         # from enum swsNonLinearStudyOptionsError_e
	swsPinConnectorEndEditErrorBodyExcludedFromAnalysis=23         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorEntityAlreadyAdded=2          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorHasBeamBody=11         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorHasMassElement=12         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorIncludeStrengthData=25         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorIndexTooBig=10         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorNoEntityAtIndex=1          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorNullEntity=24         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorPinBoltStrength=20         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorPinMass=17         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorRadiiNotEqual=7          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSafetyFactor=21         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectAssemblyDocument=8          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectCircularEdge=22         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectCircularEdges=13         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnection=9          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnector=6          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectDifferentBody=14         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectEntity=3          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectFace=4          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectFaceCylindricalSurface=5          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSelectFacesFromSameHole=15         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSpecifyPositiveValue=16         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorSuccessful=0          # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorTensileStressArea=18         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorEndEditErrorTesileStressAreaLarge=19         # from enum swsPinConnectorEndEditError_e
	swsPinConnectorErrorArrayEmtpy=16         # from enum swsPinConnectorError_e
	swsPinConnectorErrorArrayHasBeamBody=17         # from enum swsPinConnectorError_e
	swsPinConnectorErrorBodyExcludedFromAnalysis=20         # from enum swsPinConnectorError_e
	swsPinConnectorErrorComponentConcentricFacesRadiiNotEqual=8          # from enum swsPinConnectorError_e
	swsPinConnectorErrorEntitySameForComponents=14         # from enum swsPinConnectorError_e
	swsPinConnectorErrorFaceNotCylindrical=6          # from enum swsPinConnectorError_e
	swsPinConnectorErrorInvalidArray=9          # from enum swsPinConnectorError_e
	swsPinConnectorErrorInvalidMesh=1          # from enum swsPinConnectorError_e
	swsPinConnectorErrorInvalidStudy=3          # from enum swsPinConnectorError_e
	swsPinConnectorErrorNoObject  =4          # from enum swsPinConnectorError_e
	swsPinConnectorErrorNonlinearStudyPartDocument=2          # from enum swsPinConnectorError_e
	swsPinConnectorErrorNullOrEmptyArray=13         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectAssemblyDocument=10         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectCircularEdgesOnShells=19         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectConcentricCylindricalFacesForConnection=18         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectConcentricCylindricalFacesForConnector=7          # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectDifferentBody=15         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectFace=5          # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectFaceFromSameHoleForTarget=12         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSelectFacesFromSameHoleForSource=11         # from enum swsPinConnectorError_e
	swsPinConnectorErrorSuccesful =0          # from enum swsPinConnectorError_e
	swsPInballcm                  =1          # from enum swsPinballUnit_e
	swsPinaballnm                 =7          # from enum swsPinballUnit_e
	swsPinballam                  =6          # from enum swsPinballUnit_e
	swsPinballft                  =4          # from enum swsPinballUnit_e
	swsPinballftin                =5          # from enum swsPinballUnit_e
	swsPinballin                  =3          # from enum swsPinballUnit_e
	swsPinballm                   =2          # from enum swsPinballUnit_e
	swsPinballmicron              =8          # from enum swsPinballUnit_e
	swsPinballmicronIn            =10         # from enum swsPinballUnit_e
	swsPinballmil                 =9          # from enum swsPinballUnit_e
	swsPinballmm                  =0          # from enum swsPinballUnit_e
	swsPreLoadForceTypeCompression=0          # from enum swsPreLoadForceType_e
	swsPreLoadForceTypeTension    =1          # from enum swsPreLoadForceType_e
	swsPreloadForceAxial          =0          # from enum swsPreloadForce_e
	swsPreloadForceTorque         =1          # from enum swsPreloadForce_e
	swsPressureEndEditErrorEntityAlreadyAdded=2          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorNoEntities=3          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorNoEntityAtIndex=1          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorRefGeomPreExist=6          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorSelectCoordinateSystem=8          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorSelectFaceEdgePlaneOrAxis=7          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorSelectFaceOrShellEdge=5          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorSelectFacesOrShellEdges=4          # from enum swsPressureEndEditError_e
	swsPressureEndEditErrorSuccessful=0          # from enum swsPressureEndEditError_e
	swsPressureErrorCannotApplyPressure=7          # from enum swsPressureError_e
	swsPressureErrorInvalidArray  =6          # from enum swsPressureError_e
	swsPressureErrorInvalidStudy  =5          # from enum swsPressureError_e
	swsPressureErrorPressureType  =4          # from enum swsPressureError_e
	swsPressureErrorSelectFaceEdgePlaneOrAxis=3          # from enum swsPressureError_e
	swsPressureErrorSelectFaceOrFaces=1          # from enum swsPressureError_e
	swsPressureErrorSelectFacesOrShellEdges=2          # from enum swsPressureError_e
	swsPressureErrorSuccessful    =0          # from enum swsPressureError_e
	swsPressureTypeNormal         =0          # from enum swsPressureType_e
	swsPressureTypeUseReferenceGeometry=1          # from enum swsPressureType_e
	swsRadiationEndEditErrorEmissivity=6          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorEntityAlreadyExists=2          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorNoEntities=3          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorNoEntityAtIndex=1          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorSelectFace=4          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorSelectFaceOrEdge=5          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorSuccessful=0          # from enum swsRadiationEndEditError_e
	swsRadiationEndEditErrorViewFactor=7          # from enum swsRadiationEndEditError_e
	swsRadiationErrorEmtpyArray   =6          # from enum swsRadiationError_e
	swsRadiationErrorInvalidArray =5          # from enum swsRadiationError_e
	swsRadiationErrorInvalidStudy =3          # from enum swsRadiationError_e
	swsRadiationErrorRadiationType=4          # from enum swsRadiationError_e
	swsRadiationErrorSelectFaceOrShellEdge=2          # from enum swsRadiationError_e
	swsRadiationErrorSelectFaces  =1          # from enum swsRadiationError_e
	swsRadiationErrorSuccessful   =0          # from enum swsRadiationError_e
	swsRadiationOpenSystemClosed  =0          # from enum swsRadiationOpenSystem_e
	swsRadiationOpenSystemOpen    =1          # from enum swsRadiationOpenSystem_e
	swsRadiationTypeSurfaceToAmbient=0          # from enum swsRadiationType_e
	swsRadiationTypeSurfaceToSurface=1          # from enum swsRadiationType_e
	swsResistanceTypeDistributed  =1          # from enum swsResistanceType_e
	swsResistanceTypeTotal        =0          # from enum swsResistanceType_e
	swsRestraintEndEditErrorCannotRestrainRefGeometryEntity=14         # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorCyclicSymmetryRestraint=10         # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorDefineDisplacementComponent=13         # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorEntityExists=2          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorNoEntity=3          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorNoIndex=1          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectAxis=12         # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectCylindricalFaces=6          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectFaceEdgeOrVertices=4          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectFaceEdgeVertexOrFaces=8          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectFaces=5          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectPlaneAxisEdgeFaceOrCylinder=9          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectSphericalFaces=7          # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSelectTwoFaces=11         # from enum swsRestraintEndEditError_e
	swsRestraintEndEditErrorSuccess=0          # from enum swsRestraintEndEditError_e
	swsRestraintErrorCannotApplyRestraint=14         # from enum swsRestraintError_e
	swsRestraintErrorInMeshType   =8          # from enum swsRestraintError_e
	swsRestraintErrorInvalidArray =11         # from enum swsRestraintError_e
	swsRestraintErrorInvalidMesh  =15         # from enum swsRestraintError_e
	swsRestraintErrorInvalidRestraintType=13         # from enum swsRestraintError_e
	swsRestraintErrorInvalidStudyType=9          # from enum swsRestraintError_e
	swsRestraintErrorNoEntities   =10         # from enum swsRestraintError_e
	swsRestraintErrorSelectFace   =7          # from enum swsRestraintError_e
	swsRestraintErrorSelectFacesEdgesOrVertices=1          # from enum swsRestraintError_e
	swsRestraintErrorSelectPlanarFace=2          # from enum swsRestraintError_e
	swsRestraintErrorSpecifyCylindricalFace=3          # from enum swsRestraintError_e
	swsRestraintErrorSpecifyFaceEdgePlaneOrAxis=6          # from enum swsRestraintError_e
	swsRestraintErrorSpecifySphericalFace=4          # from enum swsRestraintError_e
	swsRestraintErrorSpecifyTwoFacesOneAxis=12         # from enum swsRestraintError_e
	swsRestraintErrorSuccess      =0          # from enum swsRestraintError_e
	swsRestraintTypeCyclicSymmetry=9          # from enum swsRestraintType_e
	swsRestraintTypeCylindricalFaces=7          # from enum swsRestraintType_e
	swsRestraintTypeFixed         =0          # from enum swsRestraintType_e
	swsRestraintTypeFlatFace      =6          # from enum swsRestraintType_e
	swsRestraintTypeHinge         =4          # from enum swsRestraintType_e
	swsRestraintTypeImmovable     =1          # from enum swsRestraintType_e
	swsRestraintTypeReferenceGeometry=5          # from enum swsRestraintType_e
	swsRestraintTypeRoller        =3          # from enum swsRestraintType_e
	swsRestraintTypeSphericalSurface=8          # from enum swsRestraintType_e
	swsRestraintTypeSymmetric     =2          # from enum swsRestraintType_e
	swsResultsErrorDatabaseNotAvailable=1          # from enum swsResultsError_e
	swsResultsErrorIncorrectCodeNumber=6          # from enum swsResultsError_e
	swsResultsErrorIncorrectReferenceEntity=3          # from enum swsResultsError_e
	swsResultsErrorInvalidComponent=5          # from enum swsResultsError_e
	swsResultsErrorNoResultType   =4          # from enum swsResultsError_e
	swsResultsErrorSuccessful     =0          # from enum swsResultsError_e
	swsResultsFactorsErrorInvalidEntity=7          # from enum swsResultsError_e
	swsResultsIncompatibleStudy   =8          # from enum swsResultsError_e
	swsResultssErrorIncorrectStepNumber=2          # from enum swsResultsError_e
	swsResultsRotationalDisplacementUnitDeg=0          # from enum swsResultsRotationalDisplacementUnit_e
	swsResultsRotationalDisplacementUnitDegMin=1          # from enum swsResultsRotationalDisplacementUnit_e
	swsResultsRotationalDisplacementUnitDegMinSec=2          # from enum swsResultsRotationalDisplacementUnit_e
	swsResultsRotationalDisplacementUnitRad=3          # from enum swsResultsRotationalDisplacementUnit_e
	swsRigidConnectorEndEditErrorBodyExcludedFromAnalysis=9          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorEntityAlreadyAdded=2          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorFacesOnSameComponent=8          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorHasBeamBody=6          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorHasMassBody=7          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorIndexTooBig=5          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorNoEntityAtIndex=1          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorNullEntity=10         # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorSelectFace=4          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorSelectTargetEntityOrFaces=3          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorEndEditErrorSuccessful=0          # from enum swsRigidConnectorEndEditError_e
	swsRigidConnectorErrorBodyExcludedFromAnalysis=14         # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorBodyHasRemoteMass=11         # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorFacesFromSameComponent=13         # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorInvalidMesh=1          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorInvalidSourceArray=5          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorInvalidStudy=3          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorInvalidTargetArray=7          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorNoObjectForFace=6          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorNoObjectForTarget=8          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorNonlinearStudyPartDocument=2          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorNullOrEmptyArray=12         # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorSameEntityAtFaceAndTargetArray=10         # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorSelectAssemblyDocument=4          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorSelectFace=9          # from enum swsRigidConnectorError_e
	swsRigidConnectorErrorSuccessful=0          # from enum swsRigidConnectorError_e
	swsRunAnalysisDefineInitialTemperature=3          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorAnalysisFailed=24         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorAuthorizationFailed=22         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorDefineRigidVirtualWallContact=2          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorEXMaterialPropertyNotDefined=13         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorEXValue    =14         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMaterialNotDefined=19         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMaterialNotDefinedForComponents=20         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMaterialNotDefinedForShells=18         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMeshNotFound=23         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMeshNotIdentical=11         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorMultipleLoadsUseSameTimeCurve=4          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorNeedOneOrMoreStaticStudies=6          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorNoFatigueEvent=7          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorNoSNCurve  =9          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorNoSolidBody=21         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorNoValidShell=12         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorPoissonsRatio=15         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorRemoveOrChangeCreep=17         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorSetUpDropTestStudy=5          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorSuccessful =0          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorThermalConductivityNotDefined=16         # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorTimeDependentOrAmplitideOnlyLoads=8          # from enum swsRunAnalysisError_e
	swsRunAnalysisErrorUseHighQualityMesh=1          # from enum swsRunAnalysisError_e
	swsSelectionBeamEndJoints     =1          # from enum swsSelectionType_e
	swsSelectionBeams             =2          # from enum swsSelectionType_e
	swsSelectionFaceEdgeVertexPoint=0          # from enum swsSelectionType_e
	swsShellEndEditErrorFaceAlreadyDefinedAsShell=6          # from enum swsShellEndEditError_e
	swsShellEndEditErrorFaceAlreadyExists=5          # from enum swsShellEndEditError_e
	swsShellEndEditErrorFormulation=2          # from enum swsShellEndEditError_e
	swsShellEndEditErrorNoEntitySelected=7          # from enum swsShellEndEditError_e
	swsShellEndEditErrorNotEntityAtIndex=3          # from enum swsShellEndEditError_e
	swsShellEndEditErrorSelectFace=4          # from enum swsShellEndEditError_e
	swsShellEndEditErrorShellThickness=1          # from enum swsShellEndEditError_e
	swsShellEndEditErrorSuccessful=0          # from enum swsShellEndEditError_e
	swsShellEndEditErrorUnit      =8          # from enum swsShellEndEditError_e
	swsShellFormulationThick      =1          # from enum swsShellFormulation_e
	swsShellFormulationThin       =0          # from enum swsShellFormulation_e
	swsShellManagerErrorCannotApplyShellForMesh=2          # from enum swsShellManagerError_e
	swsShellManagerErrorCannotApplyShellForStudy=1          # from enum swsShellManagerError_e
	swsShellManagerErrorEmptyArray=3          # from enum swsShellManagerError_e
	swsShellManagerErrorFaceAlreadyDefinedAsShell=6          # from enum swsShellManagerError_e
	swsShellManagerErrorFaceAlreadyExists=7          # from enum swsShellManagerError_e
	swsShellManagerErrorInvalidArray=4          # from enum swsShellManagerError_e
	swsShellManagerErrorSelectFacesOnly=5          # from enum swsShellManagerError_e
	swsShellManagerErrorSuccessful=0          # from enum swsShellManagerError_e
	swsShrinkFitOptionFitNodeToSurface=0          # from enum swsShrinkFitOption_e
	swsShrinkFitOptionSurfaceToSurface=1          # from enum swsShrinkFitOption_e
	swsSolverTypeAutomatic        =0          # from enum swsSolverType_e
	swsSolverTypeDirectSparse     =1          # from enum swsSolverType_e
	swsSolverTypeFFEPlus          =2          # from enum swsSolverType_e
	swsSpotWeldConnectorEndEditErrorBodyExcludedFromAnalysis=18         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorEntityAlreadyExists=2          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorFaceIsEmpty=3          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorGapTooBig=7          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorHasBeamBody=11         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorHasMassElement=12         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorIndexTooBig=14         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorInvalidPoints=17         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorNoEntityAtIndex=15         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorNullEntity=1          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorPlanesShouldTouch=6          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorPositiveStudDiameter=9          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorSelectDatumPoints=8          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorSelectFace=16         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorSelectParallelFaces=5          # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorSpotWeldDiameter=13         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorStudDiameter=10         # from enum swsSpotWeldConnectorEndEditError_e
	swsSpotWeldConnectorEndEditErrorSuccessful=0          # from enum swsSpotWeldConnectorEndEditError_e
	SpotWeldConnectorErrorSelectVerticesOrDatumPoint=7          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorBodyExcludedFromAnalysis=16         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorEmptyArray=14         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorGapTooBig=10         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorHasRemoteMass=15         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorInvalidArray=13         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorInvalidMesh=1          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorInvalidStudy=3          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorNonlinearStudyPartDocument=2          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorNullDispatch=4          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorPlanesNotParallel=8          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorPlanesTouching=9          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorPostWeldInvalidPoints=12         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorSelectAssemblyDocument=5          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorSelectDatumPoints=11         # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorSelectFace=6          # from enum swsSpotWeldConnectorError_e
	swsSpotWeldConnectorErrorSuccessful=0          # from enum swsSpotWeldConnectorError_e
	swsSpringConnectorEndEditErrorBodyExcludedFromAnalysis=18         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorEntityAlreadyExists=11         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorHasBeamBody=14         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorHasMassElement=15         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorIndexInvalidForRemovalOfEntity=13         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorNoEntity=1          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorNoEntityAtIndex=12         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorNormalTangentialOrRotationalStiffness=8          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorNullEntity=17         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorRadiiNotEqual=7          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectConcentricCylindricalFaces=6          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectDatumPointOrVertex=10         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectFace=2          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectFaceWithCylindricalSurface=5          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectPlanarFace=3          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectTwoParallelPlanarFaces=4          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSelectionsBelongToSameBody=16         # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorStiffness=9          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorEndEditErrorSuccessful=0          # from enum swsSpringConnectorEndEditError_e
	swsSpringConnectorErrorBodyExcludedFromAnalysis=22         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorCylindricalFacesRadiiNotEqual=8          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorEmptyArray=20         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorHasRemoteMass=19         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorInvalidArray=13         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorInvalidMesh=1          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorInvalidStudy=3          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorNoObjectForSourceOrTarget=15         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorNonlinearStudyPartDocument=2          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorNumberPlanarFacesLessThanTwo=14         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectDatumPoint=16         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectEntities=4          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectFace=5          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectFaceWithCylindricalSurface=6          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectPlanarFace=9          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectTwoConcentricCylindricalFaces=7          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectTwoPlanarFaces=10         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSelectionsOnToSameComponent=18         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSourceTargetEntitiesSame=11         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSpringSubtypeInvalidForShellMesh=21         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorStudyNonlinearAndSpringSubtypeValue=12         # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorSuccessful=0          # from enum swsSpringConnectorError_e
	swsSpringConnectorErrorTooManyEntitiesForSpringType=17         # from enum swsSpringConnectorError_e
	swsSpringConnectoryTypeBetweenVertices=2          # from enum swsSpringConnectorType_e
	swsSpringConnectoryTypeConcentricCylindricalFaces=1          # from enum swsSpringConnectorType_e
	swsSpringConnectoryTypeFlatParallelFaces=0          # from enum swsSpringConnectorType_e
	swsSpringSubTypeBetweenVertices=2          # from enum swsSpringSubType_e
	swsSpringSubTypeConcentricCylindricalFaces=1          # from enum swsSpringSubType_e
	swsSpringSubTypeFlatParallelFaces=0          # from enum swsSpringSubType_e
	swsSpringTypeCompression      =1          # from enum swsSpringType_e
	swsSpringTypeCompressionExtension=0          # from enum swsSpringType_e
	swsSpringTypeExtension        =2          # from enum swsSpringType_e
	swsStiffnessTypeDistributed   =0          # from enum swsStiffnessType_e
	swsStiffnessTypeTotal         =1          # from enum swsStiffnessType_e
	swsStrainComponentE1          =9          # from enum swsStrainComponent_e
	swsStrainComponentE2          =10         # from enum swsStrainComponent_e
	swsStrainComponentE3          =11         # from enum swsStrainComponent_e
	swsStrainComponentENERGY      =8          # from enum swsStrainComponent_e
	swsStrainComponentEPSX        =0          # from enum swsStrainComponent_e
	swsStrainComponentEPSY        =1          # from enum swsStrainComponent_e
	swsStrainComponentEPSZ        =2          # from enum swsStrainComponent_e
	swsStrainComponentESTRN       =6          # from enum swsStrainComponent_e
	swsStrainComponentGMXY        =3          # from enum swsStrainComponent_e
	swsStrainComponentGMXZ        =4          # from enum swsStrainComponent_e
	swsStrainComponentGMYZ        =5          # from enum swsStrainComponent_e
	swsStrainComponentSEDENS      =7          # from enum swsStrainComponent_e
	swsStrengthUnitKilogramsPerSquareCentimeter=2          # from enum swsStrengthUnit_e
	swsStrengthUnitNewtonPerSquareMillimeter=3          # from enum swsStrengthUnit_e
	swsStrengthUnitPascal         =0          # from enum swsStrengthUnit_e
	swsStrengthUnitpsi            =1          # from enum swsStrengthUnit_e
	swsStressComponentCP          =12         # from enum swsStressComponent_e
	swsStressComponentERR         =11         # from enum swsStressComponent_e
	swsStressComponentINT         =10         # from enum swsStressComponent_e
	swsStressComponentP1          =6          # from enum swsStressComponent_e
	swsStressComponentP2          =7          # from enum swsStressComponent_e
	swsStressComponentP3          =8          # from enum swsStressComponent_e
	swsStressComponentSX          =0          # from enum swsStressComponent_e
	swsStressComponentSY          =1          # from enum swsStressComponent_e
	swsStressComponentSZ          =2          # from enum swsStressComponent_e
	swsStressComponentTXY         =3          # from enum swsStressComponent_e
	swsStressComponentTXZ         =4          # from enum swsStressComponent_e
	swsStressComponentTYZ         =5          # from enum swsStressComponent_e
	swsStressComponentVON         =9          # from enum swsStressComponent_e
	swsNewStudyErrorInvalidMeshType=4          # from enum swsStudyError_e
	swsNewStudyErrorNoSolidBody   =1          # from enum swsStudyError_e
	swsNewStudyErrorSameNameStudyExistsOrInvalidStudyName=2          # from enum swsStudyError_e
	swsNewStudyErrorSuccessful    =0          # from enum swsStudyError_e
	swsNewStudyErrorTypeNotDefined=3          # from enum swsStudyError_e
	swsStudyErrorElementSizeTooBig=4          # from enum swsStudyMeshError_e
	swsStudyErrorElementSizeTooSmall=3          # from enum swsStudyMeshError_e
	swsStudyErrorNoSolidBody      =2          # from enum swsStudyMeshError_e
	swsStudyErrorNoValidShells    =1          # from enum swsStudyMeshError_e
	swsStudyErrorSpecifyElementSizeScaleFactor=6          # from enum swsStudyMeshError_e
	swsStudyErrorSpecifyPositiveValue=5          # from enum swsStudyMeshError_e
	swsStudyErrorSpecifyToleranceScaleFactor=7          # from enum swsStudyMeshError_e
	swsStudyErrorSuccessful       =0          # from enum swsStudyMeshError_e
	swsSupressionStateSuppressed  =0          # from enum swsSuppressionState_e
	swsSupressionStateUnsuppressed=1          # from enum swsSuppressionState_e
	swsSymmtricalBoltTypeOneHalfSymmetry=0          # from enum swsSymmetricalBoltType_e
	swsSymmtricalBoltTypeOneQuarterSymmetry=1          # from enum swsSymmetricalBoltType_e
	swsDistance                   =1          # from enum swsTableDrivenDistOption_e
	swsPercentage                 =0          # from enum swsTableDrivenDistOption_e
	swsCubic                      =1          # from enum swsTableDrivenInterpolationType_e
	swsLinear                     =0          # from enum swsTableDrivenInterpolationType_e
	swsTemperatureCurveErrorCurveCannotBeUsed=2          # from enum swsTemperatureCurveError_e
	swsTemperatureCurveErrorInvalidStudy=1          # from enum swsTemperatureCurveError_e
	swsTemperatureCurveErrorNeedDataPoints=3          # from enum swsTemperatureCurveError_e
	swsTemperatureCurveErrorSuccessful=0          # from enum swsTemperatureCurveError_e
	swsTemperatureEndEditErrorCannotSetInitialTemperatureType=5          # from enum swsTemperatureEndEditError_e
	swsTemperatureEndEditErrorEntityAlreadyExists=2          # from enum swsTemperatureEndEditError_e
	swsTemperatureEndEditErrorNoEntities=3          # from enum swsTemperatureEndEditError_e
	swsTemperatureEndEditErrorNoEntityAtIndex=1          # from enum swsTemperatureEndEditError_e
	swsTemperatureEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies=4          # from enum swsTemperatureEndEditError_e
	swsTemperatureEndEditErrorSuccessful=0          # from enum swsTemperatureEndEditError_e
	swsTemperatureErrorEmptyArray =4          # from enum swsTemperatureError_e
	swsTemperatureErrorInvalidArray=3          # from enum swsTemperatureError_e
	swsTemperatureErrorInvalidStudy=2          # from enum swsTemperatureError_e
	swsTemperatureErrorSelectVerticesEdgesFacesBodiesOrComponents=1          # from enum swsTemperatureError_e
	swsTemperatureErrorSuccessful =0          # from enum swsTemperatureError_e
	swsTemperatureTypeFixed       =1          # from enum swsTemperatureType_e
	swsTemperatureTypeInital      =0          # from enum swsTemperatureType_e
	swsTemperatureUnitCelsius     =2          # from enum swsTemperatureUnit_e
	swsTemperatureUnitFahrenheit  =1          # from enum swsTemperatureUnit_e
	swsTemperatureUnitKelvin      =0          # from enum swsTemperatureUnit_e
	swsTensileStressAreaUnitCentimetersSquared=1          # from enum swsTensileStressAreaUnit_e
	swsTensileStressAreaUnitFeetSquared=4          # from enum swsTensileStressAreaUnit_e
	swsTensileStressAreaUnitInchesSquared=3          # from enum swsTensileStressAreaUnit_e
	swsTensileStressAreaUnitMetersSquared=2          # from enum swsTensileStressAreaUnit_e
	swsTensileStressAreaUnitMillimetersSquared=0          # from enum swsTensileStressAreaUnit_e
	swsThermalComponentGRADN      =4          # from enum swsThermalComponent_e
	swsThermalComponentGRADX      =1          # from enum swsThermalComponent_e
	swsThermalComponentGRADY      =2          # from enum swsThermalComponent_e
	swsThermalComponentGRADZ      =3          # from enum swsThermalComponent_e
	swsThermalComponentHFLUXN     =8          # from enum swsThermalComponent_e
	swsThermalComponentHFLUXX     =5          # from enum swsThermalComponent_e
	swsThermalComponentHFLUXY     =6          # from enum swsThermalComponent_e
	swsThermalComponentHFLUXZ     =7          # from enum swsThermalComponent_e
	swsThermalComponentTEMP       =0          # from enum swsThermalComponent_e
	swsThermalRelaxationFactorAutomatic=0          # from enum swsThermalRelaxationFactor_e
	swsThermalRelaxationFactorFixed=1          # from enum swsThermalRelaxationFactor_e
	swsThermalSolutionTypeSteadyState=1          # from enum swsThermalSolutionType_e
	swsThermalSolutionTypeTransient=0          # from enum swsThermalSolutionType_e
	swsThreadsPerLengthUnitPerInch=1          # from enum swsThreadsPerLengthUnit_e
	swsThreadsPerLengthUnitPerMillimete=0          # from enum swsThreadsPerLengthUnit_e
	swsTimeCurveErrorCannotUseWithRestraint=2          # from enum swsTimeCurveError_e
	swsTimeCurveErrorInvalidDataPoints=4          # from enum swsTimeCurveError_e
	swsTimeCurveErrorInvalidStudyType=1          # from enum swsTimeCurveError_e
	swsTimeCurveErrorNeedTwoOrMoreDataPoints=3          # from enum swsTimeCurveError_e
	swsTimeCurveErrorSuccessful   =0          # from enum swsTimeCurveError_e
	swsUnitSystemIPS              =1          # from enum swsUnitSystem_e
	swsUnitSystemMKS              =2          # from enum swsUnitSystem_e
	swsUnitSystemSI               =0          # from enum swsUnitSystem_e
	swsUnitSystemSIWithMPA        =3          # from enum swsUnitSystem_e
	swsUnitEnglish                =1          # from enum swsUnit_e
	swsUnitMetric                 =2          # from enum swsUnit_e
	swsUnitSI                     =0          # from enum swsUnit_e
	swsWallTypeFlexible           =1          # from enum swsWallType_e
	swsWallTypeRigid              =0          # from enum swsWallType_e

from win32com.client import DispatchBaseClass
class ICWBeamBody(DispatchBaseClass):
	"""Interface for BeamBody"""
	CLSID = IID('{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}')
	coclass_clsid = IID('{EC3DF67D-5D46-45AB-8505-69670841F5BF}')

	def BeamBeginEdit(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def BeamEndEdit(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

	def ConvertToSolidBody(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	# Result is of type ICWMaterial
	def GetBeamBodyMaterial(self):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetBeamBodyMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	# Result is of type ICWMaterial
	def GetDefaultMaterial(self):
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetDefaultMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	def GetManualEnd1ConnectionType(self, BHingeIstDir=pythoncom.Missing, BHinge2ndDir=pythoncom.Missing, BHingeAlongBeam=pythoncom.Missing, BSlide1stDir=pythoncom.Missing
			, BSlide2ndDir=pythoncom.Missing, BSlideAlongBeam=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetManualEnd1ConnectionType', None,BHingeIstDir
			, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam
			)

	def GetManualEnd2ConnectionType(self, BHingeIstDir=pythoncom.Missing, BHinge2ndDir=pythoncom.Missing, BHingeAlongBeam=pythoncom.Missing, BSlide1stDir=pythoncom.Missing
			, BSlide2ndDir=pythoncom.Missing, BSlideAlongBeam=pythoncom.Missing):
		return self._ApplyTypes_(12, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetManualEnd2ConnectionType', None,BHingeIstDir
			, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam
			)

	def SetBeamBodyMaterial(self, RetVal=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((9, 1),),RetVal
			)

	def SetLibraryMaterial(self, SLibWithPathName=defaultNamedNotOptArg, SMaterialName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((8, 1), (8, 1)),SLibWithPathName
			, SMaterialName)

	def SetManualEnd1ConnectionType(self, BHingeIstDir=defaultNamedNotOptArg, BHinge2ndDir=defaultNamedNotOptArg, BHingeAlongBeam=defaultNamedNotOptArg, BSlide1stDir=defaultNamedNotOptArg
			, BSlide2ndDir=defaultNamedNotOptArg, BSlideAlongBeam=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),BHingeIstDir
			, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam
			)

	def SetManualEnd2ConnectionType(self, BHingeIstDir=defaultNamedNotOptArg, BHinge2ndDir=defaultNamedNotOptArg, BHingeAlongBeam=defaultNamedNotOptArg, BSlide1stDir=defaultNamedNotOptArg
			, BSlide2ndDir=defaultNamedNotOptArg, BSlideAlongBeam=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),BHingeIstDir
			, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam
			)

	_prop_map_get_ = {
		"BeamBodyName": (1, 2, (8, 0), (), "BeamBodyName", None),
		"BeamEnd1ConnectionType": (3, 2, (3, 0), (), "BeamEnd1ConnectionType", None),
		"BeamEnd2ConnectionType": (4, 2, (3, 0), (), "BeamEnd2ConnectionType", None),
		"BeamType": (2, 2, (3, 0), (), "BeamType", None),
	}
	_prop_map_put_ = {
		"BeamEnd1ConnectionType": ((3, LCID, 4, 0),()),
		"BeamEnd2ConnectionType": ((4, LCID, 4, 0),()),
		"BeamType": ((2, LCID, 4, 0),()),
	}

class ICWBeamManager(DispatchBaseClass):
	"""Interface for BeamManager"""
	CLSID = IID('{D770D195-0FB7-4771-A269-30BD773D393A}')
	coclass_clsid = IID('{53F66937-4219-456B-89B1-6AF4BD7C022C}')

	# Result is of type ICWBeamBody
	def GetBeamBodyAt(self, NIndex=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		"""method GetBeamBodyAt"""
		return self._ApplyTypes_(2, 1, (9, 0), ((3, 1), (16387, 2)), u'GetBeamBodyAt', '{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}',NIndex
			, ErrorCode)

	# Result is of type ICWJoints
	def GetJointGroup(self, ErrorCode=pythoncom.Missing):
		"""method GetJointGroup"""
		return self._ApplyTypes_(3, 1, (9, 0), ((16387, 2),), u'GetJointGroup', '{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}',ErrorCode
			)

	_prop_map_get_ = {
		"BeamCount": (1, 2, (3, 0), (), "BeamCount", None),
	}
	_prop_map_put_ = {
	}

class ICWBearingLoad(DispatchBaseClass):
	"""Interface for CWBearingLoad"""
	CLSID = IID('{E240A061-9543-4D8A-8749-2C9C850F7035}')
	coclass_clsid = IID('{07C2C408-612E-428F-8FD6-13230EF8D878}')

	def BearingLoadBeginEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def BearingLoadEndEdit(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	def GetEntityCount(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def GetTimeCurve(self):
		return self._ApplyTypes_(11, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def ReplaceCoordinateSystem(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"BearingLoadUnit": (1, 2, (3, 0), (), "BearingLoadUnit", None),
		"Direction": (4, 2, (3, 0), (), "Direction", None),
		"XDirectionValue": (2, 2, (5, 0), (), "XDirectionValue", None),
		"YDirectionValue": (3, 2, (5, 0), (), "YDirectionValue", None),
	}
	_prop_map_put_ = {
		"BearingLoadUnit": ((1, LCID, 4, 0),()),
		"Direction": ((4, LCID, 4, 0),()),
		"XDirectionValue": ((2, LCID, 4, 0),()),
		"YDirectionValue": ((3, LCID, 4, 0),()),
	}

class ICWBoltConnector(DispatchBaseClass):
	"""Interface for CBoltConnector"""
	CLSID = IID('{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}')
	coclass_clsid = IID('{F9A4678F-9919-4435-B903-16A426E87B64}')

	def BoltConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), (),)

	def BoltConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), (),)

	def GetBoltSeriesEntityCount(self):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), (),)

	def GetLibraryMaterial(self, SMaterialLibName=pythoncom.Missing, SMaterialName=pythoncom.Missing):
		return self._ApplyTypes_(30, 1, (24, 0), ((16392, 2), (16392, 2)), u'GetLibraryMaterial', None,SMaterialLibName
			, SMaterialName)

	def GetSourceEntityCount(self):
		return self._oleobj_.InvokeTypes(45, LCID, 1, (3, 0), (),)

	def GetStrengthData(self, DTensileStressArea=pythoncom.Missing, DPinBoltStrength=pythoncom.Missing, DSafetyFactor=pythoncom.Missing):
		return self._ApplyTypes_(32, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2)), u'GetStrengthData', None,DTensileStressArea
			, DPinBoltStrength, DSafetyFactor)

	def GetTargetEntityCount(self):
		return self._oleobj_.InvokeTypes(46, LCID, 1, (3, 0), (),)

	def InsertBoltSeriesEntity(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertEntityAtFirstLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertEntityAtSecondLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertReferenceGeometry(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertTightFitEntity(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def RemoveBoltSeriesEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveEntityAtFirstLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveEntityAtSecondLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveTightFitEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetLibraryMaterial(self, SMaterialLibName=defaultNamedNotOptArg, SMaterialName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((8, 1), (8, 1)),SMaterialLibName
			, SMaterialName)

	def SetStrengthData(self, DTensileStressArea=defaultNamedNotOptArg, DPinBoltStrength=defaultNamedNotOptArg, DSafetyFactor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),DTensileStressArea
			, DPinBoltStrength, DSafetyFactor)

	_prop_map_get_ = {
		"BoltShankDiameterUnit": (5, 2, (3, 0), (), "BoltShankDiameterUnit", None),
		"BoltShankDiameterValue": (18, 2, (5, 0), (), "BoltShankDiameterValue", None),
		"BoltType": (6, 2, (3, 0), (), "BoltType", None),
		"BoltUnit": (1, 2, (3, 0), (), "BoltUnit", None),
		"FrictionValue": (12, 2, (5, 0), (), "FrictionValue", None),
		"HeadDiameterUnit": (3, 2, (3, 0), (), "HeadDiameterUnit", None),
		"HeadDiameterValue": (16, 2, (5, 0), (), "HeadDiameterValue", None),
		"IncludeBoltSeries": (14, 2, (11, 0), (), "IncludeBoltSeries", None),
		"IncludeKnownTensileStressArea": (26, 2, (11, 0), (), "IncludeKnownTensileStressArea", None),
		"IncludeMass": (8, 2, (11, 0), (), "IncludeMass", None),
		"IncludeStrengthData": (25, 2, (11, 0), (), "IncludeStrengthData", None),
		"IncludeSymmetricalBolt": (15, 2, (11, 0), (), "IncludeSymmetricalBolt", None),
		"IncludeTightFit": (9, 2, (11, 0), (), "IncludeTightFit", None),
		"MassValue": (13, 2, (5, 0), (), "MassValue", None),
		"MaterialSource": (21, 2, (3, 0), (), "MaterialSource", None),
		"MaterialType": (7, 2, (3, 0), (), "MaterialType", None),
		"MaterialUnit": (2, 2, (3, 0), (), "MaterialUnit", None),
		"NutDiameterUnit": (4, 2, (3, 0), (), "NutDiameterUnit", None),
		"NutDiameterValue": (17, 2, (5, 0), (), "NutDiameterValue", None),
		"PinBoltStrengthUnit": (29, 2, (3, 0), (), "PinBoltStrengthUnit", None),
		"PoissonsRatio": (23, 2, (5, 0), (), "PoissonsRatio", None),
		"PreLoadForceType": (10, 2, (3, 0), (), "PreLoadForceType", None),
		"PreLoadForceValue": (11, 2, (5, 0), (), "PreLoadForceValue", None),
		"SameHeadAndNutDiameter": (19, 2, (11, 0), (), "SameHeadAndNutDiameter", None),
		"SymmetricalBoltType": (20, 2, (3, 0), (), "SymmetricalBoltType", None),
		"TensileStressAreaUnit": (27, 2, (3, 0), (), "TensileStressAreaUnit", None),
		"ThermalCoefficient": (24, 2, (5, 0), (), "ThermalCoefficient", None),
		"ThreadsPerLengthUnit": (28, 2, (3, 0), (), "ThreadsPerLengthUnit", None),
		"YoungModulus": (22, 2, (5, 0), (), "YoungModulus", None),
	}
	_prop_map_put_ = {
		"BoltShankDiameterUnit": ((5, LCID, 4, 0),()),
		"BoltShankDiameterValue": ((18, LCID, 4, 0),()),
		"BoltType": ((6, LCID, 4, 0),()),
		"BoltUnit": ((1, LCID, 4, 0),()),
		"FrictionValue": ((12, LCID, 4, 0),()),
		"HeadDiameterUnit": ((3, LCID, 4, 0),()),
		"HeadDiameterValue": ((16, LCID, 4, 0),()),
		"IncludeBoltSeries": ((14, LCID, 4, 0),()),
		"IncludeKnownTensileStressArea": ((26, LCID, 4, 0),()),
		"IncludeMass": ((8, LCID, 4, 0),()),
		"IncludeStrengthData": ((25, LCID, 4, 0),()),
		"IncludeSymmetricalBolt": ((15, LCID, 4, 0),()),
		"IncludeTightFit": ((9, LCID, 4, 0),()),
		"MassValue": ((13, LCID, 4, 0),()),
		"MaterialSource": ((21, LCID, 4, 0),()),
		"MaterialType": ((7, LCID, 4, 0),()),
		"MaterialUnit": ((2, LCID, 4, 0),()),
		"NutDiameterUnit": ((4, LCID, 4, 0),()),
		"NutDiameterValue": ((17, LCID, 4, 0),()),
		"PinBoltStrengthUnit": ((29, LCID, 4, 0),()),
		"PoissonsRatio": ((23, LCID, 4, 0),()),
		"PreLoadForceType": ((10, LCID, 4, 0),()),
		"PreLoadForceValue": ((11, LCID, 4, 0),()),
		"SameHeadAndNutDiameter": ((19, LCID, 4, 0),()),
		"SymmetricalBoltType": ((20, LCID, 4, 0),()),
		"TensileStressAreaUnit": ((27, LCID, 4, 0),()),
		"ThermalCoefficient": ((24, LCID, 4, 0),()),
		"ThreadsPerLengthUnit": ((28, LCID, 4, 0),()),
		"YoungModulus": ((22, LCID, 4, 0),()),
	}

class ICWBucklingStudyOptions(DispatchBaseClass):
	"""Interface for BuckingStudyOptions"""
	CLSID = IID('{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}')
	coclass_clsid = IID('{A7FE706C-70D4-49AD-9994-9E7139DE59A7}')

	def GetZeroStrainTemperature(self, DZeroStrainTemperature=pythoncom.Missing, NZeroStrainTemperatureUnit=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (24, 0), ((16389, 2), (16387, 2)), u'GetZeroStrainTemperature', None,DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	def SetZeroStrainTemperature(self, DZeroStrainTemperature=defaultNamedNotOptArg, NZeroStrainTemperatureUnit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((5, 1), (3, 1)),DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	_prop_map_get_ = {
		"BucklingModes": (2, 2, (3, 0), (), "BucklingModes", None),
		"ResultFolder": (4, 2, (8, 0), (), "ResultFolder", None),
		"SolverType": (1, 2, (3, 0), (), "SolverType", None),
		"UseSoftSpring": (3, 2, (3, 0), (), "UseSoftSpring", None),
	}
	_prop_map_put_ = {
		"BucklingModes": ((2, LCID, 4, 0),()),
		"ResultFolder": ((4, LCID, 4, 0),()),
		"SolverType": ((1, LCID, 4, 0),()),
		"UseSoftSpring": ((3, LCID, 4, 0),()),
	}

class ICWCentriFugalForce(DispatchBaseClass):
	"""Interface for CWCentriFugalForce"""
	CLSID = IID('{9F335011-F5A5-4992-AA03-3BEC3BDF0436}')
	coclass_clsid = IID('{61B4C22E-99B9-484D-BF0E-5C9FC1BA3B3A}')

	def CFForceBeginEdit(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def CFForceEndEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def GetTimeCurve(self):
		return self._ApplyTypes_(7, 1, (12, 0), (), u'GetTimeCurve', None,)

	def SetReferenceEntity(self, RefEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),RefEntity
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"AngularAcceleration": (3, 2, (5, 0), (), "AngularAcceleration", None),
		"AngularVelocity": (2, 2, (5, 0), (), "AngularVelocity", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"AngularAcceleration": ((3, LCID, 4, 0),()),
		"AngularVelocity": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWContactComponent(DispatchBaseClass):
	"""Interface for ICWContactComponent"""
	CLSID = IID('{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}')
	coclass_clsid = IID('{A6934603-2339-4B84-A510-E7ADE2AE7320}')

	def ContactComponentBeginEdit(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def ContactComponentEndEdit(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), (),)

	def ReplaceEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def SuppressUnSuppress(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ContactComponentType": (1, 2, (3, 0), (), "ContactComponentType", None),
		"ContactName": (5, 2, (8, 0), (), "ContactName", None),
		"FrictionValue": (4, 2, (5, 0), (), "FrictionValue", None),
		"IncludeFriction": (3, 2, (3, 0), (), "IncludeFriction", None),
		"Option": (2, 2, (3, 0), (), "Option", None),
		"State": (6, 2, (3, 0), (), "State", None),
	}
	_prop_map_put_ = {
		"ContactComponentType": ((1, LCID, 4, 0),()),
		"FrictionValue": ((4, LCID, 4, 0),()),
		"IncludeFriction": ((3, LCID, 4, 0),()),
		"Option": ((2, LCID, 4, 0),()),
	}

class ICWContactManager(DispatchBaseClass):
	"""Interface for ICWContactManager"""
	CLSID = IID('{242B7E91-5A69-4CE1-B429-7008A54F1555}')
	coclass_clsid = IID('{DBFEC66A-A413-4EB3-8A15-8F927274FECF}')

	# Result is of type ICWContactComponent
	def CreateContactComponent(self, NContactType=defaultNamedNotOptArg, NOption=defaultNamedNotOptArg, DispEntity=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(9, 1, (9, 0), ((3, 1), (3, 1), (9, 1), (16387, 2)), u'CreateContactComponent', '{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}',NContactType
			, NOption, DispEntity, ErrorCode)

	# Result is of type ICWContactSet
	def CreateContactSet(self, NContactSetType=defaultNamedNotOptArg, ArraySourceEntities=defaultNamedNotOptArg, ArrayTargetEntities=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (9, 0), ((3, 1), (12, 1), (12, 1), (16387, 2)), u'CreateContactSet', '{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}',NContactSetType
			, ArraySourceEntities, ArrayTargetEntities, ErrorCode)

	# Result is of type ICWContactSet
	def CreateContactSet2(self, NContactSetType=defaultNamedNotOptArg, NSelectionType=defaultNamedNotOptArg, ArraySourceEntities=defaultNamedNotOptArg, ArrayTargetEntities=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (9, 0), ((3, 1), (3, 1), (12, 1), (12, 1), (16387, 2)), u'CreateContactSet2', '{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}',NContactSetType
			, NSelectionType, ArraySourceEntities, ArrayTargetEntities, ErrorCode)

	def DeleteContactComponent(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1),),SName
			)

	def DeleteContactSet(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1),),SName
			)

	# Result is of type ICWContactComponent
	def GetContactComponentAt(self, NIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),NIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetContactComponentAt', '{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}')
		return ret

	# Result is of type ICWContactSet
	def GetContactSetAt(self, NIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((3, 1),),NIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetContactSetAt', '{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}')
		return ret

	def GetGlobalContact(self, NContactType=pythoncom.Missing, NOption=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (24, 0), ((16387, 2), (16387, 2)), u'GetGlobalContact', None,NContactType
			, NOption)

	def SetGlobalContact(self, NContactType=defaultNamedNotOptArg, NOption=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1), (3, 1)),NContactType
			, NOption)

	_prop_map_get_ = {
		"ContactComponentCount": (2, 2, (3, 0), (), "ContactComponentCount", None),
		"ContactSetCount": (1, 2, (3, 0), (), "ContactSetCount", None),
	}
	_prop_map_put_ = {
	}

class ICWContactSet(DispatchBaseClass):
	"""Interface for ICWContactPair"""
	CLSID = IID('{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}')
	coclass_clsid = IID('{AE787538-A050-4BBB-A27E-DB327C00848A}')

	def ContactSetBeginEdit(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def ContactSetEndEdit(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), (),)

	def GetSourceEntityAt(self, NIndex=defaultNamedNotOptArg, nSel=pythoncom.Missing):
		return self._ApplyTypes_(27, 1, (9, 0), ((3, 1), (16387, 2)), u'GetSourceEntityAt', None,NIndex
			, nSel)

	def GetTargetEntityAt(self, NIndex=defaultNamedNotOptArg, nSel=pythoncom.Missing):
		return self._ApplyTypes_(28, 1, (9, 0), ((3, 1), (16387, 2)), u'GetTargetEntityAt', None,NIndex
			, nSel)

	def InsertSourceEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def InsertTargetEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveSourceEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveTargetEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SuppressUnSuppress(self):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AxialStiffnessValue": (11, 2, (5, 0), (), "AxialStiffnessValue", None),
		"ClearanceUnit": (8, 2, (3, 0), (), "ClearanceUnit", None),
		"ClearanceValue": (7, 2, (5, 0), (), "ClearanceValue", None),
		"ContactName": (16, 2, (8, 0), (), "ContactName", None),
		"ContactSetType": (1, 2, (3, 0), (), "ContactSetType", None),
		"FrictionValue": (4, 2, (5, 0), (), "FrictionValue", None),
		"GapType": (6, 2, (3, 0), (), "GapType", None),
		"IncludeFriction": (3, 2, (3, 0), (), "IncludeFriction", None),
		"Options": (2, 2, (3, 0), (), "Options", None),
		"ResistanceType": (13, 2, (3, 0), (), "ResistanceType", None),
		"ResistanceUnit": (15, 2, (3, 0), (), "ResistanceUnit", None),
		"ResistanceValue": (14, 2, (5, 0), (), "ResistanceValue", None),
		"SourceEntityCount": (18, 2, (3, 0), (), "SourceEntityCount", None),
		"State": (17, 2, (3, 0), (), "State", None),
		"TangentialStiffnessValue": (12, 2, (5, 0), (), "TangentialStiffnessValue", None),
		"TargetEntityCount": (19, 2, (3, 0), (), "TargetEntityCount", None),
		"WallFriction": (5, 2, (5, 0), (), "WallFriction", None),
		"WallStiffnessUnit": (10, 2, (3, 0), (), "WallStiffnessUnit", None),
		"WallType": (9, 2, (3, 0), (), "WallType", None),
	}
	_prop_map_put_ = {
		"AxialStiffnessValue": ((11, LCID, 4, 0),()),
		"ClearanceUnit": ((8, LCID, 4, 0),()),
		"ClearanceValue": ((7, LCID, 4, 0),()),
		"ContactSetType": ((1, LCID, 4, 0),()),
		"FrictionValue": ((4, LCID, 4, 0),()),
		"GapType": ((6, LCID, 4, 0),()),
		"IncludeFriction": ((3, LCID, 4, 0),()),
		"Options": ((2, LCID, 4, 0),()),
		"ResistanceType": ((13, LCID, 4, 0),()),
		"ResistanceUnit": ((15, LCID, 4, 0),()),
		"ResistanceValue": ((14, LCID, 4, 0),()),
		"TangentialStiffnessValue": ((12, LCID, 4, 0),()),
		"WallFriction": ((5, LCID, 4, 0),()),
		"WallStiffnessUnit": ((10, LCID, 4, 0),()),
		"WallType": ((9, LCID, 4, 0),()),
	}

class ICWConvection(DispatchBaseClass):
	"""Interface for CWConvection"""
	CLSID = IID('{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}')
	coclass_clsid = IID('{864CF3FA-5753-46F2-9F86-F1CC135F27A0}')

	def ConvectionBeginEdit(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def ConvectionEndEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def GetBulkTemperatureTimeCurve(self):
		return self._ApplyTypes_(13, 1, (12, 0), (), u'GetBulkTemperatureTimeCurve', None,)

	def GetTemperatureCurve(self):
		return self._ApplyTypes_(11, 1, (12, 0), (), u'GetTemperatureCurve', None,)

	def GetTimeCurve(self):
		return self._ApplyTypes_(9, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetBulkTemperatureTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(12, 1, (3, 0), ((12, 1), (16387, 2)), u'SetBulkTemperatureTimeCurve', None,VarCurveData
			, ErrorCode)

	def SetTemperatureCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTemperatureCurve', None,VarCurveData
			, ErrorCode)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"BulkAmbientTemperature": (3, 2, (5, 0), (), "BulkAmbientTemperature", None),
		"ConvectionCoefficient": (2, 2, (5, 0), (), "ConvectionCoefficient", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"UseBulkTemperatureTimeCurve": (16, 2, (3, 0), (), "UseBulkTemperatureTimeCurve", None),
		"UseTemperatureCurve": (15, 2, (3, 0), (), "UseTemperatureCurve", None),
		"UseTimeCurve": (14, 2, (3, 0), (), "UseTimeCurve", None),
	}
	_prop_map_put_ = {
		"BulkAmbientTemperature": ((3, LCID, 4, 0),()),
		"ConvectionCoefficient": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"UseBulkTemperatureTimeCurve": ((16, LCID, 4, 0),()),
		"UseTemperatureCurve": ((15, LCID, 4, 0),()),
		"UseTimeCurve": ((14, LCID, 4, 0),()),
	}

class ICWElasticConnector(DispatchBaseClass):
	"""Interface for CElasticConnector"""
	CLSID = IID('{5A355F90-47EB-4A23-824C-F2379DD92252}')
	coclass_clsid = IID('{55AC868A-F6C1-4DB4-8472-F88F3DB1B05F}')

	def ElasticConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def ElasticConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	def GetEntityCount(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def InsertEntity(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def RemoveEntityAt(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	_prop_map_get_ = {
		"NormalStiffnessValue": (3, 2, (5, 0), (), "NormalStiffnessValue", None),
		"ShearStiffnessValue": (4, 2, (5, 0), (), "ShearStiffnessValue", None),
		"StiffnessType": (2, 2, (3, 0), (), "StiffnessType", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"NormalStiffnessValue": ((3, LCID, 4, 0),()),
		"ShearStiffnessValue": ((4, LCID, 4, 0),()),
		"StiffnessType": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWForce(DispatchBaseClass):
	"""Interface for CWForce"""
	CLSID = IID('{9419308B-BB2A-4842-B652-7AF115171012}')
	coclass_clsid = IID('{D83BBFB8-2E93-4581-B061-D356B67DC5C7}')

	def ForceBeginEdit(self):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), (),)

	def ForceEndEdit(self):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), (),)

	def GetCoordinateSystem(self):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetCoordinateSystem', None)
		return ret

	def GetForceComponentValues(self, B1=pythoncom.Missing, B2=pythoncom.Missing, B3=pythoncom.Missing, D1=pythoncom.Missing
			, D2=pythoncom.Missing, D3=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetForceComponentValues', None,B1
			, B2, B3, D1, D2, D3
			)

	def GetMomentComponentValues(self, B1=pythoncom.Missing, B2=pythoncom.Missing, B3=pythoncom.Missing, D1=pythoncom.Missing
			, D2=pythoncom.Missing, D3=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetMomentComponentValues', None,B1
			, B2, B3, D1, D2, D3
			)

	def GetNonUniformData(self, DConstVal=pythoncom.Missing, DX=pythoncom.Missing, DY=pythoncom.Missing, DXY=pythoncom.Missing
			, DX2=pythoncom.Missing, DY2=pythoncom.Missing):
		return self._ApplyTypes_(9, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetNonUniformData', None,DConstVal
			, DX, DY, DXY, DX2, DY2
			)

	def GetTimeCurve(self):
		return self._ApplyTypes_(14, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetCoordinateSystem(self, DispCoordinateSystem=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((9, 1),),DispCoordinateSystem
			)

	def SetForceComponentValues(self, B1=defaultNamedNotOptArg, B2=defaultNamedNotOptArg, B3=defaultNamedNotOptArg, D1=defaultNamedNotOptArg
			, D2=defaultNamedNotOptArg, D3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),B1
			, B2, B3, D1, D2, D3
			)

	def SetMomentComponentValues(self, B1=defaultNamedNotOptArg, B2=defaultNamedNotOptArg, B3=defaultNamedNotOptArg, D1=defaultNamedNotOptArg
			, D2=defaultNamedNotOptArg, D3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),B1
			, B2, B3, D1, D2, D3
			)

	def SetNonUniformData(self, constVal=defaultNamedNotOptArg, DX=defaultNamedNotOptArg, DY=defaultNamedNotOptArg, DXY=defaultNamedNotOptArg
			, DX2=defaultNamedNotOptArg, DY2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (5, 1)),constVal
			, DX, DY, DXY, DX2, DY2
			)

	def SetReferenceGeometry(self, RefEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((9, 1),),RefEntity
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"ForceType": (3, 2, (3, 0), (), "ForceType", None),
		"IncludeNonUniformDistribution": (4, 2, (3, 0), (), "IncludeNonUniformDistribution", None),
		"NormalForceOrTorqueValue": (2, 2, (5, 0), (), "NormalForceOrTorqueValue", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"ForceType": ((3, LCID, 4, 0),()),
		"IncludeNonUniformDistribution": ((4, LCID, 4, 0),()),
		"NormalForceOrTorqueValue": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWFrequencyStudyOptions(DispatchBaseClass):
	"""Interface for FrequencyStudyOptions"""
	CLSID = IID('{268D40CF-565F-4259-B009-BAC3F5DA8F60}')
	coclass_clsid = IID('{E399CE1B-28ED-48A3-A86E-A797C6556E43}')

	def GetZeroStrainTemperature(self, DZeroStrainTemperature=pythoncom.Missing, NZeroStrainTemperatureUnit=pythoncom.Missing):
		return self._ApplyTypes_(9, 1, (24, 0), ((16389, 2), (16387, 2)), u'GetZeroStrainTemperature', None,DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	def SetZeroStrainTemperature(self, DZeroStrainTemperature=defaultNamedNotOptArg, NZeroStrainTemperatureUnit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((5, 1), (3, 1)),DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	_prop_map_get_ = {
		"LowerBoundFrequency": (4, 2, (3, 0), (), "LowerBoundFrequency", None),
		"NoOfFrequencies": (3, 2, (3, 0), (), "NoOfFrequencies", None),
		"Options": (2, 2, (3, 0), (), "Options", None),
		"ResultFolder": (8, 2, (8, 0), (), "ResultFolder", None),
		"SolverType": (1, 2, (3, 0), (), "SolverType", None),
		"UpperBoundFrequency": (5, 2, (3, 0), (), "UpperBoundFrequency", None),
		"UseLowerBoundFrequency": (7, 2, (3, 0), (), "UseLowerBoundFrequency", None),
		"UseSoftSpring": (6, 2, (3, 0), (), "UseSoftSpring", None),
	}
	_prop_map_put_ = {
		"LowerBoundFrequency": ((4, LCID, 4, 0),()),
		"NoOfFrequencies": ((3, LCID, 4, 0),()),
		"Options": ((2, LCID, 4, 0),()),
		"ResultFolder": ((8, LCID, 4, 0),()),
		"SolverType": ((1, LCID, 4, 0),()),
		"UpperBoundFrequency": ((5, LCID, 4, 0),()),
		"UseLowerBoundFrequency": ((7, LCID, 4, 0),()),
		"UseSoftSpring": ((6, LCID, 4, 0),()),
	}

class ICWGravity(DispatchBaseClass):
	"""Interface for CWGravity"""
	CLSID = IID('{F932F397-D186-4381-88EF-EAA92E2ADCAE}')
	coclass_clsid = IID('{807A0872-ACA1-43A7-86F6-6D07B1989262}')

	def GetGravitationalAcclerationValues(self, DVal1=pythoncom.Missing, DVal2=pythoncom.Missing, DVal3=pythoncom.Missing):
		return self._ApplyTypes_(2, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2)), u'GetGravitationalAcclerationValues', None,DVal1
			, DVal2, DVal3)

	def GetTimeCurve(self):
		return self._ApplyTypes_(7, 1, (12, 0), (), u'GetTimeCurve', None,)

	def GravityBeginEdit(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def GravityEndEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def SetGravitationalAcclerationValues(self, DVal1=defaultNamedNotOptArg, DVal2=defaultNamedNotOptArg, DVal3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),DVal1
			, DVal2, DVal3)

	def SetReferenceEntity(self, RefEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),RefEntity
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWHeatFlux(DispatchBaseClass):
	"""Interface for CWHeatFlux"""
	CLSID = IID('{D77721DD-8FE5-45EB-92B6-FC8106968473}')
	coclass_clsid = IID('{7EBC954D-4620-418D-8740-58D288545A34}')

	def GetCutOffTemperatures(self, DVal1=pythoncom.Missing, DVal2=pythoncom.Missing):
		return self._ApplyTypes_(15, 1, (24, 0), ((16389, 2), (16389, 2)), u'GetCutOffTemperatures', None,DVal1
			, DVal2)

	def GetTemperatureCurve(self):
		return self._ApplyTypes_(11, 1, (12, 0), (), u'GetTemperatureCurve', None,)

	def GetThermostat(self):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetThermostat', None)
		return ret

	def GetTimeCurve(self):
		return self._ApplyTypes_(9, 1, (12, 0), (), u'GetTimeCurve', None,)

	def HeatFluxBeginEdit(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def HeatFluxEndEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetCutOffTemperatures(self, DVal1=defaultNamedNotOptArg, DVal2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((5, 1), (5, 1)),DVal1
			, DVal2)

	def SetTemperatureCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTemperatureCurve', None,VarCurveData
			, ErrorCode)

	def SetThermostat(self, DispCoord=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),DispCoord
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"HFValue": (2, 2, (5, 0), (), "HFValue", None),
		"IncludeThermostat": (3, 2, (3, 0), (), "IncludeThermostat", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"UseTemperatureCurve": (17, 2, (3, 0), (), "UseTemperatureCurve", None),
		"UseTimeCurve": (16, 2, (3, 0), (), "UseTimeCurve", None),
	}
	_prop_map_put_ = {
		"HFValue": ((2, LCID, 4, 0),()),
		"IncludeThermostat": ((3, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"UseTemperatureCurve": ((17, LCID, 4, 0),()),
		"UseTimeCurve": ((16, LCID, 4, 0),()),
	}

class ICWHeatPower(DispatchBaseClass):
	"""Interface for CWHeatPower"""
	CLSID = IID('{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}')
	coclass_clsid = IID('{F66EE586-499C-424B-A547-F51337C6D6C3}')

	def GetCutOffTemperatures(self, DVal1=pythoncom.Missing, DVal2=pythoncom.Missing):
		return self._ApplyTypes_(15, 1, (24, 0), ((16389, 2), (16389, 2)), u'GetCutOffTemperatures', None,DVal1
			, DVal2)

	def GetTemperatureCurve(self):
		return self._ApplyTypes_(11, 1, (12, 0), (), u'GetTemperatureCurve', None,)

	def GetThermostat(self):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetThermostat', None)
		return ret

	def GetTimeCurve(self):
		return self._ApplyTypes_(9, 1, (12, 0), (), u'GetTimeCurve', None,)

	def HeatPowerBeginEdit(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def HeatPowerEndEdit(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetCutOffTemperatures(self, DVal1=defaultNamedNotOptArg, DVal2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((5, 1), (5, 1)),DVal1
			, DVal2)

	def SetTemperatureCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTemperatureCurve', None,VarCurveData
			, ErrorCode)

	def SetThermostat(self, DispVertex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),DispVertex
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"HPValue": (2, 2, (5, 0), (), "HPValue", None),
		"IncludeThermostat": (3, 2, (3, 0), (), "IncludeThermostat", None),
		"ThermostatUnits": (18, 2, (3, 0), (), "ThermostatUnits", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"UseTemperatureCurve": (17, 2, (3, 0), (), "UseTemperatureCurve", None),
		"UseTimeCurve": (16, 2, (3, 0), (), "UseTimeCurve", None),
	}
	_prop_map_put_ = {
		"HPValue": ((2, LCID, 4, 0),()),
		"IncludeThermostat": ((3, LCID, 4, 0),()),
		"ThermostatUnits": ((18, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"UseTemperatureCurve": ((17, LCID, 4, 0),()),
		"UseTimeCurve": ((16, LCID, 4, 0),()),
	}

class ICWJoints(DispatchBaseClass):
	"""Interface for Joints"""
	CLSID = IID('{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}')
	coclass_clsid = IID('{C2C96FB8-EAE7-4BE3-9DFF-D7B3D2A37A0F}')

	def CalculateJoints(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def DeleteJoint(self, pDisp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((9, 1),),pDisp
			)

	def InsertBeamEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def JointsBeginEdit(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def JointsEndEdit(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	def RemoveBeamEntityAt(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	_prop_map_get_ = {
		"IncludeAllSelectedBeam": (1, 2, (11, 0), (), "IncludeAllSelectedBeam", None),
		"IncludeDisplayNeutralAxis": (5, 2, (11, 0), (), "IncludeDisplayNeutralAxis", None),
		"IncludeKeepModifiedJointOnUpdate": (6, 2, (11, 0), (), "IncludeKeepModifiedJointOnUpdate", None),
		"IncludeTreatAsJointForClearanceLessThan": (7, 2, (11, 0), (), "IncludeTreatAsJointForClearanceLessThan", None),
		"IncludeUserSelectedBeam": (2, 2, (11, 0), (), "IncludeUserSelectedBeam", None),
		"PinBallRadius": (4, 2, (5, 0), (), "PinBallRadius", None),
		"PinBallRadiusUnit": (3, 2, (3, 0), (), "PinBallRadiusUnit", None),
	}
	_prop_map_put_ = {
		"IncludeAllSelectedBeam": ((1, LCID, 4, 0),()),
		"IncludeDisplayNeutralAxis": ((5, LCID, 4, 0),()),
		"IncludeKeepModifiedJointOnUpdate": ((6, LCID, 4, 0),()),
		"IncludeTreatAsJointForClearanceLessThan": ((7, LCID, 4, 0),()),
		"IncludeUserSelectedBeam": ((2, LCID, 4, 0),()),
		"PinBallRadius": ((4, LCID, 4, 0),()),
		"PinBallRadiusUnit": ((3, LCID, 4, 0),()),
	}

class ICWLinkConnector(DispatchBaseClass):
	"""Interface for CLinkConnector"""
	CLSID = IID('{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}')
	coclass_clsid = IID('{19951FA7-A7F4-41C0-964A-0F79FA2A5D99}')

	def LinkConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def LinkConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def ReplaceEntityAtFirstLocation(self, pDisp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((9, 1),),pDisp
			)

	def ReplaceEntityAtSecondLocation(self, pDisp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),pDisp
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class ICWLoadsAndRestraints(DispatchBaseClass):
	"""Interface for CWLoadsAndRestraints"""
	CLSID = IID('{7BDD45B4-9046-4C42-8936-A988906D2597}')
	coclass_clsid = IID('{12FE135D-F7ED-41C7-9A15-42556526A9A9}')

	def GetEntityAt(self, NIndex=defaultNamedNotOptArg, NSelType=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (9, 0), ((3, 1), (16387, 2)), u'GetEntityAt', None,NIndex
			, NSelType)

	def GetReferenceGeometry(self, NSelType=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (9, 0), ((16387, 2),), u'GetReferenceGeometry', None,NSelType
			)

	def SuppressUnSuppress(self):
		"""SuppressUnSuppress"""
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"EntityCount": (4, 2, (3, 0), (), "EntityCount", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"State": (3, 2, (3, 0), (), "State", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}

class ICWLoadsAndRestraintsManager(DispatchBaseClass):
	"""Interface for LoadsAndRestraintsManager"""
	CLSID = IID('{9DEA3C90-44BB-45E0-A569-F4B196F47176}')
	coclass_clsid = IID('{4425FB13-4541-4079-820E-0B4AC73E5231}')

	# Result is of type ICWBearingLoad
	def AddBearingLoad(self, CoordinateSystem=defaultNamedNotOptArg, FirstFace=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), ((9, 1), (12, 1), (16387, 0)),CoordinateSystem
			, FirstFace, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddBearingLoad', '{E240A061-9543-4D8A-8749-2C9C850F7035}')
		return ret

	# Result is of type ICWBoltConnector
	def AddBoltConnector(self, nBoltType=defaultNamedNotOptArg, DispArrayBoltHead=defaultNamedNotOptArg, DispArrayBoltNut=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1), (12, 1), (12, 1), (16387, 0)),nBoltType
			, DispArrayBoltHead, DispArrayBoltNut, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddBoltConnector', '{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}')
		return ret

	# Result is of type ICWCentriFugalForce
	def AddCentrifugalForce(self, DispEntity=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (9, 0), ((9, 1), (16387, 2)), u'AddCentrifugalForce', '{9F335011-F5A5-4992-AA03-3BEC3BDF0436}',DispEntity
			, ErrorCode)

	# Result is of type ICWConvection
	def AddConvection(self, DispArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (9, 0), ((12, 1), (16387, 2)), u'AddConvection', '{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}',DispArray
			, ErrorCode)

	# Result is of type ICWElasticConnector
	def AddElasticConnector(self, DispArray=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((12, 1), (16387, 0)),DispArray
			, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddElasticConnector', '{5A355F90-47EB-4A23-824C-F2379DD92252}')
		return ret

	# Result is of type ICWForce
	def AddForce(self, NForceType=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, RefGeom=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (9, 0), ((3, 1), (12, 1), (9, 1), (16387, 2)), u'AddForce', '{9419308B-BB2A-4842-B652-7AF115171012}',NForceType
			, DispArray, RefGeom, ErrorCode)

	# Result is of type ICWForce
	def AddForce2(self, NForceType=defaultNamedNotOptArg, NSelectionType=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, RefGeom=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (9, 0), ((3, 1), (3, 1), (12, 1), (9, 1), (16387, 2)), u'AddForce2', '{9419308B-BB2A-4842-B652-7AF115171012}',NForceType
			, NSelectionType, DispArray, RefGeom, ErrorCode)

	# Result is of type ICWForce
	def AddForce3(self, ForceType=defaultNamedNotOptArg, SelectionType=defaultNamedNotOptArg, RefDirType=defaultNamedNotOptArg, InterpolationMode=defaultNamedNotOptArg
			, DistPercentageOpt=defaultNamedNotOptArg, NumOfRows=defaultNamedNotOptArg, DistValue=defaultNamedNotOptArg, ForceValue=defaultNamedNotOptArg, NonUniformLoading=defaultNamedNotOptArg
			, NULoadingOnBeam=defaultNamedNotOptArg, NonUniformLoadDistDef=defaultNamedNotOptArg, NonUniformLoadDistType=defaultNamedNotOptArg, Ucode=defaultNamedNotOptArg, TorqueNFVal=defaultNamedNotOptArg
			, Comps=defaultNamedNotOptArg, FlipOrigin=defaultNamedNotOptArg, IsCurvedBeam=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, RefGeom=defaultNamedNotOptArg
			, PerUnitLength=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(23, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (12, 1), (12, 1), (11, 1), (11, 1), (3, 1), (3, 1), (3, 1), (5, 1), (12, 1), (11, 1), (11, 1), (12, 1), (9, 1), (11, 1), (16387, 2)), u'AddForce3', '{9419308B-BB2A-4842-B652-7AF115171012}',ForceType
			, SelectionType, RefDirType, InterpolationMode, DistPercentageOpt, NumOfRows
			, DistValue, ForceValue, NonUniformLoading, NULoadingOnBeam, NonUniformLoadDistDef
			, NonUniformLoadDistType, Ucode, TorqueNFVal, Comps, FlipOrigin
			, IsCurvedBeam, DispArray, RefGeom, PerUnitLength, ErrorCode
			)

	# Result is of type ICWGravity
	def AddGravity(self, DispEntity=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (9, 0), ((9, 1), (16387, 2)), u'AddGravity', '{F932F397-D186-4381-88EF-EAA92E2ADCAE}',DispEntity
			, ErrorCode)

	# Result is of type ICWHeatFlux
	def AddHeatFlux(self, DispArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(11, 1, (9, 0), ((12, 1), (16387, 2)), u'AddHeatFlux', '{D77721DD-8FE5-45EB-92B6-FC8106968473}',DispArray
			, ErrorCode)

	# Result is of type ICWHeatPower
	def AddHeatPower(self, DispArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(12, 1, (9, 0), ((12, 1), (16387, 2)), u'AddHeatPower', '{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}',DispArray
			, ErrorCode)

	# Result is of type ICWLinkConnector
	def AddLinkConnector(self, VertexPointforFirstLocation=defaultNamedNotOptArg, VertexPointforSecondLocation=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(16, 1, (9, 0), ((9, 1), (9, 1), (16387, 2)), u'AddLinkConnector', '{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}',VertexPointforFirstLocation
			, VertexPointforSecondLocation, ErrorCode)

	# Result is of type ICWPinConnector
	def AddPinConnector(self, DispArrayComp1=defaultNamedNotOptArg, DispArrayComp2=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((12, 1), (12, 1), (16387, 0)),DispArrayComp1
			, DispArrayComp2, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddPinConnector', '{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}')
		return ret

	# Result is of type ICWPressure
	def AddPressure(self, NPressureType=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, RegGeom=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(4, 1, (9, 0), ((3, 1), (12, 1), (9, 1), (16387, 2)), u'AddPressure', '{3D12186F-4CAE-4511-9456-B42FB68F06F9}',NPressureType
			, DispArray, RegGeom, ErrorCode)

	# Result is of type ICWRadiation
	def AddRadiation(self, NRadType=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (9, 0), ((3, 1), (12, 1), (16387, 2)), u'AddRadiation', '{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}',NRadType
			, DispArray, ErrorCode)

	# Result is of type ICWRestraint
	def AddRestraint(self, NRestraintType=defaultNamedNotOptArg, DispArray=defaultNamedNotOptArg, RefGeom=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(3, 1, (9, 0), ((3, 1), (12, 1), (9, 1), (16387, 2)), u'AddRestraint', '{A1B7607C-2C6B-447B-8183-633531BFDDAF}',NRestraintType
			, DispArray, RefGeom, ErrorCode)

	# Result is of type ICWRigidConnector
	def AddRigidConnector(self, persistIDFaceArray=defaultNamedNotOptArg, persistIDTargetArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(15, 1, (9, 0), ((12, 1), (12, 1), (16387, 2)), u'AddRigidConnector', '{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}',persistIDFaceArray
			, persistIDTargetArray, ErrorCode)

	# Result is of type ICWSpotWeldConnector
	def AddSpotWeldConnector(self, FirstFace=defaultNamedNotOptArg, SecondFace=defaultNamedNotOptArg, DispArrayWeldLocations=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), ((9, 1), (9, 1), (12, 1), (16387, 0)),FirstFace
			, SecondFace, DispArrayWeldLocations, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddSpotWeldConnector', '{756B2585-6350-460A-9C2A-7F25DA9D094A}')
		return ret

	# Result is of type ICWSpringConnector
	def AddSpringConnector(self, NSpringSubType=defaultNamedNotOptArg, DispArrayComp1=defaultNamedNotOptArg, DispArrayComp2=defaultNamedNotOptArg, ErrorCode=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((3, 1), (12, 1), (12, 1), (16387, 0)),NSpringSubType
			, DispArrayComp1, DispArrayComp2, ErrorCode)
		if ret is not None:
			ret = Dispatch(ret, u'AddSpringConnector', '{96DD49CD-CC09-4FAE-A559-7A795983D6EB}')
		return ret

	# Result is of type ICWTemperature
	def AddTemperature(self, DispArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(9, 1, (9, 0), ((12, 1), (16387, 2)), u'AddTemperature', '{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}',DispArray
			, ErrorCode)

	def DeleteLoadsAndRestraints(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1),),SName
			)

	# Result is of type ICWLoadsAndRestraints
	def GetLoadsAndRestraints(self, NIndex=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		"""method GetLoadsAndRestraints"""
		return self._ApplyTypes_(2, 1, (9, 0), ((3, 1), (16387, 2)), u'GetLoadsAndRestraints', '{7BDD45B4-9046-4C42-8936-A988906D2597}',NIndex
			, ErrorCode)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ICWMaterial(DispatchBaseClass):
	"""Interface for CWMaterial"""
	CLSID = IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
	coclass_clsid = IID('{675024F4-3BEB-465F-9747-50CDB6E6FD43}')

	def GetAustenticSteelCurve(self):
		return self._ApplyTypes_(26, 1, (12, 0), (), u'GetAustenticSteelCurve', None,)

	def GetCarbonSteelCurve(self):
		return self._ApplyTypes_(27, 1, (12, 0), (), u'GetCarbonSteelCurve', None,)

	def GetFatigueSNCurve(self, NIndex=defaultNamedNotOptArg, DStressRatio=pythoncom.Missing):
		return self._ApplyTypes_(17, 1, (12, 0), ((3, 1), (16389, 2)), u'GetFatigueSNCurve', None,NIndex
			, DStressRatio)

	def GetMaterialDataCurve(self, NIndex=defaultNamedNotOptArg, BUseCurve=pythoncom.Missing):
		return self._ApplyTypes_(21, 1, (12, 0), ((3, 1), (16387, 2)), u'GetMaterialDataCurve', None,NIndex
			, BUseCurve)

	def GetPropertyByName(self, nUnit=defaultNamedNotOptArg, SName=defaultNamedNotOptArg, BTempDependent=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (5, 0), ((3, 1), (8, 1), (16387, 2)), u'GetPropertyByName', None,nUnit
			, SName, BTempDependent)

	def GetReferencePlaneName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(23, LCID, 1, (8, 0), (),)

	def GetStressStrainCurve(self):
		return self._ApplyTypes_(19, 1, (12, 0), (), u'GetStressStrainCurve', None,)

	def GetTemperatureCurveForProperty(self, SPropName=defaultNamedNotOptArg):
		return self._ApplyTypes_(15, 1, (12, 0), ((8, 1),), u'GetTemperatureCurveForProperty', None,SPropName
			)

	def SetFatigueSNCurve(self, NIndex=defaultNamedNotOptArg, DStressRatio=defaultNamedNotOptArg, VarFatigueSNCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(18, 1, (24, 0), ((3, 1), (5, 1), (12, 1), (16387, 2)), u'SetFatigueSNCurve', None,NIndex
			, DStressRatio, VarFatigueSNCurveData, ErrorCode)

	def SetMaterialDataCurve(self, NIndex=defaultNamedNotOptArg, BUseCurve=defaultNamedNotOptArg, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(22, 1, (24, 0), ((3, 1), (3, 1), (12, 1), (16387, 2)), u'SetMaterialDataCurve', None,NIndex
			, BUseCurve, VarCurveData, ErrorCode)

	def SetPropertyByName(self, SName=defaultNamedNotOptArg, DValue=defaultNamedNotOptArg, BValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1), (5, 1), (3, 1)),SName
			, DValue, BValue)

	def SetReferencePlane(self, PlaneDisp=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(24, 1, (24, 0), ((9, 1), (16387, 2)), u'SetReferencePlane', None,PlaneDisp
			, ErrorCode)

	def SetStressStrainCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(20, 1, (24, 0), ((12, 1), (16387, 2)), u'SetStressStrainCurve', None,VarCurveData
			, ErrorCode)

	def SetTemperatureCurveForProperty(self, SPropName=defaultNamedNotOptArg, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(16, 1, (24, 0), ((8, 1), (12, 1), (16387, 2)), u'SetTemperatureCurveForProperty', None,SPropName
			, VarCurveData, ErrorCode)

	_prop_map_get_ = {
		"Category": (5, 2, (8, 0), (), "Category", None),
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Description": (7, 2, (8, 0), (), "Description", None),
		"IncludeCreep": (8, 2, (3, 0), (), "IncludeCreep", None),
		"MaterialName": (6, 2, (8, 0), (), "MaterialName", None),
		"MaterialUnits": (3, 2, (3, 0), (), "MaterialUnits", None),
		"ModelType": (4, 2, (3, 0), (), "ModelType", None),
		"MooneyRivlinConstants": (9, 2, (3, 0), (), "MooneyRivlinConstants", None),
		"NoOfBulkModuli": (12, 2, (3, 0), (), "NoOfBulkModuli", None),
		"NoOfShearModuli": (11, 2, (3, 0), (), "NoOfShearModuli", None),
		"OgdenConstants": (10, 2, (3, 0), (), "OgdenConstants", None),
		"SNCurveSource": (25, 2, (3, 0), (), "SNCurveSource", None),
		"Source": (2, 2, (3, 0), (), "Source", None),
	}
	_prop_map_put_ = {
		"Category": ((5, LCID, 4, 0),()),
		"Description": ((7, LCID, 4, 0),()),
		"IncludeCreep": ((8, LCID, 4, 0),()),
		"MaterialName": ((6, LCID, 4, 0),()),
		"MaterialUnits": ((3, LCID, 4, 0),()),
		"ModelType": ((4, LCID, 4, 0),()),
		"MooneyRivlinConstants": ((9, LCID, 4, 0),()),
		"NoOfBulkModuli": ((12, LCID, 4, 0),()),
		"NoOfShearModuli": ((11, LCID, 4, 0),()),
		"OgdenConstants": ((10, LCID, 4, 0),()),
		"SNCurveSource": ((25, LCID, 4, 0),()),
	}
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ICWMesh(DispatchBaseClass):
	"""Interface for CWMesh"""
	CLSID = IID('{F5818CF4-0C05-49AC-997F-8A0DB432203B}')
	coclass_clsid = IID('{0844A890-EB4C-434E-BECB-91374A38C531}')

	# Result is of type ICWMeshControl
	def ApplyMeshControl(self, EntitiesArray=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(28, 1, (9, 0), ((12, 1), (16387, 2)), u'ApplyMeshControl', '{270F9491-0450-4BB5-BEF5-6E520C01D9AF}',EntitiesArray
			, ErrorCode)

	def DeleteMeshControl(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((8, 1),),SName
			)

	def FlipShellElements(self, DispFaceArray=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (3, 0), ((12, 1),),DispFaceArray
			)

	def GetDefaultElementSizeAndTolerance(self, NUnits=defaultNamedNotOptArg, DElementSize=pythoncom.Missing, DTolerance=pythoncom.Missing):
		return self._ApplyTypes_(40, 1, (24, 0), ((3, 1), (16389, 2), (16389, 2)), u'GetDefaultElementSizeAndTolerance', None,NUnits
			, DElementSize, DTolerance)

	def GetDefaultMaxAndMinElementSize(self, NUnits=defaultNamedNotOptArg, DMaxElementSize=pythoncom.Missing, DMinElementSize=pythoncom.Missing):
		return self._ApplyTypes_(43, 1, (24, 0), ((3, 1), (16389, 2), (16389, 2)), u'GetDefaultMaxAndMinElementSize', None,NUnits
			, DMaxElementSize, DMinElementSize)

	def GetElementDataFromEntity(self, DispEntity=defaultNamedNotOptArg, NCount=pythoncom.Missing):
		return self._ApplyTypes_(32, 1, (12, 0), ((9, 1), (16387, 2)), u'GetElementDataFromEntity', None,DispEntity
			, NCount)

	def GetElementLocation(self, NNodeNo=defaultNamedNotOptArg, XVal=pythoncom.Missing, YVal=pythoncom.Missing, ZVal=pythoncom.Missing):
		return self._ApplyTypes_(42, 1, (3, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2)), u'GetElementLocation', None,NNodeNo
			, XVal, YVal, ZVal)

	def GetElements(self):
		return self._ApplyTypes_(27, 1, (12, 0), (), u'GetElements', None,)

	def GetFailedComponents(self, NComp=pythoncom.Missing):
		return self._ApplyTypes_(38, 1, (12, 0), ((16387, 2),), u'GetFailedComponents', None,NComp
			)

	def GetFailedEdges(self, NFailedEdges=pythoncom.Missing):
		return self._ApplyTypes_(36, 1, (12, 0), ((16387, 2),), u'GetFailedEdges', None,NFailedEdges
			)

	def GetFailedFaces(self, NFailedFaces=pythoncom.Missing):
		return self._ApplyTypes_(35, 1, (12, 0), ((16387, 2),), u'GetFailedFaces', None,NFailedFaces
			)

	# Result is of type ICWMeshControl
	def GetMeshControlAt(self, NIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(37, LCID, 1, (9, 0), ((3, 1),),NIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetMeshControlAt', '{270F9491-0450-4BB5-BEF5-6E520C01D9AF}')
		return ret

	def GetNoOfFailedComponents(self):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), (),)

	def GetNodeDataFromEntity(self, DispEntity=defaultNamedNotOptArg, NCount=pythoncom.Missing):
		return self._ApplyTypes_(31, 1, (12, 0), ((9, 1), (16387, 2)), u'GetNodeDataFromEntity', None,DispEntity
			, NCount)

	def GetNodeLocation(self, NNodeNo=defaultNamedNotOptArg, XVal=pythoncom.Missing, YVal=pythoncom.Missing, ZVal=pythoncom.Missing):
		return self._ApplyTypes_(41, 1, (3, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2)), u'GetNodeLocation', None,NNodeNo
			, XVal, YVal, ZVal)

	def GetNodes(self):
		return self._ApplyTypes_(26, 1, (12, 0), (), u'GetNodes', None,)

	def GetShellElementNormalAt(self, DispFace=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), ((9, 1),),DispFace
			)

	def IsComponentFailed(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), ((8, 1),),SName
			)

	_prop_map_get_ = {
		"AutomaticLooping": (6, 2, (3, 0), (), "AutomaticLooping", None),
		"AutomaticTransition": (4, 2, (3, 0), (), "AutomaticTransition", None),
		"ElementCount": (14, 2, (3, 0), (), "ElementCount", None),
		"ElementSize": (20, 2, (5, 0), (), "ElementSize", None),
		"ElementSizeFactorForEachLoop": (8, 2, (5, 0), (), "ElementSizeFactorForEachLoop", None),
		"GrowthRatio": (22, 2, (5, 0), (), "GrowthRatio", None),
		"IsMeshFailed": (18, 2, (3, 0), (), "IsMeshFailed", None),
		"MaxAspectRatio": (16, 2, (5, 0), (), "MaxAspectRatio", None),
		"MaxElementSize": (24, 2, (5, 0), (), "MaxElementSize", None),
		"MeshControlCount": (19, 2, (3, 0), (), "MeshControlCount", None),
		"MeshState": (2, 2, (3, 0), (), "MeshState", None),
		"MeshType": (1, 2, (3, 0), (), "MeshType", None),
		"MesherType": (10, 2, (3, 0), (), "MesherType", None),
		"MinElementSize": (25, 2, (5, 0), (), "MinElementSize", None),
		"MinElementsInCircle": (15, 2, (3, 0), (), "MinElementsInCircle", None),
		"NodeCount": (13, 2, (3, 0), (), "NodeCount", None),
		"NumberOfLoops": (7, 2, (3, 0), (), "NumberOfLoops", None),
		"Quality": (3, 2, (3, 0), (), "Quality", None),
		"SmoothSurface": (5, 2, (3, 0), (), "SmoothSurface", None),
		"TimeToCompleteMesh": (17, 2, (3, 0), (), "TimeToCompleteMesh", None),
		"Tolerance": (21, 2, (5, 0), (), "Tolerance", None),
		"ToleranceFactorForEachLoop": (9, 2, (5, 0), (), "ToleranceFactorForEachLoop", None),
		"Unit": (23, 2, (3, 0), (), "Unit", None),
		"UseJacobianCheckForShells": (12, 2, (3, 0), (), "UseJacobianCheckForShells", None),
		"UseJacobianCheckForSolids": (11, 2, (3, 0), (), "UseJacobianCheckForSolids", None),
	}
	_prop_map_put_ = {
		"AutomaticLooping": ((6, LCID, 4, 0),()),
		"AutomaticTransition": ((4, LCID, 4, 0),()),
		"ElementSizeFactorForEachLoop": ((8, LCID, 4, 0),()),
		"GrowthRatio": ((22, LCID, 4, 0),()),
		"MesherType": ((10, LCID, 4, 0),()),
		"MinElementsInCircle": ((15, LCID, 4, 0),()),
		"NumberOfLoops": ((7, LCID, 4, 0),()),
		"Quality": ((3, LCID, 4, 0),()),
		"SmoothSurface": ((5, LCID, 4, 0),()),
		"ToleranceFactorForEachLoop": ((9, LCID, 4, 0),()),
		"UseJacobianCheckForShells": ((12, LCID, 4, 0),()),
		"UseJacobianCheckForSolids": ((11, LCID, 4, 0),()),
	}

class ICWMeshControl(DispatchBaseClass):
	"""Interface for ICWMeshControl"""
	CLSID = IID('{270F9491-0450-4BB5-BEF5-6E520C01D9AF}')
	coclass_clsid = IID('{96212552-8F0F-47F9-BC8F-C712081CAAD2}')

	def GetEntityAt(self, NIndex=defaultNamedNotOptArg, NSelectionType=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (9, 0), ((3, 1), (16387, 2)), u'GetEntityAt', None,NIndex
			, NSelectionType)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def MeshControlBeginEdit(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def MeshControlEndEdit(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SuppressUnSuppress(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ElementSize": (1, 2, (5, 0), (), "ElementSize", None),
		"EntityCount": (7, 2, (3, 0), (), "EntityCount", None),
		"Layers": (3, 2, (3, 0), (), "Layers", None),
		"Name": (8, 2, (8, 0), (), "Name", None),
		"NumofElementsforBeams": (16, 2, (3, 0), (), "NumofElementsforBeams", None),
		"Ratio": (2, 2, (5, 0), (), "Ratio", None),
		"State": (15, 2, (3, 0), (), "State", None),
		"Units": (4, 2, (3, 0), (), "Units", None),
		"UseSameElementSize": (5, 2, (3, 0), (), "UseSameElementSize", None),
		"WeightFactor": (6, 2, (5, 0), (), "WeightFactor", None),
	}
	_prop_map_put_ = {
		"ElementSize": ((1, LCID, 4, 0),()),
		"Layers": ((3, LCID, 4, 0),()),
		"NumofElementsforBeams": ((16, LCID, 4, 0),()),
		"Ratio": ((2, LCID, 4, 0),()),
		"Units": ((4, LCID, 4, 0),()),
		"UseSameElementSize": ((5, LCID, 4, 0),()),
		"WeightFactor": ((6, LCID, 4, 0),()),
	}

class ICWModelDoc(DispatchBaseClass):
	"""Interface for CWModelDoc"""
	CLSID = IID('{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}')
	coclass_clsid = IID('{EAFBFF38-E6B9-43D7-BE10-FE2BF2C8C0C8}')

	_prop_map_get_ = {
		"DefaultUnitSystem": (2, 2, (3, 0), (), "DefaultUnitSystem", None),
		# Method 'StudyManager' returns object of type 'ICWStudyManager'
		"StudyManager": (1, 2, (9, 0), (), "StudyManager", '{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}'),
	}
	_prop_map_put_ = {
		"DefaultUnitSystem": ((2, LCID, 4, 0),()),
	}

class ICWNonLinearStudyOptions(DispatchBaseClass):
	"""Interface for NonLinearStudyOptions"""
	CLSID = IID('{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}')
	coclass_clsid = IID('{8E88103F-7AE3-45FF-B517-AC6E5CCED6B8}')

	def GetArcLengthCompletionOptions(self, DMaxLoad=pythoncom.Missing, DMaxDisplacement=pythoncom.Missing, nUnit=pythoncom.Missing, NMaxArcSteps=pythoncom.Missing
			, DArcLengthMultiplier=pythoncom.Missing):
		return self._ApplyTypes_(23, 1, (24, 0), ((16389, 2), (16389, 2), (16387, 2), (16387, 2), (16389, 2)), u'GetArcLengthCompletionOptions', None,DMaxLoad
			, DMaxDisplacement, nUnit, NMaxArcSteps, DArcLengthMultiplier)

	def GetAutomaticTimeIncrement(self, DInitialTimeIncrement=pythoncom.Missing, DMiNVal=pythoncom.Missing, DMaxVal=pythoncom.Missing, NNoOfAdjustments=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16387, 2)), u'GetAutomaticTimeIncrement', None,DInitialTimeIncrement
			, DMiNVal, DMaxVal, NNoOfAdjustments)

	def GetDisplacementControlOptions(self, NDisplacementComponent=pythoncom.Missing, nUnit=pythoncom.Missing):
		return self._ApplyTypes_(19, 1, (24, 0), ((16387, 2), (16387, 2)), u'GetDisplacementControlOptions', None,NDisplacementComponent
			, nUnit)

	def GetDisplacementControlOptions2(self, NDisplacementComponent=pythoncom.Missing, nUnit=pythoncom.Missing, pDispatch=pythoncom.Missing):
		return self._ApplyTypes_(26, 1, (24, 0), ((16387, 2), (16387, 2), (16393, 2)), u'GetDisplacementControlOptions2', None,NDisplacementComponent
			, nUnit, pDispatch)

	def GetStepToleranceOptions(self, NEqilibriumIteration=pythoncom.Missing, NMaxEqilibriumIteration=pythoncom.Missing, DConvTol=pythoncom.Missing, DPlasticityTol=pythoncom.Missing
			, NSingularityEleFactor=pythoncom.Missing):
		return self._ApplyTypes_(25, 1, (24, 0), ((16387, 2), (16387, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetStepToleranceOptions', None,NEqilibriumIteration
			, NMaxEqilibriumIteration, DConvTol, DPlasticityTol, NSingularityEleFactor)

	def GetTimeCurve(self):
		return self._ApplyTypes_(21, 1, (12, 0), (), u'GetTimeCurve', None,)

	def GetZeroStrainTemperature(self, DZeroStrainTemperature=pythoncom.Missing, NZeroStrainTemperatureUnit=pythoncom.Missing):
		return self._ApplyTypes_(16, 1, (24, 0), ((16389, 2), (16387, 2)), u'GetZeroStrainTemperature', None,DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	def SetArcLengthCompletionOptions(self, DMaxLoad=defaultNamedNotOptArg, DMaxDisplacement=defaultNamedNotOptArg, nUnit=defaultNamedNotOptArg, NArcSteps=defaultNamedNotOptArg
			, DArcLenMultiplier=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((5, 1), (5, 1), (3, 1), (3, 1), (5, 1)),DMaxLoad
			, DMaxDisplacement, nUnit, NArcSteps, DArcLenMultiplier)

	def SetAutomaticTimeIncrement(self, DInitialTimeIncrement=defaultNamedNotOptArg, DMiNVal=defaultNamedNotOptArg, DMaxVal=defaultNamedNotOptArg, NNoOfAdjustments=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (3, 1)),DInitialTimeIncrement
			, DMiNVal, DMaxVal, NNoOfAdjustments)

	def SetDisplacementControlOptions(self, DispEntity=defaultNamedNotOptArg, NDisplacementComponent=defaultNamedNotOptArg, nUnit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((9, 1), (3, 1), (3, 1)),DispEntity
			, NDisplacementComponent, nUnit)

	def SetStepToleranceOptions(self, NEqilibriumIteration=defaultNamedNotOptArg, NMaxEqilibriumIteration=defaultNamedNotOptArg, DConvTol=defaultNamedNotOptArg, DPlasticityTol=defaultNamedNotOptArg
			, NSingularityEleFactor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),NEqilibriumIteration
			, NMaxEqilibriumIteration, DConvTol, DPlasticityTol, NSingularityEleFactor)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(20, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	def SetZeroStrainTemperature(self, DZeroStrainTemperature=defaultNamedNotOptArg, NZeroStrainTemperatureUnit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((5, 1), (3, 1)),DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	_prop_map_get_ = {
		"ControlMethodType": (13, 2, (3, 0), (), "ControlMethodType", None),
		"EndTime": (3, 2, (5, 0), (), "EndTime", None),
		"FixedTimeIncrement": (8, 2, (5, 0), (), "FixedTimeIncrement", None),
		"IntegrationMethodType": (15, 2, (3, 0), (), "IntegrationMethodType", None),
		"IterativeMethodType": (14, 2, (3, 0), (), "IterativeMethodType", None),
		"ResultFolderPath": (12, 2, (8, 0), (), "ResultFolderPath", None),
		"SaveDataForRestartingAnalysis": (4, 2, (3, 0), (), "SaveDataForRestartingAnalysis", None),
		"SolverType": (1, 2, (3, 0), (), "SolverType", None),
		"StartTime": (2, 2, (5, 0), (), "StartTime", None),
		"TimeIncrement": (5, 2, (3, 0), (), "TimeIncrement", None),
		"UseLargeDisplacement": (9, 2, (3, 0), (), "UseLargeDisplacement", None),
		"UseLargeStrain": (11, 2, (3, 0), (), "UseLargeStrain", None),
		"UseUpdateLoadDirection": (10, 2, (3, 0), (), "UseUpdateLoadDirection", None),
	}
	_prop_map_put_ = {
		"ControlMethodType": ((13, LCID, 4, 0),()),
		"EndTime": ((3, LCID, 4, 0),()),
		"FixedTimeIncrement": ((8, LCID, 4, 0),()),
		"IntegrationMethodType": ((15, LCID, 4, 0),()),
		"IterativeMethodType": ((14, LCID, 4, 0),()),
		"ResultFolderPath": ((12, LCID, 4, 0),()),
		"SaveDataForRestartingAnalysis": ((4, LCID, 4, 0),()),
		"SolverType": ((1, LCID, 4, 0),()),
		"TimeIncrement": ((5, LCID, 4, 0),()),
		"UseLargeDisplacement": ((9, LCID, 4, 0),()),
		"UseLargeStrain": ((11, LCID, 4, 0),()),
		"UseUpdateLoadDirection": ((10, LCID, 4, 0),()),
	}

class ICWPinConnector(DispatchBaseClass):
	"""Interface for CPinConnector"""
	CLSID = IID('{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}')
	coclass_clsid = IID('{A5780715-A450-40CF-B435-7A7F756B094A}')

	def GetFirstLocationEntityCount(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), (),)

	def GetLibraryMaterial(self, SMaterialLibName=pythoncom.Missing, SMaterialName=pythoncom.Missing):
		return self._ApplyTypes_(15, 1, (24, 0), ((16392, 2), (16392, 2)), u'GetLibraryMaterial', None,SMaterialLibName
			, SMaterialName)

	def GetSecondLocationEntityCount(self):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), (),)

	def InsertEntityAtFirstLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertEntityAtSecondLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def PinConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def PinConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), (),)

	def RemoveEntityFromFirstLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveEntityFromSecondLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetLibraryMaterial(self, SMaterialLibName=defaultNamedNotOptArg, SMaterialName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((8, 1), (8, 1)),SMaterialLibName
			, SMaterialName)

	_prop_map_get_ = {
		"AxialStiffnessValue": (2, 2, (5, 0), (), "AxialStiffnessValue", None),
		"IncludeMass": (6, 2, (11, 0), (), "IncludeMass", None),
		"IncludeStrengthData": (8, 2, (11, 0), (), "IncludeStrengthData", None),
		"IncludeTypeWithKey": (4, 2, (11, 0), (), "IncludeTypeWithKey", None),
		"IncludeTypeWithRetainerRing": (5, 2, (11, 0), (), "IncludeTypeWithRetainerRing", None),
		"MassValue": (7, 2, (5, 0), (), "MassValue", None),
		"MaterialType": (14, 2, (3, 0), (), "MaterialType", None),
		"PinStrengthUnit": (11, 2, (3, 0), (), "PinStrengthUnit", None),
		"PinStrengthValue": (12, 2, (5, 0), (), "PinStrengthValue", None),
		"RotationalStiffnessValue": (3, 2, (5, 0), (), "RotationalStiffnessValue", None),
		"SafetyFactor": (13, 2, (5, 0), (), "SafetyFactor", None),
		"TensileStressAreaUnit": (9, 2, (3, 0), (), "TensileStressAreaUnit", None),
		"TensileStressAreaValue": (10, 2, (5, 0), (), "TensileStressAreaValue", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"AxialStiffnessValue": ((2, LCID, 4, 0),()),
		"IncludeMass": ((6, LCID, 4, 0),()),
		"IncludeStrengthData": ((8, LCID, 4, 0),()),
		"IncludeTypeWithKey": ((4, LCID, 4, 0),()),
		"IncludeTypeWithRetainerRing": ((5, LCID, 4, 0),()),
		"MassValue": ((7, LCID, 4, 0),()),
		"MaterialType": ((14, LCID, 4, 0),()),
		"PinStrengthUnit": ((11, LCID, 4, 0),()),
		"PinStrengthValue": ((12, LCID, 4, 0),()),
		"RotationalStiffnessValue": ((3, LCID, 4, 0),()),
		"SafetyFactor": ((13, LCID, 4, 0),()),
		"TensileStressAreaUnit": ((9, LCID, 4, 0),()),
		"TensileStressAreaValue": ((10, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWPressure(DispatchBaseClass):
	"""Interface for CWPressure"""
	CLSID = IID('{3D12186F-4CAE-4511-9456-B42FB68F06F9}')
	coclass_clsid = IID('{9F100027-4912-4FDC-8386-8C9F0F6F11F3}')

	def GetCoordinateSystem(self):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetCoordinateSystem', None)
		return ret

	def GetNonUniformData(self, DConstVal=pythoncom.Missing, DX=pythoncom.Missing, DY=pythoncom.Missing, DXY=pythoncom.Missing
			, DXX=pythoncom.Missing, DYY=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetNonUniformData', None,DConstVal
			, DX, DY, DXY, DXX, DYY
			)

	def GetTimeCurve(self):
		return self._ApplyTypes_(14, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def PressureBeginEdit(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def PressureEndEdit(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetCoordinateSystem(self, DispCoordinateSystem=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((9, 1),),DispCoordinateSystem
			)

	def SetNonUniformData(self, DConstVal=defaultNamedNotOptArg, DX=defaultNamedNotOptArg, DY=defaultNamedNotOptArg, DXY=defaultNamedNotOptArg
			, DXX=defaultNamedNotOptArg, DYY=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (5, 1)),DConstVal
			, DX, DY, DXY, DXX, DYY
			)

	def SetReferenceGeometry(self, RefEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((9, 1),),RefEntity
			)

	def SetTimeCurve(self, VarCurveDate=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveDate
			, ErrorCode)

	_prop_map_get_ = {
		"DirectionType": (3, 2, (3, 0), (), "DirectionType", None),
		"IncludeNonUniformDistribution": (5, 2, (3, 0), (), "IncludeNonUniformDistribution", None),
		"PressureType": (4, 2, (3, 0), (), "PressureType", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"Value": (2, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"DirectionType": ((3, LCID, 4, 0),()),
		"IncludeNonUniformDistribution": ((5, LCID, 4, 0),()),
		"PressureType": ((4, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"Value": ((2, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(2, 2, (5, 0), (), "Value", None))
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ICWRadiation(DispatchBaseClass):
	"""Interface for CWRadiation"""
	CLSID = IID('{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}')
	coclass_clsid = IID('{333D8E64-BA1A-4008-8F28-C27B9C41FCEF}')

	def GetTemperatureCurve(self):
		return self._ApplyTypes_(14, 1, (12, 0), (), u'GetTemperatureCurve', None,)

	def GetTimeCurve(self):
		return self._ApplyTypes_(12, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RadiationBeginEdit(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def RadiationEndEdit(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetTemperatureCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTemperatureCurve', None,VarCurveData
			, ErrorCode)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(11, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	_prop_map_get_ = {
		"AmbientTemperature": (4, 2, (5, 0), (), "AmbientTemperature", None),
		"Emmisivity": (2, 2, (5, 0), (), "Emmisivity", None),
		"OpenSystem": (5, 2, (3, 0), (), "OpenSystem", None),
		"RadiationType": (6, 2, (3, 0), (), "RadiationType", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"UseTemperatureCurve": (16, 2, (3, 0), (), "UseTemperatureCurve", None),
		"UseTimeCurve": (15, 2, (3, 0), (), "UseTimeCurve", None),
		"ViewFactor": (3, 2, (5, 0), (), "ViewFactor", None),
	}
	_prop_map_put_ = {
		"AmbientTemperature": ((4, LCID, 4, 0),()),
		"Emmisivity": ((2, LCID, 4, 0),()),
		"OpenSystem": ((5, LCID, 4, 0),()),
		"RadiationType": ((6, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"UseTemperatureCurve": ((16, LCID, 4, 0),()),
		"UseTimeCurve": ((15, LCID, 4, 0),()),
		"ViewFactor": ((3, LCID, 4, 0),()),
	}

class ICWRemoteLoad(DispatchBaseClass):
	"""Interface for CWRemoteLoad"""
	CLSID = IID('{9E273951-C865-45F6-89F9-7DAAB971010E}')
	coclass_clsid = IID('{DA0FB97E-1DB2-4F38-B9CE-F57A6215B772}')

	def GetMassValues(self):
		return self._ApplyTypes_(7, 1, (12, 0), (), u'GetMassValues', None,)

	def GetValueType(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def SetMassValues(self, Var=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((12, 1),),Var
			)

	_prop_map_get_ = {
		"ForceOrTranslationUnit": (2, 2, (3, 0), (), "ForceOrTranslationUnit", None),
		"ForceOrTranslationValues": (5, 2, (12, 0), (), "ForceOrTranslationValues", None),
		"LocationUnit": (1, 2, (3, 0), (), "LocationUnit", None),
		"LocationValues": (4, 2, (12, 0), (), "LocationValues", None),
		"MomentOrRotationUnit": (3, 2, (3, 0), (), "MomentOrRotationUnit", None),
		"MomentOrRotationValues": (6, 2, (12, 0), (), "MomentOrRotationValues", None),
	}
	_prop_map_put_ = {
		"ForceOrTranslationUnit": ((2, LCID, 4, 0),()),
		"ForceOrTranslationValues": ((5, LCID, 4, 0),()),
		"LocationUnit": ((1, LCID, 4, 0),()),
		"LocationValues": ((4, LCID, 4, 0),()),
		"MomentOrRotationUnit": ((3, LCID, 4, 0),()),
		"MomentOrRotationValues": ((6, LCID, 4, 0),()),
	}

class ICWRestraint(DispatchBaseClass):
	"""Interface for CWRestraint"""
	CLSID = IID('{A1B7607C-2C6B-447B-8183-633531BFDDAF}')
	coclass_clsid = IID('{DC9FEC33-1B9A-40DA-A21A-713C86F44AE7}')

	def GetCoordinateType(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def GetRotationComponentsValues(self, BVal1=pythoncom.Missing, BVal2=pythoncom.Missing, BVal3=pythoncom.Missing, DVal1=pythoncom.Missing
			, DVal2=pythoncom.Missing, DVal3=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetRotationComponentsValues', None,BVal1
			, BVal2, BVal3, DVal1, DVal2, DVal3
			)

	def GetTimeCurve(self):
		return self._ApplyTypes_(14, 1, (12, 0), (), u'GetTimeCurve', None,)

	def GetTranslationComponentsValues(self, BVal1=pythoncom.Missing, BVal2=pythoncom.Missing, BVal3=pythoncom.Missing, DVal1=pythoncom.Missing
			, DVal2=pythoncom.Missing, DVal3=pythoncom.Missing):
		return self._ApplyTypes_(4, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16389, 2), (16389, 2), (16389, 2)), u'GetTranslationComponentsValues', None,BVal1
			, BVal2, BVal3, DVal1, DVal2, DVal3
			)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RestraintBeginEdit(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def RestraintEndEdit(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	def SetReferenceGeometry(self, DispRefEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1),),DispRefEntity
			)

	def SetRotationComponentsValues(self, BVal1=defaultNamedNotOptArg, BVal2=defaultNamedNotOptArg, BVal3=defaultNamedNotOptArg, DVal1=defaultNamedNotOptArg
			, DVal2=defaultNamedNotOptArg, DVal3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),BVal1
			, BVal2, BVal3, DVal1, DVal2, DVal3
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	def SetTranslationComponentsValues(self, BVal1=defaultNamedNotOptArg, BVal2=defaultNamedNotOptArg, BVal3=defaultNamedNotOptArg, DVal1=defaultNamedNotOptArg
			, DVal2=defaultNamedNotOptArg, DVal3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),BVal1
			, BVal2, BVal3, DVal1, DVal2, DVal3
			)

	_prop_map_get_ = {
		"RestraintType": (2, 2, (3, 0), (), "RestraintType", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"RestraintType": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWResults(DispatchBaseClass):
	"""Interface for CWResults"""
	CLSID = IID('{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}')
	coclass_clsid = IID('{B16AF523-9A34-460F-AF2E-670D3559522D}')

	def ActivatePlot(self, PlotName=defaultNamedNotOptArg):
		"""Activate Plot"""
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((8, 1),),PlotName
			)

	def DeletePlot(self, PlotName=defaultNamedNotOptArg):
		"""Delete Plot"""
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((8, 1),),PlotName
			)

	def GetBeamForcesForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, ArraySelectedEntities=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(30, 1, (12, 0), ((3, 1), (3, 1), (12, 1), (3, 1), (16387, 2)), u'GetBeamForcesForEntities', None,NComponent
			, NStepNumber, ArraySelectedEntities, NUnits, ErrorCode)

	def GetBeamMinMaxStress(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(23, 1, (12, 0), ((3, 1), (3, 1), (3, 1), (16387, 2)), u'GetBeamMinMaxStress', None,NComponent
			, NStepNumber, NUnits, ErrorCode)

	def GetBeamStressForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, ArraySelectedEntities=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(31, 1, (12, 0), ((3, 1), (3, 1), (12, 1), (3, 1), (16387, 2)), u'GetBeamStressForEntities', None,NComponent
			, NStepNumber, ArraySelectedEntities, NUnits, ErrorCode)

	def GetBucklingLoadFactors(self, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(12, 1, (12, 0), ((16387, 2),), u'GetBucklingLoadFactors', None,ErrorCode
			)

	def GetDisplacementComponentForAllStepsAtNode(self, NComponent=defaultNamedNotOptArg, NNodeNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(17, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetDisplacementComponentForAllStepsAtNode', None,NComponent
			, NNodeNum, DispPlane, NUnits, ErrorCode)

	def GetDisplacementForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ArraySelectedEntities=defaultNamedNotOptArg
			, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(21, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (12, 1), (3, 1), (16387, 2)), u'GetDisplacementForEntities', None,NComponent
			, NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode
			)

	def GetMassParticipation(self, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(11, 1, (12, 0), ((16387, 2),), u'GetMassParticipation', None,ErrorCode
			)

	def GetMaximumAvailableSteps(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetMinMaxDisplacement(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(9, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetMinMaxDisplacement', None,NComponent
			, NStepNumber, DispPlane, NUnits, ErrorCode)

	def GetMinMaxStrain(self, NComponent=defaultNamedNotOptArg, NElementNumber=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(5, 1, (12, 0), ((3, 1), (3, 1), (3, 1), (9, 1), (16387, 2)), u'GetMinMaxStrain', None,NComponent
			, NElementNumber, NStepNumber, DispPlane, ErrorCode)

	def GetMinMaxStress(self, NComponent=defaultNamedNotOptArg, NElementNumber=defaultNamedNotOptArg, NStepNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg
			, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(3, 1, (12, 0), ((3, 1), (3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetMinMaxStress', None,NComponent
			, NElementNumber, NStepNum, DispPlane, NUnits, ErrorCode
			)

	def GetMinMaxThermal(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(14, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetMinMaxThermal', None,NComponent
			, NStepNumber, DispPlane, NUnits, ErrorCode)

	def GetPlotCount(self):
		"""Get Plot Count"""
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), (),)

	def GetPlotNames(self):
		"""Get Plot Names"""
		return self._ApplyTypes_(28, 1, (12, 0), (), u'GetPlotNames', None,)

	def GetReactionForcesAndMoments(self, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(8, 1, (12, 0), ((3, 1), (9, 1), (3, 1), (16387, 2)), u'GetReactionForcesAndMoments', None,NStepNumber
			, DispPlane, NUnits, ErrorCode)

	def GetResonantFrequencies(self, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(10, 1, (12, 0), ((16387, 2),), u'GetResonantFrequencies', None,ErrorCode
			)

	def GetRotationalDisplacement(self, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (12, 0), ((3, 1), (9, 1), (3, 1), (16387, 2)), u'GetRotationalDisplacement', None,NStepNumber
			, DispPlane, NUnits, ErrorCode)

	def GetStrain(self, NElementNumber=defaultNamedNotOptArg, NStepNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(4, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (16387, 2)), u'GetStrain', None,NElementNumber
			, NStepNum, DispPlane, ErrorCode)

	def GetStrainComponentForAllStepsAtNode(self, NComponent=defaultNamedNotOptArg, NNodeNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(16, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (16387, 2)), u'GetStrainComponentForAllStepsAtNode', None,NComponent
			, NNodeNum, DispPlane, ErrorCode)

	def GetStrainForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ArraySelectedEntities=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(20, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (12, 1), (16387, 2)), u'GetStrainForEntities', None,NComponent
			, NStepNumber, DispPlane, ArraySelectedEntities, ErrorCode)

	def GetStrainForEntities2(self, bValueByNode=defaultNamedNotOptArg, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg
			, ArraySelectedEntities=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(33, 1, (12, 0), ((11, 1), (3, 1), (3, 1), (9, 1), (12, 1), (16387, 2)), u'GetStrainForEntities2', None,bValueByNode
			, NComponent, NStepNumber, DispPlane, ArraySelectedEntities, ErrorCode
			)

	def GetStress(self, NElementNumber=defaultNamedNotOptArg, NStepNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(2, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetStress', None,NElementNumber
			, NStepNum, DispPlane, NUnits, ErrorCode)

	def GetStressComponentForAllStepsAtNode(self, NComponent=defaultNamedNotOptArg, NNodeNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(15, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetStressComponentForAllStepsAtNode', None,NComponent
			, NNodeNum, DispPlane, NUnits, ErrorCode)

	def GetStressForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ArrayArraySelectedEntities=defaultNamedNotOptArg
			, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(19, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (12, 1), (3, 1), (16387, 2)), u'GetStressForEntities', None,NComponent
			, NStepNumber, DispPlane, ArrayArraySelectedEntities, NUnits, ErrorCode
			)

	def GetStressForEntities2(self, bValueByNode=defaultNamedNotOptArg, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg
			, ArrayArraySelectedEntities=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(32, 1, (12, 0), ((11, 1), (3, 1), (3, 1), (9, 1), (12, 1), (3, 1), (16387, 2)), u'GetStressForEntities2', None,bValueByNode
			, NComponent, NStepNumber, DispPlane, ArrayArraySelectedEntities, NUnits
			, ErrorCode)

	def GetThermalComponentForAllStepsAtNode(self, NComponent=defaultNamedNotOptArg, NNodeNum=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg
			, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(18, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (3, 1), (16387, 2)), u'GetThermalComponentForAllStepsAtNode', None,NComponent
			, NNodeNum, DispPlane, NUnits, ErrorCode)

	def GetThermalForEntities(self, NComponent=defaultNamedNotOptArg, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, ArraySelectedEntities=defaultNamedNotOptArg
			, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(22, 1, (12, 0), ((3, 1), (3, 1), (9, 1), (12, 1), (3, 1), (16387, 2)), u'GetThermalForEntities', None,NComponent
			, NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode
			)

	def GetThermalValues(self, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(13, 1, (12, 0), ((3, 1), (9, 1), (3, 1), (16387, 2)), u'GetThermalValues', None,NStepNumber
			, DispPlane, NUnits, ErrorCode)

	def GetTranslationalDisplacement(self, NStepNumber=defaultNamedNotOptArg, DispPlane=defaultNamedNotOptArg, NUnits=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (12, 0), ((3, 1), (9, 1), (3, 1), (16387, 2)), u'GetTranslationalDisplacement', None,NStepNumber
			, DispPlane, NUnits, ErrorCode)

	def IGetPlotNames(self, Count=defaultNamedNotOptArg):
		"""Get Plot Names"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(29, LCID, 1, (8, 0), ((3, 1),),Count
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class ICWRigidConnector(DispatchBaseClass):
	"""Interface for CWRigidConnector"""
	CLSID = IID('{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}')
	coclass_clsid = IID('{0A75503A-136F-430C-95E0-904D33F2A68C}')

	def GetFirstLocationEntityCount(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	def GetSecondLocationEntityCount(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def InsertEntityAtFirstLocation(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def InsertEntityAtSecondLocation(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntityFromFirstLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveEntityFromSecondLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RigidConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def RigidConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class ICWShell(DispatchBaseClass):
	"""Interface for ICWShell"""
	CLSID = IID('{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}')
	coclass_clsid = IID('{FCB82093-3377-4C4C-9DFE-FEDD6B0B1E51}')

	# Result is of type ICWMaterial
	def GetDefaultMaterial(self):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetDefaultMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	def GetEntityAt(self, NIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((3, 1),),NIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetEntityAt', None)
		return ret

	# Result is of type ICWMaterial
	def GetShellMaterial(self):
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetShellMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetLibraryMaterial(self, SLibraryPathName=defaultNamedNotOptArg, SMaterialName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((8, 1), (8, 1)),SLibraryPathName
			, SMaterialName)

	def SetShellMaterial(self, MaterialDisp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((9, 1),),MaterialDisp
			)

	def ShellBeginEdit(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def ShellEndEdit(self):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def SuppressUnSuppress(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"EntityCount": (11, 2, (3, 0), (), "EntityCount", None),
		"Formulation": (4, 2, (3, 0), (), "Formulation", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"ShellThickness": (2, 2, (5, 0), (), "ShellThickness", None),
		"ShellUnit": (3, 2, (3, 0), (), "ShellUnit", None),
		"State": (5, 2, (3, 0), (), "State", None),
	}
	_prop_map_put_ = {
		"Formulation": ((4, LCID, 4, 0),()),
		"ShellThickness": ((2, LCID, 4, 0),()),
		"ShellUnit": ((3, LCID, 4, 0),()),
	}

class ICWShellManager(DispatchBaseClass):
	"""Interface for ICWShellManager"""
	CLSID = IID('{0680FB2B-F938-43C4-92D0-722586C802FD}')
	coclass_clsid = IID('{4B6D9839-B25E-4FCE-AE50-47BFF0545125}')

	def CreateShell(self, DispArray=defaultNamedNotOptArg):
		"""method CreateShell"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),DispArray
			)

	def DeleteShell(self, SName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1),),SName
			)

	# Result is of type ICWShell
	def GetShellAt(self, NIndex=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		"""method GetShellAt"""
		return self._ApplyTypes_(2, 1, (9, 0), ((3, 1), (16387, 2)), u'GetShellAt', '{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}',NIndex
			, ErrorCode)

	_prop_map_get_ = {
		"ShellCount": (1, 2, (3, 0), (), "ShellCount", None),
	}
	_prop_map_put_ = {
	}

class ICWSolidBody(DispatchBaseClass):
	"""Interface for CWSolidBody"""
	CLSID = IID('{699EF572-B1EB-454A-90B7-AF0A52F59E1B}')
	coclass_clsid = IID('{61C7F978-1602-4D64-859E-88F728DB7E36}')

	def ConvertToBeamBody(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	# Result is of type ICWMaterial
	def GetDefaultMaterial(self):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetDefaultMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	# Result is of type ICWMaterial
	def GetSolidBodyMaterial(self):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetSolidBodyMaterial', '{BF582064-D953-42DD-AFAD-BBE8364B93B4}')
		return ret

	def SetLibraryMaterial(self, SLibWithPathName=defaultNamedNotOptArg, SMaterialName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((8, 1), (8, 1)),SLibWithPathName
			, SMaterialName)

	def SetSolidBodyMaterial(self, RetVal=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((9, 1),),RetVal
			)

	_prop_map_get_ = {
		"SolidBodyName": (1, 2, (8, 0), (), "SolidBodyName", None),
	}
	_prop_map_put_ = {
	}

class ICWSolidComponent(DispatchBaseClass):
	"""Interface for Solid Component"""
	CLSID = IID('{16F9E890-CC94-4F7A-B654-30D4CF5E7521}')
	coclass_clsid = IID('{C75C8C1A-1A4E-4E39-835E-32A4F36D6176}')

	# Result is of type ICWSolidBody
	def GetSolidBodyAt(self, NIndex=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		"""method GetSolidBodyAt"""
		return self._ApplyTypes_(3, 1, (9, 0), ((3, 1), (16387, 2)), u'GetSolidBodyAt', '{699EF572-B1EB-454A-90B7-AF0A52F59E1B}',NIndex
			, ErrorCode)

	_prop_map_get_ = {
		"ComponentName": (2, 2, (8, 0), (), "ComponentName", None),
		"SolidBodyCount": (1, 2, (3, 0), (), "SolidBodyCount", None),
	}
	_prop_map_put_ = {
	}

class ICWSolidManager(DispatchBaseClass):
	"""Interface for SolidManager"""
	CLSID = IID('{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}')
	coclass_clsid = IID('{92D96050-0852-4B82-BFEA-82D3CC6FEEC4}')

	# Result is of type ICWSolidComponent
	def GetComponentAt(self, NIndex=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		"""method GetComponentAt"""
		return self._ApplyTypes_(2, 1, (9, 0), ((3, 1), (16387, 2)), u'GetComponentAt', '{16F9E890-CC94-4F7A-B654-30D4CF5E7521}',NIndex
			, ErrorCode)

	_prop_map_get_ = {
		"ComponentCount": (1, 2, (3, 0), (), "ComponentCount", None),
	}
	_prop_map_put_ = {
	}

class ICWSpotWeldConnector(DispatchBaseClass):
	"""Interface for CSpotWeldConnector"""
	CLSID = IID('{756B2585-6350-460A-9C2A-7F25DA9D094A}')
	coclass_clsid = IID('{5068060C-F268-4C97-A6A7-D6F89C51159E}')

	def GetSourceEntityCount(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def GetSpotWeldLocationCount(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), (),)

	def GetTargetEntityCount(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), (),)

	def InsertSpotWeldLocations(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def RemoveSpotWeldLocationAt(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def ReplaceEntityAtFirstFace(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def ReplaceEntityAtSecondFace(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def SpotWeldConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	def SpotWeldConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		"SpotWeldDiameterUnit": (1, 2, (3, 0), (), "SpotWeldDiameterUnit", None),
		"SpotWeldDiameterValue": (2, 2, (5, 0), (), "SpotWeldDiameterValue", None),
	}
	_prop_map_put_ = {
		"SpotWeldDiameterUnit": ((1, LCID, 4, 0),()),
		"SpotWeldDiameterValue": ((2, LCID, 4, 0),()),
	}

class ICWSpringConnector(DispatchBaseClass):
	"""Interface for CSpringConnector"""
	CLSID = IID('{96DD49CD-CC09-4FAE-A559-7A795983D6EB}')
	coclass_clsid = IID('{86C8808E-7661-4FDF-AF75-63EA21F94D3D}')

	def GetSourceEntityCount(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

	def GetSpringType(self, NSpringType=pythoncom.Missing, NSpringSubType=pythoncom.Missing):
		return self._ApplyTypes_(16, 1, (24, 0), ((16387, 2), (16387, 2)), u'GetSpringType', None,NSpringType
			, NSpringSubType)

	def GetTargetEntityCount(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def InsertEntityAtFirstLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def InsertEntityAtSecondLocation(self, pDispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((9, 1),),pDispEntity
			)

	def RemoveEntityAtFirstLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def RemoveEntityAtSecondLocation(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetSpringType(self, NSpringType=defaultNamedNotOptArg, NSpringSubType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1), (3, 1)),NSpringType
			, NSpringSubType)

	def SpringConnectorBeginEdit(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def SpringConnectorEndEdit(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		"NormalRadialStiffnessValue": (3, 2, (5, 0), (), "NormalRadialStiffnessValue", None),
		"PreLoadForceType": (6, 2, (3, 0), (), "PreLoadForceType", None),
		"PreLoadForceValue": (7, 2, (5, 0), (), "PreLoadForceValue", None),
		"RotationalStiffnessValue": (5, 2, (5, 0), (), "RotationalStiffnessValue", None),
		"StiffnessType": (2, 2, (3, 0), (), "StiffnessType", None),
		"TangentialOrShearStiffnessValue": (4, 2, (5, 0), (), "TangentialOrShearStiffnessValue", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"NormalRadialStiffnessValue": ((3, LCID, 4, 0),()),
		"PreLoadForceType": ((6, LCID, 4, 0),()),
		"PreLoadForceValue": ((7, LCID, 4, 0),()),
		"RotationalStiffnessValue": ((5, LCID, 4, 0),()),
		"StiffnessType": ((2, LCID, 4, 0),()),
		"TangentialOrShearStiffnessValue": ((4, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
	}

class ICWStaticStudyOptions(DispatchBaseClass):
	"""Interface for StaticStudyOptions"""
	CLSID = IID('{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}')
	coclass_clsid = IID('{AB747841-0F4F-4C92-A357-855616AE7B9C}')

	def GetZeroStrainTemperature(self, DZeroStrainTemperature=pythoncom.Missing, NZeroStrainTemperatureUnit=pythoncom.Missing):
		return self._ApplyTypes_(11, 1, (24, 0), ((16389, 2), (16387, 2)), u'GetZeroStrainTemperature', None,DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	def SetZeroStrainTemperature(self, DZeroStrainTemperature=defaultNamedNotOptArg, NZeroStrainTemperatureUnit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((5, 1), (3, 1)),DZeroStrainTemperature
			, NZeroStrainTemperatureUnit)

	_prop_map_get_ = {
		"ComputeFreeBodyForce": (6, 2, (3, 0), (), "ComputeFreeBodyForce", None),
		"FrictionCoefficient": (3, 2, (5, 0), (), "FrictionCoefficient", None),
		"IgnoreClearanceForSurfaceContact": (4, 2, (3, 0), (), "IgnoreClearanceForSurfaceContact", None),
		"IncludeGlobalFriction": (2, 2, (3, 0), (), "IncludeGlobalFriction", None),
		"LargeDisplacement": (5, 2, (3, 0), (), "LargeDisplacement", None),
		"ResultFolder": (10, 2, (8, 0), (), "ResultFolder", None),
		"SolverType": (1, 2, (3, 0), (), "SolverType", None),
		"UseInPlaneEffect": (7, 2, (3, 0), (), "UseInPlaneEffect", None),
		"UseInertialRelief": (9, 2, (3, 0), (), "UseInertialRelief", None),
		"UseSoftSpring": (8, 2, (3, 0), (), "UseSoftSpring", None),
	}
	_prop_map_put_ = {
		"ComputeFreeBodyForce": ((6, LCID, 4, 0),()),
		"FrictionCoefficient": ((3, LCID, 4, 0),()),
		"IgnoreClearanceForSurfaceContact": ((4, LCID, 4, 0),()),
		"IncludeGlobalFriction": ((2, LCID, 4, 0),()),
		"LargeDisplacement": ((5, LCID, 4, 0),()),
		"ResultFolder": ((10, LCID, 4, 0),()),
		"SolverType": ((1, LCID, 4, 0),()),
		"UseInPlaneEffect": ((7, LCID, 4, 0),()),
		"UseInertialRelief": ((9, LCID, 4, 0),()),
		"UseSoftSpring": ((8, LCID, 4, 0),()),
	}

class ICWStudy(DispatchBaseClass):
	"""Interface for CWStudy"""
	CLSID = IID('{999CA1B7-177C-4823-9F0E-A1816C1A003C}')
	coclass_clsid = IID('{54B982A6-721E-4305-ADF3-934EAA6D7113}')

	def ConnectAnalysisDatabase(self, sResultPathName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((8, 1),),sResultPathName
			)

	def CreateAnalysisDatabase(self, sResultPathName=defaultNamedNotOptArg, sDataBaseName=pythoncom.Missing):
		return self._ApplyTypes_(20, 1, (3, 0), ((8, 1), (16392, 2)), u'CreateAnalysisDatabase', None,sResultPathName
			, sDataBaseName)

	def CreateMesh(self, NUnits=defaultNamedNotOptArg, NElementSize=defaultNamedNotOptArg, NTolerance=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),NUnits
			, NElementSize, NTolerance)

	def RunAnalysis(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), (),)

	def SetNonLinearStudyOptions(self, NonLinearOption=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((9, 1),),NonLinearOption
			)

	def UpdateAllComponents(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AnalysisType": (3, 2, (3, 0), (), "AnalysisType", None),
		# Method 'BeamManager' returns object of type 'ICWBeamManager'
		"BeamManager": (19, 2, (9, 0), (), "BeamManager", '{D770D195-0FB7-4771-A269-30BD773D393A}'),
		# Method 'BucklingStudyOptions' returns object of type 'ICWBucklingStudyOptions'
		"BucklingStudyOptions": (15, 2, (9, 0), (), "BucklingStudyOptions", '{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}'),
		# Method 'ContactManager' returns object of type 'ICWContactManager'
		"ContactManager": (7, 2, (9, 0), (), "ContactManager", '{242B7E91-5A69-4CE1-B429-7008A54F1555}'),
		# Method 'FrequencyStudyOptions' returns object of type 'ICWFrequencyStudyOptions'
		"FrequencyStudyOptions": (14, 2, (9, 0), (), "FrequencyStudyOptions", '{268D40CF-565F-4259-B009-BAC3F5DA8F60}'),
		# Method 'LoadsAndRestraintsManager' returns object of type 'ICWLoadsAndRestraintsManager'
		"LoadsAndRestraintsManager": (8, 2, (9, 0), (), "LoadsAndRestraintsManager", '{9DEA3C90-44BB-45E0-A569-F4B196F47176}'),
		# Method 'Mesh' returns object of type 'ICWMesh'
		"Mesh": (4, 2, (9, 0), (), "Mesh", '{F5818CF4-0C05-49AC-997F-8A0DB432203B}'),
		"MeshType": (2, 2, (3, 0), (), "MeshType", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		# Method 'NonLinearStudyOptions' returns object of type 'ICWNonLinearStudyOptions'
		"NonLinearStudyOptions": (17, 2, (9, 0), (), "NonLinearStudyOptions", '{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}'),
		# Method 'Results' returns object of type 'ICWResults'
		"Results": (13, 2, (9, 0), (), "Results", '{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}'),
		# Method 'ShellManager' returns object of type 'ICWShellManager'
		"ShellManager": (6, 2, (9, 0), (), "ShellManager", '{0680FB2B-F938-43C4-92D0-722586C802FD}'),
		# Method 'SolidManager' returns object of type 'ICWSolidManager'
		"SolidManager": (5, 2, (9, 0), (), "SolidManager", '{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}'),
		# Method 'StaticStudyOptions' returns object of type 'ICWStaticStudyOptions'
		"StaticStudyOptions": (16, 2, (9, 0), (), "StaticStudyOptions", '{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}'),
		# Method 'ThermalStudyOptions' returns object of type 'ICWThermalStudyOptions'
		"ThermalStudyOptions": (12, 2, (9, 0), (), "ThermalStudyOptions", '{43AA3958-9093-4066-BA75-21EA9E206C98}'),
	}
	_prop_map_put_ = {
	}

class ICWStudyManager(DispatchBaseClass):
	"""Interface for CWStudyManager"""
	CLSID = IID('{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}')
	coclass_clsid = IID('{9D21C234-564F-4C51-8513-A6F93697E7DE}')

	# Result is of type ICWStudy
	def CreateNewStudy(self, SName=defaultNamedNotOptArg, NAnalysisType=defaultNamedNotOptArg, NMeshType=defaultNamedNotOptArg, Errors=pythoncom.Missing):
		return self._ApplyTypes_(3, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (16387, 2)), u'CreateNewStudy', '{999CA1B7-177C-4823-9F0E-A1816C1A003C}',SName
			, NAnalysisType, NMeshType, Errors)

	# Result is of type ICWStudy
	def CreateNewStudy2(self, SName=defaultNamedNotOptArg, NAnalysisType=defaultNamedNotOptArg, Errors=pythoncom.Missing):
		return self._ApplyTypes_(6, 1, (9, 0), ((8, 1), (3, 1), (16387, 2)), u'CreateNewStudy2', '{999CA1B7-177C-4823-9F0E-A1816C1A003C}',SName
			, NAnalysisType, Errors)

	def DeleteStudy(self, StudyName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1),),StudyName
			)

	# Result is of type ICWStudy
	def GetStudy(self, NIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),NIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetStudy', '{999CA1B7-177C-4823-9F0E-A1816C1A003C}')
		return ret

	_prop_map_get_ = {
		"ActiveStudy": (1, 2, (3, 0), (), "ActiveStudy", None),
		"StudyCount": (2, 2, (3, 0), (), "StudyCount", None),
	}
	_prop_map_put_ = {
		"ActiveStudy": ((1, LCID, 4, 0),()),
	}

class ICWTemperature(DispatchBaseClass):
	"""Interface for CWTemperature"""
	CLSID = IID('{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}')
	coclass_clsid = IID('{25E6E227-6678-419F-81F2-1A97FEF0583D}')

	def GetTimeCurve(self):
		return self._ApplyTypes_(8, 1, (12, 0), (), u'GetTimeCurve', None,)

	def InsertEntity(self, DispEntity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1),),DispEntity
			)

	def RemoveEntity(self, NIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 1),),NIndex
			)

	def SetTimeCurve(self, VarCurveData=defaultNamedNotOptArg, ErrorCode=pythoncom.Missing):
		return self._ApplyTypes_(7, 1, (3, 0), ((12, 1), (16387, 2)), u'SetTimeCurve', None,VarCurveData
			, ErrorCode)

	def TemperatureBeginEdit(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	def TemperatureEndEdit(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		"TemperatureType": (10, 2, (3, 0), (), "TemperatureType", None),
		"TemperatureValue": (2, 2, (5, 0), (), "TemperatureValue", None),
		"Unit": (1, 2, (3, 0), (), "Unit", None),
		"UseTimeCurve": (9, 2, (3, 0), (), "UseTimeCurve", None),
	}
	_prop_map_put_ = {
		"TemperatureType": ((10, LCID, 4, 0),()),
		"TemperatureValue": ((2, LCID, 4, 0),()),
		"Unit": ((1, LCID, 4, 0),()),
		"UseTimeCurve": ((9, LCID, 4, 0),()),
	}

class ICWThermalStudyOptions(DispatchBaseClass):
	"""Interface for ThermalStudyOptions"""
	CLSID = IID('{43AA3958-9093-4066-BA75-21EA9E206C98}')
	coclass_clsid = IID('{A78EC78E-A6AB-4435-B0DA-9069B090FF37}')

	_prop_map_get_ = {
		"ConvergenceTolerance": (5, 2, (5, 0), (), "ConvergenceTolerance", None),
		"FixedValue": (7, 2, (5, 0), (), "FixedValue", None),
		"RelaxationFactor": (6, 2, (3, 0), (), "RelaxationFactor", None),
		"ResultFolder": (11, 2, (8, 0), (), "ResultFolder", None),
		"SolutionType": (2, 2, (3, 0), (), "SolutionType", None),
		"SolverType": (1, 2, (3, 0), (), "SolverType", None),
		"ThermalStudyNameUsedForInitialTemperature": (9, 2, (8, 0), (), "ThermalStudyNameUsedForInitialTemperature", None),
		"TimeIncrement": (4, 2, (5, 0), (), "TimeIncrement", None),
		"TimeSteps": (10, 2, (3, 0), (), "TimeSteps", None),
		"TotalTime": (3, 2, (5, 0), (), "TotalTime", None),
		"UseTemperatureFromThermalStudy": (8, 2, (3, 0), (), "UseTemperatureFromThermalStudy", None),
	}
	_prop_map_put_ = {
		"ConvergenceTolerance": ((5, LCID, 4, 0),()),
		"FixedValue": ((7, LCID, 4, 0),()),
		"RelaxationFactor": ((6, LCID, 4, 0),()),
		"ResultFolder": ((11, LCID, 4, 0),()),
		"SolutionType": ((2, LCID, 4, 0),()),
		"SolverType": ((1, LCID, 4, 0),()),
		"ThermalStudyNameUsedForInitialTemperature": ((9, LCID, 4, 0),()),
		"TimeIncrement": ((4, LCID, 4, 0),()),
		"TimeSteps": ((10, LCID, 4, 0),()),
		"TotalTime": ((3, LCID, 4, 0),()),
		"UseTemperatureFromThermalStudy": ((8, LCID, 4, 0),()),
	}

class ICosmosWorks(DispatchBaseClass):
	"""ICosmosWorks Interface"""
	CLSID = IID('{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}')
	coclass_clsid = IID('{13527C80-537C-4F69-94F8-BC09F9755CC6}')

	_prop_map_get_ = {
		# Method 'ActiveDoc' returns object of type 'ICWModelDoc'
		"ActiveDoc": (1, 2, (9, 0), (), "ActiveDoc", '{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}'),
		"VersionNumber": (2, 2, (8, 0), (), "VersionNumber", None),
	}
	_prop_map_put_ = {
	}

class ICwAddincallback(DispatchBaseClass):
	"""ICwAddincallback Interface"""
	CLSID = IID('{49EEE451-912D-444C-BB23-A6976F71AA25}')
	coclass_clsid = IID('{4405E07F-4621-4481-B925-449A88051523}')

	def AddFatigueEvent(self):
		"""AddFatigueEvent"""
		return self._oleobj_.InvokeTypes(84, LCID, 1, (24, 0), (),)

	def AddGlobalDamping(self):
		"""AddGlobalDamping"""
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), (),)

	def AddGlobalDampingUpdate(self):
		"""AddGlobalDampingUpdate"""
		return self._oleobj_.InvokeTypes(114, LCID, 1, (3, 0), (),)

	def AddInitialCondition(self):
		"""AddInitialCondition"""
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), (),)

	def AddInitialConditionUpdate(self):
		"""AddInitialConditionUpdate"""
		return self._oleobj_.InvokeTypes(112, LCID, 1, (3, 0), (),)

	def AddSelectBaseExcitation(self):
		"""AddSelectBaseExcitation"""
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), (),)

	def AddSelectBaseExcitationUpdate(self):
		"""AddSelectBaseExcitationUpdate"""
		return self._oleobj_.InvokeTypes(110, LCID, 1, (3, 0), (),)

	def AddTrackedDataGraph(self):
		"""AddTrackedDataGraph"""
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), (),)

	def AddTrackedDataGraphUpdate(self):
		"""AddTrackedDataGraphUpdate"""
		return self._oleobj_.InvokeTypes(106, LCID, 1, (3, 0), (),)

	def AddUniformBaseExcitation(self):
		"""AddUniformBaseExcitation"""
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), (),)

	def AddUniformBaseExcitationUpdate(self):
		"""AddUniformBaseExcitationUpdate"""
		return self._oleobj_.InvokeTypes(108, LCID, 1, (3, 0), (),)

	def AppUpdate(self):
		"""AppUpdate"""
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def AutomatedTest(self, ArgList=defaultNamedNotOptArg):
		"""Run the automated tests"""
		return self._ApplyTypes_(93, 1, (12, 0), ((12, 1),), u'AutomatedTest', None,ArgList
			)

	def ChangeFatigueEventType(self):
		"""ChangeFatigueEventType"""
		return self._oleobj_.InvokeTypes(83, LCID, 1, (24, 0), (),)

	def CommonPostResultsUpdate(self):
		"""CommonPostResultsUpdate"""
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), (),)

	def CommonPostResultsUpdate2(self):
		"""CommonPostResultsUpdate2"""
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), (),)

	def CommonPostResultsUpdate3(self):
		"""CommonPostResultsUpdate3"""
		return self._oleobj_.InvokeTypes(64, LCID, 1, (3, 0), (),)

	def CommonPostResultsUpdateBeam(self):
		"""CommonPostResultsUpdateBeam"""
		return self._oleobj_.InvokeTypes(97, LCID, 1, (3, 0), (),)

	def CommonPostResultsUpdateBeam2(self):
		"""CommonPostResultsUpdateBeam2"""
		return self._oleobj_.InvokeTypes(98, LCID, 1, (3, 0), (),)

	def ContactSetUpdate(self):
		"""ContactSetUpdate"""
		return self._oleobj_.InvokeTypes(120, LCID, 1, (3, 0), (),)

	def ContactUpdate(self):
		"""ContactUpdate"""
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def CreateMesh(self):
		"""CreateMesh"""
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def DefineBearingLoads(self):
		"""DefineBearingLoads"""
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	def DefineCentriFugal(self):
		"""DefineCentriFugal"""
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def DefineContactSet(self):
		"""DefineContactSet"""
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def DefineConvection(self):
		"""DefineConvection"""
		return self._oleobj_.InvokeTypes(56, LCID, 1, (24, 0), (),)

	def DefineDesignResultGraph(self):
		"""DefineDesignResultGraph"""
		return self._oleobj_.InvokeTypes(75, LCID, 1, (24, 0), (),)

	def DefineForces(self):
		"""DefineForces"""
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def DefineGlobalContact(self):
		"""DefineGlobalContact"""
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def DefineGravity(self):
		"""DefineGravity"""
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def DefineHeatFlux(self):
		"""DefineHeatFlux"""
		return self._oleobj_.InvokeTypes(58, LCID, 1, (24, 0), (),)

	def DefineHeatPower(self):
		"""DefineHeatPower"""
		return self._oleobj_.InvokeTypes(57, LCID, 1, (24, 0), (),)

	def DefineMeshControl(self):
		"""DefineMeshControl"""
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def DefineOptConstraint(self):
		"""DefineOptConstraint"""
		return self._oleobj_.InvokeTypes(78, LCID, 1, (24, 0), (),)

	def DefineOptDesignVar(self):
		"""DefineOptDesignVar"""
		return self._oleobj_.InvokeTypes(77, LCID, 1, (24, 0), (),)

	def DefineOptObjective(self):
		"""DefineOptObjective"""
		return self._oleobj_.InvokeTypes(76, LCID, 1, (24, 0), (),)

	def DefinePressures(self):
		"""DefinePressures"""
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def DefineRadiation(self):
		"""DefineRadiation"""
		return self._oleobj_.InvokeTypes(59, LCID, 1, (24, 0), (),)

	def DefineRemoteLoads(self):
		"""DefineRemoteLoads"""
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), (),)

	def DefineResponseGraph(self):
		"""DefineResponseGraph"""
		return self._oleobj_.InvokeTypes(67, LCID, 1, (24, 0), (),)

	def DefineRestraints(self):
		"""DefineRestraints"""
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	def DefineRigidConnections(self):
		"""DefineRigidConnections"""
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), (),)

	def DefineShellBySelectedSurfaces(self):
		"""DefineShellBySelectedSurfaces"""
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def DefineTemperature(self):
		"""DefineTemperature"""
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def DesignResultShowSummary(self):
		"""DesignResultShowSummary"""
		return self._oleobj_.InvokeTypes(73, LCID, 1, (24, 0), (),)

	def DropTestResultOptions(self):
		"""DropTestResultOptions"""
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

	def DropTestResultOptionsUpdate(self):
		"""DropTestResultOptionsUpdate"""
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), (),)

	def DropTestSetUpdate(self):
		"""DropTestSetUpdate"""
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def DropTestSetup(self):
		"""DropTestSetup"""
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def EditDefineDesignScenario(self):
		"""EditDefineDesignScenario"""
		return self._oleobj_.InvokeTypes(70, LCID, 1, (24, 0), (),)

	def EditDefineMaterial(self):
		"""EditDefineMaterial"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	def EditDefineMaterialUpdate(self):
		"""EditDefineMaterialUpdate"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def FatigueDefinePlot(self):
		"""FatigueDefinePlot"""
		return self._oleobj_.InvokeTypes(86, LCID, 1, (24, 0), (),)

	def FatigueList(self):
		"""FatigueList"""
		return self._oleobj_.InvokeTypes(87, LCID, 1, (24, 0), (),)

	def FatiguePlotUpdate(self):
		"""FatiguePlotUpdate"""
		return self._oleobj_.InvokeTypes(88, LCID, 1, (3, 0), (),)

	def FatigueStudyUpdate(self):
		"""FatigueStudyUpdate"""
		return self._oleobj_.InvokeTypes(85, LCID, 1, (3, 0), (),)

	def FreqPostResultsUpdate(self):
		"""FreqPostResultsUpdate"""
		return self._oleobj_.InvokeTypes(66, LCID, 1, (3, 0), (),)

	def HelpErrCallback(self, mainProduct=defaultNamedNotOptArg, helpFile=defaultNamedNotOptArg, helpTopic=defaultNamedNotOptArg, topicFile=defaultNamedNotOptArg):
		"""HelpErrCallback"""
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((3, 1), (8, 1), (3, 1), (8, 1)),mainProduct
			, helpFile, helpTopic, topicFile)

	def ListModeShape(self):
		"""ListModeShape"""
		return self._oleobj_.InvokeTypes(65, LCID, 1, (24, 0), (),)

	def LoadsAndRestraintsUpdate(self):
		"""LoadsAndRestraintsUpdate"""
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), (),)

	def LoadsAndRestraintsUpdate2(self):
		"""LoadsAndRestraintsUpdate2"""
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), (),)

	def LoadsAndRestraintsUpdate3(self):
		"""LoadsAndRestraintsUpdate3"""
		return self._oleobj_.InvokeTypes(95, LCID, 1, (3, 0), (),)

	def MeshControlUpdate(self):
		"""MeshControlUpdate"""
		return self._oleobj_.InvokeTypes(96, LCID, 1, (3, 0), (),)

	def NewStudy(self):
		"""NewStudy"""
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def NonlinearPostResultsUpdate(self):
		"""NonlinearPostResultsUpdate"""
		return self._oleobj_.InvokeTypes(68, LCID, 1, (3, 0), (),)

	def OptDesignCycleResults(self):
		"""OptDesignCycleResults"""
		return self._oleobj_.InvokeTypes(80, LCID, 1, (24, 0), (),)

	def OptDesignHistoryGraph(self):
		"""OptDesignHistoryGraph"""
		return self._oleobj_.InvokeTypes(81, LCID, 1, (24, 0), (),)

	def OptLocalTrendGraph(self):
		"""OptLocalTrendGraph"""
		return self._oleobj_.InvokeTypes(82, LCID, 1, (24, 0), (),)

	def OptimizationStudyUpdate(self):
		"""OptimizationStudyUpdate"""
		return self._oleobj_.InvokeTypes(79, LCID, 1, (3, 0), (),)

	def Parameters(self):
		"""Parameters"""
		return self._oleobj_.InvokeTypes(69, LCID, 1, (24, 0), (),)

	def PlotDisplacement(self):
		"""PlotDisplacement"""
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def PlotStrain(self):
		"""PlotStrain"""
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), (),)

	def PlotStress(self):
		"""PlotStress"""
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), (),)

	def PlotThermal(self):
		"""PlotThermal"""
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), (),)

	def PostResultCompareIn4Viewports(self):
		"""PostResultCompareIn4Viewports"""
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), (),)

	def PostResultCompareIn4ViewportsUpdate(self):
		"""PostResultCompareIn4ViewportsUpdate"""
		return self._oleobj_.InvokeTypes(118, LCID, 1, (3, 0), (),)

	def PostResultsUpdate(self):
		"""PostResultsUpdate"""
		return self._oleobj_.InvokeTypes(91, LCID, 1, (3, 0), (),)

	def PostResultsUpdateAnimate(self):
		"""PostResultsUpdateAnimate"""
		return self._oleobj_.InvokeTypes(40, LCID, 1, (3, 0), (),)

	def PostResultsUpdateClippingIso(self):
		"""PostResultsUpdateClippingIso"""
		return self._oleobj_.InvokeTypes(45, LCID, 1, (3, 0), (),)

	def PostResultsUpdateClippingSec(self):
		"""PostResultsUpdateClippingSec"""
		return self._oleobj_.InvokeTypes(43, LCID, 1, (3, 0), (),)

	def PostResultsUpdateDeformMode(self):
		"""PostResultsUpdateDeformMode"""
		return self._oleobj_.InvokeTypes(116, LCID, 1, (3, 0), (),)

	def PostResultsUpdateListSelected(self):
		"""PostResultsUpdateListSelected"""
		return self._oleobj_.InvokeTypes(51, LCID, 1, (3, 0), (),)

	def PostResultsUpdatePostMode(self):
		"""PostResultsUpdatePostMode"""
		return self._oleobj_.InvokeTypes(55, LCID, 1, (3, 0), (),)

	def PostResultsUpdateProbe(self):
		"""PostResultsUpdateProbe"""
		return self._oleobj_.InvokeTypes(49, LCID, 1, (3, 0), (),)

	def PostResultsUpdateSettings(self):
		"""PostResultsUpdateSettings"""
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), (),)

	def ReportTemplate(self):
		"""ReportTemplate"""
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def ReportUpdate(self):
		"""ReportUpdate"""
		return self._oleobj_.InvokeTypes(99, LCID, 1, (3, 0), (),)

	def ResultToolsAnimate(self):
		"""ResultToolsAnimate"""
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), (),)

	def ResultToolsClipping(self):
		"""ResultToolsClipping"""
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), (),)

	def ResultToolsClippingIso(self):
		"""ResultToolsClippingIso"""
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), (),)

	def ResultToolsContactForce(self):
		"""ResultToolsContactForce"""
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), (),)

	def ResultToolsDesignCheck(self):
		"""ResultToolsDesignCheck"""
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), (),)

	def ResultToolsListSelected(self):
		"""ResultToolsListSelected"""
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), (),)

	def ResultToolsPinForce(self):
		"""ResultToolsPinForce"""
		return self._oleobj_.InvokeTypes(63, LCID, 1, (24, 0), (),)

	def ResultToolsProbe(self):
		"""ResultToolsProbe"""
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), (),)

	def ResultToolsReactionForce(self):
		"""ResultToolsReactionForce"""
		return self._oleobj_.InvokeTypes(61, LCID, 1, (24, 0), (),)

	def ResultToolsSaveAs(self):
		"""ResultToolsSaveAs"""
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)

	def ResultToolsSettings(self):
		"""ResultToolsSettings"""
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), (),)

	def RunAnalysis(self):
		"""RunAnalysis"""
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def RunCosworksBackOffice(self, ArgList=defaultNamedNotOptArg):
		"""Run Cosworks BackOffice"""
		return self._ApplyTypes_(94, 1, (12, 0), ((12, 1),), u'RunCosworksBackOffice', None,ArgList
			)

	def RunDesidnScenario(self):
		"""RunDesidnScenario"""
		return self._oleobj_.InvokeTypes(72, LCID, 1, (24, 0), (),)

	def SetBaseline(self):
		"""SetBaseline"""
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

	def SetBaselineUpdate(self):
		"""SetBaselineUpdate"""
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), (),)

	def ShellUpdate(self):
		"""ShellUpdate"""
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def StaticPostResultsUpdate(self):
		"""StaticPostResultsUpdate"""
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), (),)

	def StudyRunUpdate(self):
		"""StudyRunUpdate"""
		return self._oleobj_.InvokeTypes(90, LCID, 1, (3, 0), (),)

	def StudyUpdate(self):
		"""StudyUpdate"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	def TemperatureUpdate(self):
		"""TemperatureUpdate"""
		return self._oleobj_.InvokeTypes(89, LCID, 1, (3, 0), (),)

	def ThermPostResultsUpdate(self):
		"""ThermPostResultsUpdate"""
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), (),)

	def ThermalStudyLoadsAndRestraintsUpdate(self):
		"""ThermalStudyLoadsAndRestraintsUpdate"""
		return self._oleobj_.InvokeTypes(60, LCID, 1, (3, 0), (),)

	def ToggleDeformMode(self):
		"""ToggleDeformMode"""
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), (),)

	def ToggleDisplay(self):
		"""ToggleDisplay"""
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), (),)

	def TogglePostMode(self):
		"""TogglePostMode"""
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), (),)

	def TrendTracker(self):
		"""TrendTracker"""
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

	def TrendTrackerUpdate(self):
		"""TrendTrackerUpdate"""
		return self._oleobj_.InvokeTypes(102, LCID, 1, (3, 0), (),)

	def UpdateDesignResult(self):
		"""UpdateDesignResult"""
		return self._oleobj_.InvokeTypes(74, LCID, 1, (3, 0), (),)

	def UpdateDesignScenario(self):
		"""UpdateDesignScenario"""
		return self._oleobj_.InvokeTypes(71, LCID, 1, (3, 0), (),)

	def appCallbackFunction(self, cmd=defaultNamedNotOptArg, data=defaultNamedNotOptArg, dsp=defaultNamedNotOptArg):
		"""appCallbackFunction"""
		return self._oleobj_.InvokeTypes(92, LCID, 1, (3, 0), ((3, 1), (3, 1), (9, 1)),cmd
			, data, dsp)

	_prop_map_get_ = {
		# Method 'CosmosWorks' returns object of type 'ICosmosWorks'
		"CosmosWorks": (100, 2, (9, 0), (), "CosmosWorks", '{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}'),
	}
	_prop_map_put_ = {
	}

from win32com.client import CoClassBaseClass
class CWBeamBody(CoClassBaseClass): # A CoClass
	CLSID = IID('{EC3DF67D-5D46-45AB-8505-69670841F5BF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWBeamBody,
	]
	default_interface = ICWBeamBody

class CWBeamManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{53F66937-4219-456B-89B1-6AF4BD7C022C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWBeamManager,
	]
	default_interface = ICWBeamManager

class CWBearingLoad(CoClassBaseClass): # A CoClass
	CLSID = IID('{07C2C408-612E-428F-8FD6-13230EF8D878}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWBearingLoad,
	]
	default_interface = ICWBearingLoad

class CWBoltConnector(CoClassBaseClass): # A CoClass
	# CWBoltConnector Class 
	CLSID = IID('{F9A4678F-9919-4435-B903-16A426E87B64}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWBoltConnector,
	]
	default_interface = ICWBoltConnector

class CWBucklingStudyOptions(CoClassBaseClass): # A CoClass
	CLSID = IID('{A7FE706C-70D4-49AD-9994-9E7139DE59A7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWBucklingStudyOptions,
	]
	default_interface = ICWBucklingStudyOptions

class CWCentriFugalForce(CoClassBaseClass): # A CoClass
	CLSID = IID('{61B4C22E-99B9-484D-BF0E-5C9FC1BA3B3A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWCentriFugalForce,
	]
	default_interface = ICWCentriFugalForce

class CWContactComponent(CoClassBaseClass): # A CoClass
	CLSID = IID('{A6934603-2339-4B84-A510-E7ADE2AE7320}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWContactComponent,
	]
	default_interface = ICWContactComponent

class CWContactManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{DBFEC66A-A413-4EB3-8A15-8F927274FECF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWContactManager,
	]
	default_interface = ICWContactManager

class CWContactSet(CoClassBaseClass): # A CoClass
	CLSID = IID('{AE787538-A050-4BBB-A27E-DB327C00848A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWContactSet,
	]
	default_interface = ICWContactSet

class CWConvection(CoClassBaseClass): # A CoClass
	CLSID = IID('{864CF3FA-5753-46F2-9F86-F1CC135F27A0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWConvection,
	]
	default_interface = ICWConvection

class CWElasticConnector(CoClassBaseClass): # A CoClass
	# CWElasticConnector Class 
	CLSID = IID('{55AC868A-F6C1-4DB4-8472-F88F3DB1B05F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWElasticConnector,
	]
	default_interface = ICWElasticConnector

class CWForce(CoClassBaseClass): # A CoClass
	CLSID = IID('{D83BBFB8-2E93-4581-B061-D356B67DC5C7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWForce,
	]
	default_interface = ICWForce

class CWFrequencyStudyOptions(CoClassBaseClass): # A CoClass
	CLSID = IID('{E399CE1B-28ED-48A3-A86E-A797C6556E43}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWFrequencyStudyOptions,
	]
	default_interface = ICWFrequencyStudyOptions

class CWGravity(CoClassBaseClass): # A CoClass
	CLSID = IID('{807A0872-ACA1-43A7-86F6-6D07B1989262}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWGravity,
	]
	default_interface = ICWGravity

class CWHeatFlux(CoClassBaseClass): # A CoClass
	CLSID = IID('{7EBC954D-4620-418D-8740-58D288545A34}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWHeatFlux,
	]
	default_interface = ICWHeatFlux

class CWHeatPower(CoClassBaseClass): # A CoClass
	CLSID = IID('{F66EE586-499C-424B-A547-F51337C6D6C3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWHeatPower,
	]
	default_interface = ICWHeatPower

class CWJoints(CoClassBaseClass): # A CoClass
	CLSID = IID('{C2C96FB8-EAE7-4BE3-9DFF-D7B3D2A37A0F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWJoints,
	]
	default_interface = ICWJoints

class CWLinkConnector(CoClassBaseClass): # A CoClass
	# CWLinkConnector Class 
	CLSID = IID('{19951FA7-A7F4-41C0-964A-0F79FA2A5D99}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWLinkConnector,
	]
	default_interface = ICWLinkConnector

class CWLoadsAndRestraints(CoClassBaseClass): # A CoClass
	CLSID = IID('{12FE135D-F7ED-41C7-9A15-42556526A9A9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWLoadsAndRestraints,
	]
	default_interface = ICWLoadsAndRestraints

class CWLoadsAndRestraintsManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{4425FB13-4541-4079-820E-0B4AC73E5231}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWLoadsAndRestraintsManager,
	]
	default_interface = ICWLoadsAndRestraintsManager

class CWMaterial(CoClassBaseClass): # A CoClass
	CLSID = IID('{675024F4-3BEB-465F-9747-50CDB6E6FD43}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWMaterial,
	]
	default_interface = ICWMaterial

class CWMesh(CoClassBaseClass): # A CoClass
	CLSID = IID('{0844A890-EB4C-434E-BECB-91374A38C531}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWMesh,
	]
	default_interface = ICWMesh

class CWMeshControl(CoClassBaseClass): # A CoClass
	CLSID = IID('{96212552-8F0F-47F9-BC8F-C712081CAAD2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWMeshControl,
	]
	default_interface = ICWMeshControl

class CWModelDoc(CoClassBaseClass): # A CoClass
	# ModelDoc Class 
	CLSID = IID('{EAFBFF38-E6B9-43D7-BE10-FE2BF2C8C0C8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWModelDoc,
	]
	default_interface = ICWModelDoc

class CWNonLinearStudyOptions(CoClassBaseClass): # A CoClass
	CLSID = IID('{8E88103F-7AE3-45FF-B517-AC6E5CCED6B8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWNonLinearStudyOptions,
	]
	default_interface = ICWNonLinearStudyOptions

class CWPinConnector(CoClassBaseClass): # A CoClass
	# CWPinConnector Class 
	CLSID = IID('{A5780715-A450-40CF-B435-7A7F756B094A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWPinConnector,
	]
	default_interface = ICWPinConnector

class CWPressure(CoClassBaseClass): # A CoClass
	CLSID = IID('{9F100027-4912-4FDC-8386-8C9F0F6F11F3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWPressure,
	]
	default_interface = ICWPressure

class CWRadiation(CoClassBaseClass): # A CoClass
	CLSID = IID('{333D8E64-BA1A-4008-8F28-C27B9C41FCEF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWRadiation,
	]
	default_interface = ICWRadiation

class CWRemoteLoad(CoClassBaseClass): # A CoClass
	CLSID = IID('{DA0FB97E-1DB2-4F38-B9CE-F57A6215B772}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWRemoteLoad,
	]
	default_interface = ICWRemoteLoad

class CWRestraint(CoClassBaseClass): # A CoClass
	CLSID = IID('{DC9FEC33-1B9A-40DA-A21A-713C86F44AE7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWRestraint,
	]
	default_interface = ICWRestraint

class CWResults(CoClassBaseClass): # A CoClass
	# Results Class 
	CLSID = IID('{B16AF523-9A34-460F-AF2E-670D3559522D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWResults,
	]
	default_interface = ICWResults

class CWRigidConnector(CoClassBaseClass): # A CoClass
	# CWRigidConnector Class 
	CLSID = IID('{0A75503A-136F-430C-95E0-904D33F2A68C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWRigidConnector,
	]
	default_interface = ICWRigidConnector

class CWShell(CoClassBaseClass): # A CoClass
	CLSID = IID('{FCB82093-3377-4C4C-9DFE-FEDD6B0B1E51}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWShell,
	]
	default_interface = ICWShell

class CWShellManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{4B6D9839-B25E-4FCE-AE50-47BFF0545125}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWShellManager,
	]
	default_interface = ICWShellManager

class CWSolidBody(CoClassBaseClass): # A CoClass
	CLSID = IID('{61C7F978-1602-4D64-859E-88F728DB7E36}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWSolidBody,
	]
	default_interface = ICWSolidBody

class CWSolidComponent(CoClassBaseClass): # A CoClass
	CLSID = IID('{C75C8C1A-1A4E-4E39-835E-32A4F36D6176}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWSolidComponent,
	]
	default_interface = ICWSolidComponent

class CWSolidManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{92D96050-0852-4B82-BFEA-82D3CC6FEEC4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWSolidManager,
	]
	default_interface = ICWSolidManager

class CWSpotWeldConnector(CoClassBaseClass): # A CoClass
	# CWSpotWeldConnector Class 
	CLSID = IID('{5068060C-F268-4C97-A6A7-D6F89C51159E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWSpotWeldConnector,
	]
	default_interface = ICWSpotWeldConnector

class CWSpringConnector(CoClassBaseClass): # A CoClass
	# CWSpringConnector Class 
	CLSID = IID('{86C8808E-7661-4FDF-AF75-63EA21F94D3D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWSpringConnector,
	]
	default_interface = ICWSpringConnector

class CWStaticStudyOptions(CoClassBaseClass): # A CoClass
	CLSID = IID('{AB747841-0F4F-4C92-A357-855616AE7B9C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWStaticStudyOptions,
	]
	default_interface = ICWStaticStudyOptions

class CWStudy(CoClassBaseClass): # A CoClass
	# Study Class 
	CLSID = IID('{54B982A6-721E-4305-ADF3-934EAA6D7113}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWStudy,
	]
	default_interface = ICWStudy

class CWStudyManager(CoClassBaseClass): # A CoClass
	# Study Manager Class 
	CLSID = IID('{9D21C234-564F-4C51-8513-A6F93697E7DE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWStudyManager,
	]
	default_interface = ICWStudyManager

class CWTemperature(CoClassBaseClass): # A CoClass
	CLSID = IID('{25E6E227-6678-419F-81F2-1A97FEF0583D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWTemperature,
	]
	default_interface = ICWTemperature

class CWThermalStudyOptions(CoClassBaseClass): # A CoClass
	CLSID = IID('{A78EC78E-A6AB-4435-B0DA-9069B090FF37}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICWThermalStudyOptions,
	]
	default_interface = ICWThermalStudyOptions

class CosmosWorks(CoClassBaseClass): # A CoClass
	# Application Class CosmosWorks
	CLSID = IID('{13527C80-537C-4F69-94F8-BC09F9755CC6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICosmosWorks,
	]
	default_interface = ICosmosWorks

class CwAddincallback(CoClassBaseClass): # A CoClass
	# CwAddincallback Class
	CLSID = IID('{4405E07F-4621-4481-B925-449A88051523}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICwAddincallback,
	]
	default_interface = ICwAddincallback

ICWBeamBody_vtables_dispatch_ = 1
ICWBeamBody_vtables_ = [
	(( u'BeamBodyName' , u'SName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'BeamType' , u'NType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'BeamType' , u'NType' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'BeamEnd1ConnectionType' , u'NType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'BeamEnd1ConnectionType' , u'NType' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'BeamEnd2ConnectionType' , u'NType' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'BeamEnd2ConnectionType' , u'NType' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultMaterial' , u'RetVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetBeamBodyMaterial' , u'RetVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'SetBeamBodyMaterial' , u'RetVal' , u'ErrorCode' , ), 7, (7, (), [ (9, 1, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetLibraryMaterial' , u'SLibWithPathName' , u'SMaterialName' , u'BValue' , ), 8, (8, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SetManualEnd1ConnectionType' , u'BHingeIstDir' , u'BHinge2ndDir' , u'BHingeAlongBeam' , u'BSlide1stDir' , 
			u'BSlide2ndDir' , u'BSlideAlongBeam' , ), 9, (9, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetManualEnd1ConnectionType' , u'BHingeIstDir' , u'BHinge2ndDir' , u'BHingeAlongBeam' , u'BSlide1stDir' , 
			u'BSlide2ndDir' , u'BSlideAlongBeam' , ), 10, (10, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetManualEnd2ConnectionType' , u'BHingeIstDir' , u'BHinge2ndDir' , u'BHingeAlongBeam' , u'BSlide1stDir' , 
			u'BSlide2ndDir' , u'BSlideAlongBeam' , ), 11, (11, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetManualEnd2ConnectionType' , u'BHingeIstDir' , u'BHinge2ndDir' , u'BHingeAlongBeam' , u'BSlide1stDir' , 
			u'BSlide2ndDir' , u'BSlideAlongBeam' , ), 12, (12, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'BeamBeginEdit' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'BeamEndEdit' , u'ErrorCode' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ConvertToSolidBody' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ICWBeamManager_vtables_dispatch_ = 1
ICWBeamManager_vtables_ = [
	(( u'BeamCount' , u'NCompCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetBeamBodyAt' , u'NIndex' , u'ErrorCode' , u'RetVal' , ), 2, (2, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetJointGroup' , u'ErrorCode' , u'RetVal' , ), 3, (3, (), [ (16387, 2, None, None) , 
			(16393, 10, None, "IID('{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ICWBearingLoad_vtables_dispatch_ = 1
ICWBearingLoad_vtables_ = [
	(( u'BearingLoadUnit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'BearingLoadUnit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'XDirectionValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'XDirectionValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'YDirectionValue' , u'DValue' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'YDirectionValue' , u'DValue' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Direction' , u'NValue' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Direction' , u'NValue' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'BearingLoadBeginEdit' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'BearingLoadEndEdit' , u'ErrorCode' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'pDispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceCoordinateSystem' , u'pDispEntity' , ), 8, (8, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 10, (10, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'BValue' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetEntityCount' , u'NEntityCount' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ICWBoltConnector_vtables_dispatch_ = 1
ICWBoltConnector_vtables_ = [
	(( u'BoltUnit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'BoltUnit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'MaterialUnit' , u'nUnit' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'MaterialUnit' , u'nUnit' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'HeadDiameterUnit' , u'nUnit' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'HeadDiameterUnit' , u'nUnit' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'NutDiameterUnit' , u'nUnit' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'NutDiameterUnit' , u'nUnit' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'BoltShankDiameterUnit' , u'nUnit' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'BoltShankDiameterUnit' , u'nUnit' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'BoltType' , u'NValue' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'BoltType' , u'NValue' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'MaterialType' , u'NValue' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'MaterialType' , u'NValue' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'IncludeMass' , u'BValue' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'IncludeMass' , u'BValue' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTightFit' , u'BValue' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTightFit' , u'BValue' , ), 9, (9, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceType' , u'NValue' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceType' , u'NValue' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceValue' , u'DValue' , ), 11, (11, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceValue' , u'DValue' , ), 11, (11, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DValue' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DValue' , ), 12, (12, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'MassValue' , u'DValue' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'MassValue' , u'DValue' , ), 13, (13, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'IncludeBoltSeries' , u'BValue' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'IncludeBoltSeries' , u'BValue' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'IncludeSymmetricalBolt' , u'BValue' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'IncludeSymmetricalBolt' , u'BValue' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'HeadDiameterValue' , u'DValue' , ), 16, (16, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'HeadDiameterValue' , u'DValue' , ), 16, (16, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'NutDiameterValue' , u'DValue' , ), 17, (17, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'NutDiameterValue' , u'DValue' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'BoltShankDiameterValue' , u'DValue' , ), 18, (18, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'BoltShankDiameterValue' , u'DValue' , ), 18, (18, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'SameHeadAndNutDiameter' , u'BValue' , ), 19, (19, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'SameHeadAndNutDiameter' , u'BValue' , ), 19, (19, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SymmetricalBoltType' , u'NValue' , ), 20, (20, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'SymmetricalBoltType' , u'NValue' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'MaterialSource' , u'NMaterialSource' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'MaterialSource' , u'NMaterialSource' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'YoungModulus' , u'DYoungModulus' , ), 22, (22, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'YoungModulus' , u'DYoungModulus' , ), 22, (22, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'PoissonsRatio' , u'DPoissonsRatio' , ), 23, (23, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'PoissonsRatio' , u'DPoissonsRatio' , ), 23, (23, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'ThermalCoefficient' , u'DThermalCoefficient' , ), 24, (24, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'ThermalCoefficient' , u'DThermalCoefficient' , ), 24, (24, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'IncludeStrengthData' , u'BValue' , ), 25, (25, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'IncludeStrengthData' , u'BValue' , ), 25, (25, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'IncludeKnownTensileStressArea' , u'BValue' , ), 26, (26, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'IncludeKnownTensileStressArea' , u'BValue' , ), 26, (26, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaUnit' , u'nUnit' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaUnit' , u'nUnit' , ), 27, (27, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'ThreadsPerLengthUnit' , u'nUnit' , ), 28, (28, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'ThreadsPerLengthUnit' , u'nUnit' , ), 28, (28, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'PinBoltStrengthUnit' , u'nUnit' , ), 29, (29, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( u'PinBoltStrengthUnit' , u'nUnit' , ), 29, (29, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'GetLibraryMaterial' , u'SMaterialLibName' , u'SMaterialName' , ), 30, (30, (), [ (16392, 2, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( u'SetLibraryMaterial' , u'SMaterialLibName' , u'SMaterialName' , ), 31, (31, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'GetStrengthData' , u'DTensileStressArea' , u'DPinBoltStrength' , u'DSafetyFactor' , ), 32, (32, (), [ 
			(16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( u'SetStrengthData' , u'DTensileStressArea' , u'DPinBoltStrength' , u'DSafetyFactor' , ), 33, (33, (), [ 
			(5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'BoltConnectorBeginEdit' , ), 34, (34, (), [ ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( u'BoltConnectorEndEdit' , u'ErrorCode' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtFirstLocation' , u'pDispEntity' , ), 36, (36, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtSecondLocation' , u'pDispEntity' , ), 37, (37, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityAtFirstLocation' , u'NIndex' , ), 38, (38, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityAtSecondLocation' , u'NIndex' , ), 39, (39, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( u'InsertReferenceGeometry' , u'pDispEntity' , ), 40, (40, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( u'InsertBoltSeriesEntity' , u'pDispEntity' , ), 41, (41, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( u'RemoveBoltSeriesEntity' , u'NIndex' , ), 42, (42, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( u'InsertTightFitEntity' , u'pDispEntity' , ), 43, (43, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( u'RemoveTightFitEntity' , u'NIndex' , ), 44, (44, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( u'GetSourceEntityCount' , u'NEntityCount' , ), 45, (45, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( u'GetTargetEntityCount' , u'NEntityCount' , ), 46, (46, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( u'GetBoltSeriesEntityCount' , u'NEntityCount' , ), 47, (47, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

ICWBucklingStudyOptions_vtables_dispatch_ = 1
ICWBucklingStudyOptions_vtables_ = [
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'BucklingModes' , u'NOptions' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'BucklingModes' , u'NOptions' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 5, (5, (), [ (16389, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'SetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 6, (6, (), [ (5, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ICWCentriFugalForce_vtables_dispatch_ = 1
ICWCentriFugalForce_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'AngularVelocity' , u'DAngularVelocity' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'AngularVelocity' , u'DAngularVelocity' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'AngularAcceleration' , u'DAngularAcceleration' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'AngularAcceleration' , u'DAngularAcceleration' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SetReferenceEntity' , u'RefEntity' , ), 4, (4, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'CFForceEndEdit' , u'ErrorCode' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 6, (6, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'CFForceBeginEdit' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

ICWContactComponent_vtables_dispatch_ = 1
ICWContactComponent_vtables_ = [
	(( u'ContactComponentType' , u'NType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ContactComponentType' , u'NType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Option' , u'NOption' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Option' , u'NOption' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IncludeFriction' , u'BInclude' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'IncludeFriction' , u'BInclude' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DValue' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DValue' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ContactName' , u'SName' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'NState' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceEntity' , u'DispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SuppressUnSuppress' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ContactComponentBeginEdit' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ContactComponentEndEdit' , u'ErrorCode' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ICWContactManager_vtables_dispatch_ = 1
ICWContactManager_vtables_ = [
	(( u'ContactSetCount' , u'NCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ContactComponentCount' , u'NCount' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetContactSetAt' , u'NIndex' , u'RetVal' , ), 3, (3, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'GetContactComponentAt' , u'NIndex' , u'RetVal' , ), 4, (4, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetGlobalContact' , u'NContactType' , u'NOption' , ), 5, (5, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'SetGlobalContact' , u'NContactType' , u'NOption' , ), 6, (6, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'CreateContactSet' , u'NContactSetType' , u'ArraySourceEntities' , u'ArrayTargetEntities' , u'ErrorCode' , 
			u'RetVal' , ), 7, (7, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'CreateContactSet2' , u'NContactSetType' , u'NSelectionType' , u'ArraySourceEntities' , u'ArrayTargetEntities' , 
			u'ErrorCode' , u'RetVal' , ), 8, (8, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(12, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'CreateContactComponent' , u'NContactType' , u'NOption' , u'DispEntity' , u'ErrorCode' , 
			u'RetVal' , ), 9, (9, (), [ (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'DeleteContactSet' , u'SName' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'DeleteContactComponent' , u'SName' , ), 11, (11, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

ICWContactSet_vtables_dispatch_ = 1
ICWContactSet_vtables_ = [
	(( u'ContactSetType' , u'NType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ContactSetType' , u'NType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Options' , u'NOptions' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Options' , u'NOptions' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IncludeFriction' , u'BIncludeFriction' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'IncludeFriction' , u'BIncludeFriction' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DFrictionValue' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'FrictionValue' , u'DFrictionValue' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'WallFriction' , u'DWallFriction' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'WallFriction' , u'DWallFriction' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GapType' , u'NGapType' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GapType' , u'NGapType' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ClearanceValue' , u'DClearanceValue' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ClearanceValue' , u'DClearanceValue' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'ClearanceUnit' , u'NClearanceUnit' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ClearanceUnit' , u'NClearanceUnit' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'WallType' , u'NWallType' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'WallType' , u'NWallType' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'WallStiffnessUnit' , u'nUnit' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'WallStiffnessUnit' , u'nUnit' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AxialStiffnessValue' , u'DAxialStiffnessValue' , ), 11, (11, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'AxialStiffnessValue' , u'DAxialStiffnessValue' , ), 11, (11, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'TangentialStiffnessValue' , u'DTangentialStiffnessValue' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'TangentialStiffnessValue' , u'DTangentialStiffnessValue' , ), 12, (12, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceType' , u'NResistanceType' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceType' , u'NResistanceType' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceValue' , u'DResistanceValue' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceValue' , u'DResistanceValue' , ), 14, (14, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceUnit' , u'nUnit' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'ResistanceUnit' , u'nUnit' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'ContactName' , u'SName' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'NState' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'SourceEntityCount' , u'NSourceEntityCount' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'TargetEntityCount' , u'NTargetEntityCount' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'SuppressUnSuppress' , ), 20, (20, (), [ ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'ContactSetBeginEdit' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'ContactSetEndEdit' , u'ErrorCode' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'RemoveTargetEntity' , u'NIndex' , ), 23, (23, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'RemoveSourceEntity' , u'NIndex' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'InsertTargetEntity' , u'DispEntity' , ), 25, (25, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'InsertSourceEntity' , u'DispEntity' , ), 26, (26, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'GetSourceEntityAt' , u'NIndex' , u'nSel' , u'DispEntity' , ), 27, (27, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'GetTargetEntityAt' , u'NIndex' , u'nSel' , u'DispEntity' , ), 28, (28, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
]

ICWConvection_vtables_dispatch_ = 1
ICWConvection_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ConvectionCoefficient' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ConvectionCoefficient' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'BulkAmbientTemperature' , u'DValue' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'BulkAmbientTemperature' , u'DValue' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ConvectionBeginEdit' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'ConvectionEndEdit' , u'ErrorCode' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 8, (8, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetTemperatureCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 10, (10, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'GetTemperatureCurve' , u'VarCurveData' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetBulkTemperatureTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 12, (12, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetBulkTemperatureTimeCurve' , u'VarCurveData' , ), 13, (13, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UseBulkTemperatureTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'UseBulkTemperatureTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ICWElasticConnector_vtables_dispatch_ = 1
ICWElasticConnector_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'StiffnessType' , u'NStiffnessType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'StiffnessType' , u'NStiffnessType' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'NormalStiffnessValue' , u'DValue' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'NormalStiffnessValue' , u'DValue' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ShearStiffnessValue' , u'DValue' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'ShearStiffnessValue' , u'DValue' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ElasticConnectorBeginEdit' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ElasticConnectorEndEdit' , u'ErrorCode' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'pDispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityAt' , u'NIndex' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetEntityCount' , u'NEntityCount' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

ICWForce_vtables_dispatch_ = 1
ICWForce_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NormalForceOrTorqueValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'NormalForceOrTorqueValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ForceType' , u'NForceType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ForceType' , u'NForceType' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'IncludeNonUniformDistribution' , u'BInclude' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'IncludeNonUniformDistribution' , u'BInclude' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetForceComponentValues' , u'B1' , u'B2' , u'B3' , u'D1' , 
			u'D2' , u'D3' , ), 5, (5, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'SetForceComponentValues' , u'B1' , u'B2' , u'B3' , u'D1' , 
			u'D2' , u'D3' , ), 6, (6, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetMomentComponentValues' , u'B1' , u'B2' , u'B3' , u'D1' , 
			u'D2' , u'D3' , ), 7, (7, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SetMomentComponentValues' , u'B1' , u'B2' , u'B3' , u'D1' , 
			u'D2' , u'D3' , ), 8, (8, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetNonUniformData' , u'DConstVal' , u'DX' , u'DY' , u'DXY' , 
			u'DX2' , u'DY2' , ), 9, (9, (), [ (16389, 2, None, None) , (16389, 2, None, None) , 
			(16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetNonUniformData' , u'constVal' , u'DX' , u'DY' , u'DXY' , 
			u'DX2' , u'DY2' , ), 10, (10, (), [ (5, 1, None, None) , (5, 1, None, None) , 
			(5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 11, (11, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'SetReferenceGeometry' , u'RefEntity' , ), 12, (12, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 13, (13, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'BValue' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetCoordinateSystem' , u'DispCoord' , ), 15, (15, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'SetCoordinateSystem' , u'DispCoordinateSystem' , ), 16, (16, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'ForceBeginEdit' , ), 18, (18, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'ForceEndEdit' , u'ErrorCode' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

ICWFrequencyStudyOptions_vtables_dispatch_ = 1
ICWFrequencyStudyOptions_vtables_ = [
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Options' , u'NOptions' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Options' , u'NOptions' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'NoOfFrequencies' , u'NNoOfFreq' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'NoOfFrequencies' , u'NNoOfFreq' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'LowerBoundFrequency' , u'NLowerBoundFreq' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'LowerBoundFrequency' , u'NLowerBoundFreq' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'UpperBoundFrequency' , u'NUpperBoundFreq' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'UpperBoundFrequency' , u'NUpperBoundFreq' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'UseLowerBoundFrequency' , u'BUseLBFreq' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'UseLowerBoundFrequency' , u'BUseLBFreq' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 9, (9, (), [ (16389, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'SetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 10, (10, (), [ (5, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ICWGravity_vtables_dispatch_ = 1
ICWGravity_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetGravitationalAcclerationValues' , u'DVal1' , u'DVal2' , u'DVal3' , ), 2, (2, (), [ 
			(16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'SetGravitationalAcclerationValues' , u'DVal1' , u'DVal2' , u'DVal3' , ), 3, (3, (), [ 
			(5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SetReferenceEntity' , u'RefEntity' , ), 4, (4, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'GravityEndEdit' , u'ErrorCode' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 6, (6, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GravityBeginEdit' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

ICWHeatFlux_vtables_dispatch_ = 1
ICWHeatFlux_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'HFValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'HFValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IncludeThermostat' , u'BInclude' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'IncludeThermostat' , u'BInclude' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'HeatFluxBeginEdit' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'HeatFluxEndEdit' , u'ErrorCode' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 8, (8, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetTemperatureCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 10, (10, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'GetTemperatureCurve' , u'VarCurveData' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetThermostat' , u'DispCoord' , ), 12, (12, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'SetThermostat' , u'DispCoord' , ), 13, (13, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetCutOffTemperatures' , u'DVal1' , u'DVal2' , ), 14, (14, (), [ (5, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetCutOffTemperatures' , u'DVal1' , u'DVal2' , ), 15, (15, (), [ (16389, 2, None, None) , 
			(16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ICWHeatPower_vtables_dispatch_ = 1
ICWHeatPower_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'HPValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'HPValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IncludeThermostat' , u'BInclude' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'IncludeThermostat' , u'BInclude' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'HeatPowerBeginEdit' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'HeatPowerEndEdit' , u'ErrorCode' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 8, (8, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetTemperatureCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 10, (10, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'GetTemperatureCurve' , u'VarCurveData' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetThermostat' , u'DispVertex' , ), 12, (12, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'SetThermostat' , u'DispVertex' , ), 13, (13, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetCutOffTemperatures' , u'DVal1' , u'DVal2' , ), 14, (14, (), [ (5, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetCutOffTemperatures' , u'DVal1' , u'DVal2' , ), 15, (15, (), [ (16389, 2, None, None) , 
			(16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'ThermostatUnits' , u'nUnit' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'ThermostatUnits' , u'nUnit' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ICWJoints_vtables_dispatch_ = 1
ICWJoints_vtables_ = [
	(( u'IncludeAllSelectedBeam' , u'BYesNo' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'IncludeAllSelectedBeam' , u'BYesNo' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'IncludeUserSelectedBeam' , u'BYesNo' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'IncludeUserSelectedBeam' , u'BYesNo' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'PinBallRadiusUnit' , u'NType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'PinBallRadiusUnit' , u'NType' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'PinBallRadius' , u'DType' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'PinBallRadius' , u'DType' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'IncludeDisplayNeutralAxis' , u'BYesNo' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'IncludeDisplayNeutralAxis' , u'BYesNo' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'IncludeKeepModifiedJointOnUpdate' , u'BYesNo' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'IncludeKeepModifiedJointOnUpdate' , u'BYesNo' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTreatAsJointForClearanceLessThan' , u'BYesNo' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTreatAsJointForClearanceLessThan' , u'BYesNo' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'CalculateJoints' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'DeleteJoint' , u'pDisp' , ), 9, (9, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'InsertBeamEntity' , u'DispEntity' , ), 10, (10, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'RemoveBeamEntityAt' , u'NIndex' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'JointsBeginEdit' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'JointsEndEdit' , u'ErrorCode' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ICWLinkConnector_vtables_dispatch_ = 1
ICWLinkConnector_vtables_ = [
	(( u'LinkConnectorBeginEdit' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LinkConnectorEndEdit' , u'ErrorCode' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceEntityAtFirstLocation' , u'pDisp' , ), 3, (3, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceEntityAtSecondLocation' , u'pDisp' , ), 4, (4, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ICWLoadsAndRestraints_vtables_dispatch_ = 1
ICWLoadsAndRestraints_vtables_ = [
	(( u'Name' , u'SName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Type' , u'NonLinearoadsAndRestraintsType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'NState' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'EntityCount' , u'NCount' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SuppressUnSuppress' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'GetEntityAt' , u'NIndex' , u'NSelType' , u'DispEntity' , ), 6, (6, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetReferenceGeometry' , u'NSelType' , u'DispRefGeom' , ), 7, (7, (), [ (16387, 2, None, None) , 
			(16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ICWLoadsAndRestraintsManager_vtables_dispatch_ = 1
ICWLoadsAndRestraintsManager_vtables_ = [
	(( u'Count' , u'NCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetLoadsAndRestraints' , u'NIndex' , u'ErrorCode' , u'RetVal' , ), 2, (2, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{7BDD45B4-9046-4C42-8936-A988906D2597}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'AddRestraint' , u'NRestraintType' , u'DispArray' , u'RefGeom' , u'ErrorCode' , 
			u'RetVal' , ), 3, (3, (), [ (3, 1, None, None) , (12, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{A1B7607C-2C6B-447B-8183-633531BFDDAF}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'AddPressure' , u'NPressureType' , u'DispArray' , u'RegGeom' , u'ErrorCode' , 
			u'RetVal' , ), 4, (4, (), [ (3, 1, None, None) , (12, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{3D12186F-4CAE-4511-9456-B42FB68F06F9}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'AddForce' , u'NForceType' , u'DispArray' , u'RefGeom' , u'ErrorCode' , 
			u'RetVal' , ), 5, (5, (), [ (3, 1, None, None) , (12, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{9419308B-BB2A-4842-B652-7AF115171012}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'AddForce2' , u'NForceType' , u'NSelectionType' , u'DispArray' , u'RefGeom' , 
			u'ErrorCode' , u'RetVal' , ), 6, (6, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(12, 1, None, None) , (9, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{9419308B-BB2A-4842-B652-7AF115171012}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'AddGravity' , u'DispEntity' , u'ErrorCode' , u'RetVal' , ), 7, (7, (), [ 
			(9, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{F932F397-D186-4381-88EF-EAA92E2ADCAE}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'AddCentrifugalForce' , u'DispEntity' , u'ErrorCode' , u'RetVal' , ), 8, (8, (), [ 
			(9, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{9F335011-F5A5-4992-AA03-3BEC3BDF0436}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AddTemperature' , u'DispArray' , u'ErrorCode' , u'RetVal' , ), 9, (9, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'AddConvection' , u'DispArray' , u'ErrorCode' , u'RetVal' , ), 10, (10, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddHeatFlux' , u'DispArray' , u'ErrorCode' , u'RetVal' , ), 11, (11, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{D77721DD-8FE5-45EB-92B6-FC8106968473}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'AddHeatPower' , u'DispArray' , u'ErrorCode' , u'RetVal' , ), 12, (12, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AddRadiation' , u'NRadType' , u'DispArray' , u'ErrorCode' , u'RetVal' , 
			), 13, (13, (), [ (3, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'DeleteLoadsAndRestraints' , u'SName' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AddRigidConnector' , u'persistIDFaceArray' , u'persistIDTargetArray' , u'ErrorCode' , u'RetVal' , 
			), 15, (15, (), [ (12, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'AddLinkConnector' , u'VertexPointforFirstLocation' , u'VertexPointforSecondLocation' , u'ErrorCode' , u'RetVal' , 
			), 16, (16, (), [ (9, 1, None, None) , (9, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AddElasticConnector' , u'DispArray' , u'ErrorCode' , u'RetVal' , ), 17, (17, (), [ 
			(12, 1, None, None) , (16387, 0, None, None) , (16393, 10, None, "IID('{5A355F90-47EB-4A23-824C-F2379DD92252}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'AddPinConnector' , u'DispArrayComp1' , u'DispArrayComp2' , u'ErrorCode' , u'RetVal' , 
			), 18, (18, (), [ (12, 1, None, None) , (12, 1, None, None) , (16387, 0, None, None) , (16393, 10, None, "IID('{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AddSpringConnector' , u'NSpringSubType' , u'DispArrayComp1' , u'DispArrayComp2' , u'ErrorCode' , 
			u'RetVal' , ), 19, (19, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(16387, 0, None, None) , (16393, 10, None, "IID('{96DD49CD-CC09-4FAE-A559-7A795983D6EB}')") , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'AddBoltConnector' , u'nBoltType' , u'DispArrayBoltHead' , u'DispArrayBoltNut' , u'ErrorCode' , 
			u'RetVal' , ), 20, (20, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(16387, 0, None, None) , (16393, 10, None, "IID('{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AddSpotWeldConnector' , u'FirstFace' , u'SecondFace' , u'DispArrayWeldLocations' , u'ErrorCode' , 
			u'RetVal' , ), 21, (21, (), [ (9, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , 
			(16387, 0, None, None) , (16393, 10, None, "IID('{756B2585-6350-460A-9C2A-7F25DA9D094A}')") , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'AddBearingLoad' , u'CoordinateSystem' , u'FirstFace' , u'ErrorCode' , u'RetVal' , 
			), 22, (22, (), [ (9, 1, None, None) , (12, 1, None, None) , (16387, 0, None, None) , (16393, 10, None, "IID('{E240A061-9543-4D8A-8749-2C9C850F7035}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'AddForce3' , u'ForceType' , u'SelectionType' , u'RefDirType' , u'InterpolationMode' , 
			u'DistPercentageOpt' , u'NumOfRows' , u'DistValue' , u'ForceValue' , u'NonUniformLoading' , 
			u'NULoadingOnBeam' , u'NonUniformLoadDistDef' , u'NonUniformLoadDistType' , u'Ucode' , u'TorqueNFVal' , 
			u'Comps' , u'FlipOrigin' , u'IsCurvedBeam' , u'DispArray' , u'RefGeom' , 
			u'PerUnitLength' , u'ErrorCode' , u'RetVal' , ), 23, (23, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(12, 1, None, None) , (12, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (12, 1, None, None) , (11, 1, None, None) , 
			(11, 1, None, None) , (12, 1, None, None) , (9, 1, None, None) , (11, 1, None, None) , (16387, 2, None, None) , 
			(16393, 10, None, "IID('{9419308B-BB2A-4842-B652-7AF115171012}')") , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

ICWMaterial_vtables_dispatch_ = 1
ICWMaterial_vtables_ = [
	(( u'Count' , u'NCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Source' , u'NSource' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'MaterialUnits' , u'NUnits' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'MaterialUnits' , u'NUnits' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ModelType' , u'NModelType' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ModelType' , u'NModelType' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'SCategory' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'SCategory' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'MaterialName' , u'SMaterialName' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'MaterialName' , u'SMaterialName' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'SDescription' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'SDescription' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'IncludeCreep' , u'BIncludeCreep' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'IncludeCreep' , u'BIncludeCreep' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'MooneyRivlinConstants' , u'NMooneyConstants' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'MooneyRivlinConstants' , u'NMooneyConstants' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'OgdenConstants' , u'NOgdenConstant' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'OgdenConstants' , u'NOgdenConstant' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'NoOfShearModuli' , u'NShearModuliNumber' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'NoOfShearModuli' , u'NShearModuliNumber' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'NoOfBulkModuli' , u'NBulkModuliNumber' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'NoOfBulkModuli' , u'NBulkModuliNumber' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetPropertyByName' , u'nUnit' , u'SName' , u'BTempDependent' , u'DValue' , 
			), 13, (13, (), [ (3, 1, None, None) , (8, 1, None, None) , (16387, 2, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'SetPropertyByName' , u'SName' , u'DValue' , u'BValue' , ), 14, (14, (), [ 
			(8, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetTemperatureCurveForProperty' , u'SPropName' , u'VarCurveData' , ), 15, (15, (), [ (8, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'SetTemperatureCurveForProperty' , u'SPropName' , u'VarCurveData' , u'ErrorCode' , ), 16, (16, (), [ 
			(8, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetFatigueSNCurve' , u'NIndex' , u'DStressRatio' , u'VarFatigueSNCurveData' , ), 17, (17, (), [ 
			(3, 1, None, None) , (16389, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'SetFatigueSNCurve' , u'NIndex' , u'DStressRatio' , u'VarFatigueSNCurveData' , u'ErrorCode' , 
			), 18, (18, (), [ (3, 1, None, None) , (5, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetStressStrainCurve' , u'VarCurveData' , ), 19, (19, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SetStressStrainCurve' , u'VarCurveData' , u'ErrorCode' , ), 20, (20, (), [ (12, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetMaterialDataCurve' , u'NIndex' , u'BUseCurve' , u'VarCurveData' , ), 21, (21, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'SetMaterialDataCurve' , u'NIndex' , u'BUseCurve' , u'VarCurveData' , u'ErrorCode' , 
			), 22, (22, (), [ (3, 1, None, None) , (3, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'GetReferencePlaneName' , u'SRefPlaneName' , ), 23, (23, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'SetReferencePlane' , u'PlaneDisp' , u'ErrorCode' , ), 24, (24, (), [ (9, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'SNCurveSource' , u'NSource' , ), 25, (25, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'SNCurveSource' , u'NSource' , ), 25, (25, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetAustenticSteelCurve' , u'VarCurveData' , ), 26, (26, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'GetCarbonSteelCurve' , u'VarCurveData' , ), 27, (27, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ICWMesh_vtables_dispatch_ = 1
ICWMesh_vtables_ = [
	(( u'MeshType' , u'NMeshType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'MeshState' , u'NMeshState' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Quality' , u'NQuality' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Quality' , u'NQuality' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'AutomaticTransition' , u'BValue' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'AutomaticTransition' , u'BValue' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SmoothSurface' , u'BValue' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'SmoothSurface' , u'BValue' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AutomaticLooping' , u'BValue' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'AutomaticLooping' , u'BValue' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLoops' , u'DValue' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLoops' , u'DValue' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ElementSizeFactorForEachLoop' , u'DValue' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ElementSizeFactorForEachLoop' , u'DValue' , ), 8, (8, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'ToleranceFactorForEachLoop' , u'DValue' , ), 9, (9, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ToleranceFactorForEachLoop' , u'DValue' , ), 9, (9, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'MesherType' , u'NMesherType' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'MesherType' , u'NMesherType' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'UseJacobianCheckForSolids' , u'BUse' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'UseJacobianCheckForSolids' , u'BUse' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UseJacobianCheckForShells' , u'BUse' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'UseJacobianCheckForShells' , u'BUse' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'NodeCount' , u'RetVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'ElementCount' , u'RetVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'MinElementsInCircle' , u'NElements' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'MinElementsInCircle' , u'NElements' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'MaxAspectRatio' , u'DRatio' , ), 16, (16, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'TimeToCompleteMesh' , u'NVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'IsMeshFailed' , u'BMeshFailed' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'MeshControlCount' , u'RetVal' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'ElementSize' , u'DElementSize' , ), 20, (20, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'Tolerance' , u'DTolerance' , ), 21, (21, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'GrowthRatio' , u'dGrowthRatio' , ), 22, (22, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'GrowthRatio' , u'dGrowthRatio' , ), 22, (22, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'MaxElementSize' , u'dMaxEleSize' , ), 24, (24, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'MinElementSize' , u'dMinEleSize' , ), 25, (25, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'GetNodes' , u'RetVal' , ), 26, (26, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'GetElements' , u'RetVal' , ), 27, (27, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'ApplyMeshControl' , u'EntitiesArray' , u'ErrorCode' , u'RetVal' , ), 28, (28, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{270F9491-0450-4BB5-BEF5-6E520C01D9AF}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'DeleteMeshControl' , u'SName' , ), 29, (29, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'GetShellElementNormalAt' , u'DispFace' , u'ErrorCode' , ), 30, (30, (), [ (9, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'GetNodeDataFromEntity' , u'DispEntity' , u'NCount' , u'VarOut' , ), 31, (31, (), [ 
			(9, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'GetElementDataFromEntity' , u'DispEntity' , u'NCount' , u'VarOut' , ), 32, (32, (), [ 
			(9, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'GetNoOfFailedComponents' , u'NCompFailed' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'IsComponentFailed' , u'SName' , u'BbCompFailed' , ), 34, (34, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'GetFailedFaces' , u'NFailedFaces' , u'DispFaces' , ), 35, (35, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'GetFailedEdges' , u'NFailedEdges' , u'DispEdges' , ), 36, (36, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'GetMeshControlAt' , u'NIndex' , u'RetVal' , ), 37, (37, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{270F9491-0450-4BB5-BEF5-6E520C01D9AF}')") , ], 1 , 1 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'GetFailedComponents' , u'NComp' , u'DispComps' , ), 38, (38, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'FlipShellElements' , u'DispFaceArray' , u'ErrorCode' , ), 39, (39, (), [ (12, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultElementSizeAndTolerance' , u'NUnits' , u'DElementSize' , u'DTolerance' , ), 40, (40, (), [ 
			(3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'GetNodeLocation' , u'NNodeNo' , u'XVal' , u'YVal' , u'ZVal' , 
			u'ErrorCode' , ), 41, (41, (), [ (3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , 
			(16389, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'GetElementLocation' , u'NNodeNo' , u'XVal' , u'YVal' , u'ZVal' , 
			u'ErrorCode' , ), 42, (42, (), [ (3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , 
			(16389, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultMaxAndMinElementSize' , u'NUnits' , u'DMaxElementSize' , u'DMinElementSize' , ), 43, (43, (), [ 
			(3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
]

ICWMeshControl_vtables_dispatch_ = 1
ICWMeshControl_vtables_ = [
	(( u'ElementSize' , u'DEleSize' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ElementSize' , u'DEleSize' , ), 1, (1, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Ratio' , u'DRatio' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Ratio' , u'DRatio' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Layers' , u'NVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Layers' , u'NVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Units' , u'NUnits' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Units' , u'NUnits' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'UseSameElementSize' , u'BUseSame' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'UseSameElementSize' , u'BUseSame' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'WeightFactor' , u'DWeightfactor' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'WeightFactor' , u'DWeightfactor' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'EntityCount' , u'NCount' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'SName' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SuppressUnSuppress' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetEntityAt' , u'NIndex' , u'NSelectionType' , u'DispEntity' , ), 10, (10, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'MeshControlBeginEdit' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'MeshControlEndEdit' , u'ErrorCode' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 13, (13, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'NState' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'NumofElementsforBeams' , u'NNumofEle' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'NumofElementsforBeams' , u'NNumofEle' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

ICWModelDoc_vtables_dispatch_ = 1
ICWModelDoc_vtables_ = [
	(( u'StudyManager' , u'RetVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'DefaultUnitSystem' , u'DefaultUnit' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'DefaultUnitSystem' , u'DefaultUnit' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ICWNonLinearStudyOptions_vtables_dispatch_ = 1
ICWNonLinearStudyOptions_vtables_ = [
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'StartTime' , u'DStartTime' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'EndTime' , u'DEndTime' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'EndTime' , u'DEndTime' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'SaveDataForRestartingAnalysis' , u'BSave' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SaveDataForRestartingAnalysis' , u'BSave' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'TimeIncrement' , u'NTimeIncrement' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'TimeIncrement' , u'NTimeIncrement' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'GetAutomaticTimeIncrement' , u'DInitialTimeIncrement' , u'DMiNVal' , u'DMaxVal' , u'NNoOfAdjustments' , 
			), 6, (6, (), [ (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetAutomaticTimeIncrement' , u'DInitialTimeIncrement' , u'DMiNVal' , u'DMaxVal' , u'NNoOfAdjustments' , 
			), 7, (7, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'FixedTimeIncrement' , u'DFixeDTimeIncrement' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'FixedTimeIncrement' , u'DFixeDTimeIncrement' , ), 8, (8, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'UseLargeDisplacement' , u'BUseLargeDisplacement' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'UseLargeDisplacement' , u'BUseLargeDisplacement' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'UseUpdateLoadDirection' , u'BUseUpdateLoadDir' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'UseUpdateLoadDirection' , u'BUseUpdateLoadDir' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'UseLargeStrain' , u'BUseLargeStrain' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'UseLargeStrain' , u'BUseLargeStrain' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolderPath' , u'SResultFolderPath' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolderPath' , u'SResultFolderPath' , ), 12, (12, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'ControlMethodType' , u'NType' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'ControlMethodType' , u'NType' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'IterativeMethodType' , u'NType' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'IterativeMethodType' , u'NType' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'IntegrationMethodType' , u'NType' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'IntegrationMethodType' , u'NType' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'GetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 16, (16, (), [ (16389, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 17, (17, (), [ (5, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SetDisplacementControlOptions' , u'DispEntity' , u'NDisplacementComponent' , u'nUnit' , u'ErrorCode' , 
			), 18, (18, (), [ (9, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplacementControlOptions' , u'NDisplacementComponent' , u'nUnit' , ), 19, (19, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 20, (20, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'BValue' , ), 21, (21, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'SetArcLengthCompletionOptions' , u'DMaxLoad' , u'DMaxDisplacement' , u'nUnit' , u'NArcSteps' , 
			u'DArcLenMultiplier' , u'ErrorCode' , ), 22, (22, (), [ (5, 1, None, None) , (5, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'GetArcLengthCompletionOptions' , u'DMaxLoad' , u'DMaxDisplacement' , u'nUnit' , u'NMaxArcSteps' , 
			u'DArcLengthMultiplier' , ), 23, (23, (), [ (16389, 2, None, None) , (16389, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'SetStepToleranceOptions' , u'NEqilibriumIteration' , u'NMaxEqilibriumIteration' , u'DConvTol' , u'DPlasticityTol' , 
			u'NSingularityEleFactor' , u'ErrorCode' , ), 24, (24, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetStepToleranceOptions' , u'NEqilibriumIteration' , u'NMaxEqilibriumIteration' , u'DConvTol' , u'DPlasticityTol' , 
			u'NSingularityEleFactor' , ), 25, (25, (), [ (16387, 2, None, None) , (16387, 2, None, None) , (16389, 2, None, None) , 
			(16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplacementControlOptions2' , u'NDisplacementComponent' , u'nUnit' , u'pDispatch' , ), 26, (26, (), [ 
			(16387, 2, None, None) , (16387, 2, None, None) , (16393, 2, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ICWPinConnector_vtables_dispatch_ = 1
ICWPinConnector_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'AxialStiffnessValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'AxialStiffnessValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'RotationalStiffnessValue' , u'DValue' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'RotationalStiffnessValue' , u'DValue' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTypeWithKey' , u'BValue' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTypeWithKey' , u'BValue' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTypeWithRetainerRing' , u'BValue' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'IncludeTypeWithRetainerRing' , u'BValue' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'IncludeMass' , u'BValue' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'IncludeMass' , u'BValue' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'MassValue' , u'DValue' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'MassValue' , u'DValue' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'IncludeStrengthData' , u'BValue' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'IncludeStrengthData' , u'BValue' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaUnit' , u'NValue' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaUnit' , u'NValue' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaValue' , u'DValue' , ), 10, (10, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'TensileStressAreaValue' , u'DValue' , ), 10, (10, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'PinStrengthUnit' , u'NValue' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'PinStrengthUnit' , u'NValue' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'PinStrengthValue' , u'NValue' , ), 12, (12, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'PinStrengthValue' , u'NValue' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'SafetyFactor' , u'NValue' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'SafetyFactor' , u'NValue' , ), 13, (13, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'MaterialType' , u'NMaterialType' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'MaterialType' , u'NMaterialType' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetLibraryMaterial' , u'SMaterialLibName' , u'SMaterialName' , ), 15, (15, (), [ (16392, 2, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SetLibraryMaterial' , u'SMaterialLibName' , u'SMaterialName' , ), 16, (16, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'PinConnectorBeginEdit' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'PinConnectorEndEdit' , u'ErrorCode' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtFirstLocation' , u'pDispEntity' , ), 19, (19, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtSecondLocation' , u'pDispEntity' , ), 20, (20, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityFromFirstLocation' , u'NIndex' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityFromSecondLocation' , u'NIndex' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetFirstLocationEntityCount' , u'NEntityCount' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'GetSecondLocationEntityCount' , u'NEntityCount' , ), 24, (24, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ICWPressure_vtables_dispatch_ = 1
ICWPressure_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'DirectionType' , u'NDirectionType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'DirectionType' , u'NDirectionType' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'PressureType' , u'NPressureType' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'PressureType' , u'NPressureType' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'IncludeNonUniformDistribution' , u'BInclude' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'IncludeNonUniformDistribution' , u'BInclude' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetNonUniformData' , u'DConstVal' , u'DX' , u'DY' , u'DXY' , 
			u'DXX' , u'DYY' , ), 6, (6, (), [ (16389, 2, None, None) , (16389, 2, None, None) , 
			(16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SetNonUniformData' , u'DConstVal' , u'DX' , u'DY' , u'DXY' , 
			u'DXX' , u'DYY' , ), 7, (7, (), [ (5, 1, None, None) , (5, 1, None, None) , 
			(5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'PressureBeginEdit' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'PressureEndEdit' , u'ErrorCode' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 11, (11, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetReferenceGeometry' , u'RefEntity' , ), 12, (12, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveDate' , u'ErrorCode' , u'BValue' , ), 13, (13, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveDate' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GetCoordinateSystem' , u'DispCoordinateSystem' , ), 15, (15, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SetCoordinateSystem' , u'DispCoordinateSystem' , ), 16, (16, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
]

ICWRadiation_vtables_dispatch_ = 1
ICWRadiation_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Emmisivity' , u'DEmmisivityValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Emmisivity' , u'DEmmisivityValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ViewFactor' , u'DViewFactor' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ViewFactor' , u'DViewFactor' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'AmbientTemperature' , u'DAmbientTemperature' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'AmbientTemperature' , u'DAmbientTemperature' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'OpenSystem' , u'BOpenSystem' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'OpenSystem' , u'BOpenSystem' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'RadiationType' , u'NRadType' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'RadiationType' , u'NRadType' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'RadiationBeginEdit' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'RadiationEndEdit' , u'ErrorCode' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 10, (10, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 11, (11, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 12, (12, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'SetTemperatureCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 13, (13, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GetTemperatureCurve' , u'VarCurveData' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseCurve' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureCurve' , u'BUseCurve' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ICWRemoteLoad_vtables_dispatch_ = 1
ICWRemoteLoad_vtables_ = [
	(( u'LocationUnit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LocationUnit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ForceOrTranslationUnit' , u'nUnit' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ForceOrTranslationUnit' , u'nUnit' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'MomentOrRotationUnit' , u'nUnit' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'MomentOrRotationUnit' , u'nUnit' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'LocationValues' , u'Var' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'LocationValues' , u'Var' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ForceOrTranslationValues' , u'Var' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ForceOrTranslationValues' , u'Var' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'MomentOrRotationValues' , u'Var' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'MomentOrRotationValues' , u'Var' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetMassValues' , u'Var' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetMassValues' , u'Var' , ), 8, (8, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetValueType' , u'NType' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
]

ICWRestraint_vtables_dispatch_ = 1
ICWRestraint_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'RestraintType' , u'NRestraintType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'RestraintType' , u'NRestraintType' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetCoordinateType' , u'NCoordType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'GetTranslationComponentsValues' , u'BVal1' , u'BVal2' , u'BVal3' , u'DVal1' , 
			u'DVal2' , u'DVal3' , ), 4, (4, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetRotationComponentsValues' , u'BVal1' , u'BVal2' , u'BVal3' , u'DVal1' , 
			u'DVal2' , u'DVal3' , ), 5, (5, (), [ (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'RestraintBeginEdit' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RestraintEndEdit' , u'ErrorCode' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 9, (9, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SetReferenceGeometry' , u'DispRefEntity' , ), 10, (10, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetTranslationComponentsValues' , u'BVal1' , u'BVal2' , u'BVal3' , u'DVal1' , 
			u'DVal2' , u'DVal3' , ), 11, (11, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetRotationComponentsValues' , u'BVal1' , u'BVal2' , u'BVal3' , u'DVal1' , 
			u'DVal2' , u'DVal3' , ), 12, (12, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 13, (13, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ICWResults_vtables_dispatch_ = 1
ICWResults_vtables_ = [
	(( u'GetMaximumAvailableSteps' , u'NMaxStepNum' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetStress' , u'NElementNumber' , u'NStepNum' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 2, (2, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetMinMaxStress' , u'NComponent' , u'NElementNumber' , u'NStepNum' , u'DispPlane' , 
			u'NUnits' , u'ErrorCode' , u'RetVal' , ), 3, (3, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'GetStrain' , u'NElementNumber' , u'NStepNum' , u'DispPlane' , u'ErrorCode' , 
			u'RetVal' , ), 4, (4, (), [ (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetMinMaxStrain' , u'NComponent' , u'NElementNumber' , u'NStepNumber' , u'DispPlane' , 
			u'ErrorCode' , u'RetVal' , ), 5, (5, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (9, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'GetTranslationalDisplacement' , u'NStepNumber' , u'DispPlane' , u'NUnits' , u'ErrorCode' , 
			u'RetVal' , ), 6, (6, (), [ (3, 1, None, None) , (9, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetRotationalDisplacement' , u'NStepNumber' , u'DispPlane' , u'NUnits' , u'ErrorCode' , 
			u'RetVal' , ), 7, (7, (), [ (3, 1, None, None) , (9, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'GetReactionForcesAndMoments' , u'NStepNumber' , u'DispPlane' , u'NUnits' , u'ErrorCode' , 
			u'RetVal' , ), 8, (8, (), [ (3, 1, None, None) , (9, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetMinMaxDisplacement' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 9, (9, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'GetResonantFrequencies' , u'ErrorCode' , u'RetVal' , ), 10, (10, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetMassParticipation' , u'ErrorCode' , u'RetVal' , ), 11, (11, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GetBucklingLoadFactors' , u'ErrorCode' , u'RetVal' , ), 12, (12, (), [ (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetThermalValues' , u'NStepNumber' , u'DispPlane' , u'NUnits' , u'ErrorCode' , 
			u'RetVal' , ), 13, (13, (), [ (3, 1, None, None) , (9, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'GetMinMaxThermal' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 14, (14, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetStressComponentForAllStepsAtNode' , u'NComponent' , u'NNodeNum' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 15, (15, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetStrainComponentForAllStepsAtNode' , u'NComponent' , u'NNodeNum' , u'DispPlane' , u'ErrorCode' , 
			u'RetVal' , ), 16, (16, (), [ (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplacementComponentForAllStepsAtNode' , u'NComponent' , u'NNodeNum' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 17, (17, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetThermalComponentForAllStepsAtNode' , u'NComponent' , u'NNodeNum' , u'DispPlane' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 18, (18, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetStressForEntities' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'ArrayArraySelectedEntities' , 
			u'NUnits' , u'ErrorCode' , u'RetVal' , ), 19, (19, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GetStrainForEntities' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'ArraySelectedEntities' , 
			u'ErrorCode' , u'RetVal' , ), 20, (20, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(9, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplacementForEntities' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'ArraySelectedEntities' , 
			u'NUnits' , u'ErrorCode' , u'RetVal' , ), 21, (21, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'GetThermalForEntities' , u'NComponent' , u'NStepNumber' , u'DispPlane' , u'ArraySelectedEntities' , 
			u'NUnits' , u'ErrorCode' , u'RetVal' , ), 22, (22, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetBeamMinMaxStress' , u'NComponent' , u'NStepNumber' , u'NUnits' , u'ErrorCode' , 
			u'RetVal' , ), 23, (23, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'DeletePlot' , u'PlotName' , u'RetVal' , ), 24, (24, (), [ (8, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'ActivatePlot' , u'PlotName' , u'RetVal' , ), 26, (26, (), [ (8, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'GetPlotCount' , u'Count' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetPlotNames' , u'PlotNames' , ), 28, (28, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'IGetPlotNames' , u'Count' , u'PlotNames' , ), 29, (29, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetBeamForcesForEntities' , u'NComponent' , u'NStepNumber' , u'ArraySelectedEntities' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 30, (30, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'GetBeamStressForEntities' , u'NComponent' , u'NStepNumber' , u'ArraySelectedEntities' , u'NUnits' , 
			u'ErrorCode' , u'RetVal' , ), 31, (31, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			(12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetStressForEntities2' , u'bValueByNode' , u'NComponent' , u'NStepNumber' , u'DispPlane' , 
			u'ArrayArraySelectedEntities' , u'NUnits' , u'ErrorCode' , u'RetVal' , ), 32, (32, (), [ 
			(11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , 
			(3, 1, None, None) , (16387, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'GetStrainForEntities2' , u'bValueByNode' , u'NComponent' , u'NStepNumber' , u'DispPlane' , 
			u'ArraySelectedEntities' , u'ErrorCode' , u'RetVal' , ), 33, (33, (), [ (11, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , (12, 1, None, None) , (16387, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ICWRigidConnector_vtables_dispatch_ = 1
ICWRigidConnector_vtables_ = [
	(( u'RigidConnectorBeginEdit' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'RigidConnectorEndEdit' , u'ErrorCode' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityFromFirstLocation' , u'NIndex' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtFirstLocation' , u'DispEntity' , ), 4, (4, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtSecondLocation' , u'DispEntity' , ), 5, (5, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityFromSecondLocation' , u'NIndex' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetFirstLocationEntityCount' , u'NEntityCount' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'GetSecondLocationEntityCount' , u'NEntityCount' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

ICWShell_vtables_dispatch_ = 1
ICWShell_vtables_ = [
	(( u'Name' , u'SName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ShellThickness' , u'DThickness' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ShellThickness' , u'DThickness' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ShellUnit' , u'nUnit' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ShellUnit' , u'nUnit' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Formulation' , u'NFormulation' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Formulation' , u'NFormulation' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'NState' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SetLibraryMaterial' , u'SLibraryPathName' , u'SMaterialName' , u'ErrorCode' , ), 6, (6, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'GetShellMaterial' , u'RetVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultMaterial' , u'RetVal' , ), 8, (8, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SetShellMaterial' , u'MaterialDisp' , u'ErrorCode' , ), 9, (9, (), [ (9, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SuppressUnSuppress' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'EntityCount' , u'NCount' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetEntityAt' , u'NIndex' , u'DispEntity' , ), 12, (12, (), [ (3, 1, None, None) , 
			(16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 13, (13, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ShellBeginEdit' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'ShellEndEdit' , u'ErrorCode' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

ICWShellManager_vtables_dispatch_ = 1
ICWShellManager_vtables_ = [
	(( u'ShellCount' , u'NCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetShellAt' , u'NIndex' , u'ErrorCode' , u'RetVal' , ), 2, (2, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'CreateShell' , u'DispArray' , u'ErrorCode' , ), 3, (3, (), [ (12, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'DeleteShell' , u'SName' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ICWSolidBody_vtables_dispatch_ = 1
ICWSolidBody_vtables_ = [
	(( u'SolidBodyName' , u'SName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultMaterial' , u'RetVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetSolidBodyMaterial' , u'RetVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'SetSolidBodyMaterial' , u'RetVal' , u'ErrorCode' , ), 4, (4, (), [ (9, 1, None, "IID('{BF582064-D953-42DD-AFAD-BBE8364B93B4}')") , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SetLibraryMaterial' , u'SLibWithPathName' , u'SMaterialName' , u'BValue' , ), 5, (5, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ConvertToBeamBody' , u'ErrorCode' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ICWSolidComponent_vtables_dispatch_ = 1
ICWSolidComponent_vtables_ = [
	(( u'SolidBodyCount' , u'NCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ComponentName' , u'SName' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetSolidBodyAt' , u'NIndex' , u'ErrorCode' , u'RetVal' , ), 3, (3, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{699EF572-B1EB-454A-90B7-AF0A52F59E1B}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ICWSolidManager_vtables_dispatch_ = 1
ICWSolidManager_vtables_ = [
	(( u'ComponentCount' , u'NCompCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'GetComponentAt' , u'NIndex' , u'ErrorCode' , u'RetVal' , ), 2, (2, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{16F9E890-CC94-4F7A-B654-30D4CF5E7521}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ICWSpotWeldConnector_vtables_dispatch_ = 1
ICWSpotWeldConnector_vtables_ = [
	(( u'SpotWeldDiameterUnit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SpotWeldDiameterUnit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SpotWeldDiameterValue' , u'DValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'SpotWeldDiameterValue' , u'DValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SpotWeldConnectorBeginEdit' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'SpotWeldConnectorEndEdit' , u'ErrorCode' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceEntityAtFirstFace' , u'pDispEntity' , ), 5, (5, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'ReplaceEntityAtSecondFace' , u'pDispEntity' , ), 6, (6, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'InsertSpotWeldLocations' , u'pDispEntity' , ), 7, (7, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'RemoveSpotWeldLocationAt' , u'NIndex' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetSourceEntityCount' , u'NEntityCount' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'GetTargetEntityCount' , u'NEntityCount' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetSpotWeldLocationCount' , u'NEntityCount' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

ICWSpringConnector_vtables_dispatch_ = 1
ICWSpringConnector_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'StiffnessType' , u'NValue' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'StiffnessType' , u'NValue' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'NormalRadialStiffnessValue' , u'DValue' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'NormalRadialStiffnessValue' , u'DValue' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'TangentialOrShearStiffnessValue' , u'DValue' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'TangentialOrShearStiffnessValue' , u'DValue' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RotationalStiffnessValue' , u'DValue' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'RotationalStiffnessValue' , u'DValue' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceType' , u'NValue' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceType' , u'NValue' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceValue' , u'DValue' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'PreLoadForceValue' , u'DValue' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SpringConnectorBeginEdit' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'SpringConnectorEndEdit' , u'ErrorCode' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtFirstLocation' , u'pDispEntity' , ), 10, (10, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntityAtSecondLocation' , u'pDispEntity' , ), 11, (11, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityAtFirstLocation' , u'NIndex' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntityAtSecondLocation' , u'NIndex' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetSourceEntityCount' , u'NEntityCount' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'GetTargetEntityCount' , u'NEntityCount' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetSpringType' , u'NSpringType' , u'NSpringSubType' , ), 16, (16, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'SetSpringType' , u'NSpringType' , u'NSpringSubType' , ), 17, (17, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ICWStaticStudyOptions_vtables_dispatch_ = 1
ICWStaticStudyOptions_vtables_ = [
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'IncludeGlobalFriction' , u'BIncludeGlobalFriction' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'IncludeGlobalFriction' , u'BIncludeGlobalFriction' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'FrictionCoefficient' , u'DFrictionCoeff' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'FrictionCoefficient' , u'DFrictionCoeff' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'IgnoreClearanceForSurfaceContact' , u'BIgnoreClearacne' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'IgnoreClearanceForSurfaceContact' , u'BIgnoreClearacne' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'LargeDisplacement' , u'BLargeDisplacement' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'LargeDisplacement' , u'BLargeDisplacement' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'ComputeFreeBodyForce' , u'BComputeBodyForce' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ComputeFreeBodyForce' , u'BComputeBodyForce' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'UseInPlaneEffect' , u'BInPlaneEffect' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'UseInPlaneEffect' , u'BInPlaneEffect' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'UseSoftSpring' , u'BUseSoftSpring' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'UseInertialRelief' , u'BUseInertialRelief' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'UseInertialRelief' , u'BUseInertialRelief' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 11, (11, (), [ (16389, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'SetZeroStrainTemperature' , u'DZeroStrainTemperature' , u'NZeroStrainTemperatureUnit' , ), 12, (12, (), [ (5, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ICWStudy_vtables_dispatch_ = 1
ICWStudy_vtables_ = [
	(( u'Name' , u'SName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'MeshType' , u'NMeshType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'AnalysisType' , u'NAnalysisType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Mesh' , u'RetVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{F5818CF4-0C05-49AC-997F-8A0DB432203B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SolidManager' , u'RetVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ShellManager' , u'RetVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{0680FB2B-F938-43C4-92D0-722586C802FD}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ContactManager' , u'RetVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{242B7E91-5A69-4CE1-B429-7008A54F1555}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'LoadsAndRestraintsManager' , u'RetVal' , ), 8, (8, (), [ (16393, 10, None, "IID('{9DEA3C90-44BB-45E0-A569-F4B196F47176}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'CreateMesh' , u'NUnits' , u'NElementSize' , u'NTolerance' , u'ErrorCode' , 
			), 9, (9, (), [ (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'RunAnalysis' , u'ErrorCode' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'UpdateAllComponents' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ThermalStudyOptions' , u'RetVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{43AA3958-9093-4066-BA75-21EA9E206C98}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Results' , u'RetVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'FrequencyStudyOptions' , u'RetVal' , ), 14, (14, (), [ (16393, 10, None, "IID('{268D40CF-565F-4259-B009-BAC3F5DA8F60}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'BucklingStudyOptions' , u'RetVal' , ), 15, (15, (), [ (16393, 10, None, "IID('{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'StaticStudyOptions' , u'RetVal' , ), 16, (16, (), [ (16393, 10, None, "IID('{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'NonLinearStudyOptions' , u'RetVal' , ), 17, (17, (), [ (16393, 10, None, "IID('{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'SetNonLinearStudyOptions' , u'NonLinearOption' , u'ErrorCode' , ), 18, (18, (), [ (9, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'BeamManager' , u'RetVal' , ), 19, (19, (), [ (16393, 10, None, "IID('{D770D195-0FB7-4771-A269-30BD773D393A}')") , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'CreateAnalysisDatabase' , u'sResultPathName' , u'sDataBaseName' , u'ErrorCode' , ), 20, (20, (), [ 
			(8, 1, None, None) , (16392, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'ConnectAnalysisDatabase' , u'sResultPathName' , u'ErrorCode' , ), 21, (21, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
]

ICWStudyManager_vtables_dispatch_ = 1
ICWStudyManager_vtables_ = [
	(( u'ActiveStudy' , u'StudyIndex' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ActiveStudy' , u'StudyIndex' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'StudyCount' , u'RetVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'CreateNewStudy' , u'SName' , u'NAnalysisType' , u'NMeshType' , u'Errors' , 
			u'RetVal' , ), 3, (3, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16393, 10, None, "IID('{999CA1B7-177C-4823-9F0E-A1816C1A003C}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetStudy' , u'NIndex' , u'RetVal' , ), 4, (4, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{999CA1B7-177C-4823-9F0E-A1816C1A003C}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'DeleteStudy' , u'StudyName' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'CreateNewStudy2' , u'SName' , u'NAnalysisType' , u'Errors' , u'RetVal' , 
			), 6, (6, (), [ (8, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16393, 10, None, "IID('{999CA1B7-177C-4823-9F0E-A1816C1A003C}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ICWTemperature_vtables_dispatch_ = 1
ICWTemperature_vtables_ = [
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Unit' , u'nUnit' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureValue' , u'DTempValue' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureValue' , u'DTempValue' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureBeginEdit' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureEndEdit' , u'ErrorCode' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'RemoveEntity' , u'NIndex' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'InsertEntity' , u'DispEntity' , ), 6, (6, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SetTimeCurve' , u'VarCurveData' , u'ErrorCode' , u'BValue' , ), 7, (7, (), [ 
			(12, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'GetTimeCurve' , u'VarCurveData' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseTimeCurve' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'UseTimeCurve' , u'BUseTimeCurve' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureType' , u'NTempType' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'TemperatureType' , u'NTempType' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ICWThermalStudyOptions_vtables_dispatch_ = 1
ICWThermalStudyOptions_vtables_ = [
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SolverType' , u'NSolverType' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SolutionType' , u'NSolutionType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'SolutionType' , u'NSolutionType' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'TotalTime' , u'DTotalTime' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'TotalTime' , u'DTotalTime' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'TimeIncrement' , u'DTimeIncrement' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'TimeIncrement' , u'DTimeIncrement' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ConvergenceTolerance' , u'DConvgTolerance' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ConvergenceTolerance' , u'DConvgTolerance' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'RelaxationFactor' , u'NRelaxFactor' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'RelaxationFactor' , u'NRelaxFactor' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'FixedValue' , u'DFixedValue' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'FixedValue' , u'DFixedValue' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureFromThermalStudy' , u'BUseTemperatureForThermalStudy' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'UseTemperatureFromThermalStudy' , u'BUseTemperatureForThermalStudy' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'ThermalStudyNameUsedForInitialTemperature' , u'SThermalStudyName' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ThermalStudyNameUsedForInitialTemperature' , u'SThermalStudyName' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'TimeSteps' , u'NTimeSteps' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'TimeSteps' , u'NTimeSteps' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 11, (11, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'ResultFolder' , u'SResultFolderPathName' , ), 11, (11, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ICosmosWorks_vtables_dispatch_ = 1
ICosmosWorks_vtables_ = [
	(( u'ActiveDoc' , u'RetVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'VersionNumber' , u'SVersionNo' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ICwAddincallback_vtables_dispatch_ = 1
ICwAddincallback_vtables_ = [
	(( u'NewStudy' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 64 , )),
	(( u'AppUpdate' , u'retCode' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 64 , )),
	(( u'EditDefineMaterial' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 64 , )),
	(( u'EditDefineMaterialUpdate' , u'retCode' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 64 , )),
	(( u'CreateMesh' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 64 , )),
	(( u'StudyUpdate' , u'retCode' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 64 , )),
	(( u'RunAnalysis' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 64 , )),
	(( u'DefineShellBySelectedSurfaces' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
	(( u'ShellUpdate' , u'retCode' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 64 , )),
	(( u'DefineMeshControl' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( u'DefineGlobalContact' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 64 , )),
	(( u'ContactUpdate' , u'retCode' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( u'DefineContactSet' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 64 , )),
	(( u'DropTestSetup' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( u'DropTestSetUpdate' , u'retCode' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 64 , )),
	(( u'DropTestResultOptions' , ), 16, (16, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( u'DropTestResultOptionsUpdate' , u'retCode' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 64 , )),
	(( u'LoadsAndRestraintsUpdate' , u'retCode' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( u'DefineRestraints' , ), 19, (19, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 64 , )),
	(( u'DefinePressures' , ), 20, (20, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( u'DefineForces' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 64 , )),
	(( u'DefineGravity' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( u'DefineCentriFugal' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 64 , )),
	(( u'DefineRemoteLoads' , ), 24, (24, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( u'DefineRigidConnections' , ), 25, (25, (), [ ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 64 , )),
	(( u'DefineBearingLoads' , ), 26, (26, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
	(( u'LoadsAndRestraintsUpdate2' , u'retCode' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 64 , )),
	(( u'DefineTemperature' , ), 28, (28, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsDesignCheck' , ), 29, (29, (), [ ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 64 , )),
	(( u'StaticPostResultsUpdate' , u'retCode' , ), 30, (30, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( u'PlotStress' , ), 31, (31, (), [ ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 64 , )),
	(( u'PlotDisplacement' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( u'PlotStrain' , ), 33, (33, (), [ ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 64 , )),
	(( u'PlotThermal' , ), 34, (34, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( u'CommonPostResultsUpdate' , u'retCode' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 64 , )),
	(( u'CommonPostResultsUpdate2' , u'retCode' , ), 36, (36, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( u'ThermPostResultsUpdate' , u'retCode' , ), 37, (37, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 64 , )),
	(( u'ReportTemplate' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsAnimate' , ), 39, (39, (), [ ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateAnimate' , u'retCode' , ), 40, (40, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsClipping' , ), 41, (41, (), [ ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateClippingSec' , u'retCode' , ), 43, (43, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsClippingIso' , ), 44, (44, (), [ ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateClippingIso' , u'retCode' , ), 45, (45, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsSettings' , ), 46, (46, (), [ ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateSettings' , u'retCode' , ), 47, (47, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsProbe' , ), 48, (48, (), [ ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateProbe' , u'retCode' , ), 49, (49, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsListSelected' , ), 50, (50, (), [ ], 1 , 1 , 4 , 0 , 220 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateListSelected' , u'retCode' , ), 51, (51, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsSaveAs' , ), 52, (52, (), [ ], 1 , 1 , 4 , 0 , 228 , (3, 0, None, None) , 64 , )),
	(( u'ToggleDisplay' , ), 53, (53, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( u'TogglePostMode' , ), 54, (54, (), [ ], 1 , 1 , 4 , 0 , 236 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdatePostMode' , u'retCode' , ), 55, (55, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( u'DefineConvection' , ), 56, (56, (), [ ], 1 , 1 , 4 , 0 , 244 , (3, 0, None, None) , 64 , )),
	(( u'DefineHeatPower' , ), 57, (57, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( u'DefineHeatFlux' , ), 58, (58, (), [ ], 1 , 1 , 4 , 0 , 252 , (3, 0, None, None) , 64 , )),
	(( u'DefineRadiation' , ), 59, (59, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( u'ThermalStudyLoadsAndRestraintsUpdate' , u'retCode' , ), 60, (60, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 260 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsReactionForce' , ), 61, (61, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsContactForce' , ), 62, (62, (), [ ], 1 , 1 , 4 , 0 , 268 , (3, 0, None, None) , 64 , )),
	(( u'ResultToolsPinForce' , ), 63, (63, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 64 , )),
	(( u'CommonPostResultsUpdate3' , u'retCode' , ), 64, (64, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 64 , )),
	(( u'ListModeShape' , ), 65, (65, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( u'FreqPostResultsUpdate' , u'retCode' , ), 66, (66, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 64 , )),
	(( u'DefineResponseGraph' , ), 67, (67, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( u'NonlinearPostResultsUpdate' , u'retCode' , ), 68, (68, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 292 , (3, 0, None, None) , 64 , )),
	(( u'Parameters' , ), 69, (69, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( u'EditDefineDesignScenario' , ), 70, (70, (), [ ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 64 , )),
	(( u'UpdateDesignScenario' , u'retCode' , ), 71, (71, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( u'RunDesidnScenario' , ), 72, (72, (), [ ], 1 , 1 , 4 , 0 , 308 , (3, 0, None, None) , 64 , )),
	(( u'DesignResultShowSummary' , ), 73, (73, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( u'UpdateDesignResult' , u'retCode' , ), 74, (74, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 316 , (3, 0, None, None) , 64 , )),
	(( u'DefineDesignResultGraph' , ), 75, (75, (), [ ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( u'DefineOptObjective' , ), 76, (76, (), [ ], 1 , 1 , 4 , 0 , 324 , (3, 0, None, None) , 64 , )),
	(( u'DefineOptDesignVar' , ), 77, (77, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( u'DefineOptConstraint' , ), 78, (78, (), [ ], 1 , 1 , 4 , 0 , 332 , (3, 0, None, None) , 64 , )),
	(( u'OptimizationStudyUpdate' , u'retCode' , ), 79, (79, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( u'OptDesignCycleResults' , ), 80, (80, (), [ ], 1 , 1 , 4 , 0 , 340 , (3, 0, None, None) , 64 , )),
	(( u'OptDesignHistoryGraph' , ), 81, (81, (), [ ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( u'OptLocalTrendGraph' , ), 82, (82, (), [ ], 1 , 1 , 4 , 0 , 348 , (3, 0, None, None) , 64 , )),
	(( u'ChangeFatigueEventType' , ), 83, (83, (), [ ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( u'AddFatigueEvent' , ), 84, (84, (), [ ], 1 , 1 , 4 , 0 , 356 , (3, 0, None, None) , 64 , )),
	(( u'FatigueStudyUpdate' , u'retCode' , ), 85, (85, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( u'FatigueDefinePlot' , ), 86, (86, (), [ ], 1 , 1 , 4 , 0 , 364 , (3, 0, None, None) , 64 , )),
	(( u'FatigueList' , ), 87, (87, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( u'FatiguePlotUpdate' , u'retCode' , ), 88, (88, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 372 , (3, 0, None, None) , 64 , )),
	(( u'TemperatureUpdate' , u'retCode' , ), 89, (89, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 64 , )),
	(( u'StudyRunUpdate' , u'retCode' , ), 90, (90, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 380 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdate' , u'retCode' , ), 91, (91, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( u'appCallbackFunction' , u'cmd' , u'data' , u'dsp' , u'retCode' , 
			), 92, (92, (), [ (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 388 , (3, 0, None, None) , 64 , )),
	(( u'AutomatedTest' , u'ArgList' , u'RetVal' , ), 93, (93, (), [ (12, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 64 , )),
	(( u'RunCosworksBackOffice' , u'ArgList' , u'RetVal' , ), 94, (94, (), [ (12, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 396 , (3, 0, None, None) , 64 , )),
	(( u'LoadsAndRestraintsUpdate3' , u'retCode' , ), 95, (95, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 64 , )),
	(( u'MeshControlUpdate' , u'retCode' , ), 96, (96, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 404 , (3, 0, None, None) , 64 , )),
	(( u'CommonPostResultsUpdateBeam' , u'retCode' , ), 97, (97, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 64 , )),
	(( u'CommonPostResultsUpdateBeam2' , u'retCode' , ), 98, (98, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 412 , (3, 0, None, None) , 64 , )),
	(( u'ReportUpdate' , u'retCode' , ), 99, (99, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 64 , )),
	(( u'CosmosWorks' , u'RetVal' , ), 100, (100, (), [ (16393, 10, None, "IID('{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}')") , ], 1 , 2 , 4 , 0 , 420 , (3, 0, None, None) , 0 , )),
	(( u'TrendTracker' , ), 101, (101, (), [ ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 64 , )),
	(( u'TrendTrackerUpdate' , u'retCode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 428 , (3, 0, None, None) , 64 , )),
	(( u'SetBaseline' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 64 , )),
	(( u'SetBaselineUpdate' , u'retCode' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 436 , (3, 0, None, None) , 64 , )),
	(( u'AddTrackedDataGraph' , ), 105, (105, (), [ ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 64 , )),
	(( u'AddTrackedDataGraphUpdate' , u'retCode' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 444 , (3, 0, None, None) , 64 , )),
	(( u'AddUniformBaseExcitation' , ), 107, (107, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 64 , )),
	(( u'AddUniformBaseExcitationUpdate' , u'retCode' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 452 , (3, 0, None, None) , 64 , )),
	(( u'AddSelectBaseExcitation' , ), 109, (109, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 64 , )),
	(( u'AddSelectBaseExcitationUpdate' , u'retCode' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 460 , (3, 0, None, None) , 64 , )),
	(( u'AddInitialCondition' , ), 111, (111, (), [ ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 64 , )),
	(( u'AddInitialConditionUpdate' , u'retCode' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 468 , (3, 0, None, None) , 64 , )),
	(( u'AddGlobalDamping' , ), 113, (113, (), [ ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 64 , )),
	(( u'AddGlobalDampingUpdate' , u'retCode' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 476 , (3, 0, None, None) , 64 , )),
	(( u'ToggleDeformMode' , ), 115, (115, (), [ ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 64 , )),
	(( u'PostResultsUpdateDeformMode' , u'retCode' , ), 116, (116, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 484 , (3, 0, None, None) , 64 , )),
	(( u'PostResultCompareIn4Viewports' , ), 117, (117, (), [ ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 64 , )),
	(( u'PostResultCompareIn4ViewportsUpdate' , u'retCode' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 492 , (3, 0, None, None) , 64 , )),
	(( u'HelpErrCallback' , u'mainProduct' , u'helpFile' , u'helpTopic' , u'topicFile' , 
			), 119, (119, (), [ (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 64 , )),
	(( u'ContactSetUpdate' , u'retCode' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 500 , (3, 0, None, None) , 64 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{C2C96FB8-EAE7-4BE3-9DFF-D7B3D2A37A0F}' : CWJoints,
	'{FCB82093-3377-4C4C-9DFE-FEDD6B0B1E51}' : CWShell,
	'{7BDD45B4-9046-4C42-8936-A988906D2597}' : ICWLoadsAndRestraints,
	'{54B982A6-721E-4305-ADF3-934EAA6D7113}' : CWStudy,
	'{25E6E227-6678-419F-81F2-1A97FEF0583D}' : CWTemperature,
	'{96212552-8F0F-47F9-BC8F-C712081CAAD2}' : CWMeshControl,
	'{4B6D9839-B25E-4FCE-AE50-47BFF0545125}' : CWShellManager,
	'{999CA1B7-177C-4823-9F0E-A1816C1A003C}' : ICWStudy,
	'{699EF572-B1EB-454A-90B7-AF0A52F59E1B}' : ICWSolidBody,
	'{43AA3958-9093-4066-BA75-21EA9E206C98}' : ICWThermalStudyOptions,
	'{807A0872-ACA1-43A7-86F6-6D07B1989262}' : CWGravity,
	'{EC3DF67D-5D46-45AB-8505-69670841F5BF}' : CWBeamBody,
	'{242B7E91-5A69-4CE1-B429-7008A54F1555}' : ICWContactManager,
	'{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}' : ICWResults,
	'{D77721DD-8FE5-45EB-92B6-FC8106968473}' : ICWHeatFlux,
	'{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}' : ICWJoints,
	'{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}' : ICWContactSet,
	'{D770D195-0FB7-4771-A269-30BD773D393A}' : ICWBeamManager,
	'{61B4C22E-99B9-484D-BF0E-5C9FC1BA3B3A}' : CWCentriFugalForce,
	'{A7FE706C-70D4-49AD-9994-9E7139DE59A7}' : CWBucklingStudyOptions,
	'{0A75503A-136F-430C-95E0-904D33F2A68C}' : CWRigidConnector,
	'{DBFEC66A-A413-4EB3-8A15-8F927274FECF}' : CWContactManager,
	'{7EBC954D-4620-418D-8740-58D288545A34}' : CWHeatFlux,
	'{F9A4678F-9919-4435-B903-16A426E87B64}' : CWBoltConnector,
	'{13527C80-537C-4F69-94F8-BC09F9755CC6}' : CosmosWorks,
	'{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}' : ICWContactComponent,
	'{A5780715-A450-40CF-B435-7A7F756B094A}' : CWPinConnector,
	'{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}' : ICWConvection,
	'{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}' : ICWShell,
	'{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}' : ICWSolidManager,
	'{9F335011-F5A5-4992-AA03-3BEC3BDF0436}' : ICWCentriFugalForce,
	'{BF582064-D953-42DD-AFAD-BBE8364B93B4}' : ICWMaterial,
	'{AE787538-A050-4BBB-A27E-DB327C00848A}' : CWContactSet,
	'{49EEE451-912D-444C-BB23-A6976F71AA25}' : ICwAddincallback,
	'{16F9E890-CC94-4F7A-B654-30D4CF5E7521}' : ICWSolidComponent,
	'{E240A061-9543-4D8A-8749-2C9C850F7035}' : ICWBearingLoad,
	'{A6934603-2339-4B84-A510-E7ADE2AE7320}' : CWContactComponent,
	'{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}' : ICWModelDoc,
	'{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}' : ICWTemperature,
	'{9F100027-4912-4FDC-8386-8C9F0F6F11F3}' : CWPressure,
	'{F932F397-D186-4381-88EF-EAA92E2ADCAE}' : ICWGravity,
	'{96DD49CD-CC09-4FAE-A559-7A795983D6EB}' : ICWSpringConnector,
	'{C75C8C1A-1A4E-4E39-835E-32A4F36D6176}' : CWSolidComponent,
	'{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}' : ICWPinConnector,
	'{07C2C408-612E-428F-8FD6-13230EF8D878}' : CWBearingLoad,
	'{DC9FEC33-1B9A-40DA-A21A-713C86F44AE7}' : CWRestraint,
	'{9E273951-C865-45F6-89F9-7DAAB971010E}' : ICWRemoteLoad,
	'{F66EE586-499C-424B-A547-F51337C6D6C3}' : CWHeatPower,
	'{864CF3FA-5753-46F2-9F86-F1CC135F27A0}' : CWConvection,
	'{55AC868A-F6C1-4DB4-8472-F88F3DB1B05F}' : CWElasticConnector,
	'{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}' : ICWBeamBody,
	'{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}' : ICWStudyManager,
	'{61C7F978-1602-4D64-859E-88F728DB7E36}' : CWSolidBody,
	'{19951FA7-A7F4-41C0-964A-0F79FA2A5D99}' : CWLinkConnector,
	'{675024F4-3BEB-465F-9747-50CDB6E6FD43}' : CWMaterial,
	'{92D96050-0852-4B82-BFEA-82D3CC6FEEC4}' : CWSolidManager,
	'{8E88103F-7AE3-45FF-B517-AC6E5CCED6B8}' : CWNonLinearStudyOptions,
	'{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}' : ICWBucklingStudyOptions,
	'{B16AF523-9A34-460F-AF2E-670D3559522D}' : CWResults,
	'{9D21C234-564F-4C51-8513-A6F93697E7DE}' : CWStudyManager,
	'{F5818CF4-0C05-49AC-997F-8A0DB432203B}' : ICWMesh,
	'{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}' : ICWNonLinearStudyOptions,
	'{AB747841-0F4F-4C92-A357-855616AE7B9C}' : CWStaticStudyOptions,
	'{DA0FB97E-1DB2-4F38-B9CE-F57A6215B772}' : CWRemoteLoad,
	'{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}' : ICosmosWorks,
	'{3D12186F-4CAE-4511-9456-B42FB68F06F9}' : ICWPressure,
	'{E399CE1B-28ED-48A3-A86E-A797C6556E43}' : CWFrequencyStudyOptions,
	'{0680FB2B-F938-43C4-92D0-722586C802FD}' : ICWShellManager,
	'{9419308B-BB2A-4842-B652-7AF115171012}' : ICWForce,
	'{9DEA3C90-44BB-45E0-A569-F4B196F47176}' : ICWLoadsAndRestraintsManager,
	'{53F66937-4219-456B-89B1-6AF4BD7C022C}' : CWBeamManager,
	'{A1B7607C-2C6B-447B-8183-633531BFDDAF}' : ICWRestraint,
	'{A78EC78E-A6AB-4435-B0DA-9069B090FF37}' : CWThermalStudyOptions,
	'{5A355F90-47EB-4A23-824C-F2379DD92252}' : ICWElasticConnector,
	'{4425FB13-4541-4079-820E-0B4AC73E5231}' : CWLoadsAndRestraintsManager,
	'{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}' : ICWStaticStudyOptions,
	'{EAFBFF38-E6B9-43D7-BE10-FE2BF2C8C0C8}' : CWModelDoc,
	'{270F9491-0450-4BB5-BEF5-6E520C01D9AF}' : ICWMeshControl,
	'{D83BBFB8-2E93-4581-B061-D356B67DC5C7}' : CWForce,
	'{5068060C-F268-4C97-A6A7-D6F89C51159E}' : CWSpotWeldConnector,
	'{12FE135D-F7ED-41C7-9A15-42556526A9A9}' : CWLoadsAndRestraints,
	'{86C8808E-7661-4FDF-AF75-63EA21F94D3D}' : CWSpringConnector,
	'{756B2585-6350-460A-9C2A-7F25DA9D094A}' : ICWSpotWeldConnector,
	'{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}' : ICWRigidConnector,
	'{268D40CF-565F-4259-B009-BAC3F5DA8F60}' : ICWFrequencyStudyOptions,
	'{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}' : ICWBoltConnector,
	'{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}' : ICWHeatPower,
	'{4405E07F-4621-4481-B925-449A88051523}' : CwAddincallback,
	'{0844A890-EB4C-434E-BECB-91374A38C531}' : CWMesh,
	'{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}' : ICWLinkConnector,
	'{333D8E64-BA1A-4008-8F28-C27B9C41FCEF}' : CWRadiation,
	'{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}' : ICWRadiation,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{9419308B-BB2A-4842-B652-7AF115171012}' : 'ICWForce',
	'{9DEA3C90-44BB-45E0-A569-F4B196F47176}' : 'ICWLoadsAndRestraintsManager',
	'{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}' : 'ICWContactComponent',
	'{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}' : 'ICWShell',
	'{7BDD45B4-9046-4C42-8936-A988906D2597}' : 'ICWLoadsAndRestraints',
	'{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}' : 'ICWSolidManager',
	'{A1B7607C-2C6B-447B-8183-633531BFDDAF}' : 'ICWRestraint',
	'{5A355F90-47EB-4A23-824C-F2379DD92252}' : 'ICWElasticConnector',
	'{9F335011-F5A5-4992-AA03-3BEC3BDF0436}' : 'ICWCentriFugalForce',
	'{BF582064-D953-42DD-AFAD-BBE8364B93B4}' : 'ICWMaterial',
	'{268D40CF-565F-4259-B009-BAC3F5DA8F60}' : 'ICWFrequencyStudyOptions',
	'{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}' : 'ICWStaticStudyOptions',
	'{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}' : 'ICWBeamBody',
	'{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}' : 'ICWTemperature',
	'{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}' : 'ICWStudyManager',
	'{49EEE451-912D-444C-BB23-A6976F71AA25}' : 'ICwAddincallback',
	'{16F9E890-CC94-4F7A-B654-30D4CF5E7521}' : 'ICWSolidComponent',
	'{270F9491-0450-4BB5-BEF5-6E520C01D9AF}' : 'ICWMeshControl',
	'{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}' : 'ICosmosWorks',
	'{E240A061-9543-4D8A-8749-2C9C850F7035}' : 'ICWBearingLoad',
	'{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}' : 'ICWBucklingStudyOptions',
	'{999CA1B7-177C-4823-9F0E-A1816C1A003C}' : 'ICWStudy',
	'{699EF572-B1EB-454A-90B7-AF0A52F59E1B}' : 'ICWSolidBody',
	'{43AA3958-9093-4066-BA75-21EA9E206C98}' : 'ICWThermalStudyOptions',
	'{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}' : 'ICWModelDoc',
	'{F5818CF4-0C05-49AC-997F-8A0DB432203B}' : 'ICWMesh',
	'{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}' : 'ICWNonLinearStudyOptions',
	'{756B2585-6350-460A-9C2A-7F25DA9D094A}' : 'ICWSpotWeldConnector',
	'{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}' : 'ICWRigidConnector',
	'{F932F397-D186-4381-88EF-EAA92E2ADCAE}' : 'ICWGravity',
	'{96DD49CD-CC09-4FAE-A559-7A795983D6EB}' : 'ICWSpringConnector',
	'{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}' : 'ICWBoltConnector',
	'{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}' : 'ICWResults',
	'{D77721DD-8FE5-45EB-92B6-FC8106968473}' : 'ICWHeatFlux',
	'{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}' : 'ICWHeatPower',
	'{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}' : 'ICWJoints',
	'{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}' : 'ICWContactSet',
	'{D770D195-0FB7-4771-A269-30BD773D393A}' : 'ICWBeamManager',
	'{3D12186F-4CAE-4511-9456-B42FB68F06F9}' : 'ICWPressure',
	'{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}' : 'ICWConvection',
	'{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}' : 'ICWPinConnector',
	'{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}' : 'ICWLinkConnector',
	'{242B7E91-5A69-4CE1-B429-7008A54F1555}' : 'ICWContactManager',
	'{9E273951-C865-45F6-89F9-7DAAB971010E}' : 'ICWRemoteLoad',
	'{0680FB2B-F938-43C4-92D0-722586C802FD}' : 'ICWShellManager',
	'{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}' : 'ICWRadiation',
}


NamesToIIDMap = {
	'ICWSpotWeldConnector' : '{756B2585-6350-460A-9C2A-7F25DA9D094A}',
	'ICWShell' : '{34E51079-B9CD-4FD3-B862-E4EC94DDBE13}',
	'ICWBearingLoad' : '{E240A061-9543-4D8A-8749-2C9C850F7035}',
	'ICWShellManager' : '{0680FB2B-F938-43C4-92D0-722586C802FD}',
	'ICWSolidComponent' : '{16F9E890-CC94-4F7A-B654-30D4CF5E7521}',
	'ICWStudy' : '{999CA1B7-177C-4823-9F0E-A1816C1A003C}',
	'ICWMesh' : '{F5818CF4-0C05-49AC-997F-8A0DB432203B}',
	'ICWConvection' : '{45DADB3D-E02B-4A7B-9BF0-D5536A3680A7}',
	'ICWRestraint' : '{A1B7607C-2C6B-447B-8183-633531BFDDAF}',
	'ICWStaticStudyOptions' : '{62C99DD5-374D-4444-B8F3-4163C5F6FB6F}',
	'ICWGravity' : '{F932F397-D186-4381-88EF-EAA92E2ADCAE}',
	'ICWHeatPower' : '{9D89A6CF-C25E-4F41-8CB1-1F5722FD6DC3}',
	'ICWFrequencyStudyOptions' : '{268D40CF-565F-4259-B009-BAC3F5DA8F60}',
	'ICWBeamManager' : '{D770D195-0FB7-4771-A269-30BD773D393A}',
	'ICWSolidManager' : '{B9D3E9AB-01A4-4B1C-A609-79E6A11D79C5}',
	'ICWLoadsAndRestraints' : '{7BDD45B4-9046-4C42-8936-A988906D2597}',
	'ICosmosWorks' : '{E6F43AD9-2A3B-498D-B2D3-B8EA97AED8D8}',
	'ICWJoints' : '{6FFA493C-E5DC-4BA4-A0F6-F838A41A1563}',
	'ICWMeshControl' : '{270F9491-0450-4BB5-BEF5-6E520C01D9AF}',
	'ICWModelDoc' : '{B07A5588-BDE6-420D-9A02-BBB8BC822D1B}',
	'ICWContactComponent' : '{E739B4C6-B6A5-4C1D-830A-C7A29C746A46}',
	'ICWRemoteLoad' : '{9E273951-C865-45F6-89F9-7DAAB971010E}',
	'ICWStudyManager' : '{C9C3BEAB-0B21-41C1-8B44-2DE3CF28A03E}',
	'ICWElasticConnector' : '{5A355F90-47EB-4A23-824C-F2379DD92252}',
	'ICWLinkConnector' : '{63F1A46F-2BDE-4367-83A1-FA3A22FCA775}',
	'ICWMaterial' : '{BF582064-D953-42DD-AFAD-BBE8364B93B4}',
	'ICWBucklingStudyOptions' : '{8B6B0702-61D6-4C9B-9A1F-1FAAC4DCF0E4}',
	'ICWNonLinearStudyOptions' : '{F7A7474A-BAA4-45BC-A752-3D06B294EAA4}',
	'ICWRadiation' : '{EB7E570D-AAF9-4925-AC3A-91C54A699DCD}',
	'ICWRigidConnector' : '{05882CCB-5A00-4CD5-B77F-8D374DEFEEAD}',
	'ICWThermalStudyOptions' : '{43AA3958-9093-4066-BA75-21EA9E206C98}',
	'ICWLoadsAndRestraintsManager' : '{9DEA3C90-44BB-45E0-A569-F4B196F47176}',
	'ICWSolidBody' : '{699EF572-B1EB-454A-90B7-AF0A52F59E1B}',
	'ICWResults' : '{C5AC1F26-0CD1-4A33-81D3-571ADE6A7ECD}',
	'ICWPinConnector' : '{1CDE52B5-1CA2-486A-AABB-093CED1BDF61}',
	'ICWBoltConnector' : '{9BA4876E-EFB8-45C6-B0FB-BF93FF54C065}',
	'ICWForce' : '{9419308B-BB2A-4842-B652-7AF115171012}',
	'ICWPressure' : '{3D12186F-4CAE-4511-9456-B42FB68F06F9}',
	'ICWTemperature' : '{94DD4C40-F7FA-47E3-BA06-BFEFD28F8E62}',
	'ICwAddincallback' : '{49EEE451-912D-444C-BB23-A6976F71AA25}',
	'ICWBeamBody' : '{BE3D86C7-8AD9-463F-A134-8B70E114BF1B}',
	'ICWCentriFugalForce' : '{9F335011-F5A5-4992-AA03-3BEC3BDF0436}',
	'ICWContactSet' : '{0ED1F73C-9EAC-4D6A-9CCA-B637D9C9A0CB}',
	'ICWHeatFlux' : '{D77721DD-8FE5-45EB-92B6-FC8106968473}',
	'ICWSpringConnector' : '{96DD49CD-CC09-4FAE-A559-7A795983D6EB}',
	'ICWContactManager' : '{242B7E91-5A69-4CE1-B429-7008A54F1555}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

