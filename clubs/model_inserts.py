#from django.db import models
import requests
from lxml import html
#from clubs.models import Club


counties_page = requests.get('http://www.gaapitchlocator.net/')
counties_tree = html.fromstring(counties_page.content)
counties = counties_tree.xpath('//*[@id="map-ireland-counties"]/ul/li/a/text()')

#dublin_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/dublin/#0/-60/-121') #Works
#dublin_tree = html.fromstring(dublin_page.content)
#Dublin_clubs = dublin_tree.xpath('//a[@title="show marker on map"]/text()')
#Dublin_locations = dublin_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')

# counties[9] = Dublin

for index in range(len(counties)):
	print("<option name=\"County\" id= \"County\" value=\""+counties[index]+"\">"+counties[index]+"</option>")
#	p = Club(name=Dublin_clubs[index], location=Dublin_locations[index], county='Dublin', province='Leinster')
#	p.save()
	
# <option value="volvo">Antrim</option>

#"('10',Dublin_clubs[index],'N/A','N/A',Dublin_locations[index],'N/A')," +
#"('22','Moylagh','N/A','N/A','53.7339336,-7.1522973','N/A')," +
