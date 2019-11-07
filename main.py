import random
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
	
	def structured_output():
		pass
	
	def feedback():
		pass


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



array_people = ['Ann Kathrin', 'Ben', 'Charlotte', 'Dana', 'Emily', 'Erik', 'Henrike', 'Jannis', 'John', 'Jonas', 'Julius', 'Martin', 'Mieke', 'Niklas', 'Niko', 'Ole', 'Oliver', 'Robin', 'Sam', 'Thore', 'Tim Ole', 'Volker']
array_people_sorted = generateRandomSeating(array_people).randomize()

output_file = open("output.txt","w+")
output = ''

for i in range(len(array_people_sorted)):
	output_file.write(str(i+1)+': '+array_people_sorted[i]+'\n')
	output = output+str(i+1)+': '+array_people_sorted[i]+'\n'

post_to_whatsapp(output)
