#!/usr/bin/env python3
import subprocess, optparse

parser = optparse.OptionParser()
parser.add_option("-f","--fullinstall",action="store_true",dest="full",help="\"Install Pip\",\" Push Burp Certificate and frida server to the emulator \"")
parser.add_option("-d","--default",action="store_true",dest="default",help="Start the frida server")
parser.add_option("-a","--appname",dest="appName",help="Application Name")
(options, argument) = parser.parse_args()
AppName=options.appName
if(options.full):
    subprocess.call("pip install Frida && pip install frida-tools", shell=True)
    subprocess.call("./adb push cacert.cer /sdcard/Download/", shell=True)
if(options.default):
    subprocess.call("./adb push frida-server /data/local/tmp", shell=True)
    subprocess.call("./adb shell chmod 777 /data/local/tmp/frida-server", shell=True)
    subprocess.call("./adb shell /data/local/tmp/frida-server &", shell=True)
    output = subprocess.Popen("frida-ps -U | grep "+"\""+AppName+"\"", shell=True, stdout=subprocess.PIPE).stdout.read()
    try:
        strn=str(output); AppName=strn[(strn.index("c")):strn.index("\\")]
    except:
        r="y"
        r=input("Application not running on the emulator. After running, press \"Y\" to continue or \"Ctrl+C\" to exit [Y]: ")
    finally:
        subprocess.call("frida -U -f " + AppName + " -l fridascript.js --no-paus", shell=True)
