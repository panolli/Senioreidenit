import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os","webbrowser","tkinter","subprocess","win32api"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Appi.py", base=base)])
