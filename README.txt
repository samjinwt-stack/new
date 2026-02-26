# 안드로이드 버전 (Kivy APK) — WorkLog Notion

## 핵심
- PC(Tkinter)는 APK로 바로 못 바꿉니다.
- 안드로이드는 별도 앱이 필요해서 Kivy로 동일 기능 앱을 만들었습니다.
- 이 앱은 Notion API를 '앱'에서 직접 호출하므로(브라우저 아님) CORS 문제를 피합니다.

## 1) config.json 수정
notion_token 값을 실제 토큰(secret_...)으로 바꾸세요.

## 2) APK 만들기 (윈도우: WSL2 추천)
### 2-1) WSL2 Ubuntu 설치
Windows에서 WSL2 + Ubuntu 설치 후 Ubuntu 터미널 실행

### 2-2) 빌드 준비
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3 python3-pip build-essential   ccache libffi-dev libssl-dev autoconf automake libtool pkg-config

python3 -m pip install --upgrade pip
python3 -m pip install cython buildozer

### 2-3) 이 폴더로 이동 후 빌드
buildozer -v android debug

## 3) 결과 APK
bin/WorkLogNotion-0.1.0-debug.apk
이 파일을 폰으로 옮겨 설치하면 됩니다(알 수 없는 앱 설치 허용 필요할 수 있음).

## 4) 노션 권한
DB 페이지에서 Share → Add connections → Integration 추가 필수

## 5) 보안 주의
이 버전은 요청대로 토큰을 앱에 넣는 간단 버전입니다(내부용 권장).
