from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import requests
from bs4 import BeautifulSoup as bs4

import re

Form, Window = uic.loadUiType("main.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# urls for course
url_eth_rub = 'https://www.google.com/search?q=eth+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=eth+d+&aqs=chrome.1.69i57j0i10l3j0i10i395j69i60l2.5254j1j9&sourceid=chrome&ie=UTF-8'
url_bit_rub = 'https://www.google.com/search?sxsrf=ALeKk00gp0m_7ZHxbnPSkN8w8wvqcK8moA%3A1612088586887&ei=CoUWYOLWNaWQrgS28qywCQ&q=bitcoin+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=bitcoin+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjICCAAyBggAEAcQHjIGCAAQBRAeOgQIABBHOggIABAHEAUQHjoECAAQDToICAAQDRAFEB46CQgAEA0QRhCCAlCj9gFYzIcCYPGIAmgAcAN4AIABXYgB3wSSAQE4mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjig8X8-cXuAhUliIsKHTY5C5YQ4dUDCA0&uact=5'
url_eth_dol = 'https://www.google.com/search?q=eth+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&oq=eth+%D0%B2+ljkk&aqs=chrome.1.69i57j0i13j0i5i13i30l6.7255j1j7&sourceid=chrome&ie=UTF-8'
url_bit_dol = 'https://www.google.com/search?sxsrf=ALeKk02TfhQGoTrBGtizCqyBtk21QmaKSQ%3A1615631857428&ei=8ZVMYIveGZeEwPAPz-iXyAs&q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIcCELEDEBQyAggAMgIIADICCAAyAggAMgIIADIGCAAQBxAeMgIIADICCAAyAggAOgcIIxCwAxAnOgcIABBHELADULMTWOEfYPcgaAJwAngAgAFPiAH5BJIBATmYAQCgAQGqAQdnd3Mtd2l6yAEJwAEB&sclient=gws-wiz&ved=0ahUKEwjLmszXia3vAhUXAhAIHU_0BbkQ4dUDCA0&uact=5'


# get a course in google and return in string
def get_course(url):
    try:
        r = requests.get(url)
        soup = bs4(r.text, features="html.parser")
        course = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
    except:
        print('have problem with requests')
    course = course.split(' ')
    course = re.sub(r'\s', '', course[0])
    course = course.replace(course[-3], '.')
    return course


eth_rub = get_course(url_eth_rub)
eth_dollars = get_course(url_eth_dol)
bicoin_rub = get_course(url_bit_rub)
bicoin_dollars = get_course(url_bit_dol)

print(eth_rub)
print(eth_dollars)
print(bicoin_rub)
print(bicoin_dollars)


# set course from google in label
def set_eth_rub_course():
    form.eth_rub_course.setText(eth_rub)


def set_eth_dollars_course():
    form.eth_dollars_course.setText(eth_dollars)


def set_bicoin_rub_course():
    form.bicoin_rub_course.setText(bicoin_rub)


def set_bicoin_dollars_course():
    form.bicoin_dollars_course.setText(bicoin_dollars)


# calculate the rate with the desired value
def calc_eth_rub_value():
    course = float(eth_rub)
    value = form.eth_rub_value.value()
    result = float('{:.2f}'.format(course * value))
    form.eth_rub_course.setText(str(result))


def calc_eth_dollars_value():
    course = float(eth_dollars)
    value = form.eth_dol_value.value()
    result = float('{:.2f}'.format(course * value))
    form.eth_dollars_course.setText(str(result))


def calc_bicoin_rub_value():
    course = float(bicoin_rub)
    value = form.bitcoin_rub_value.value()
    result = float('{:.2f}'.format(course * value))
    form.bicoin_rub_course.setText(str(result))


def calc_bicoin_dollars_value():
    course = float(bicoin_dollars)
    value = form.bitcoin_dol_value.value()
    result = float('{:.2f}'.format(course * value))
    form.bicoin_dollars_course.setText(str(result))


# refresh rate and values, when button clicked
def on_click():
    form.eth_rub_course.setText(get_course(url_eth_rub))
    form.eth_dollars_course.setText(get_course(url_eth_dol))
    form.bicoin_rub_course.setText(get_course(url_bit_rub))
    form.bicoin_dollars_course.setText(get_course(url_bit_dol))
    form.eth_rub_value.setValue(1)
    form.eth_dol_value.setValue(1)
    form.bitcoin_rub_value.setValue(1)
    form.bitcoin_dol_value.setValue(1)


# set rate, when app start
set_eth_rub_course()
set_eth_dollars_course()
set_bicoin_rub_course()
set_bicoin_dollars_course()

form.refresh.clicked.connect(on_click)
form.eth_rub_value.valueChanged.connect(calc_eth_rub_value)
form.eth_dol_value.valueChanged.connect(calc_eth_dollars_value)
form.bitcoin_rub_value.valueChanged.connect(calc_bicoin_rub_value)
form.bitcoin_dol_value.valueChanged.connect(calc_bicoin_dollars_value)
app.exec()
