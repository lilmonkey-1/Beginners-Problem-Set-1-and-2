#mad-libs

print("welcome to Doreens mad-libs!")

name = input("what is your name?")
dessert = input("what is the most disgusting substance you can think of?")
pet = input("what is the coolest animal")
setting = input("what is the worst place in the world?")


print(name+" smothered a "+pet+" in "+dessert+" at "+setting+" because they turned evil after their love rejected them.")

#minutes to seconds


minutes=int(input("How many seconds are in ____ minutes? I'll tell you."))


seconds=(str(minutes*60))


print(seconds+" minutes")

#Jane always gets at least twice as many birthday cards as her older sister Cruella. Write a program that tells you how many cards Jane gets as a minimum. Input will be a positive integer representing how many cards Cruella received for her last birthday.


cruellasCards=int(input("psst I'll tell you how many cards at minumum this year. Just tell me how many poor Cruella got. She was mauled by a rat as a baby."))


janesCards=str(cruellasCards*2)


print("Oh, that means that Jane got more than "+janesCards+" cards! Cruella looks really sad.")

"""
Age to Days
Let the user take their age (in years) and convert this to the equivalent number of days. Note: Use 365 days as the length for a year
Ignore leap years and days between last birthday and now. (So they just turned the age they inputted)
"""


years=int(input("Mysterious Man: Hi. I know how many days old you are. Seconds even. ENTER YOUR AGE:"))


days=(years*365)
seconds=(days*86400)
daysLeft=str(36500-days)
secondsLeft=str(3153600000-seconds)
yearsLived=str(years)
daysLived=str(days)
secondsLived=str(seconds)


print("Hmm..... interesting. I can feel that you're "+yearsLived+". You'll die the second you are a century old. You have "+secondsLeft+" seconds till then. Thats "+daysLeft+" days. You look like you've had a hard "+daysLived+" days on earth and I'm sorry to say life's not going to get any better for you.")
print("POOF, HE DISAPPEARS IN A CLOUD OF SMOKE.")
