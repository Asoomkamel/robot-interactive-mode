from google import genai
import os

# تأكد من وضع مفتاحك هنا إذا لم يكن في متغيرات البيئة
API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyDKwmYqPfWaNPzsrVt2UmLdPSdNqFMFQ30"

def list_available_models():
    print(f"🔍 جاري الاتصال بجوجل لجلب الموديلات...\n")
    
    try:
        client = genai.Client(api_key=API_KEY)
        
        # تنسيق الجدول
        print(f"{'Model Name':<40} | {'Display Name'}")
        print("-" * 70)
        
        # جلب القائمة مباشرة بدون فلاتر معقدة
        for model in client.models.list():
            # في النسخة الجديدة، الاسم يكون عادة بصيغة "models/gemini-..."
            name = model.name
            display_name = model.display_name if hasattr(model, 'display_name') else "N/A"
            
            # تنظيف الاسم للعرض
            clean_name = name.replace("models/", "")
            
            print(f"{clean_name:<40} | {display_name}")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    list_available_models()
