#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Creator Bot - יוצר וידאו מסיפור
"""

import os
import json
from pathlib import Path

class VideoCreator:
    def __init__(self, output_dir="./videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def create_video_script(self, story):
        """יוצר סקריפט לעריכת וידאו"""

        script = {
            "video_config": {
                "title": story["title"],
                "fps": 24,
                "resolution": "1920x1080",
                "duration": story["duration"]
            },
            "narration": {
                "text": story["text"],
                "language": "he",
                "gender": "male",
                "speed": 1.0
            },
            "images": {
                "keywords": story["images"],
                "transition": "fade",
                "duration_per_image": 5,
                "number_of_images": story["duration"] // 5
            },
            "metadata": {
                "description": f"סיפור: {story['title']}\n\nסיפור מעניין על {story['theme']}",
                "tags": [story["theme"], "סיפור", "השראה", "וידאו"],
                "category": "Education"
            }
        }

        return script

    def save_script(self, story):
        """שומר את הסקריפט כקובץ JSON"""
        script = self.create_video_script(story)
        filename = f"{self.output_dir}/{story['title'].replace(' ', '_')}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(script, f, ensure_ascii=False, indent=2)

        return filename

    def get_processing_instructions(self):
        """מחזיר הוראות לעיבוד הוידאו"""

        instructions = """
╔════════════════════════════════════════════════════════════╗
║        הוראות יצירת וידאו מהסקריפט                      ║
╚════════════════════════════════════════════════════════════╝

1️⃣ התקן את הספריות הנדרשות:
   pip install moviepy pyttsx3 pillow requests

2️⃣ הוראות לעריכת הוידאו (Python):

   from moviepy.editor import *
   from PIL import Image, ImageDraw
   import pyttsx3

   # א) יצור קול (Text-to-Speech)
   engine = pyttsx3.init()
   engine.setProperty('rate', 150)  # מהירות קריאה
   engine.setProperty('voice', 'hebrew')  # קול גברי בעברית
   engine.save_to_file(text, 'narration.mp3')
   engine.runAndWait()

   # ב) הוסף תמונות (חפש או הוסף תמונות מקומיות)
   images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
   clips = [ImageClip(img).set_duration(5) for img in images]

   # ג) חבר אודיו לוידאו
   audio = AudioFileClip('narration.mp3')
   final = concatenate_videoclips(clips).set_audio(audio)

   # ד) שמור את הוידאו
   final.write_videofile('output.mp4', fps=24)

3️⃣ חלופה מהירה - השתמש בכלי אנלינאיים:
   ✓ CapCut (desktop/mobile)
   ✓ OpenShot
   ✓ DaVinci Resolve (חינם)

4️⃣ אחרי שהוידאו מוכן:
   ✓ בדוק את האיכות
   ✓ הוסף תמונה עיטור (thumbnail)
   ✓ עלה ל-YouTube

╔════════════════════════════════════════════════════════════╗
║  אנא בדוק את הניהול של זכויות יוצרים על התמונות        ║
╚════════════════════════════════════════════════════════════╝
"""
        return instructions

    def create_sample_config(self):
        """יוצר קובץ הגדרות לדוגמה"""
        config = {
            "sources": {
                "image_apis": [
                    "unsplash",  # תמונות בחינם
                    "pexels",    # תמונות בחינם
                    "pixabay"    # תמונות בחינם
                ],
                "tts_services": [
                    "google_tts",  # Google Text-to-Speech
                    "pyttsx3",     # Local TTS (Python)
                    "elevenlabs"   # Paid - טוב יותר
                ]
            },
            "video_settings": {
                "resolution": "1920x1080",
                "fps": 24,
                "bitrate": "5000k",
                "codec": "h264"
            },
            "upload_settings": {
                "platform": "youtube",
                "schedule": "daily",
                "time": "18:00"
            }
        }

        with open(f"{self.output_dir}/config.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        return config


if __name__ == "__main__":
    from story_generator import StoryGenerator

    # יוצר סיפור ובונה וידאו סקריפט
    generator = StoryGenerator()
    creator = VideoCreator()

    story = generator.generate_story(0)
    script_file = creator.save_script(story)

    print(f"✅ סקריפט נשמר: {script_file}")
    print(creator.get_processing_instructions())
