
# This module sets up the guests playing and introduction speech by Abe

def setup():
	guests = {
		'cade' : '3372501081',
		'rachael' : '32452345',
		'alec' : '34234',
		'abbie' : '5434563',
		'ben' : '15666666',
		'steve' : '145236453',
		'reagan' : '8868686868',
	}

	introduction = "Goodevening guests!\
					I am your host's Automated Butler Executable Service, but you may call me Abe. I will be assisting you this evening whenever Mr. Beller is unavailable. He built me to oversee his estate and made me unable to deny guests in any capacity. Please make yourself comfortable as he should be along shortly. I will be monitoring your evening for the remainder of the night so that I may better serve you. There is no need to respond to me directly as I see Everything in this house. \
					Have a wonderful evening."

	return introduction, guests 

def setupTests():
	

	#for i in guests:
		#print("{}'s phone number is {}".format(i,guests[i]))

	return introduction, guests
 if __name__ == '__main__':
 	setupTests()