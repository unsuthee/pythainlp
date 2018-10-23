# -*- coding: utf-8 -*-
"""
Spell checking using hunspell
"""
import subprocess
import sys


def spell(word, lang="th_TH"):
    """เป็นคำสั่งตรวจคำผิดโดยใช้ hunspell
    รับค่า str ส่งออกเป็น list
    """
    try:
        if sys.platform == "win32":
            cmd = "echo " + word + " | hunspell -d " + lang
        else:
            cmd = 'echo "' + word + '" | hunspell -d ' + lang
        getoutput = subprocess.getoutput(cmd)
        del cmd
        get = getoutput.split("\n")
        del get[0]
        if get[0] == "*":
            getoutput = []
        else:
            if get[1] == "":
                del get[1]
            get = get[0].split(":")
            del get[0]
            getoutput = get[0].replace(" ", "")
            getoutput = getoutput.split(",")
        del get
        return getoutput
    except subprocess.CalledProcessError:
        print("Error: Please install hunspell.")
        return None
    except BaseException as exception:
        print("Errr: Other error: {}".format(exception))
        return None


if __name__ == "__main__":
    input1 = spell("appoe", "")
    print(input1)
    input2 = spell("คลินิค", "th_TH")
    print(input2)
    input3 = spell("สี่เหลียม", "th_TH")
    print(input3)
