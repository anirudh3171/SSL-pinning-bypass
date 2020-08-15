#!/usr/bin/env python3
import subprocess, optparse

parser = optparse.OptionParser()
parser.add_option("-f","--fullinstall",action="store_true",dest="full",help="\"Install Pip\",\" Push Burp Certificate and frida server to the emulator \"")
parser.add_option("-d","--default",action="store_true",dest="default",help="Start the frida server")
parser.add_option("-a","--appname",dest="appName",help="Application Name")
(options, argument) = parser.parse_args()
AppName=options.appName
output = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE).stdout.read()
FLAG2 = "UNCHANGED"
if "genymotion/tools/SSL-pinning-bypass" in str(output):
    FLAG = "CONT_GEN"
else:
    FLAG = "CONT_WO_GEN"
if FLAG == "CONT_GEN" or (FLAG == "CONT_WO_GEN" and FLAG2 == "CHANGED"):
    if(options.full):
        subprocess.call("pip install Frida && pip install frida-tools", shell=True)
        subprocess.call("./../adb push cacert.cer /sdcard/Download/", shell=True)
        output = subprocess.Popen("./../adb shell getprop ro.product.cpu.abi", shell=True, stdout=subprocess.PIPE).stdout.read()
        if "x86" in str(output):
            subprocess.call("cp frida-server-x86 frida-server", shell=True)
        else:
            subprocess.call("cp frida-server-x86_64 frida-server", shell=True)
        subprocess.call("./../adb push frida-server /data/local/tmp", shell=True)
        subprocess.call("./../adb shell chmod 777 /data/local/tmp/frida-server", shell=True)
    if(options.default):    
        subprocess.call("./../adb shell /data/local/tmp/frida-server &", shell=True)
        output = subprocess.Popen("./../adb shell ls /data/data/ | grep "+"\""+AppName+"\"", shell=True, stdout=subprocess.PIPE).stdout.read()
        try:
            strn=str(output); AppName=strn[(strn.index("c")):strn.index("\\")]
        except:
            r="y"
            r=input("Application not running on the emulator. After running, press \"Y\" to continue or \"Ctrl+C\" to exit [Y]: ")
        finally:
            subprocess.call("frida -U -f " + AppName + " -l fridascript.js --no-paus", shell=True)
else:
    print("It is adviced to clone the SSL-bypass tool in the \"/genymotion/tools\" directory. If you are not using Genymotion, please use the following command,\"python3 no_geny.py\" and try again")
        
