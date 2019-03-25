import pyautogui
import makroRun
import sys
pyautogui.PAUSE = 3

if len(sys.argv) > 2:
    setUpScriptName = sys.argv[2]
else:
    setUpScriptName = input("Enter your setup script name: ")

if len(sys.argv) > 1:
    runScriptName = sys.argv[1]
else:
    runScriptName = input("Enter your main script name: ")

setup = makroRun.Makrorun(setUpScriptName)
runscript = makroRun.Makrorun(runScriptName)

setup.exec()
runscript.exec()

