#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Uploader Bot - העלאה ליוטיוב בטוח
"""

class YouTubeUploader:
    def __init__(self):
        self.setup_instructions = """
╔════════════════════════════════════════════════════════════╗
║         הוראות התחברות ליוטיוב API בטוח                  ║
╚════════════════════════════════════════════════════════════╝

שלב 1️⃣: יצור OAuth Credentials
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. לך ל: https://console.cloud.google.com/
2. צור פרויקט חדש
3. הפעל את "YouTube Data API v3"
4. צור OAuth 2.0 credentials
5. בחר "Desktop application"
6. הורד את הקובץ JSON

שלב 2️⃣: התקן את הספריות
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pip install google-auth-oauthlib google-auth-httplib2

שלב 3️⃣: שתמש בקוד זה להעלאה

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# התחברות
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/youtube.upload']
)
credentials = flow.run_local_server()
youtube = build('youtube', 'v3', credentials=credentials)

# העלאה
request = youtube.videos().insert(
    part='snippet,status',
    body={
        'snippet': {
            'title': 'סיפורך',
            'description': 'תיאור...',
            'tags': ['סיפור', 'השראה'],
            'categoryId': '22'  # Education
        },
        'status': {
            'privacyStatus': 'public'  # או 'unlisted'
        }
    },
    media_body=MediaFileUpload('video.mp4')
)
response = request.execute()
print(f"Video ID: {response['id']}")

שלב 4️⃣: אבטחה ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ לא תשמור סיסמאות
✓ הקובץ credentials.json בעל הרשאות בלבד
✓ לא תשתף סיסמאות עם בוטים אחרים
✓ הרשאות OAuth אפשר לבטל כל עת

"""

    def create_uploader_script(self):
        """יוצר סקריפט העלאה בטוח"""
        script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Secure YouTube Uploader - בוט העלאה בטוח
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class SecureYouTubeUploader:
    def __init__(self, credentials_file='credentials.json'):
        self.credentials_file = credentials_file
        self.youtube = self._authenticate()

    def _authenticate(self):
        """התחברות בטוחה דרך OAuth"""
        if not os.path.exists(self.credentials_file):
            raise FileNotFoundError(f"אנא הורד את {self.credentials_file} מ-Google Cloud Console")

        flow = InstalledAppFlow.from_client_secrets_file(
            self.credentials_file,
            scopes=['https://www.googleapis.com/auth/youtube.upload']
        )
        credentials = flow.run_local_server(port=0)
        return build('youtube', 'v3', credentials=credentials)

    def upload_video(self, video_file, title, description, tags):
        """העלאת וידאו ליוטיוב"""
        try:
            print(f"📤 מעלה: {title}...")

            request = self.youtube.videos().insert(
                part='snippet,status',
                body={
                    'snippet': {
                        'title': title,
                        'description': description,
                        'tags': tags,
                        'categoryId': '22',  # Education
                        'defaultLanguage': 'he',
                        'defaultAudioLanguage': 'he'
                    },
                    'status': {
                        'privacyStatus': 'unlisted'  # תחילה בדוק את הוידאו
                    }
                },
                media_body=MediaFileUpload(video_file, chunksize=-1)
            )

            response = request.execute()
            video_id = response.get('id')
            print(f"✅ הוידאו הועלה בהצלחה!")
            print(f"🔗 קישור: https://youtu.be/{video_id}")
            return video_id

        except Exception as e:
            print(f"❌ שגיאה בהעלאה: {e}")
            return None


if __name__ == "__main__":
    uploader = SecureYouTubeUploader()

    # דוגמה - בדוק שקובץ הוידאו קיים
    # uploader.upload_video(
    #     "video.mp4",
    #     "סיפור מעניין",
    #     "סיפור על השראה וחוסן",
    #     ["סיפור", "השראה", "וידאו"]
    # )
'''
        return script

    def get_schedule_script(self):
        """יוצר סקריפט לתזמון העלאות אוטומטיות"""
        script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scheduled Uploader - העלאה אוטומטית בתזמון קבוע
"""

import schedule
import time
from youtube_uploader import SecureYouTubeUploader
from story_generator import StoryGenerator
from video_creator import VideoCreator

class ScheduledUploader:
    def __init__(self):
        self.uploader = SecureYouTubeUploader()
        self.generator = StoryGenerator()
        self.creator = VideoCreator()

    def upload_daily_video(self):
        """העלאה יומית של וידאו חדש"""
        try:
            # 1. יוצר סיפור
            story = self.generator.generate_story()

            # 2. יוצר סקריפט וידאו
            script = self.creator.create_video_script(story)

            # 3. בדיקה - האם הוידאו מוכן?
            video_path = f"./videos/{story['title']}.mp4"
            if not os.path.exists(video_path):
                print(f"⚠️ וידאו לא נמצא: {video_path}")
                print("נא להשתמש בדו\"ח וידאו קודם")
                return

            # 4. העלאה
            self.uploader.upload_video(
                video_path,
                story['title'],
                script['metadata']['description'],
                script['metadata']['tags']
            )

        except Exception as e:
            print(f"❌ שגיאה בהעלאה היומית: {e}")

    def schedule_uploads(self):
        """קביעת תזמון של העלאות"""
        # דוגמה: העלאה כל יום בשעה 18:00
        schedule.every().day.at("18:00").do(self.upload_daily_video)

        print("📅 תזמון מופעל...")
        while True:
            schedule.run_pending()
            time.sleep(60)


if __name__ == "__main__":
    uploader = ScheduledUploader()
    uploader.schedule_uploads()
'''
        return script

    def get_instructions(self):
        return self.setup_instructions


if __name__ == "__main__":
    uploader = YouTubeUploader()
    print(uploader.get_instructions())
    print("\n📝 קובץ סקריפט בוט העלאה נוצר בהצלחה!")
