#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Orchestrator - מנהל הבוטים הראשי
"""

import sys
from story_generator import StoryGenerator
from video_creator import VideoCreator
from youtube_uploader import YouTubeUploader

class BotOrchestrator:
    def __init__(self):
        self.story_generator = StoryGenerator()
        self.video_creator = VideoCreator()
        self.youtube_uploader = YouTubeUploader()

    def generate_workflow(self, num_stories=3):
        """יוצר זרימת עבודה של יצירת סיפורים וסקריפטים"""
        print("=" * 60)
        print("🤖 בוט אורכסטרציה - מערכת יצירת תוכן ליוטיוב")
        print("=" * 60)

        workflows = []

        for i in range(num_stories):
            print(f"\n📖 סיפור #{i + 1}")
            print("-" * 60)

            # 1. יוצר סיפור
            story = self.story_generator.generate_story(i)
            print(f"✓ סיפור: {story['title']}")
            print(f"  ערכת: {story['theme']}")
            print(f"  משך משוער: {story['duration']} שניות")

            # 2. יוצר סקריפט וידאו
            script_file = self.video_creator.save_script(story)
            print(f"✓ סקריפט נשמר: {script_file}")

            # 3. הוראות עריכה
            print(f"✓ תמונות מומלצות: {', '.join(story['images'])}")

            workflows.append({
                "story": story,
                "script_file": script_file,
                "status": "ready_for_editing"
            })

        return workflows

    def display_full_workflow(self):
        """מציג את זרימת העבודה המלאה"""
        print("\n" + "=" * 60)
        print("📋 זרימת העבודה המלאה")
        print("=" * 60)

        workflow_steps = """
1️⃣ יוצר סיפור 🤖 (בוט סיפורים)
   ↓
2️⃣ יוצר סקריפט וידאו (בוט וידאו)
   ↓
3️⃣ משתמש עורך את הוידאו 👨‍💻
   • הוסף תמונות
   • הוסף אודיו (TTS)
   • עריכה בחירה
   ↓
4️⃣ יוצר קובץ MP4 סופי
   ↓
5️⃣ מעלה ליוטיוב 📤 (בוט יוטיוב - בטוח)
   ✓ OAuth - ללא סיסמאות
   ✓ ללא בוטים מזויפים
   ✓ תוכן אמיתי 100%
"""
        print(workflow_steps)

    def display_technical_stack(self):
        """מציג את הטכנולוגיה המשמשת"""
        print("\n" + "=" * 60)
        print("🛠️ מחסנית טכנולוגית")
        print("=" * 60)

        stack = """
📚 Story Generator (Python)
   • יוצר סיפורים מעניינים
   • ערכות שונות
   • אפשרות להוסיף סיפורים משלך

🎬 Video Creator (Python + moviepy)
   • יוצר סקריפטים
   • תמונות מומלצות
   • הוראות עריכה מפורשות

🎤 Text-to-Speech (pyttsx3 / Google TTS)
   • קול גברי בעברית
   • חינם (pyttsx3) או טוב יותר (Google)
   • בדיקת איכות

🎥 Video Editing (DaVinci Resolve / CapCut)
   • חינם וקל לשימוש
   • ממשק ויזואלי
   • ייצוא ל-MP4

📤 YouTube Uploader (Google API)
   • OAuth - התחברות בטוחה
   • ללא סיסמאות מאוחסנות
   • בדיקה אחד-אחד

🕐 Scheduler (schedule + APScheduler)
   • העלאה אוטומטית יומית
   • התזמון גמיש
   • דיווח שגיאות
"""
        print(stack)

    def display_security_info(self):
        """מציג מידע אבטחה חשוב"""
        print("\n" + "=" * 60)
        print("🔒 אבטחה וגישור חוקי")
        print("=" * 60)

        security = """
✅ ללא בוטים מזויפים
   • תצפיות אמיתיות בלבד
   • לא שוברים את כללי יוטיוב

✅ התחברות בטוחה
   • OAuth 2.0
   • ללא שמירת סיסמאות
   • יכול לבטל הרשאות כל עת

✅ זכויות יוצרים
   • השתמש בתמונות בחינם
   • (Unsplash, Pexels, Pixabay)
   • בדוק רישיונות

✅ תוכן מתאים
   • ללא מילים גסות
   • ללא תוכן פוגעני
   • מתאים לכל הגילאים
"""
        print(security)


def main():
    """תוכנית ראשית"""
    orchestrator = BotOrchestrator()

    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + " " * 10 + "🤖 מערכת יצירת תוכן ליוטיוב בוט 🤖" + " " * 15 + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    # אפשרות 1: יוצר סיפורים וסקריפטים
    print("💡 יצירת סיפורים וסקריפטים:")
    print("-" * 60)
    workflows = orchestrator.generate_workflow(3)

    # אפשרות 2: תזכורות
    print("\n")
    orchestrator.display_full_workflow()
    orchestrator.display_technical_stack()
    orchestrator.display_security_info()

    # הוראות סיום
    print("\n" + "=" * 60)
    print("📝 השלבים הבאים:")
    print("=" * 60)
    print("""
1. התקן את הספריות:
   pip install moviepy pyttsx3 google-auth-oauthlib google-auth-httplib2

2. הרץ את הגנרטור:
   python bot_orchestrator.py

3. בחר כלי עריכה וידאו (חינם):
   ✓ DaVinci Resolve
   ✓ CapCut
   ✓ OpenShot

4. עבור ל-YouTube:
   https://console.cloud.google.com/
   • צור OAuth credentials
   • הורד את credentials.json

5. העלה את הוידאו בטוח דרך:
   python youtube_uploader.py

צלחתם! 🎉
""")


if __name__ == "__main__":
    main()
