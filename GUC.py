import webbrowser
import threading
from dotenv import load_dotenv
import os
load_dotenv()


def open_url(url):
    chrome_browser = webbrowser.get(os.getenv('chrome_path'))
    chrome_browser.open_new_tab(url)


mail = 'https://mail.guc.edu.eg/owa/'
cms = 'https://cms.guc.edu.eg/apps/student/HomePageStn.aspx'
portal = 'https://apps.guc.edu.eg/student_ext/Console.aspx'

t1 = threading.Thread(target=open_url, args=(mail,))
t2 = threading.Thread(target=open_url, args=(cms,))
t3 = threading.Thread(target=open_url, args=(portal,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
