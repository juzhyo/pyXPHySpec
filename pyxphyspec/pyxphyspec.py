# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# From type library 'xphyspec.exe'
# On Tue Jan 18 13:33:45 2022
'xphyspec 2.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x30808f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{0DDCEB0A-8516-49B0-BF9C-B3D032466D31}')
MajorVersion = 2
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	ClickFocus                    =2          # from enum FocusPolicy
	NoFocus                       =0          # from enum FocusPolicy
	StrongFocus                   =11         # from enum FocusPolicy
	TabFocus                      =1          # from enum FocusPolicy
	WheelFocus                    =15         # from enum FocusPolicy
	ArrowCursor                   =0          # from enum MousePointer
	BlankCursor                   =10         # from enum MousePointer
	BusyCursor                    =16         # from enum MousePointer
	CrossCursor                   =2          # from enum MousePointer
	ForbiddenCursor               =14         # from enum MousePointer
	IBeamCursor                   =4          # from enum MousePointer
	PointingHandCursor            =13         # from enum MousePointer
	SizeAllCursor                 =9          # from enum MousePointer
	SizeBDiagCursor               =7          # from enum MousePointer
	SizeFDiagCursor               =8          # from enum MousePointer
	SizeHorCursor                 =6          # from enum MousePointer
	SizeVerCursor                 =5          # from enum MousePointer
	SplitHCursor                  =12         # from enum MousePointer
	SplitVCursor                  =11         # from enum MousePointer
	UpArrowCursor                 =1          # from enum MousePointer
	WaitCursor                    =3          # from enum MousePointer
	WhatsThisCursor               =15         # from enum MousePointer

from win32com.client import DispatchBaseClass
class IXPHySpecAndorIxon(DispatchBaseClass):
	'XPHySpecAndorIxon Interface'
	CLSID = IID('{A3EF76AB-75D5-4ECA-B794-00C2C8CDF35C}')
	coclass_clsid = IID('{2C85E8A5-0E6B-4D4A-AEDF-D54B3459844A}')

	def CloseShutter(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), (),)

	def GetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._ApplyTypes_(18, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetBinning', None,p_horizontal
			, p_vertical)

	def GetDetectorSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(17, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetDetectorSize', None,p_width
			, p_height)

	def GetEMGainsRange(self, p_minimum=defaultNamedNotOptArg, p_maximum=defaultNamedNotOptArg):
		return self._ApplyTypes_(22, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetEMGainsRange', None,p_minimum
			, p_maximum)

	def GetExposureRange(self, p_minimum=defaultNamedNotOptArg, p_maximum=defaultNamedNotOptArg):
		return self._ApplyTypes_(16, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetExposureRange', None,p_minimum
			, p_maximum)

	def GetPixelSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(15, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetPixelSize', None,p_width
			, p_height)

	def GetROISize(self, p_ROIWidth=defaultNamedNotOptArg, p_ROIHeight=defaultNamedNotOptArg):
		return self._ApplyTypes_(20, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROISize', None,p_ROIWidth
			, p_ROIHeight)

	def GetROIStart(self, p_x=defaultNamedNotOptArg, p_y=defaultNamedNotOptArg):
		return self._ApplyTypes_(21, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROIStart', None,p_x
			, p_y)

	def OpenShutter(self):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), (),)

	def SetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((3, 1), (3, 1)),p_horizontal
			, p_vertical)

	def SetCoolerTemp(self, p_Temperature=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((5, 1),),p_Temperature
			)

	def SetEMGain(self, p_EMGain=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((19, 1),),p_EMGain
			)

	def SetOutputAmpType(self, p_AmplifierType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((19, 1),),p_AmplifierType
			)

	def SetReadOutResolution(self, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),p_resolution
			)

	def SetVerticalAmplitude(self, p_VAmplitude=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((19, 1),),p_VAmplitude
			)

	def TakeSinglePicture(self, p_ExposureTime=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((5, 1),),p_ExposureTime
			)

	_prop_map_get_ = {
		"AvailablePreAmpGains": (11, 2, (8204, 0), (), "AvailablePreAmpGains", None),
		"CameraName": (2, 2, (8, 0), (), "CameraName", None),
		"CoolerAvailable": (4, 2, (11, 0), (), "CoolerAvailable", None),
		"CoolerOn": (8, 2, (11, 0), (), "CoolerOn", None),
		"CurrentReadOutSpeed": (9, 2, (5, 0), (), "CurrentReadOutSpeed", None),
		"LastImageTaken": (1, 2, (8209, 0), (), "LastImageTaken", None),
		"PreAmpGain": (10, 2, (5, 0), (), "PreAmpGain", None),
		"ReadoutResolutions": (5, 2, (8204, 0), (), "ReadoutResolutions", None),
		"ReadoutSpeeds": (6, 2, (8204, 0), (), "ReadoutSpeeds", None),
		"Status": (7, 2, (3, 0), (), "Status", None),
		"Temperature": (3, 2, (5, 0), (), "Temperature", None),
		"VerticalSpeed": (12, 2, (5, 0), (), "VerticalSpeed", None),
	}
	_prop_map_put_ = {
		"AvailablePreAmpGains" : ((11, LCID, 4, 0),()),
		"CameraName" : ((2, LCID, 4, 0),()),
		"CoolerAvailable" : ((4, LCID, 4, 0),()),
		"CoolerOn" : ((8, LCID, 4, 0),()),
		"CurrentReadOutSpeed" : ((9, LCID, 4, 0),()),
		"LastImageTaken" : ((1, LCID, 4, 0),()),
		"PreAmpGain" : ((10, LCID, 4, 0),()),
		"ReadoutResolutions" : ((5, LCID, 4, 0),()),
		"ReadoutSpeeds" : ((6, LCID, 4, 0),()),
		"Status" : ((7, LCID, 4, 0),()),
		"Temperature" : ((3, LCID, 4, 0),()),
		"VerticalSpeed" : ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecAndorIxonEvents:
	'XPHySpecAndorIxon Events Interface'
	CLSID = CLSID_Sink = IID('{02A4C8CD-F1E3-4DA3-A79F-E4EA68E25799}')
	coclass_clsid = IID('{2C85E8A5-0E6B-4D4A-AEDF-D54B3459844A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnImageReceived",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrorCode=defaultNamedNotOptArg, p_ErrMessage=defaultNamedNotOptArg):
#	def OnImageReceived(self):


class IXPHySpecApogee(DispatchBaseClass):
	'XPHySpecApogee Interface'
	CLSID = IID('{26CA5819-80BE-4F05-9DDF-C10477669586}')
	coclass_clsid = IID('{88A5D497-C66D-4DB3-8331-420EE8A57AC4}')

	def CloseShutter(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), (),)

	def GetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._ApplyTypes_(17, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetBinning', None,p_horizontal
			, p_vertical)

	def GetDetectorSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(16, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetDetectorSize', None,p_width
			, p_height)

	def GetExposureRange(self, p_minimum=defaultNamedNotOptArg, p_maximum=defaultNamedNotOptArg):
		return self._ApplyTypes_(15, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetExposureRange', None,p_minimum
			, p_maximum)

	def GetPixelSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(14, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetPixelSize', None,p_width
			, p_height)

	def GetROISize(self, p_ROIWidth=defaultNamedNotOptArg, p_ROIHeight=defaultNamedNotOptArg):
		return self._ApplyTypes_(19, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROISize', None,p_ROIWidth
			, p_ROIHeight)

	def GetROIStart(self, p_x=defaultNamedNotOptArg, p_y=defaultNamedNotOptArg):
		return self._ApplyTypes_(20, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROIStart', None,p_x
			, p_y)

	def OpenShutter(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), (),)

	def SetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 1), (3, 1)),p_horizontal
			, p_vertical)

	def SetCoolerOn(self, p_On=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((11, 1),),p_On
			)

	def SetReadOutResolution(self, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),p_resolution
			)

	def TakeSinglePicture(self, p_ExposureTime=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((5, 1),),p_ExposureTime
			)

	_prop_map_get_ = {
		"CameraName": (2, 2, (8, 0), (), "CameraName", None),
		"CoolerAvailable": (4, 2, (11, 0), (), "CoolerAvailable", None),
		"CoolerTemperature": (8, 2, (5, 0), (), "CoolerTemperature", None),
		"CurrentReadOutSpeed": (9, 2, (5, 0), (), "CurrentReadOutSpeed", None),
		"Gain": (10, 2, (19, 0), (), "Gain", None),
		"LastImageTaken": (1, 2, (8209, 0), (), "LastImageTaken", None),
		"Offset": (11, 2, (19, 0), (), "Offset", None),
		"ReadoutResolutions": (5, 2, (8204, 0), (), "ReadoutResolutions", None),
		"ReadoutSpeeds": (6, 2, (8204, 0), (), "ReadoutSpeeds", None),
		"Status": (7, 2, (3, 0), (), "Status", None),
		"Temperature": (3, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"CameraName" : ((2, LCID, 4, 0),()),
		"CoolerAvailable" : ((4, LCID, 4, 0),()),
		"CoolerTemperature" : ((8, LCID, 4, 0),()),
		"CurrentReadOutSpeed" : ((9, LCID, 4, 0),()),
		"Gain" : ((10, LCID, 4, 0),()),
		"LastImageTaken" : ((1, LCID, 4, 0),()),
		"Offset" : ((11, LCID, 4, 0),()),
		"ReadoutResolutions" : ((5, LCID, 4, 0),()),
		"ReadoutSpeeds" : ((6, LCID, 4, 0),()),
		"Status" : ((7, LCID, 4, 0),()),
		"Temperature" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecApogeeEvents:
	'XPHySpecApogee Events Interface'
	CLSID = CLSID_Sink = IID('{2F301635-D8DB-4EA3-ABA4-BFA4098D6764}')
	coclass_clsid = IID('{88A5D497-C66D-4DB3-8331-420EE8A57AC4}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnImageReceived",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrorCode=defaultNamedNotOptArg, p_ErrMessage=defaultNamedNotOptArg):
#	def OnImageReceived(self):


class IXPHySpecCamera(DispatchBaseClass):
	'XPHySpecCamera Interface'
	CLSID = IID('{5D62EC7B-B46A-487D-8CFC-2770BDA8E621}')
	coclass_clsid = IID('{54D42933-D77B-433D-90FB-1120C2E6EC37}')

	def GetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._ApplyTypes_(13, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetBinning', None,p_horizontal
			, p_vertical)

	def GetDetectorSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(12, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetDetectorSize', None,p_width
			, p_height)

	def GetExposureRange(self, p_minimum=defaultNamedNotOptArg, p_maximum=defaultNamedNotOptArg):
		return self._ApplyTypes_(11, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetExposureRange', None,p_minimum
			, p_maximum)

	def GetPixelSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(10, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetPixelSize', None,p_width
			, p_height)

	def GetROISize(self, p_ROIWidth=defaultNamedNotOptArg, p_ROIHeight=defaultNamedNotOptArg):
		return self._ApplyTypes_(15, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROISize', None,p_ROIWidth
			, p_ROIHeight)

	def GetROIStart(self, p_x=defaultNamedNotOptArg, p_y=defaultNamedNotOptArg):
		return self._ApplyTypes_(16, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROIStart', None,p_x
			, p_y)

	def SetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1), (3, 1)),p_horizontal
			, p_vertical)

	def SetReadOutResolution(self, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1),),p_resolution
			)

	def TakeSinglePicture(self, p_ExposureTime=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((5, 1),),p_ExposureTime
			)

	_prop_map_get_ = {
		"CameraName": (2, 2, (8, 0), (), "CameraName", None),
		"CoolerAvailable": (4, 2, (11, 0), (), "CoolerAvailable", None),
		"LastImageTaken": (1, 2, (8209, 0), (), "LastImageTaken", None),
		"ReadoutResolutions": (5, 2, (8204, 0), (), "ReadoutResolutions", None),
		"ReadoutSpeeds": (6, 2, (8204, 0), (), "ReadoutSpeeds", None),
		"Status": (7, 2, (3, 0), (), "Status", None),
		"Temperature": (3, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"CameraName" : ((2, LCID, 4, 0),()),
		"CoolerAvailable" : ((4, LCID, 4, 0),()),
		"LastImageTaken" : ((1, LCID, 4, 0),()),
		"ReadoutResolutions" : ((5, LCID, 4, 0),()),
		"ReadoutSpeeds" : ((6, LCID, 4, 0),()),
		"Status" : ((7, LCID, 4, 0),()),
		"Temperature" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecCameraEvents:
	'XPHySpecCamera Events Interface'
	CLSID = CLSID_Sink = IID('{CB3ECF4B-5851-490C-9FD0-43A785FFFDCB}')
	coclass_clsid = IID('{54D42933-D77B-433D-90FB-1120C2E6EC37}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnImageReceived",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrorCode=defaultNamedNotOptArg, p_ErrMessage=defaultNamedNotOptArg):
#	def OnImageReceived(self):


class IXPHySpecHImager(DispatchBaseClass):
	'XPHySpecHImager Interface'
	CLSID = IID('{D690FAD2-3EDA-4051-BCF2-A6F112719432}')
	coclass_clsid = IID('{E301F06E-1BA2-4895-9040-23C7F157B35A}')

	def CalibrateFromFile(self, p_Filename=defaultNamedNotOptArg, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((8, 1), (3, 1), (3, 1)),p_Filename
			, p_width, p_height)

	def CalibrateGrating(self, p_lambda1=defaultNamedNotOptArg, p_realAngle1=defaultNamedNotOptArg, p_lambda2=defaultNamedNotOptArg, p_realAngle2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((5, 1), (5, 1), (5, 1), (5, 1)),p_lambda1
			, p_realAngle1, p_lambda2, p_realAngle2)

	def CalibrateMotorizedLens(self, p_gratingIndex=defaultNamedNotOptArg, p_position=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_position, p_wavelength)

	def EnableFollowWavelength(self, p_automatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 1),),p_automatic
			)

	def IsCalibrated(self, p_gratingIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((3, 1),),p_gratingIndex
			)

	def MoveMotorizedLens(self, p_position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1),),p_position
			)

	def MoveToAngle(self, p_TargetAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((5, 1),),p_TargetAngle
			)

	def MoveToWavelengthInGrating(self, p_gratingIndex=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1), (5, 1)),p_gratingIndex
			, p_wavelength)

	def MovetoWavelength(self, p_TargetWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((5, 1),),p_TargetWavelength
			)

	def SaveCalibrationMatrices(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def Step(self, p_StepWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((5, 1),),p_StepWavelength
			)

	_prop_map_get_ = {
		"BraggAngle": (3, 2, (5, 0), (), "BraggAngle", None),
		"CurrentWavelength": (1, 2, (5, 0), (), "CurrentWavelength", None),
		"GratingIndex": (10, 2, (3, 0), (), "GratingIndex", None),
		"GratingPeriod": (9, 2, (5, 0), (), "GratingPeriod", None),
		"MotorizedLensPosition": (5, 2, (3, 0), (), "MotorizedLensPosition", None),
		"NumberOfGratings": (6, 2, (3, 0), (), "NumberOfGratings", None),
		"SerialNumber": (4, 2, (8, 0), (), "SerialNumber", None),
		"StageAngle": (2, 2, (5, 0), (), "StageAngle", None),
		"Status": (8, 2, (3, 0), (), "Status", None),
		"Temperature": (7, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"BraggAngle" : ((3, LCID, 4, 0),()),
		"CurrentWavelength" : ((1, LCID, 4, 0),()),
		"GratingIndex" : ((10, LCID, 4, 0),()),
		"GratingPeriod" : ((9, LCID, 4, 0),()),
		"MotorizedLensPosition" : ((5, LCID, 4, 0),()),
		"NumberOfGratings" : ((6, LCID, 4, 0),()),
		"SerialNumber" : ((4, LCID, 4, 0),()),
		"StageAngle" : ((2, LCID, 4, 0),()),
		"Status" : ((8, LCID, 4, 0),()),
		"Temperature" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecHImagerEvents:
	'XPHySpecHImager Events Interface'
	CLSID = CLSID_Sink = IID('{577CE3FD-CE6B-4A05-853A-CC955B4BAE94}')
	coclass_clsid = IID('{E301F06E-1BA2-4895-9040-23C7F157B35A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnsigStageMoved",
		        3 : "OnsigMotorizedLensMoved",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrCode=defaultNamedNotOptArg, p_ErrMsg=defaultNamedNotOptArg):
#	def OnsigStageMoved(self):
#	def OnsigMotorizedLensMoved(self):


class IXPHySpecLLTunableFilter(DispatchBaseClass):
	'XPHySpecLLTunableFilter Interface'
	CLSID = IID('{84314DEF-5693-4984-B321-24DA730B8C3E}')
	coclass_clsid = IID('{CE2270A9-81C7-4105-BE61-949C3D98B617}')

	def CalibrateFromFile(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def CalibrateGrating(self, p_lambda1=defaultNamedNotOptArg, p_realAngle1=defaultNamedNotOptArg, p_lambda2=defaultNamedNotOptArg, p_realAngle2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((5, 1), (5, 1), (5, 1), (5, 1)),p_lambda1
			, p_realAngle1, p_lambda2, p_realAngle2)

	def CalibrateGrating_1(self, p_gratingIndex=defaultNamedNotOptArg, p_lambda=defaultNamedNotOptArg, p_realAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_lambda, p_realAngle)

	def CalibrateMotorizedLens(self, p_gratingIndex=defaultNamedNotOptArg, p_position=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_position, p_wavelength)

	def EnableFollowWavelength(self, p_automatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 1),),p_automatic
			)

	def IsCalibrated(self, p_gratingIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((3, 1),),p_gratingIndex
			)

	def MoveMotorizedLens(self, p_position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1),),p_position
			)

	def MoveToAngle(self, p_TargetAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((5, 1),),p_TargetAngle
			)

	def MoveToWavelengthInGrating(self, p_gratingIndex=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1), (5, 1)),p_gratingIndex
			, p_wavelength)

	def MovetoWavelength(self, p_TargetWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((5, 1),),p_TargetWavelength
			)

	def SaveCalibrationMatrices(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def Step(self, p_StepWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((5, 1),),p_StepWavelength
			)

	_prop_map_get_ = {
		"BraggAngle": (3, 2, (5, 0), (), "BraggAngle", None),
		"CurrentWavelength": (1, 2, (5, 0), (), "CurrentWavelength", None),
		"GratingIndex": (10, 2, (3, 0), (), "GratingIndex", None),
		"GratingPeriod": (9, 2, (5, 0), (), "GratingPeriod", None),
		"MotorizedLensPosition": (5, 2, (3, 0), (), "MotorizedLensPosition", None),
		"NumberOfGratings": (6, 2, (3, 0), (), "NumberOfGratings", None),
		"SerialNumber": (4, 2, (8, 0), (), "SerialNumber", None),
		"StageAngle": (2, 2, (5, 0), (), "StageAngle", None),
		"Status": (8, 2, (3, 0), (), "Status", None),
		"Temperature": (7, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"BraggAngle" : ((3, LCID, 4, 0),()),
		"CurrentWavelength" : ((1, LCID, 4, 0),()),
		"GratingIndex" : ((10, LCID, 4, 0),()),
		"GratingPeriod" : ((9, LCID, 4, 0),()),
		"MotorizedLensPosition" : ((5, LCID, 4, 0),()),
		"NumberOfGratings" : ((6, LCID, 4, 0),()),
		"SerialNumber" : ((4, LCID, 4, 0),()),
		"StageAngle" : ((2, LCID, 4, 0),()),
		"Status" : ((8, LCID, 4, 0),()),
		"Temperature" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecLLTunableFilterEvents:
	'XPHySpecLLTunableFilter Events Interface'
	CLSID = CLSID_Sink = IID('{B0D24E91-61F6-41ED-993E-D55CD302C939}')
	coclass_clsid = IID('{CE2270A9-81C7-4105-BE61-949C3D98B617}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnsigStageMoved",
		        3 : "OnsigMotorizedLensMoved",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrCode=defaultNamedNotOptArg, p_ErrMsg=defaultNamedNotOptArg):
#	def OnsigStageMoved(self):
#	def OnsigMotorizedLensMoved(self):


class IXPHySpecPCO(DispatchBaseClass):
	'XPHySpecPCO Interface'
	CLSID = IID('{041691C6-E10E-40FA-B328-189A17914EA9}')
	coclass_clsid = IID('{A2985B2A-2290-4164-A2F6-8EF98823C3BC}')

	def GetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._ApplyTypes_(16, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetBinning', None,p_horizontal
			, p_vertical)

	def GetDetectorSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(15, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetDetectorSize', None,p_width
			, p_height)

	def GetExposureRange(self, p_minimum=defaultNamedNotOptArg, p_maximum=defaultNamedNotOptArg):
		return self._ApplyTypes_(14, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetExposureRange', None,p_minimum
			, p_maximum)

	def GetPixelSize(self, p_width=defaultNamedNotOptArg, p_height=defaultNamedNotOptArg):
		return self._ApplyTypes_(13, 1, (24, 0), ((16389, 3), (16389, 3)), 'GetPixelSize', None,p_width
			, p_height)

	def GetROISize(self, p_ROIWidth=defaultNamedNotOptArg, p_ROIHeight=defaultNamedNotOptArg):
		return self._ApplyTypes_(18, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROISize', None,p_ROIWidth
			, p_ROIHeight)

	def GetROIStart(self, p_x=defaultNamedNotOptArg, p_y=defaultNamedNotOptArg):
		return self._ApplyTypes_(19, 1, (24, 0), ((16387, 3), (16387, 3)), 'GetROIStart', None,p_x
			, p_y)

	def SetBinning(self, p_horizontal=defaultNamedNotOptArg, p_vertical=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1), (3, 1)),p_horizontal
			, p_vertical)

	def SetReadOutResolution(self, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1),),p_resolution
			)

	def TakeSinglePicture(self, p_ExposureTime=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((5, 1),),p_ExposureTime
			)

	_prop_map_get_ = {
		"CameraName": (2, 2, (8, 0), (), "CameraName", None),
		"CoolerAvailable": (4, 2, (11, 0), (), "CoolerAvailable", None),
		"CoolerOn": (9, 2, (11, 0), (), "CoolerOn", None),
		"CoolerTemperature": (10, 2, (5, 0), (), "CoolerTemperature", None),
		"IRSensitivity": (8, 2, (11, 0), (), "IRSensitivity", None),
		"LastImageTaken": (1, 2, (8209, 0), (), "LastImageTaken", None),
		"ReadoutResolutions": (5, 2, (8204, 0), (), "ReadoutResolutions", None),
		"ReadoutSpeeds": (6, 2, (8204, 0), (), "ReadoutSpeeds", None),
		"Status": (7, 2, (3, 0), (), "Status", None),
		"Temperature": (3, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"CameraName" : ((2, LCID, 4, 0),()),
		"CoolerAvailable" : ((4, LCID, 4, 0),()),
		"CoolerOn" : ((9, LCID, 4, 0),()),
		"CoolerTemperature" : ((10, LCID, 4, 0),()),
		"IRSensitivity" : ((8, LCID, 4, 0),()),
		"LastImageTaken" : ((1, LCID, 4, 0),()),
		"ReadoutResolutions" : ((5, LCID, 4, 0),()),
		"ReadoutSpeeds" : ((6, LCID, 4, 0),()),
		"Status" : ((7, LCID, 4, 0),()),
		"Temperature" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecPCOEvents:
	'XPHySpecPCO Events Interface'
	CLSID = CLSID_Sink = IID('{CAF9355A-98F6-4C41-B3B9-166C85CE2A96}')
	coclass_clsid = IID('{A2985B2A-2290-4164-A2F6-8EF98823C3BC}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnImageReceived",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrorCode=defaultNamedNotOptArg, p_ErrMessage=defaultNamedNotOptArg):
#	def OnImageReceived(self):


class IXPHySpecTunableFilter(DispatchBaseClass):
	'XPHySpecTunableFilter Interface'
	CLSID = IID('{E5405403-6597-41EE-B0DC-B079616D414E}')
	coclass_clsid = IID('{332C623C-678E-4BA5-95B8-51F2DC6B5729}')

	def CalibrateGrating(self, p_lambda1=defaultNamedNotOptArg, p_realAngle1=defaultNamedNotOptArg, p_lambda2=defaultNamedNotOptArg, p_realAngle2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((5, 1), (5, 1), (5, 1), (5, 1)),p_lambda1
			, p_realAngle1, p_lambda2, p_realAngle2)

	def CalibrateMotorizedLens(self, p_gratingIndex=defaultNamedNotOptArg, p_position=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_position, p_wavelength)

	def EnableFollowWavelength(self, p_automatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 1),),p_automatic
			)

	def IsCalibrated(self, p_gratingIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((3, 1),),p_gratingIndex
			)

	def MoveMotorizedLens(self, p_position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1),),p_position
			)

	def MoveToAngle(self, p_TargetAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((5, 1),),p_TargetAngle
			)

	def MoveToWavelengthInGrating(self, p_gratingIndex=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1), (5, 1)),p_gratingIndex
			, p_wavelength)

	def MovetoWavelength(self, p_TargetWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((5, 1),),p_TargetWavelength
			)

	def SaveCalibrationMatrices(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def Step(self, p_StepWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((5, 1),),p_StepWavelength
			)

	_prop_map_get_ = {
		"BraggAngle": (3, 2, (5, 0), (), "BraggAngle", None),
		"CurrentWavelength": (1, 2, (5, 0), (), "CurrentWavelength", None),
		"GratingIndex": (10, 2, (3, 0), (), "GratingIndex", None),
		"GratingPeriod": (9, 2, (5, 0), (), "GratingPeriod", None),
		"MotorizedLensPosition": (5, 2, (3, 0), (), "MotorizedLensPosition", None),
		"NumberOfGratings": (6, 2, (3, 0), (), "NumberOfGratings", None),
		"SerialNumber": (4, 2, (8, 0), (), "SerialNumber", None),
		"StageAngle": (2, 2, (5, 0), (), "StageAngle", None),
		"Status": (8, 2, (3, 0), (), "Status", None),
		"Temperature": (7, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"BraggAngle" : ((3, LCID, 4, 0),()),
		"CurrentWavelength" : ((1, LCID, 4, 0),()),
		"GratingIndex" : ((10, LCID, 4, 0),()),
		"GratingPeriod" : ((9, LCID, 4, 0),()),
		"MotorizedLensPosition" : ((5, LCID, 4, 0),()),
		"NumberOfGratings" : ((6, LCID, 4, 0),()),
		"SerialNumber" : ((4, LCID, 4, 0),()),
		"StageAngle" : ((2, LCID, 4, 0),()),
		"Status" : ((8, LCID, 4, 0),()),
		"Temperature" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecTunableFilterEvents:
	'XPHySpecTunableFilter Events Interface'
	CLSID = CLSID_Sink = IID('{391CD165-E90F-4478-BBE5-33747FD734A7}')
	coclass_clsid = IID('{332C623C-678E-4BA5-95B8-51F2DC6B5729}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnsigStageMoved",
		        3 : "OnsigMotorizedLensMoved",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrCode=defaultNamedNotOptArg, p_ErrMsg=defaultNamedNotOptArg):
#	def OnsigStageMoved(self):
#	def OnsigMotorizedLensMoved(self):


class IXPHySpecTunableLaserSource(DispatchBaseClass):
	'XPHySpecTunableLaserSource Interface'
	CLSID = IID('{723BA71F-AEC7-4314-A538-293FD9F1B815}')
	coclass_clsid = IID('{91B751EB-7CD9-4492-AC41-22562CBB128E}')

	def CalibrateFromFile(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def CalibrateGrating(self, p_lambda1=defaultNamedNotOptArg, p_realAngle1=defaultNamedNotOptArg, p_lambda2=defaultNamedNotOptArg, p_realAngle2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((5, 1), (5, 1), (5, 1), (5, 1)),p_lambda1
			, p_realAngle1, p_lambda2, p_realAngle2)

	def CalibrateGrating_1(self, p_gratingIndex=defaultNamedNotOptArg, p_lambda=defaultNamedNotOptArg, p_realAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_lambda, p_realAngle)

	def CalibrateMotorizedLens(self, p_gratingIndex=defaultNamedNotOptArg, p_position=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_position, p_wavelength)

	def EnableFollowWavelength(self, p_automatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((11, 1),),p_automatic
			)

	def IsCalibrated(self, p_gratingIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((3, 1),),p_gratingIndex
			)

	def MoveMotorizedLens(self, p_position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((3, 1),),p_position
			)

	def MoveToAngle(self, p_TargetAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((5, 1),),p_TargetAngle
			)

	def MoveToWavelengthInGrating(self, p_gratingIndex=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1), (5, 1)),p_gratingIndex
			, p_wavelength)

	def MovetoWavelength(self, p_TargetWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((5, 1),),p_TargetWavelength
			)

	def SaveCalibrationMatrices(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def Step(self, p_StepWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((5, 1),),p_StepWavelength
			)

	_prop_map_get_ = {
		"BraggAngle": (3, 2, (5, 0), (), "BraggAngle", None),
		"CurrentWavelength": (1, 2, (5, 0), (), "CurrentWavelength", None),
		"GratingIndex": (10, 2, (3, 0), (), "GratingIndex", None),
		"GratingPeriod": (9, 2, (5, 0), (), "GratingPeriod", None),
		"LampState": (11, 2, (11, 0), (), "LampState", None),
		"MotorizedLensPosition": (5, 2, (3, 0), (), "MotorizedLensPosition", None),
		"NumberOfGratings": (6, 2, (3, 0), (), "NumberOfGratings", None),
		"SerialNumber": (4, 2, (8, 0), (), "SerialNumber", None),
		"StageAngle": (2, 2, (5, 0), (), "StageAngle", None),
		"Status": (8, 2, (3, 0), (), "Status", None),
		"Temperature": (7, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"BraggAngle" : ((3, LCID, 4, 0),()),
		"CurrentWavelength" : ((1, LCID, 4, 0),()),
		"GratingIndex" : ((10, LCID, 4, 0),()),
		"GratingPeriod" : ((9, LCID, 4, 0),()),
		"LampState" : ((11, LCID, 4, 0),()),
		"MotorizedLensPosition" : ((5, LCID, 4, 0),()),
		"NumberOfGratings" : ((6, LCID, 4, 0),()),
		"SerialNumber" : ((4, LCID, 4, 0),()),
		"StageAngle" : ((2, LCID, 4, 0),()),
		"Status" : ((8, LCID, 4, 0),()),
		"Temperature" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecTunableLaserSourceEvents:
	'XPHySpecTunableLaserSource Events Interface'
	CLSID = CLSID_Sink = IID('{9B683107-10ED-4781-B64E-B81CC58AC783}')
	coclass_clsid = IID('{91B751EB-7CD9-4492-AC41-22562CBB128E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnsigStageMoved",
		        3 : "OnsigMotorizedLensMoved",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrCode=defaultNamedNotOptArg, p_ErrMsg=defaultNamedNotOptArg):
#	def OnsigStageMoved(self):
#	def OnsigMotorizedLensMoved(self):


class IXPHySpecTunableSource(DispatchBaseClass):
	'XPHySpecTunableSource Interface'
	CLSID = IID('{5B95EB30-5B89-40BE-81A2-8F0A76C489A1}')
	coclass_clsid = IID('{A0FC4B8D-EBA8-499D-A5C2-011925B73F82}')

	def CalibrateFromFile(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def CalibrateGrating(self, p_lambda1=defaultNamedNotOptArg, p_realAngle1=defaultNamedNotOptArg, p_lambda2=defaultNamedNotOptArg, p_realAngle2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((5, 1), (5, 1), (5, 1), (5, 1)),p_lambda1
			, p_realAngle1, p_lambda2, p_realAngle2)

	def CalibrateGrating_1(self, p_gratingIndex=defaultNamedNotOptArg, p_lambda=defaultNamedNotOptArg, p_realAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_lambda, p_realAngle)

	def CalibrateMotorizedLens(self, p_gratingIndex=defaultNamedNotOptArg, p_position=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((3, 1), (5, 1), (5, 1)),p_gratingIndex
			, p_position, p_wavelength)

	def EnableFollowWavelength(self, p_automatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((11, 1),),p_automatic
			)

	def IsCalibrated(self, p_gratingIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((3, 1),),p_gratingIndex
			)

	def MoveMotorizedLens(self, p_position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 1),),p_position
			)

	def MoveSrcLampMirror(self, p_MirrorAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), ((5, 1),),p_MirrorAngle
			)

	def MoveToAngle(self, p_TargetAngle=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((5, 1),),p_TargetAngle
			)

	def MoveToWavelengthInGrating(self, p_gratingIndex=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((3, 1), (5, 1)),p_gratingIndex
			, p_wavelength)

	def MovetoWavelength(self, p_TargetWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((5, 1),),p_TargetWavelength
			)

	def RequestPhotodiodeAmplifierValue(self):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), (),)

	def SaveCalibrationMatrices(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def Step(self, p_StepWavelength=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((5, 1),),p_StepWavelength
			)

	def setDeviceFan(self, p_State=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((11, 1),),p_State
			)

	def setInteralMirror(self, p_State=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((11, 1),),p_State
			)

	_prop_map_get_ = {
		"AvailableLamps": (12, 2, (8200, 0), (), "AvailableLamps", None),
		"BraggAngle": (3, 2, (5, 0), (), "BraggAngle", None),
		"CurrentLamp": (13, 2, (8, 0), (), "CurrentLamp", None),
		"CurrentLampMirrorAngle": (15, 2, (5, 0), (), "CurrentLampMirrorAngle", None),
		"CurrentWavelength": (1, 2, (5, 0), (), "CurrentWavelength", None),
		"GratingIndex": (10, 2, (3, 0), (), "GratingIndex", None),
		"GratingPeriod": (9, 2, (5, 0), (), "GratingPeriod", None),
		"LampPosition": (14, 2, (5, 0), (), "LampPosition", None),
		"LampState": (11, 2, (11, 0), (), "LampState", None),
		"MotorizedLensPosition": (5, 2, (3, 0), (), "MotorizedLensPosition", None),
		"NumberOfGratings": (6, 2, (3, 0), (), "NumberOfGratings", None),
		"SerialNumber": (4, 2, (8, 0), (), "SerialNumber", None),
		"StageAngle": (2, 2, (5, 0), (), "StageAngle", None),
		"Status": (8, 2, (3, 0), (), "Status", None),
		"Temperature": (7, 2, (5, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"AvailableLamps" : ((12, LCID, 4, 0),()),
		"BraggAngle" : ((3, LCID, 4, 0),()),
		"CurrentLamp" : ((13, LCID, 4, 0),()),
		"CurrentLampMirrorAngle" : ((15, LCID, 4, 0),()),
		"CurrentWavelength" : ((1, LCID, 4, 0),()),
		"GratingIndex" : ((10, LCID, 4, 0),()),
		"GratingPeriod" : ((9, LCID, 4, 0),()),
		"LampPosition" : ((14, LCID, 4, 0),()),
		"LampState" : ((11, LCID, 4, 0),()),
		"MotorizedLensPosition" : ((5, LCID, 4, 0),()),
		"NumberOfGratings" : ((6, LCID, 4, 0),()),
		"SerialNumber" : ((4, LCID, 4, 0),()),
		"StageAngle" : ((2, LCID, 4, 0),()),
		"Status" : ((8, LCID, 4, 0),()),
		"Temperature" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPHySpecTunableSourceEvents:
	'XPHySpecTunableSource Events Interface'
	CLSID = CLSID_Sink = IID('{1919FA94-81BB-435B-AFC7-464F30469F99}')
	coclass_clsid = IID('{A0FC4B8D-EBA8-499D-A5C2-011925B73F82}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnsigError",
		        2 : "OnsigStageMoved",
		        3 : "OnsigMotorizedLensMoved",
		        4 : "OnSrcLampMirrorMoved",
		        5 : "OnPhotodiodeAmplifierValue",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnsigError(self, p_ErrCode=defaultNamedNotOptArg, p_ErrMsg=defaultNamedNotOptArg):
#	def OnsigStageMoved(self):
#	def OnsigMotorizedLensMoved(self):
#	def OnSrcLampMirrorMoved(self):
#	def OnPhotodiodeAmplifierValue(self, p_Value=defaultNamedNotOptArg):


class IXPhySpec(DispatchBaseClass):
	'XPhySpec Interface'
	CLSID = IID('{C18BE94C-6154-4684-8748-3A8E5D8BF1A8}')
	coclass_clsid = IID('{87A4718C-8FF0-43F4-B183-754ACF267A8F}')

	def AbortAcquisition(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def Acquire(self, p_device=defaultNamedNotOptArg, p_Camera=defaultNamedNotOptArg, p_cubeName=defaultNamedNotOptArg, p_lowerLambda=defaultNamedNotOptArg
			, p_higherLambda=defaultNamedNotOptArg, p_step=defaultNamedNotOptArg, p_ExposureTime=defaultNamedNotOptArg, p_coverGradient=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((13, 1), (13, 1), (8, 1), (5, 1), (5, 1), (5, 1), (5, 1), (11, 1)),p_device
			, p_Camera, p_cubeName, p_lowerLambda, p_higherLambda, p_step
			, p_ExposureTime, p_coverGradient)

	def AddCameraToSystem(self, p_CameraName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((8, 1),),p_CameraName
			)

	def AddCube(self, p_cubeName=defaultNamedNotOptArg, p_imageWidth=defaultNamedNotOptArg, p_imageHeight=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), ((8, 1), (3, 1), (3, 1)),p_cubeName
			, p_imageWidth, p_imageHeight)

	def AddCurrentImage(self, p_cubeName=defaultNamedNotOptArg, p_device=defaultNamedNotOptArg, p_Camera=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), ((8, 1), (13, 1), (13, 1)),p_cubeName
			, p_device, p_Camera)

	def AddImage(self, p_cubeName=defaultNamedNotOptArg, p_data=defaultNamedNotOptArg, p_wavelength=defaultNamedNotOptArg, p_braggAngle=defaultNamedNotOptArg
			, p_gratingPeriod=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((8, 1), (8209, 1), (5, 1), (5, 1), (5, 1)),p_cubeName
			, p_data, p_wavelength, p_braggAngle, p_gratingPeriod)

	def CalibrateHImagerGrating(self, p_HImager=defaultNamedNotOptArg, p_Camera=defaultNamedNotOptArg, p_ExposureTime=defaultNamedNotOptArg, p_RaysFilename=defaultNamedNotOptArg
			, p_GratingNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), ((13, 1), (13, 1), (5, 1), (8, 1), (19, 1)),p_HImager
			, p_Camera, p_ExposureTime, p_RaysFilename, p_GratingNumber)

	def CalibrateTSrcGrating(self, p_TunableSrc=defaultNamedNotOptArg, p_GratingNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((13, 1), (19, 1)),p_TunableSrc
			, p_GratingNumber)

	def DeleteCube(self, p_cubeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), ((8, 1),),p_cubeName
			)

	def DetectCameras(self, p_DriverName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((8, 1),),p_DriverName
			)

	def DetectDevices(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	# Result is of type XPHySpecCamera
	def GetCameraInterface(self, p_CameraName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (13, 0), ((8, 1),),p_CameraName
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetCameraInterface', '{54D42933-D77B-433D-90FB-1120C2E6EC37}')
		return ret

	# Result is of type XPHySpecTunableFilter
	def GetDeviceInterface(self, p_SerialNumber=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (13, 0), ((8, 1),),p_SerialNumber
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetDeviceInterface', '{332C623C-678E-4BA5-95B8-51F2DC6B5729}')
		return ret

	def InitializeSystem(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def LoadCube(self, p_Filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), ((8, 1),),p_Filename
			)

	def RectifyCube(self, p_device=defaultNamedNotOptArg, p_cubeName=defaultNamedNotOptArg, p_WavelengthStart=defaultNamedNotOptArg, p_WavelengthEnd=defaultNamedNotOptArg
			, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), ((13, 1), (8, 1), (5, 1), (5, 1), (5, 1)),p_device
			, p_cubeName, p_WavelengthStart, p_WavelengthEnd, p_resolution)

	def RectifyCubeFromCalibFile(self, p_MatrixFileName=defaultNamedNotOptArg, p_cubeName=defaultNamedNotOptArg, p_WavelengthStart=defaultNamedNotOptArg, p_WavelengthEnd=defaultNamedNotOptArg
			, p_resolution=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), ((8, 1), (8, 1), (5, 1), (5, 1), (5, 1)),p_MatrixFileName
			, p_cubeName, p_WavelengthStart, p_WavelengthEnd, p_resolution)

	def SaveCube(self, p_cubeName=defaultNamedNotOptArg, p_Filename=defaultNamedNotOptArg, p_cubeType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), ((8, 1), (8, 1), (3, 1)),p_cubeName
			, p_Filename, p_cubeType)

	def SetCubeMetaInfo(self, p_cubeName=defaultNamedNotOptArg, p_name=defaultNamedNotOptArg, p_Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), ((8, 1), (8, 1), (8, 1)),p_cubeName
			, p_name, p_Value)

	# Result is of type XPHySpecAndorIxon
	def ToAndorIxon(self, p_CameraInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (13, 0), ((13, 1),),p_CameraInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToAndorIxon', '{2C85E8A5-0E6B-4D4A-AEDF-D54B3459844A}')
		return ret

	# Result is of type XPHySpecApogee
	def ToApogee(self, p_CameraInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (13, 0), ((13, 1),),p_CameraInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToApogee', '{88A5D497-C66D-4DB3-8331-420EE8A57AC4}')
		return ret

	# Result is of type XPHySpecHImager
	def ToHI(self, p_DeviceInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (13, 0), ((13, 1),),p_DeviceInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToHI', '{E301F06E-1BA2-4895-9040-23C7F157B35A}')
		return ret

	# Result is of type XPHySpecLLTunableFilter
	def ToLLTF(self, p_DeviceInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (13, 0), ((13, 1),),p_DeviceInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToLLTF', '{CE2270A9-81C7-4105-BE61-949C3D98B617}')
		return ret

	# Result is of type XPHySpecPCO
	def ToPCO(self, p_CameraInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (13, 0), ((13, 1),),p_CameraInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToPCO', '{A2985B2A-2290-4164-A2F6-8EF98823C3BC}')
		return ret

	# Result is of type XPHySpecTunableLaserSource
	def ToTLS(self, p_DeviceInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (13, 0), ((13, 1),),p_DeviceInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToTLS', '{91B751EB-7CD9-4492-AC41-22562CBB128E}')
		return ret

	# Result is of type XPHySpecTunableSource
	def ToTS(self, p_DeviceInterface=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (13, 0), ((13, 1),),p_DeviceInterface
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'ToTS', '{A0FC4B8D-EBA8-499D-A5C2-011925B73F82}')
		return ret

	_prop_map_get_ = {
		"AcquisitionProgress": (6, 2, (19, 0), (), "AcquisitionProgress", None),
		"AndorDriverName": (4, 2, (8, 0), (), "AndorDriverName", None),
		"ApogeeDriverName": (3, 2, (8, 0), (), "ApogeeDriverName", None),
		"AutoCalibProgress": (7, 2, (19, 0), (), "AutoCalibProgress", None),
		"IsAcquiring": (1, 2, (11, 0), (), "IsAcquiring", None),
		"ListOfAvailableCameras": (11, 2, (8200, 0), (), "ListOfAvailableCameras", None),
		"ListOfAvailableDevices": (10, 2, (8200, 0), (), "ListOfAvailableDevices", None),
		"ListOfAvailableRawCubes": (9, 2, (8204, 0), (), "ListOfAvailableRawCubes", None),
		"PCODriverName": (5, 2, (8, 0), (), "PCODriverName", None),
		"RectificationProgress": (8, 2, (19, 0), (), "RectificationProgress", None),
		"SerialPortIsOpen": (2, 2, (11, 0), (), "SerialPortIsOpen", None),
	}
	_prop_map_put_ = {
		"AcquisitionProgress" : ((6, LCID, 4, 0),()),
		"AndorDriverName" : ((4, LCID, 4, 0),()),
		"ApogeeDriverName" : ((3, LCID, 4, 0),()),
		"AutoCalibProgress" : ((7, LCID, 4, 0),()),
		"IsAcquiring" : ((1, LCID, 4, 0),()),
		"ListOfAvailableCameras" : ((11, LCID, 4, 0),()),
		"ListOfAvailableDevices" : ((10, LCID, 4, 0),()),
		"ListOfAvailableRawCubes" : ((9, LCID, 4, 0),()),
		"PCODriverName" : ((5, LCID, 4, 0),()),
		"RectificationProgress" : ((8, LCID, 4, 0),()),
		"SerialPortIsOpen" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXPhySpecEvents:
	'XPhySpec Events Interface'
	CLSID = CLSID_Sink = IID('{2D4A9EC8-5304-4F3F-827F-6120AB255E39}')
	coclass_clsid = IID('{87A4718C-8FF0-43F4-B183-754ACF267A8F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDeviceDetectionFinished",
		        2 : "OnCameraAdded",
		        3 : "OnsigError",
		        4 : "OnCalibrationDone",
		        6 : "OnAcquisitionFinished",
		        7 : "OnCubeRectificationDone",
		        8 : "OnNewCubeAdded",
		        9 : "OnSendToSerial",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnDeviceDetectionFinished(self):
#	def OnCameraAdded(self):
#	def OnsigError(self, p_ErrorCode=defaultNamedNotOptArg, p_ErrMessage=defaultNamedNotOptArg):
#	def OnCalibrationDone(self):
#	def OnAcquisitionFinished(self):
#	def OnCubeRectificationDone(self):
#	def OnNewCubeAdded(self):
#	def OnSendToSerial(self, p_Bytes=defaultNamedNotOptArg):


from win32com.client import CoClassBaseClass
class XPHySpecAndorIxon(CoClassBaseClass): # A CoClass
	# XPHySpecAndorIxon Class
	CLSID = IID('{2C85E8A5-0E6B-4D4A-AEDF-D54B3459844A}')
	coclass_sources = [
		IXPHySpecAndorIxonEvents,
	]
	default_source = IXPHySpecAndorIxonEvents
	coclass_interfaces = [
		IXPHySpecAndorIxon,
	]
	default_interface = IXPHySpecAndorIxon

class XPHySpecApogee(CoClassBaseClass): # A CoClass
	# XPHySpecApogee Class
	CLSID = IID('{88A5D497-C66D-4DB3-8331-420EE8A57AC4}')
	coclass_sources = [
		IXPHySpecApogeeEvents,
	]
	default_source = IXPHySpecApogeeEvents
	coclass_interfaces = [
		IXPHySpecApogee,
	]
	default_interface = IXPHySpecApogee

class XPHySpecCamera(CoClassBaseClass): # A CoClass
	# XPHySpecCamera Class
	CLSID = IID('{54D42933-D77B-433D-90FB-1120C2E6EC37}')
	coclass_sources = [
		IXPHySpecCameraEvents,
	]
	default_source = IXPHySpecCameraEvents
	coclass_interfaces = [
		IXPHySpecCamera,
	]
	default_interface = IXPHySpecCamera

class XPHySpecHImager(CoClassBaseClass): # A CoClass
	# XPHySpecHImager Class
	CLSID = IID('{E301F06E-1BA2-4895-9040-23C7F157B35A}')
	coclass_sources = [
		IXPHySpecHImagerEvents,
	]
	default_source = IXPHySpecHImagerEvents
	coclass_interfaces = [
		IXPHySpecHImager,
	]
	default_interface = IXPHySpecHImager

class XPHySpecLLTunableFilter(CoClassBaseClass): # A CoClass
	# XPHySpecLLTunableFilter Class
	CLSID = IID('{CE2270A9-81C7-4105-BE61-949C3D98B617}')
	coclass_sources = [
		IXPHySpecLLTunableFilterEvents,
	]
	default_source = IXPHySpecLLTunableFilterEvents
	coclass_interfaces = [
		IXPHySpecLLTunableFilter,
	]
	default_interface = IXPHySpecLLTunableFilter

class XPHySpecPCO(CoClassBaseClass): # A CoClass
	# XPHySpecPCO Class
	CLSID = IID('{A2985B2A-2290-4164-A2F6-8EF98823C3BC}')
	coclass_sources = [
		IXPHySpecPCOEvents,
	]
	default_source = IXPHySpecPCOEvents
	coclass_interfaces = [
		IXPHySpecPCO,
	]
	default_interface = IXPHySpecPCO

class XPHySpecTunableFilter(CoClassBaseClass): # A CoClass
	# XPHySpecTunableFilter Class
	CLSID = IID('{332C623C-678E-4BA5-95B8-51F2DC6B5729}')
	coclass_sources = [
		IXPHySpecTunableFilterEvents,
	]
	default_source = IXPHySpecTunableFilterEvents
	coclass_interfaces = [
		IXPHySpecTunableFilter,
	]
	default_interface = IXPHySpecTunableFilter

class XPHySpecTunableLaserSource(CoClassBaseClass): # A CoClass
	# XPHySpecTunableLaserSource Class
	CLSID = IID('{91B751EB-7CD9-4492-AC41-22562CBB128E}')
	coclass_sources = [
		IXPHySpecTunableLaserSourceEvents,
	]
	default_source = IXPHySpecTunableLaserSourceEvents
	coclass_interfaces = [
		IXPHySpecTunableLaserSource,
	]
	default_interface = IXPHySpecTunableLaserSource

class XPHySpecTunableSource(CoClassBaseClass): # A CoClass
	# XPHySpecTunableSource Class
	CLSID = IID('{A0FC4B8D-EBA8-499D-A5C2-011925B73F82}')
	coclass_sources = [
		IXPHySpecTunableSourceEvents,
	]
	default_source = IXPHySpecTunableSourceEvents
	coclass_interfaces = [
		IXPHySpecTunableSource,
	]
	default_interface = IXPHySpecTunableSource

# This CoClass is known by the name 'XPHySpec.XPhySpec.1'
class XPhySpec(CoClassBaseClass): # A CoClass
	# XPhySpec Class
	CLSID = IID('{87A4718C-8FF0-43F4-B183-754ACF267A8F}')
	coclass_sources = [
		IXPhySpecEvents,
	]
	default_source = IXPhySpecEvents
	coclass_interfaces = [
		IXPhySpec,
	]
	default_interface = IXPhySpec

RecordMap = {
	'QRect': '{34030F30-E359-4FE6-AB82-39766F5D91EE}',
	'QSize': '{CB5F84B3-29E5-491D-BA18-5472488EEFBA}',
	'QPoint': '{3BE838A3-3FAC-BFC4-4C6C-37C44D030252}',
}

CLSIDToClassMap = {
	'{E5405403-6597-41EE-B0DC-B079616D414E}' : IXPHySpecTunableFilter,
	'{391CD165-E90F-4478-BBE5-33747FD734A7}' : IXPHySpecTunableFilterEvents,
	'{332C623C-678E-4BA5-95B8-51F2DC6B5729}' : XPHySpecTunableFilter,
	'{D690FAD2-3EDA-4051-BCF2-A6F112719432}' : IXPHySpecHImager,
	'{577CE3FD-CE6B-4A05-853A-CC955B4BAE94}' : IXPHySpecHImagerEvents,
	'{E301F06E-1BA2-4895-9040-23C7F157B35A}' : XPHySpecHImager,
	'{5B95EB30-5B89-40BE-81A2-8F0A76C489A1}' : IXPHySpecTunableSource,
	'{1919FA94-81BB-435B-AFC7-464F30469F99}' : IXPHySpecTunableSourceEvents,
	'{A0FC4B8D-EBA8-499D-A5C2-011925B73F82}' : XPHySpecTunableSource,
	'{723BA71F-AEC7-4314-A538-293FD9F1B815}' : IXPHySpecTunableLaserSource,
	'{9B683107-10ED-4781-B64E-B81CC58AC783}' : IXPHySpecTunableLaserSourceEvents,
	'{91B751EB-7CD9-4492-AC41-22562CBB128E}' : XPHySpecTunableLaserSource,
	'{84314DEF-5693-4984-B321-24DA730B8C3E}' : IXPHySpecLLTunableFilter,
	'{B0D24E91-61F6-41ED-993E-D55CD302C939}' : IXPHySpecLLTunableFilterEvents,
	'{CE2270A9-81C7-4105-BE61-949C3D98B617}' : XPHySpecLLTunableFilter,
	'{5D62EC7B-B46A-487D-8CFC-2770BDA8E621}' : IXPHySpecCamera,
	'{CB3ECF4B-5851-490C-9FD0-43A785FFFDCB}' : IXPHySpecCameraEvents,
	'{54D42933-D77B-433D-90FB-1120C2E6EC37}' : XPHySpecCamera,
	'{A3EF76AB-75D5-4ECA-B794-00C2C8CDF35C}' : IXPHySpecAndorIxon,
	'{02A4C8CD-F1E3-4DA3-A79F-E4EA68E25799}' : IXPHySpecAndorIxonEvents,
	'{2C85E8A5-0E6B-4D4A-AEDF-D54B3459844A}' : XPHySpecAndorIxon,
	'{26CA5819-80BE-4F05-9DDF-C10477669586}' : IXPHySpecApogee,
	'{2F301635-D8DB-4EA3-ABA4-BFA4098D6764}' : IXPHySpecApogeeEvents,
	'{88A5D497-C66D-4DB3-8331-420EE8A57AC4}' : XPHySpecApogee,
	'{041691C6-E10E-40FA-B328-189A17914EA9}' : IXPHySpecPCO,
	'{CAF9355A-98F6-4C41-B3B9-166C85CE2A96}' : IXPHySpecPCOEvents,
	'{A2985B2A-2290-4164-A2F6-8EF98823C3BC}' : XPHySpecPCO,
	'{C18BE94C-6154-4684-8748-3A8E5D8BF1A8}' : IXPhySpec,
	'{2D4A9EC8-5304-4F3F-827F-6120AB255E39}' : IXPhySpecEvents,
	'{87A4718C-8FF0-43F4-B183-754ACF267A8F}' : XPhySpec,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IXPHySpecTunableFilter' : '{E5405403-6597-41EE-B0DC-B079616D414E}',
	'IXPHySpecTunableFilterEvents' : '{391CD165-E90F-4478-BBE5-33747FD734A7}',
	'IXPHySpecHImager' : '{D690FAD2-3EDA-4051-BCF2-A6F112719432}',
	'IXPHySpecHImagerEvents' : '{577CE3FD-CE6B-4A05-853A-CC955B4BAE94}',
	'IXPHySpecTunableSource' : '{5B95EB30-5B89-40BE-81A2-8F0A76C489A1}',
	'IXPHySpecTunableSourceEvents' : '{1919FA94-81BB-435B-AFC7-464F30469F99}',
	'IXPHySpecTunableLaserSource' : '{723BA71F-AEC7-4314-A538-293FD9F1B815}',
	'IXPHySpecTunableLaserSourceEvents' : '{9B683107-10ED-4781-B64E-B81CC58AC783}',
	'IXPHySpecLLTunableFilter' : '{84314DEF-5693-4984-B321-24DA730B8C3E}',
	'IXPHySpecLLTunableFilterEvents' : '{B0D24E91-61F6-41ED-993E-D55CD302C939}',
	'IXPHySpecCamera' : '{5D62EC7B-B46A-487D-8CFC-2770BDA8E621}',
	'IXPHySpecCameraEvents' : '{CB3ECF4B-5851-490C-9FD0-43A785FFFDCB}',
	'IXPHySpecAndorIxon' : '{A3EF76AB-75D5-4ECA-B794-00C2C8CDF35C}',
	'IXPHySpecAndorIxonEvents' : '{02A4C8CD-F1E3-4DA3-A79F-E4EA68E25799}',
	'IXPHySpecApogee' : '{26CA5819-80BE-4F05-9DDF-C10477669586}',
	'IXPHySpecApogeeEvents' : '{2F301635-D8DB-4EA3-ABA4-BFA4098D6764}',
	'IXPHySpecPCO' : '{041691C6-E10E-40FA-B328-189A17914EA9}',
	'IXPHySpecPCOEvents' : '{CAF9355A-98F6-4C41-B3B9-166C85CE2A96}',
	'IXPhySpec' : '{C18BE94C-6154-4684-8748-3A8E5D8BF1A8}',
	'IXPhySpecEvents' : '{2D4A9EC8-5304-4F3F-827F-6120AB255E39}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

