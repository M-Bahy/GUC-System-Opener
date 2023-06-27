import webbrowser
import threading

def open_url(url):
    chrome_browser = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
    chrome_browser.open_new_tab(url)


mail = 'https://mail.guc.edu.eg/owa/'
cms = 'https://cms.guc.edu.eg/apps/student/HomePageStn.aspx'
portal = 'https://apps.guc.edu.eg/student_ext/Console.aspx'

# create three threads, each of which opens a different URL in a new tab
t1 = threading.Thread(target=open_url, args=(mail,))
t2 = threading.Thread(target=open_url, args=(cms,))
t3 = threading.Thread(target=open_url, args=(portal,))

# start the threads
t1.start()
t2.start()
t3.start()

# wait for the threads to finish
t1.join()
t2.join()
t3.join()

