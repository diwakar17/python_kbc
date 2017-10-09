question_list = ["what is the capital of India","who is the prime minister of India","who is the president of India","who is the home minister of India","who is the chief minister of New Delhi","what is the capital of MP","who is the president USA","which continent do the red color present on the olympics logo rpresents","who is the founder of facebook","what is the capital of germany"]
first_option = ["bhopal","raj nath singh","ramnath kobind","jitan manhi","manish shisodia","maharastra","Jorj bush","America","charles babges","Islamabad"]
second_option = ["New Delhi","Nrender modi","APJ Abdul Kalam","Nitish Kumar","sheela dixit","New Delhi","Donald trump","africa","bill gates","columbo"]
third_option = ["marastra","Arun Jetli","Pranab mukherji","Raj nath singh","Arbind Kejriwal","bhopal","Brak Obama","america continent","mark jukelberg","sydney"]
forth_option = ["gandhi nagar","pratibha patil","Manmohan singh","Susma swaraj","Rahul Gandhi","tiruvanant puram","hillary clinton","Europe","James clerk Maxwel","Berlin"]
prize = [10000, 30000, 50000, 100000, 500000, 1000000, 2500000, 5000000, 7500000, 10000000]
answer_key = int()
ans_store = []
ans_key = [2, 2, 1, 3, 3, 3, 2, 3, 3, 4]
for index in range(10):
	print "aap ka sawal hai"
	print "Q-" + question_list[index]
        print "1-" + first_option[index]
	print "2-" + second_option[index]
	print "3-" + third_option[index]
	print "4-" + forth_option[index]
	print ""
        user = int(raw_input("apna answer dalo\n"))
	ans_store.append(user)
	if user  == ans_key[index]:
                answer_key = answer_key + 1
		print "Congratulation!"
		print "you won ",prize[index], " rupees"
	if prize[index] == 100000:
		print "Congrats! appka pehla padav pura hua"
	if prize[index] == 5000000:
		print "congrats! aapka dusra padav pura hua"
	if prize[index] == 10000000:
		print "Congrats! you won 1 crore"
	if user != ans_key[index]:
		print "app KBC har chuke hai aur aapne jeeta hai ",prize[index]
                break
		
	
