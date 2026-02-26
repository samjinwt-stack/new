[app]

# (str) Application title
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

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# -------------------------------------------------
# ANDROID 설정 (🔥 중요)
# -------------------------------------------------

# Target API
android.api = 34

# Minimum supported API
android.minapi = 23

# SDK version
android.sdk = 34

# Recommended NDK for p4a
android.ndk = 25b

# 🔥 Preview 차단 — 안정 버전 고정
android.build_tools = 34.0.0

# Architecture (Play Store 기준 arm64 필수)
android.arch = arm64-v8a

# Required permissions
android.permissions = INTERNET

# Android entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# (optional) Prevent automatic version changes
android.allow_backup = False


# -------------------------------------------------
# Buildozer 설정
# -------------------------------------------------

log_level = 2
warn_on_root = 1


[buildozer]

# Debug log level
log_level = 2
