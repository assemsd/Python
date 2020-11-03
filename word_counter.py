def word_counter(filepath):
	with open(filepath, "r") as file:
		f = file.read()
		f_list = f.split()
		return len(f_list)

filepath = "words1.txt"
print(word_counter(filepath))
