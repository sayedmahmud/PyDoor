"""
https://github.com/Y4hL/PyDoor

Author(s): Y4hL

License: [gpl-3.0](https://www.gnu.org/licenses/gpl-3.0.html)
"""
import sys
import time

try:
    from cx_Freeze import setup, Executable
except ImportError:
    print('Missing module "cx_Freeze". Install it using "pip install --upgrade cx_Freeze"')
    print('Exiting...')
    time.sleep(5)
    sys.exit(1)

BASE = None

if sys.platform == "win32":
    BASE = "Win32GUI"

build_exe_options = {
    # Packages to include
    'includes': [],
    # Files to include
    'include_files': []
}

setup(name="PyDoor",
      version="1.1",
      description="Remote Administration Tool",
      options={'build_exe': build_exe_options},
      executables=[Executable("client.py", base=BASE)])

# python setup.py build
