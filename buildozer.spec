[app]
title = YourAppTitle
package.name = yourapppackagename
package.domain = com.interp
source.dir = .
requirements = python3,kivy,requests,pyjnius
version = 0.1

# Create the APK
osx.python_version = 3
osx.kivy_version = 1.11.1
android.permissions = INTERNET,SEND_SMS

[buildozer]
log_level = 2
warn_on_root = 1
