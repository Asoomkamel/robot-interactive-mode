# 🤖 Robot Interactive Mode (KAMEL) | وضع التفاعل للروبوت (كامل)

This repository contains the source code for an interactive robot named **KAMEL**, powered by a Raspberry Pi 5. The robot uses a microphone and speaker connected via a 3D USB sound card to interact with users in Arabic, utilizing Google's Gemini AI for intelligence and Edge-TTS for high-quality speech synthesis.

يحتوي هذا المستودع على الكود المصدري لروبوت تفاعلي باسم **كامل**، يعمل بواسطة رازبيري باي 5. يستخدم الروبوت ميكروفوناً وسماعة متصلين عبر بطاقة صوت USB ثلاثية الأبعاد للتفاعل مع المستخدمين باللغة العربية، معتمداً على ذكاء Gemini الاصطناعي من جوجل وتقنية Edge-TTS لتوليد الصوت بجودة عالية.

---

## 📸 Demo | العرض المرئي
[Watch the Robot in Action | شاهد الروبوت وهو يعمل](https://drive.google.com/file/d/1w_BwCKqQYVkbbFMpG29M60be989f4-x5/view?usp=drivesdk)

---

## 🛠️ Hardware Components | المكونات العتادية

To build this project, the following components were used:
لبناء هذا المشروع، تم استخدام المكونات التالية:

| Component | المكون | Description | الوصف |
| :--- | :--- | :--- | :--- |
| **Raspberry Pi 5** | **رازبيري باي 5** | The main controller for the robot. | المتحكم الرئيسي للروبوت. |
| **USB 3D Sound Card** | **بطاقة صوت USB 3D** | [Technotech Sound Adapter 7.1](https://www.amazon.in/Technotech-Sound-Adapter-Virtual-Channel/dp/B017B8UPVW) for audio I/O. | بطاقة صوت لتوصيل الميكروفون والسماعة. |
| **Microphone** | **ميكروفون** | Standard 3.5mm mic connected to the sound card. | ميكروفون قياسي متصل ببطاقة الصوت. |
| **Speaker** | **سماعة** | External speaker for robot voice output. | سماعة خارجية لإخراج صوت الروبوت. |
| **Robot Body** | **جسم الروبوت** | Custom red and black chassis as seen in the video. | هيكل الروبوت (أحمر وأسود) كما يظهر في الفيديو. |

---

## 🚀 Software Features | مميزات البرمجيات

- **Wake Word Detection**: Responds to "Kamel" (كامل) to start interaction.
- **AI Intelligence**: Uses Google Gemini 2.5 Flash for fast and smart responses.
- **Bilingual Support**: Fully optimized for Arabic interaction.
- **Voice Synthesis**: Uses `edge-tts` for natural-sounding Arabic speech.
- **Hardware Utility**: Includes scripts to find microphone sample rates and list AI models.

- **التعرف على كلمة التنبيه**: يستجيب لكلمة "كامل" لبدء التفاعل.
- **ذكاء اصطناعي**: يستخدم Gemini 2.5 Flash لردود سريعة وذكية.
- **دعم اللغة العربية**: محسن بالكامل للتفاعل باللغة العربية.
- **توليد الصوت**: يستخدم `edge-tts` لصوت عربي طبيعي.
- **أدوات العتاد**: يتضمن سكربتات لفحص الميكروفون وقائمة موديلات الذكاء الاصطناعي.

---

## 📂 File Structure | هيكل الملفات

- `main.py`: The entry point that manages the wake-word state and main loop.
- `bot.py`: Contains the `NovaRobot` class handling speech, listening, and AI logic.
- `find_rate.py`: Utility to find the correct sample rate for your USB microphone.
- `list_models.py`: Utility to list available Google GenAI models.

- `main.py`: الملف الرئيسي الذي يدير حالة الاستيقاظ وحلقة العمل الأساسية.
- `bot.py`: يحتوي على كلاس `NovaRobot` المسؤول عن التحدث والاستماع والذكاء الاصطناعي.
- `find_rate.py`: أداة لإيجاد تردد العينة (Sample Rate) المناسب للميكروفون.
- `list_models.py`: أداة لعرض موديلات الذكاء الاصطناعي المتاحة من جوجل.

---

## ⚙️ Installation | التثبيت

1. **Clone the repo | استنساخ المستودع**:
   ```bash
   git clone https://github.com/Asoomkamel/robot-interactive-mode.git
   cd robot-interactive-mode
   ```

2. **Install dependencies | تثبيت المكتبات**:
   ```bash
   pip install google-genai speechrecognition edge-tts
   sudo apt-get install alsa-utils mpg123
   ```

3. **Configure API Key | إعداد مفتاح API**:
   Update the `API_KEY` in `bot.py` or set it as an environment variable.
   قم بتحديث مفتاح `API_KEY` في ملف `bot.py`.

4. **Run | التشغيل**:
   ```bash
   python main.py
   ```

---

## 👨‍💻 Author | المطور
**Asoomkamel**
