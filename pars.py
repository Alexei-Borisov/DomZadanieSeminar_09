#запросы на импорт
#из bs4 импорт BeautifulSoup как bs
url = "https://cbr.ru"
ответ = запросы. get(url). СМС
soup = bs(ответ, 'html.parser')
rubl_dollar = суп. find('div', class_='col-md-2 col-xs-9 _right mono-num')
rubl_inf = суп. find('div', class_="main-indicator_value")
print(f'1 $ = {rubl_dollar. текст}')
print(f'Целевая инфляция = {rubl_inf. текст}')
