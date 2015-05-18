from lxml import etree
from django.core.files import File
from os.path import join
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

def generate_squadxml(members):
	# tworzy squad/root
	squad = etree.Element('squad', nick="ITS")


	#dane squadu
	squadname = etree.SubElement(squad, 'name')
	squadname.text = 'Intactilis'
	email = etree.SubElement(squad, 'email')
	email.text = 'admin@intactilis.pl'
	web = etree.SubElement(squad, 'web')
	web.text = 'http://intactilis.pl'
	picture = etree.SubElement(squad, 'picture')
	picture.text = 'logo.paa'
	title = etree.SubElement(squad, 'title')
	title.text = 'Intactilis'

	#petla dodajaca userow
	for player in members:
		try:
			member = etree.SubElement(squad, 'member', id = player.userprofile.player_id, nick=player.userprofile.nick)
		except ObjectDoesNotExist:
			member = etree.SubElement(squad, 'member', id = '', nick=player.username)
		name = etree.SubElement(member, 'name')
		name.text= 'N/A'
		email = etree.SubElement(member, 'email')
		email.text= 'N/A'
		icq = etree.SubElement(member, 'icq')
		icq.text= 'N/A'
		remark = etree.SubElement(member, 'remark')
		remark.text= 'N/A'

	#tworzenie 'drzewa' 
	tree = etree.ElementTree(squad)
	#print(etree.tostring(tree, pretty_print=True, xml_declaration=True, doctype='<!DOCTYPE squad SYSTEM "squad.dtd">', encoding='utf-8'))

	#zapis do pliku razem z okresleniem doctype
	filename = join(settings.MEDIA_ROOT, 'squadxml', 'squad.xml')
	#filename = join(settings.BASE_DIR, 'templates', 'squad.xml')
	#os.path.join(BASE_DIR, 'media')
	with open(filename, 'wb') as f:
		myfile=File(f)
		# myfile.write('xml')
		myfile.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, doctype='<!DOCTYPE squad SYSTEM "squad.dtd">', encoding='utf-8'))
		myfile.close()
		#f.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, doctype='<!DOCTYPE squad SYSTEM "squad.dtd">', encoding='utf-8'))
	

