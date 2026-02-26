[app]

# (str) Title of your application
title = WorkLogNotion

# (str) Package name
package.name = worklog

# (str) Package domain (reverse domain style)
package.domain = org.samjinwt

# (str) Source code folder
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,json,png,jpg,ttf

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Application version
version = 1.0

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# -------------------------------------------------
# ANDROID SETTINGS (이게 핵심)
# -------------------------------------------------

# Target Android API
android.api = 34

# Minimum API
android.minapi = 23

# SDK version
android.sdk = 34

# NDK version (p4a 권장)
android.ndk = 25b

# 🔥 중요: Preview 막고 안정판 build-tools 고정
android.build_tools = 34.0.0

# Architecture
android.arch = arm64-v8a

# Permissions (필요한 것만)
android.permissions = INTERNET

# -------------------------------------------------
# Buildozer options
# -------------------------------------------------

log_level = 2

warn_on_root = 1


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
