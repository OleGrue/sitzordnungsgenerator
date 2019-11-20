import random
import pdfkit
import re
from selenium import webdriver



class generateRandomSeating:
	def __init__(self, people):
		self.people = people
		self.number_of_seats = len(people)

	def randomize(self):
		result = []
		numbers = []

		for i in range(len(self.people)):
			numbers.append(i)
			result.append(str(i))

		for i_i in self.people:
			temp = random.randint(0, len(numbers)-1)
			position = numbers[temp]
			result[position] = i_i
			numbers.remove(position)
		
		print(result)
		return result


def post_to_whatsapp(message):
	driver = webdriver.Chrome('/home/ole/programm_files/chromedriver')
	driver.get('https://web.whatsapp.com/')

	name = '9a Sitzordnung'
	msg = message
	count = 1

	input('Enter anything after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_13mgZ')

	for i in range(count):
	    msg_box.send_keys(msg)
	    button = driver.find_element_by_class_name('_3M-N-')
	    button.click()


def generate_pdf(array_people):

	count = 1
	page = '<!DOCTYPE html> <html lang="de"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title>Titel</title> <style type="text/css"> .platz{ background-color:#797979; color:#ffff; text-align:center; } html{ font-size: 200%; } </style> </head> <body> <div> <table> <tr> <th id="11" class="platz">p11p</th> <th id="10"class="platz">p10p</th> <th id="9"class="platz">p9p</th> <th></th> <th id="8"class="platz">p8p</th> <th id="7"class="platz">p7p</th> <th id="6"class="platz">p6p</th> <td>|</td> </tr> <tr> <td id="12"class="platz">p12p</td> <td></td> <td></td> <td></td> <td></td> <td></td> <td id="5"class="platz">p5p</td> <td>|</td> </tr> <tr> <td id="13"class="platz">p13p</td> <td></td> <td></td> <td></td> <td id="22"class="platz"></td> <td id="23"class="platz">p22p</td> <td id="4"class="platz">p4p</td> <td>|</td> </tr> <tr> <td id="14"class="platz">p14p</td> <td id="21"class="platz">p21p</td> <td id="20"class="platz">p20p</td> <td></td> <td></td> <td></td> <td id="3"class="platz">p3p</td> <td>|</td> </tr> <tr> <td id="15"class="platz">p15p</td> <td></td> <td></td> <td></td> <td id="18"class="platz">p18p</td> <td id="19"class="platz">p19p</td> <td id="2"class="platz">p2p</td> <td>|</td> </tr> <tr> <td id="16"class="platz">p16p</td> <td></td> <td></td> <td></td> <td></td> <td></td> <td id="1"class="platz">p1p</td> <td>|</td> </tr> <tr> <td id="17"class="platz">p17p</td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td>|</td> </tr> <tr> <td>------</td> <td>------</td> <td>------</td> <td>------</td> <td>------</td> <td>------</td> <td>------</td> <td>|</td> </tr> </table> </div> </body> </html>'
	for i in array_people:
		print(i)
		print(count)
		page = re.sub('p'+str(count)+'p', i, page)
		count += 1

	print(array_people)

	pdfkit.from_string(page,'plan.pdf')




array_people = ['Ann Kathrin', 'Ben', 'Charlotte', 'Dana', 'Emily', 'Erik', 'Henrieke', 'Jannis', 'John', 'Jonas', 'Julius', 'Martin', 'Mieke', 'Niklas', 'Niko', 'Ole', 'Oliver', 'Robin', 'Sam', 'Thore', 'Tim Ole', 'Volker']
array_people_sorted = generateRandomSeating(array_people).randomize()

output_file = open("output.txt","w+")
output = ''

for i in range(len(array_people_sorted)):
	output_file.write(str(i+1)+': '+array_people_sorted[i]+'\n')
	output = output+str(i+1)+': '+array_people_sorted[i]+'\n'

#post_to_whatsapp(output)
generate_pdf(array_people_sorted)
