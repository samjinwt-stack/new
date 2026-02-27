[app]

# -------------------------------------------------
# 기본 정보
# -------------------------------------------------

# 앱 이름
title = WorkLogNotion

# 패키지 이름
package.name = worklog

# 도메인 (역순 도메인 형식)
package.domain = org.samjinwt

# 소스 코드 위치
source.dir = .

# 포함할 파일 확장자
source.include_exts = py,kv,json,png,jpg,ttf

# 버전
version = 1.0

# 화면 방향
orientation = portrait

# 전체화면 여부
fullscreen = 0

# 필요한 라이브러리
requirements = python3,kivy,requests


# -------------------------------------------------
# Android 설정 (🔥 매우 중요)
# -------------------------------------------------

# 타겟 API
android.api = 34

# 최소 지원 API
android.minapi = 23

# NDK (python-for-android 안정 버전)
android.ndk = 25b

# 🔥 Preview build-tools 차단 (가장 중요)
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
# Build 설정
# -------------------------------------------------

# 로그 레벨
log_level = 2

# root 경고 허용
warn_on_root = 1


[buildozer]

# 빌드 로그 레벨
log_level = 2
