from datetime import date
import json
import os

import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

KV = r"""
<RootUI>:
    orientation: "vertical"
    padding: dp(12)
    spacing: dp(10)

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        Label:
            text: "작업자"
            size_hint_x: None
            width: dp(90)
            halign: "left"
            valign: "middle"
            text_size: self.size
        Spinner:
            id: worker
            text: root.default_worker
            values: root.workers
            size_hint_x: 1

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        Label:
            text: "날짜"
            size_hint_x: None
            width: dp(90)
            halign: "left"
            valign: "middle"
            text_size: self.size
        TextInput:
            id: work_date
            text: root.default_date
            multiline: False
            hint_text: "YYYY-MM-DD"

    Label:
        text: "작업내용"
        size_hint_y: None
        height: dp(24)
        halign: "left"
        valign: "middle"
        text_size: self.size

    TextInput:
        id: content
        hint_text: "오늘 작업 내용을 입력하세요"
        multiline: True

    Button:
        text: "등록"
        size_hint_y: None
        height: dp(48)
        on_release: root.submit()

    Label:
        text: root.status_text
        size_hint_y: None
        height: dp(24)
"""

def show_popup(title: str, msg: str):
    Popup(title=title, content=Label(text=msg), size_hint=(0.85, 0.35)).open()

def load_config():
    path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def is_valid_date(s: str) -> bool:
    try:
        y, m, d = map(int, s.split("-"))
        date(y, m, d)
        return True
    except Exception:
        return False

class RootUI(BoxLayout):
    workers = ListProperty([])
    default_worker = StringProperty("")
    default_date = StringProperty("")
    status_text = StringProperty("대기중")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cfg = load_config()
        self.workers = self.cfg.get("workers") or ["충북해","배성학","박진영","박현철","조성규","이상원","하진우"]
        self.default_worker = self.workers[0]
        self.default_date = date.today().strftime("%Y-%m-%d")

    def submit(self):
        worker = self.ids.worker.text.strip()
        work_date = self.ids.work_date.text.strip()
        content = self.ids.content.text.strip()

        if not worker:
            show_popup("입력 오류", "작업자를 선택하세요.")
            return
        if not is_valid_date(work_date):
            show_popup("입력 오류", "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형태로 입력하세요.")
            return
        if not content:
            show_popup("입력 오류", "작업내용을 입력하세요.")
            return

        token = (self.cfg.get("notion_token") or "").strip()
        dbid = (self.cfg.get("database_id") or "").strip()
        props = self.cfg.get("properties") or {}
        prop_worker = props.get("worker", "작업자")
        prop_date = props.get("work_date", "날짜")
        prop_content = props.get("content", "작업내용")

        if not token.startswith("secret_") or not dbid:
            show_popup("설정 오류", "config.json의 notion_token / database_id를 확인하세요.")
            return

        self.status_text = "등록 중..."

        try:
            url = "https://api.notion.com/v1/pages"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Notion-Version": self.cfg.get("notion_version", "2022-06-28"),
            }

            payload = {
                "parent": {"database_id": dbid},
                "properties": {
                    prop_worker: {"select": {"name": worker}},
                    prop_date: {"date": {"start": work_date}},
                    prop_content: {"rich_text": [{"type": "text", "text": {"content": content}}]},
                }
            }

            r = requests.post(url, headers=headers, json=payload, timeout=20)
            if r.status_code >= 300:
                try:
                    err = r.json()
                except Exception:
                    err = {"status_code": r.status_code, "text": r.text[:500]}
                self.status_text = "실패"
                show_popup("등록 실패", str(err))
                return

            self.status_text = "✅ 등록 완료"
            show_popup("완료", "노션에 등록되었습니다.")
            self.ids.content.text = ""

        except Exception as e:
            self.status_text = "실패"
            show_popup("오류", str(e))

class WorkLogApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootUI()

if __name__ == "__main__":
    WorkLogApp().run()
