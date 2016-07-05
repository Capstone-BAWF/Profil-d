import sys

Tweet = ""
while Tweet == "" or len(Tweet) > 150:
	Tweet = raw_input("You should totally enter a tweet brah: ")
	print(Tweet)
	if len(Tweet) > 150:
		print("Sorry that's not a tweet!")

twitters = []

twitters.append(Tweet.split())

print(twitters)
print (len(Tweet))
print (-len(Tweet))

"""for index in twitters:
	print(index)"""

