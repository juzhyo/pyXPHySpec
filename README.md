# pyXPHySpec

[![PyPI version](https://badge.fury.io/py/pyxphyspec.svg)](https://pypi.org/project/pyxphyspec/)

pyXPhySpec is a Python wrapper for XPhySpec, an ActiveX control for Photon etc. instruments.

## Installation
You can install pyXPHySpec via pip:

```
pip install pyxphyspec
```

## Example
Here is an example of moving to a wavelength of 550nm with a laser line tunable filter:

```python
import os
import time
import pyxphyspec
import win32com.client

xphyspec = win32com.client.Dispatch("XPHySpec.XPhySpec.1")
xphyspec.InitializeSystem()
xphyspec.DetectDevices()
time.sleep(3)

lltf = xphyspec.GetDeviceInterface("M000XXXXXX")
pyxphyspec.IXPHySpecTunableFilter.MovetoWavelength(lltf,550)

os.system("taskkill /im xphyspec.exe /f")
```
I find a delay of at least 2 seconds necessary for `xphyspec.DetectDevices()` to complete.

Note that `"M000XXXXXX"` is a placeholder string for the serial number of the Photon etc. instrument. The serial number can usually be found on a sticker attached to your instrument. Replace this string with the serial number on your sticker.

`os.system("taskkill /im xphyspec.exe /f")` is used here because XPHySpec does not include an exit method.

## Third Party Libraries and Dependencies

Ensure you have XPHySpec ActiveX control, which can be installed through installation of the PHySpec software.

The following library will be installed when you install this library:
* [pywin32](https://github.com/mhammond/pywin32)
