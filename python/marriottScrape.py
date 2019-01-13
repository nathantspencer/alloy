from bs4 import BeautifulSoup as bsoup
import mechanicalsoup as msoup


browser = msoup.StatefulBrowser(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:64.0) Gecko/20100101 Firefox/64.0")
browser.open("https://marriott.com/sign-in.mi")
login_page = browser.get_current_page()
form_handle = login_page.find("form", { "name": "signInForm" })

form = browser.select_form(form_handle)
form.set_input({ "userID": "nathantspencer@gmail.com", "password": "askMe!5038E" })
browser.submit_selected()

browser.launch_browser()
