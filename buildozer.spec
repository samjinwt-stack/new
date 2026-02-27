[app]

# -------------------------------------------------
# 기본 정보
# -------------------------------------------------

title = WorkLogNotion
package.name = worklog
package.domain = org.samjinwt

source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf

version = 1.0

orientation = portrait
fullscreen = 0

requirements = python3,kivy,requests


# -------------------------------------------------
# Android 설정 (🔥 매우 중요)
# -------------------------------------------------

# Target API
android.api = 34

# Minimum API
android.minapi = 23

# Stable NDK (python-for-android 호환 안정판)
android.ndk = 25b

# 🔥 Preview build-tools 차단 (이 줄 반드시 필요)
android.sdk_build_tools = 34.0.0

# Architecture (Play Store 기준 arm64 필수)
android.arch = arm64-v8a

# Permissions
android.permissions = INTERNET

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# 자동 백업 비활성화
android.allow_backup = False


# -------------------------------------------------
# 빌드 옵션
# -------------------------------------------------

log_level = 2
warn_on_root = 1

p4a.branch = stable


[buildozer]

log_level = 2
