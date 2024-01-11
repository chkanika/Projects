import pyinputplus as pyip 

totalcost = 0 
prices = {"wheat": 0.5, "white": 0.25, "sourdough": 0.75,
          "chicken": 0.5, "turkey": 0.45, "ham": 0.3, "tofu": 0.25,
          "cheddar": 0.15, "Swiss": 0.2, "mozzarella": 0.15,
          "mayo": 0.05, "mustard": 0.08, "lettuce": 0.03, "tomato": 0.01}

# To allow for different sandwiches in the order
while True:
    # Make an empty dictionary to store the order details - resets order in the event of a second
    order = {}
    print('What bread would you like?')
    order = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)
    print('What kind of protein would you like?')
    order = pyip.inputMenu(["Chicken", "Turkey", "Ham", "Tofu"], numbered=True)
    wantCheese = pyip.inputYesNo("Do you want cheese? ")
    if wantCheese == "yes":
        order["cheese"] = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered=True)
    wantdressing = pyip.inputYesNo("Do you want dressing? ")           
    # Could put a while loop to allow for multiple options here
    if wantdressing == "Yes":
        order["side"] = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered=True)
    ordernum = pyip.inputInt("How many of those would you like?", min=1)
        
    # Calculate cost of the order
    for choice in order: 
        if order[choice] in prices.keys():
            totalcost += prices[order[choice]]
   
    # Adjust if more than one
    totalcost *= ordernum
    anotherorder = pyip.inputYesNo("Is it all? ")
    if anotherorder == "yes":
        break
    
# THe string.format forces 2 decimal places (e.g. 13.10 rather than 13.1)
print("That will be $" + "{:.2f}".format(totalcost)+ "please!")