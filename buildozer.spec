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
# Android 설정 (🔥 중요)
# -------------------------------------------------

# 타겟 API
android.api = 34

# 최소 지원 API
android.minapi = 23

# NDK (python-for-android 안정 버전)
android.ndk = 25b

# ✅ Preview 차단 — build-tools 안정 버전 고정
android.sdk_build_tools = 34.0.0

# 아키텍처 (PlayStore 기준 필수)
android.arch = arm64-v8a

# 권한
android.permissions = INTERNET

# Entry point
android.entrypoint = org.kivy.android.PythonActivity

# 자동 백업 비활성화
android.allow_backup = False


# -------------------------------------------------
# 빌드 설정
# -------------------------------------------------

log_level = 2
warn_on_root = 1

[buildozer]

log_level = 2
