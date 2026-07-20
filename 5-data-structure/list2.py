# cars = ["Suzuki" , "Nissan" , "Toyota" , "BMW"]

# print(cars)

# popedCar = cars.pop()
# print(popedCar)
# print(cars)

## Try It Yourself - Python Crash Course Book
#? The following exercises are a bit more complex than those in Chapter 2, but
#? they give you an opportunity to use lists in all of the ways described.
#? 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#? would you invite? Make a list that includes at least three people you’d like to
#? invite to dinner. Then use your list to print a message to each person, inviting
#? them to dinner.

heshamGuests = ["Roqaya", "Abdallah" , "Fatma"]
print(f"hesham guests are : {heshamGuests}")
#of course we could use loop but not for now

# print(f"Hello and Welcome to my dinner, {heshamGuests[0]}")
# print(f"Hello and Welcome to my dinner, {heshamGuests[1]}")
# print(f"Hello and Welcome to my dinner, {heshamGuests[2]}")

#? 3-5. Changing Guest List: You just heard that one of your guests can’t make the
#? dinner, so you need to send out a new set of invitations. You’ll have to think of
#? someone else to invite.
#? •	 Start with your program from Exercise 3-4. Add a print statement at the
#? end of your program stating the name of the guest who can’t make it.
#? •	 Modify your list, replacing the name of the guest who can’t make it with
#? the name of the new person you are inviting.
#? •	 Print a second set of invitation messages, one for each person who is still
#? in your list

print(f"Abdallah can't make it at time , so he apologized")
heshamGuests.remove("Abdallah")
heshamGuests.append("Khaled")
print(f"The new guest list as follow: {heshamGuests}")