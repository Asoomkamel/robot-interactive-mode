
from bot import NovaRobot
import time

def main():
    # Initialize the robot | تهيئة الروبوت
    nova = NovaRobot()
    
    # Wake state variable (Initially asleep) | متغير حالة الاستيقاظ (في البداية يكون نائماً)
    is_awake = False
    
    print("\n--- 🌑 System in Standby Mode | النظام يعمل في وضع الاستعداد ---")
    print("--- 🗣️ Say 'Kamel' to activate | قل 'كامل' لتفعيل الروبوت ---")

    while True:
        # 1. Robot is always listening | الروبوت يستمع دائماً
        user_text = nova.listen()

        # If nothing heard or error, retry | إذا لم يسمع شيئاً أو حدث خطأ، أعد المحاولة
        if user_text is None:
            continue

        # 2. Mode 1: Robot is asleep (Waiting for wake word) | الوضع الأول: الروبوت نائم (ينتظر كلمة السر)
        if not is_awake:
            # Check for "Kamel" in the sentence | التحقق من وجود كلمة "كامل" في الجملة
            if "كامل" in user_text or "يا كامل" in user_text:
                print("🟢 System Activated! | تم تفعيل النظام!")
                is_awake = True
                
                # Greeting message | رسالة الترحيب المطلوبة
                nova.speak("أهلاً بك. أنا كامل، الروبوت الذكي. كيف يمكنني مساعدتك؟")
            else:
                # Print heard text but ignore | يطبع ما سمعه ولكنه يتجاهله
                print(f"😴 (Ignored | تجاهل): {user_text}")

        # 3. Mode 2: Robot is awake (Interacting with Gemini) | الوضع الثاني: الروبوت مستيقظ (يعمل مع Gemini)
        else:
            # (Optional) Sleep command | (اختياري) أمر لإعادة الروبوت للنوم
            if "شكرا" in user_text or "توقف" in user_text or "نوم" in user_text:
                is_awake = False
                nova.speak("عفواً. سأكون في الانتظار.")
                print("--- 🌑 System returned to Standby | عاد النظام لوضع الاستعداد ---")
                continue

            # Send text to AI and get reply | إرسال النص للذكاء الاصطناعي والرد
            reply = nova.think(user_text)
            nova.speak(reply)

if __name__ == "__main__":
    main()


