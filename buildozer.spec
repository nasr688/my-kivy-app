[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# ----------------------------------
# Android configuration
# ----------------------------------

# (int) Android API to use
android.api = 34

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android Build Tools version to use
android.build_tools_version = 34.0.0

# (bool) Allow meta building process
android.allow_meta_building = yes

# (bool) Accept android licenses
android.accept_apk_license = yes

# (str) The Android arch to build for
android.archs = arm64-v8a

# (list) Permissions
android.permissions = INTERNET

# (int) Target MDPI icon for the app
#android.icon.target_mdpi = %(source.dir)s/icon.png

# (str) Presplash of the application
#android.presplash_src = %(source.dir)s/presplash.png

# (list) List of Java .jar files to add to the libs so that pyobjus can use
#android.add_jars = foo.jar

# (list) List of Java files to add to the android project
#android.add_src = src/MyActivity.java

# (list) Gradle dependencies
#android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = yes

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
