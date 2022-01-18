<div align="center">

# pyXPHySpec
A Python wrapper for Photon etc.'s XPHySpec

</div>

---

### Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)



# Introduction
XPHySpec is intended to be used by advanced users that need to integrate Photon etc. instrument in their
process. XPHySpec is an ActiveX control and therefore can only work on a Windows platform. It is possible to
access XPHySpec functions through scripting languages (VBscript) or software that support ActiveX interface
(LabView, MATLAB). XPHySpec does not provide a graphical interface, which is the role of PHySpec, but rather
offer access to many low-level functions of PHySpec. These functions consist of controlling Photon etc.
instruments, managing memory of a cube and correcting images with various techniques. The XPHySpec control
is registered in Windows at the installation process of the PHySpec software.
For those unfamiliar with ActiveX, it is useful to know that an ActiveX object, or COM object, has methods,
properties and events. A method is a function, which can take both input and output parameters, executing a
complex action. A property is a value that can be read-only, write-only or read-write. An event is an asynchronous
message sent by the object to inform the user of a change. In XPHySpec, properties are used to get or set
various states of an object, whether turning on and off a lamp or knowing the current position.
The following sections are ordered by ActiveX object accessible to the user and their hierarchical dependency.
Each section describes the methods and properties of the specific object. Events are only mentioned in the
description of the function that gen


# Prerequisites
+ pywin32
