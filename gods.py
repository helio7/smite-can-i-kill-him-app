import xml.etree.ElementTree as ET
tree = ET.parse('gods.xml')
root = tree.getroot() #element

#print root[0][0].text
#print root[0][1].text
#print root[0][2].text
#print root[0][3].text
#print ""

for god in root.findall("god"):
	name = god.get("name")
	number_of_abilities = god.find("number_of_abilities").text
	diamond_states = god.find("diamond_states").text
	special_input = god.find("special_input").text
	print name
	print number_of_abilities
	print diamond_states
	print special_input
	print ""
