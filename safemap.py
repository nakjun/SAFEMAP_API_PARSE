import urllib
import requests
import pandas as pd
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup


# 연동정보
api_key = "QVFI5DIP-QVFI-QVFI-QVFI-QVFI5DIPH5"
service = "WFS"
request = "GetFeature"
typename = "A2SM_CRMNLSTATS"
outputformat = "GML2"
base_url = "http://www.safemap.go.kr/sm/commonpoi.do"
option = "?apikey=%s&SERVICE=%s&REQUEST=%s&SRS=EPSG&TYPENAME=%s&OUTPUTFORMAT=%s"
url = base_url + option % (api_key, service, request, typename,outputformat)

resp = requests.get(url)
resp.encoding = 'utf-8'

# text 추출
text = resp.text

soup = BeautifulSoup(text, 'lxml')
stats = soup.findAll('safemap:a2sm_crmnlstats')

header = ['objt_id','polc_nm','polc_se','plcstn_nm','murder','brglr','rape','theft','violn','arson','nrctc','tmpt','gamble','tot','ctprvn_nm','sgg_kor_nm','ctprvn_cd','sgg_cd','x','y']
body = [header]

for stat in stats:    
    line = []
    line.append(stat.find('safemap:objt_id').text)
    line.append(stat.find('safemap:polc_nm').text)
    line.append(stat.find('safemap:polc_se').text)       
    line.append(stat.find('safemap:murder').text)
    line.append(stat.find('safemap:brglr').text)
    line.append(stat.find('safemap:rape').text)
    line.append(stat.find('safemap:theft').text)
    line.append(stat.find('safemap:violn').text)
    line.append(stat.find('safemap:arson').text)
    line.append(stat.find('safemap:nrctc').text)
    line.append(stat.find('safemap:tmpt').text)
    line.append(stat.find('safemap:gamble').text)
    line.append(stat.find('safemap:tot').text)
    line.append(stat.find('safemap:ctprvn_nm').text)
    line.append(stat.find('safemap:sgg_kor_nm').text)
    line.append(stat.find('safemap:ctprvn_cd').text)
    line.append(stat.find('safemap:sgg_cd').text)
    line.append(stat.find('safemap:x').text)
    line.append(stat.find('safemap:y').text)
    body.append(line)    

df = pd.DataFrame(body)
#df.to_csv("data.csv",header=True,index=True,encoding="utf-8")
df.to_excel("data.xlsx",sheet_name='sheet1')
