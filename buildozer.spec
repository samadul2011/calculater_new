[app]

# (str) Title of your application
title = Simple Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of: landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

#
# Android specific
#

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private to include all source files
android.private_storage = True

# (str) Path to a custom buildozer.spec
#android.add_src = 

# (str) Name of the .so file
#android.add_libs_armeabi = libs/armeabi/libexample.so
#android.add_libs_armeabi_v7a = libs/armeabi-v7a/libexample.so
#android.add_libs_arm64_v8a = libs/arm64-v8a/libexample.so
#android.add_libs_x86 = libs/x86/libexample.so
#android.add_libs_x86_64 = libs/x86_64/libexample.so

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Bootstrap to use
p4a.bootstrap = sdl2

# (str) The command to run your app
command = python3 main.py

#
# iOS specific
#
# ... (not needed for Android)

#
# Buildozer
#
build_dir = .buildozer
log_level = 2
warn_on_root = 1
