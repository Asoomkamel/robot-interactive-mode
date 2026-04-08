import os
import time
import subprocess
import speech_recognition as sr
from datetime import datetime
from google import genai
from google.genai import types

class NovaRobot:

    def __init__(self):
        # 1. API Key Setup
        self.API_KEY = "AIzaSyAqAJfbYC_3CwdZlJSVWIm4FQbiYQK8UdE"
        self.client = genai.Client(api_key=self.API_KEY)

        # 2. Persona Definition
        self.system_instruction = """
أنت كامل (KAMEL)، روبوت خدمة ذكي يعمل في منشأة داخلية.
🔴 القواعد:
- نفذ مهام التوصيل المعينة من النظام المركزي فقط.
- اعتذر بأدب عن طلبات الزوار المباشرة ووجههم للموظفين.
- أجب عن الأسئلة العامة (وقت، اتجاهات) باختصار.
- رمز التفعيل الإداري: "كامل أدمن".
أسلوبك: محترف، هادئ، وباللغة العربية.
""" 
        # 3. Initialize Chat with Flash (Fastest model)
        self.chat = self.client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0.7,
            ),
        )

        # 4. Speech Recognition Setup
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 70  # Slightly higher to ignore background hum
        self.recognizer.dynamic_energy_threshold = False

    def listen(self):
        wav_file = "/tmp/nova_mic.wav"
        if os.path.exists(wav_file):
            os.remove(wav_file)

        print("\n🎤 (كامل يستمع...)")
        
        try:
            # -d 5: Listen for 5 seconds per turn
            command = f"arecord -D plughw:2,0 -d 5 -f S16_LE -r 16000 -c 1 -q {wav_file}"
            subprocess.run(command, shell=True, check=True)
            
            if not os.path.exists(wav_file):
                return None

            with sr.AudioFile(wav_file) as source:
                audio = self.recognizer.record(source)
                try:
                    text = self.recognizer.recognize_google(audio, language="ar-SA")
                    print(f"👤 قلت: {text}")
                    return text
                except sr.UnknownValueError:
                    return None
                except sr.RequestError:
                    return "ERROR_STT"

        except Exception as e:
            print(f"❌ Mic Error: {e}")
            return None
    
    def speak(self, text):
        if not text:
            return

        print(f"🤖 KAMEL: {text}")
        filename = "/tmp/voice_out.mp3"

        # Generate using edge-tts
        cmd_gen = f'edge-tts --voice ar-SA-HamedNeural --text "{text}" --write-media {filename}'
        subprocess.run(cmd_gen, shell=True)

        # Play using mpg123
        if os.path.exists(filename):
            cmd_play = f"mpg123 -q {filename}"
           # cmd_play = f"mpg123 -f 65536 -q {filename}"
            subprocess.run(cmd_play, shell=True)
            os.remove(filename)

    def think(self, user_text):
        """Process user text with Gemini AI | معالجة نص المستخدم عبر الذكاء الاصطناعي"""
        try:
            current_time = datetime.now().strftime("%A, %H:%M")
            prompt_with_context = f"[System Time: {current_time}] User asks: {user_text}"

            # Memory reset logic | منطق تصفير الذاكرة
            if any(word in user_text for word in ["انسى", "موضوع جديد"]):
                self.chat = self.client.chats.create(
                    model="gemini-2.5-flash",
                    config=types.GenerateContentConfig(
                        system_instruction=self.system_instruction,
                        temperature=0.7,
                    ),
                )
                return "تم تصفير الذاكرة. كيف يمكنني مساعدتك الآن؟"

            response = self.chat.send_message(prompt_with_context)
            return response.text

        except Exception as e:
            print(f"⚠️ Gemini Error: {e}")
            return self.offline_reply(user_text)

    def offline_reply(self, text):
        if "الوقت" in text: return datetime.now().strftime("الساعة الآن %H:%M")
        return "أواجه مشكلة في الاتصال حالياً."
