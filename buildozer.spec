[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy==2.3.0, hostpython3
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
