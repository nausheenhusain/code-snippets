import csv
"""
translates hate crimes from integer code to string, extracts columns for mapping
"""

#global dictionaries with key/values for biases and crimes
biases = {
	"11" : "Anti-White",
	"12" : "Anti-Black",
	"13" : "Anti-Native American",
	"14" : "Anti-Asian",
	"15" : "Anti-Multiple races",
	"16" : "Anti-Native Hawaiian/Pacific Islander",
	"31" : "Anti-Arab",
	"32" : "Anti-Latino",
	"33" : "Anti-Other ethnicity",
	"21" : "Anti-Jewish",
	"22" : "Anti-Catholic",
	"23" : "Anti-Protestant",
	"24" : "Anti-Muslim",
	"25" : "Anti-Other religion",
	"26" : "Anti-Multiple religions",
	"27" : "Anti-Atheist or agnostic",
	"28" : "Anti-Mormon",
	"29" : "Anti-Jehovah's Witness",
	"81" : "Anti-Eastern Orthodox",
	"82" : "Anti-Other Christian",
	"83" : "Anti-Buddhist",
	"84" : "Anti-Hindu",
	"85" : "Anti-Sikh",
	"41" : "Anti-Gay (Male)",
	"42" : "Anti-Lesbian",
	"43" : "Anti-Mixed group (non-straight)",
	"44" : "Anti-Heterosexual",
	"45" : "Anti-Bisexual",
	"51" : "Anti-Physical disability",
	"52" : "Anti-Mental disability",
	"61" : "Anti-Male",
	"62" : "Anti-Female",
	"71" : "Anti-Transgender",
	"72" : "Anti-Gender non-conforming"
}

crimes = {
	"1" : "Homicide",
	"2" : "Criminal sexual assault",
	"3" : "Armed robbery or robbery",
	"4" : "Agravated battery",
	"5" : "Burglary",
	"6" : "Theft",
	"7" : "Motor vehicle theft",
	"8" : "Arson",
	"9" : "Battery",
	"10" : "Disorderly conduct",
	"11" : "Criminal damage to property",
	"12" : "Assault",
	"13" : "Aggravated assault",
	"14" : "Criminal trespass",
	"15" : "Mob action",
	"16" : "Harassment"
}

def write_csv():
	"""
	Extracts and handles relevant columns
	"""

	with open('/Users/Desktop/data/hate-crimes/crimes-2017.csv', 'rU') as f:
		reader = csv.reader(f)
		# it1, it2 = itertools.tee(reader, 2)
		with open('/Users/Desktop/data/hate-crimes/crimes-2017-mapping.csv', 'w') as g:
			writer = csv.writer(g)

			header_row = ['RD', 'date', 'bias', 'loc-type', 'crime-code', 'description', 'location_lat', 'location_long', 'arrest']
			writer.writerow(header_row)

			for row in reader:

				# make ID for each row
				ID = row[16]
				print("Working on", ID)

				# replace bias from number to corresponding string
				if row[1] in biases:
					bias = biases.get(row[1], "none")
					print(bias)
				else:
					print("This bias code isn't in my dictionary:", row[1])
					continue

				# camel case location type
				location = row[6].lower()

				# replace crime code to corresponding string
				if row[8] in crimes:
					crime_type = crimes.get(row[8], "none")
				else:
					print("This crime code isn't in my dictionary:", row[8])
					continue

				print("Done with", ID)
				new_row = [ID, row[2], bias, location, crime_type, row[22], row[35], row[36], row[24]]
				writer.writerow(new_row)

write_csv()