#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story Generator Bot - יוצר סיפורים מעניינים
"""

import random
from datetime import datetime

class StoryGenerator:
    def __init__(self):
        self.story_templates = [
            {
                "title": "הסיפור של הנקות",
                "theme": "מטפורה",
                "story": "בעולם שחור קטן היו שלושה אנשים שחברו לאחד השני. כל יום הם היו עושים משהו טוב לאחרים. עם הזמן, הם הבחינו שהעולם סביבם הופך לבהיר יותר ויותר. הם לא ידעו שכל מעשה טוב משדר אור. בסוף, כל העולם היה מלא בתאורה. הם למדו שאפילו המעשים הקטנים ביותר יכולים לשנות הכל."
            },
            {
                "title": "הנסיעה לעצמי",
                "theme": "השקעה אישית",
                "story": "הייתה דרך ארוכה למדי. אדם אחד החליט ללכת בה בלי לדעת לאן הוא הולך. הוא פגש אנשים רבים, כל אחד ואחד לימד אותו משהו חדש. לא הכל היה קל - היו ימים קשים מאוד. אבל הוא לא הפסיק. לבסוף, הוא הבין שהנסיעה הייתה לא אל מקום, אלא אל עצמו."
            },
            {
                "title": "הגן הנשכח",
                "theme": "תקווה",
                "story": "בעיר רועמת הייתה זוית שקטה - גן קטן ישן. אנשים עברו לידו בלי לשים לב. אך אחד מהם עצר וראה. הוא התחיל לטעת זרעים. לאט לאט, אחרים הצטרפו אליו. שנה אחת, הגן היה יפה וצבוני. העיר כולה התחילה להשתנות. הם למדו שתקווה גדלה לאט, אבל היא חזקה מאוד."
            },
            {
                "title": "החיבור הביתי",
                "theme": "משפחה",
                "story": "משפחה אחת החיתה חיים מלאים לחץ. כולם עסוקים בעבודה, טלפונים וחומרים. עד שיום אחד, הם התיישבו יחד ללא דברים אלה. התחילו לדבר, לצחוק ולשמוע אחד את השני. זה היה פשוט אבל עמוק מאוד. הם היו משחזרים מה שכמעט איבדו - חיבור אמיתי."
            },
            {
                "title": "העיר של הצבעים",
                "theme": "יצירתיות",
                "story": "עיר אפורה הייתה עם בניינים גרועים. אמן אחד התחיל לצייר על קירות. צבעים בהירים הופיעו בכל מקום. אנשים התחילו להבחין בעוצמה חדשה. עיר שלמה התחילה להשתנות דרך צבע. הם למדו שיצירתיות יכולה להגיע לכל מקום ולהשפיע על כולם."
            }
        ]

        self.images_keywords = {
            "מטפורה": ["אור", "חושך", "נקות", "זוהר"],
            "הנסיעה": ["דרך", "הרים", "עצים", "אופק"],
            "תקווה": ["פרחים", "זרעים", "שמש", "גן"],
            "משפחה": ["ידיים", "חיוך", "שולחן", "בית"],
            "יצירתיות": ["צבעים", "קיר", "ציור", "אמנות"]
        }

    def generate_story(self, index=None):
        """יוצר סיפור אקראי או בתור מסוים"""
        if index is None:
            story = random.choice(self.story_templates)
        else:
            story = self.story_templates[index % len(self.story_templates)]

        return {
            "title": story["title"],
            "theme": story["theme"],
            "text": story["story"],
            "images": self.images_keywords[story["theme"]],
            "duration": len(story["story"].split()) // 15 + 10,  # משך משוער בשניות
            "timestamp": datetime.now().isoformat()
        }

    def get_all_stories(self):
        """מחזיר את כל הסיפורים"""
        return self.story_templates

    def add_custom_story(self, title, theme, text):
        """הוסף סיפור מותאם אישית"""
        self.story_templates.append({
            "title": title,
            "theme": theme,
            "story": text
        })
        return f"סיפור '{title}' נוסף בהצלחה!"


if __name__ == "__main__":
    generator = StoryGenerator()

    # דוגמה: יוצר 3 סיפורים
    for i in range(3):
        story = generator.generate_story(i)
        print(f"\n📖 {story['title']}")
        print(f"🎨 ערכת: {story['theme']}")
        print(f"⏱️ משך: {story['duration']} שניות")
        print(f"📝 {story['text'][:100]}...")
        print(f"🖼️ תמונות: {', '.join(story['images'])}")
