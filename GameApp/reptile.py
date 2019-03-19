from bs4 import BeautifulSoup
from urllib import request

def AddNews():
    url = r'https://www.thepaper.cn/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read()
    page_info = page_info.decode('utf-8')
    soup = BeautifulSoup(page_info, 'html.parser')

    links = soup.find_all('div','news_li',limit=12)
    return links


# 爬去天气信息

city = {"苏州":"101190401","涟水":"101190905","南京":"101190101",
        "上海":"101280601","北京":"101010100","深圳":"101280601"}

def GetWeather(cityName):
    cityNo = city[cityName]
    url = r'http://www.weather.com.cn/weather1d/%s.shtml' %cityNo
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read()
    page_info = page_info.decode('utf-8')
    soup = BeautifulSoup(page_info, 'html.parser')

    weather = soup.find_all('p', class_="wea")
    temperature = soup.find_all('p', class_="tem")
    wind = soup.find_all('p', class_="win")

    tday_temperature = temperature[0].find("span").string
    yday_temperature = temperature[1].find("span").string
    tday_weather = weather[0].string
    yday_weather = weather[1].string
    tday_wind_dir = wind[0].find("span")["title"]
    tday_wind_lev = wind[0].find("span").string
    wind_dir_lev = tday_wind_dir + " " + tday_wind_lev
    return [tday_temperature, yday_temperature, tday_weather, yday_weather,wind_dir_lev]


GetWeather("苏州")


def GetWeatherInfo():
    sz = GetWeather("苏州")
    sz.append('bgc_1')
    ls = GetWeather("涟水")
    ls.append('bgc_2')
    nj = GetWeather("南京")
    nj.append('bgc_3')
    sh = GetWeather("上海")
    sh.append('bgc_4')
    bj = GetWeather("北京")
    bj.append('bgc_5')
    szh = GetWeather("深圳")
    szh.append('bgc_6')
    weatherInfo = (
        {
            "苏州":sz,
            "涟水":ls,
            "南京":nj
        },
        {
            "上海":sh,
            "北京":bj,
            "深圳":szh
        }
                   )
    return weatherInfo


# for i in GetWeatherInfo():
#     for x in i.values():
#         print(x)
#         break

