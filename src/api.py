import mechanicalsoup


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://github.com")
browser.follow_link("login")
browser.select_form('#login form')
browser["login"] = "justinphan3110"
browser["password"] = "Longphan31"
reso = browser.submit_selected()

page = browser.get_current_page()
messages = page.find("h2", class_="shelf-title")
if messages:
    print(messages.text)
assert page.select(".logout-form")
print(page.title.text)