
import random


act_list = [

	'Bake something to give away',
	'Donate $5 to a charitable org',
	'Donate clothing',
	'Write a gratitude letter to a friend',
	'Pay for the person behind you in a drive-through',
	'Pick up 10 pieces of litter',
	'Leave a great review for a local business',
	'Donate blood',
	'Buy a meal for a homeless person',
	'Double the next tip you leave',
	'Don\'t complain about anything for 24 hours'
]

act = act_list[random.randrange(0,len(act_list))]

print(act)