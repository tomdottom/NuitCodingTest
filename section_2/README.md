#### a) Print the complete contents of a file, given path in command line

Answer:

	cd task_a
	python task_a.py lorem.txt

####b) Check if the input is palindrome

Answer:

	cd task_b
	python task_b.py palindromes.txt
	
Tests:

	cd task_b
	nosetests

####c) Create an odd numbers generator

Answer:

	cd task_c
	python task_c.py

####d) Iterate over a list of words and use a dictionary to keep track of the frequency(count) of each word

example: 
    
    ["one" , "two", "one", "one"]  => {"one": 3, "two": 1}
    
Answer:

	cd task_d
	python task_d.py
    
####e Iterate over a list of items and match parent with sons items

example:

    [{id: 1, parent: 2}, {id: 2, parent: null}, {id: 3, parent: 2}, {id: 4, parent: 5}, {id: 5, parent: null}, ...]
    [{id: 1, parent: 2}, {id: 2, parent: null, sons: [1, 3]}, {id: 3, parent: 2}, {id: 4, parent: 5}, {id: 5, parent: null, sons: [4]}, ...]

solution:
	
	cd task_e
	python task_e.py induviduvals.txt

tests:

	cd task_e
	nosetests