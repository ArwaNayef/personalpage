def create():
 	countries={
 		"palestine" : "jerusalem",
 		"jordan" : "amman",
 		"england" : "landon" 
 		}
	return countries



def print_output(capital, country):
	#print " Palestian's capital is " + capital["palestine"]
	print country + "'s capital is " + capital[country]
	

def main():
	coun=create()
	print_output(coun, "palestine")
	print coun
if __name__ == "__main__":
	main()
