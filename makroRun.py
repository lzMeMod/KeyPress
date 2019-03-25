import pyautogui
import os

class Makrorun(object):

    maindata = list()

    def __init__(self, comma):
        if os.path.isfile(comma + ".keypress"):
            self.maindata = self.importOperatoren(comma)
        elif os.path.isfile(comma):
            self.maindata = self.importOperatoren(comma.replace(".keypress", ""))

    def exec(self):
        commands = self.maindata
        print(commands)
        z = self.runFeins(commands)
        if (z[0]):
            r = z[1]
        else:
            r = 1

        keys = list()
        i = 0
        while i < r:
            for c in commands:
                if not self.scanspecial(c):
                    if '{' in c:
                        x = c.replace("{", "")
                        if pyautogui.isValidKey(x):
                            keys.append(x)
                            pyautogui.keyDown(x)
                    elif '}' in c:
                        if pyautogui.isValidKey(keys[len(keys) - 1]):
                            pyautogui.keyUp(keys[len(keys) - 1])
                            keys.pop(len(keys) - 1)
                    else:
                        if pyautogui.isValidKey(c):
                            pyautogui.keyDown(c)
            i = i + 1

    def stripAll(self, dataIn):
        x = dataIn.replace('\n', "")
        y = x.replace(' ', "")
        if "TEXT:" in x:
            y = x

        return y

    def importOperatoren(self, file):

        f = open(file + '.keypress', 'r')

        main = list()

        for x in f:
            main.append(self.stripAll(x))

        return main

    def runFeins(self, eins):
        out = list()
        if len(eins) > 0:
            if "REP" in eins[0]:
                out.append(True)
                out.append(int(eins[0].replace("REP:", "")))
            else:
                out.append(False)
        else:
            out.append(False)

        return out

    def scanspecial(self, c):
        out = False
        if 'TEXT:' in c:
            out = True
            x = c.replace("TEXT: ", "")
            pyautogui.typewrite(x)
        return out
