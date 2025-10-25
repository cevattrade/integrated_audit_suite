# Integrated Audit Suite

یک اپلیکیشن اختصاصی برای ERPNext که مجموعه‌ای از ماژول‌های استانداردهای مدیریتی و حسابرسی را در قالب یک بسته فراهم می‌کند. این اپلیکیشن با نسخه‌های زیر سازگار است:

- Frappe Framework: v15.86.0 (version-15)
- ERPNext: v15.84.0 (version-15)
- Frappe HR: v16.0.0-dev (develop)
- Frappe LMS: v2.39.1 (develop)
- Payments: v0.0.1 (develop)
- Wiki: v2.0.0 (master)
- Frappe Builder: v1.18.0 (develop)
- Print Designer: v1.x.x-develop (develop)
- Frappe Drive: v0.3.0 (develop)
- Gameplan: v0.0.1 (develop)
- Telephony: v0.0.1 (develop)
- Helpdesk: v1.16.0 (develop)
- Raven: v2.6.4 (develop)
- Jalali Calendar: v0.0.1

## ماژول‌ها

- **ISO 9001** – ثبت بندهای استاندارد، وضعیت انطباق و شواهد پشتیبان.
- **ISO 34000** – ثبت ریسک‌ها و برنامه‌های کاهش ریسک مطابق استاندارد مدیریت ریسک.
- **ISO 13053** – مدیریت پروژه‌های بهبود فرآیند بر مبنای چرخه DMAIC.
- **EFQM** – خودارزیابی مدل تعالی سازمانی و ثبت نقاط قوت و حوزه‌های بهبود.
- **Accounting Audit** – چک‌لیست حسابرسی داخلی با پیگیری وضعیت و یافته‌ها.

## نصب

1. مخزن را در محیط Bench خود کلون کنید:
   ```bash
   bench get-app integrated_audit_suite https://example.com/integrated_audit_suite.git
   ```
2. اپلیکیشن را روی سایت موردنظر نصب کنید:
   ```bash
   bench --site your-site install-app integrated_audit_suite
   ```
3. نقش‌های مناسب (System Manager، Quality Manager، Risk Manager، Project Manager و Accounts Manager) را به کاربران موردنظر اختصاص دهید.

## توسعه

- تمام DocTypeها در مسیر `integrated_audit_suite/<module>/doctype` قرار دارند.
- برای اضافه کردن فیلد یا رول جدید می‌توانید فایل JSON مربوط به DocType را ویرایش کنید.
- برای تنظیمات Desk، فایل `integrated_audit_suite/config/desktop.py` را به‌روزرسانی کنید.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. جزئیات بیشتر در فایل `license.txt` قرار دارد.
