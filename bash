# إنشاء مجلد المشروع
mkdir investment_system
cd investment_system

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # أو venv\Scripts\activate في Windows

# تثبيت الحزم الأساسية
pip install django djangorestframework django-cors-headers psycopg2-binary