def countWord(n):
	#n = "i am with am"
	new_word = n.split()
	word = {}

	for x in new_word:
		if x in word:
			continue
		else:
			word[x] = new_word.count(x)

	result = {}
	
	for i in word.items():
		if i[0].isdigit():
			result[int(i[0])] = i[i]

		else:
			result[i[0]] = i[1]

	return result

			
