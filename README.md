# SSL-pinning-bypass

This is a python code that automates the hefty setup of frida server for SSL Pinning Bypass.

Basic Command:
```
python3 ssl_pinning_bypass.py -d -a <target_app>
```

There are several options that will be used:

`-f` `--fullinstall` : Is used to initialize the tool and automatically configure everything for you.(Only to be used once, per device)<br>
`-d` `--default` : Is used to start the Frida Server in the Android app, and bypass the SSL Pinning.(Needs to be used everytime)<br>
`-a` `--appname` : Is used to provide the application name.(Here you can either give simply the Application Name or give the complete package name, both will work perfectly)<bR>


## Cloning and setting up:

---
If you use Genymotion as an Emulator while testing, is adviced to clone the repo in the "/genymotion/tools/" folder. If not, you can clone it anywhere. There will be some additional setup, that can be found at the end.

---
**1. Clone the repo:**
```
git clone https://github.com/anirudh3171/SSL-pinning-bypass
```

**2. Open the folder**
```
cd SSL-pinning-bypass:
```

**3. Initialize the application:**
```
python3 ssl_pinning_bypass.py -f
```

Now everything is configured and ready to go.

**4. Bypassing SSL Pinning:**
```
python3 ssl_pinning_bypass.py -d -a <target_app>
```
Here in <target_app>, both package name as well as the application name can be given.
Example:
- python3 ssl_pinning_bypass.py -d -a target_app
- python3 ssl_pinning_bypass.py -d -a com.xyz.target_app

---
### Only for users that donot use Genymotion:

After Steps 1 and 2, run the following command,
```
python3 no_geny.py
```
then follow the step 3, and you are good to go.

<br>

After the above step, If you want to use it with Genymotion, use the command,
```
python3 with_geny.py
```
---

If you need help setting up your Android with Burp Suite, follow the steps given here, https://webkul.com/blog/configure-android-device-with-burpsuite/


The following tools are used in this project are not needed to be downloaded again:
- Javascript file used for bypass can be found at "https://codeshare.frida.re/@pcipolloni/universal-android-ssl-pinning-bypass-with-frida/".
- Frida-Servers used can be downloaded from, "https://github.com/frida/frida/releases/"

Some great articles on SSL Pinning Bypass can be found here,
- https://securitygrind.com/bypassing-android-ssl-pinning-with-frida/
- https://medium.com/@ved_wayal/hail-frida-the-universal-ssl-pinning-bypass-for-android-e9e1d733d29
