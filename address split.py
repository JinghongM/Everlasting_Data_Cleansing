import pandas as pd
import googlemaps
import time
key= 'AIzaSyC5fiUp5J66tv_LmaAfk0Bu7v2qLW_5608'
gmaps = googlemaps.Client(key=key)
xls = pd.ExcelFile('Master Boutique List  .xlsx')
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
for name in xls.sheet_names:
	print(name)
	tbl = pd.read_excel(xls,name)
	tbl.insert(3,'street',None)
	tbl.insert(4,'city',None)
	tbl.insert(5,'state',None)
	tbl.insert(6,'zipcode',None)
	tbl.insert(7,'latitude',None)
	tbl.insert(8,'longitude',None)
	tbl.insert(9,'ID',None)

	if "Address" not in list(tbl.columns.values):
		print("False")
	else:
		for row in range(tbl["Address"].shape[0]):
			print(row)
			address = tbl["Address"][row]
			print(address)
			if address=="" or type(address) == float:
				continue
			else:
				geocode_result = gmaps.geocode(address)
				time.sleep(3)
				if len(geocode_result) == 0:
					continue
				else:
					for element in geocode_result[0]['address_components']:
						if element['types'] == ['street_number']:
							streetNumber = element['long_name']
						if element['types'] == ['route']:
							street = element['long_name']
						if element['types'] == ['locality','political']:
							city = element['long_name']
						if element['types'] == ['administrative_area_level_1', 'political']:
							state = element['long_name']
						if element['types'] == ['postal_code']:
							zipcode = element['long_name']
					tbl.iat[row,3] = streetNumber + street
					tbl.iat[row,4] = city
					tbl.iat[row,5] = state
					tbl.iat[row,6] = zipcode
					latitude = geocode_result[0]['geometry']['location']['lat']
					longitude = geocode_result[0]['geometry']['location']['lng']
					tbl.iat[row,7] = latitude
					tbl.iat[row,8] = longitude
					ID = geocode_result[0]['place_id']
					tbl.iat[row,9] = ID
				
	tbl.to_excel(writer,sheet_name=name)          
