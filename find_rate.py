import speech_recognition as sr

r = sr.Recognizer()
# استبدل رقم 2 برقم جهازك إذا تغير
mic_index = 2 

print(f"🔍 جاري فحص المايكروفون رقم {mic_index}...")

# قائمة الترددات الشائعة
rates = [48000, 44100, 32000, 16000, 8000]

for rate in rates:
    try:
        with sr.Microphone(device_index=mic_index, sample_rate=rate) as source:
            print(f"✅ نجح الاتصال بتردد: {rate} Hz")
            print("   -> جاري تجربة السماع...")
            try:
                audio = r.listen(source, timeout=3)
                print(f"   🎉 ممتاز! هذا التردد يعمل.")
                print(f"   🔴 استخدم sample_rate={rate} في الكود الخاص بك.")
                break # وجدنا التردد، نخرج
            except:
                print("   ⚠️ اتصلنا ولكن لم نسمع صوتاً (Timeout).")
    except Exception as e:
        print(f"❌ فشل التردد {rate} Hz")

print("\n--- انتهى الفحص ---")
