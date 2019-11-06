import random


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



array_people = ['Ann Kathrin', 'Ben', 'Charlotte', 'Dana', 'Emily', 'Erik', 'Henrike', 'Jannis', 'John', 'Jonas', 'Julius', 'Martin', 'Mieke', 'Niklas', 'Niko', 'Ole', 'Oliver', 'Robin', 'Sam', 'Thore', 'Tim Ole', 'Volker']
array_people_sorted = generateRandomSeating(array_people).randomize()