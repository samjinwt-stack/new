[app]

# -------------------------------------------------
# 기본 정보
# -------------------------------------------------

# 앱 이름
title = WorkLogNotion

# 패키지 이름 (소문자/숫자만)
package.name = worklognotion

# 도메인 (역순 도메인 형식)
package.domain = com.samjinwt

# 소스 코드 위치
source.dir = .

# 포함할 파일 확장자
source.include_exts = py,kv,json,png,jpg,jpeg,webp,txt,ini,ttf,otf,atlas

# 앱 버전
version = 0.1.0

# 화면 방향
orientation = portrait

# 전체화면 여부
fullscreen = 0

# 의존성 (실제 import 기준으로 맞춰야 함)
requirements = python3,kivy,requests,notion-client

# 엔트리 파일
entrypoint = main.py

# 로그 레벨
log_level = 2


# -------------------------------------------------
# Buildozer 설정
# -------------------------------------------------

[buildozer]

warn_on_root = 1
log_level = 2


# -------------------------------------------------
# Android 설정 (🔥 매우 중요)
# -------------------------------------------------

[android]

# 타겟 API
android.api = 34

# 최소 API
android.minapi = 24

# 🔥 build-tools 고정 (Preview 37-rc 방지 핵심)
android.build_tools_version = 34.0.0

# 아키텍처 (Play Store 기준 arm64 필수)
android.archs = arm64-v8a,armeabi-v7a

# 권한
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# AndroidX 사용
android.enable_androidx = True

# SDK 라이선스 자동 동의
android.accept_sdk_license = True

# 🔥 p4a가 SDK 업데이트 못하게 막기 (중요)
p4a.extra_args = --no-sdk-update

# (선택) NDK 고정 필요시
# android.ndk = 25b
