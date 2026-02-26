[app]
title = WorkLogNotion
package.name = worklog
package.domain = org.samjinwt
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
requirements = python3,kivy,requests
version = 1.0
orientation = portrait
fullscreen = 0

# -------------------------------------------------
# ANDROID 설정
# -------------------------------------------------
android.api = 34
android.minapi = 23

# (선택) android.sdk 는 보통 필요 없음. 헷갈리면 빼도 됨.
# android.sdk = 34

android.ndk = 25b

# ✅ build-tools 안정버전 고정 (가장 중요)
android.sdk_build_tools = 34.0.0

android.arch = arm64-v8a
android.permissions = INTERNET
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = False

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
