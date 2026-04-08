
from bot import NovaRobot
import time

def main():
    # تهيئة الروبوت
    nova = NovaRobot()
    
    # متغير حالة الاستيقاظ (في البداية يكون نائماً)
    is_awake = False
    
    print("\n--- 🌑 النظام يعمل في وضع الاستعداد ---")
    print("--- 🗣️ قل 'كامل' لتفعيل الروبوت ---")

    while True:
        # 1. الروبوت يستمع دائماً
        user_text = nova.listen()

        # إذا لم يسمع شيئاً أو حدث خطأ، أعد المحاولة
        if user_text is None:
            continue

        # 2. الوضع الأول: الروبوت نائم (ينتظر كلمة السر)
        if not is_awake:
            # التحقق من وجود كلمة "كامل" في الجملة
            if "كامل" in user_text or "يا كامل" in user_text:
                print("🟢 تم تفعيل النظام!")
                is_awake = True
                
                # رسالة الترحيب المطلوبة
                nova.speak("أهلاً بك. أنا كامل، الروبوت الذكي. كيف يمكنني مساعدتك؟")
            else:
                # يطبع ما سمعه ولكنه يتجاهله
                print(f"😴 (تجاهل): {user_text}")

        # 3. الوضع الثاني: الروبوت مستيقظ (يعمل مع Gemini)
        else:
            # (اختياري) أمر لإعادة الروبوت للنوم
            if "شكرا" in user_text or "توقف" in user_text or "نوم" in user_text:
                is_awake = False
                nova.speak("عفواً. سأكون في الانتظار.")
                print("--- 🌑 عاد النظام لوضع الاستعداد ---")
                continue

            # إرسال النص للذكاء الاصطناعي والرد
            reply = nova.think(user_text)
            nova.speak(reply)

if __name__ == "__main__":
    main()


