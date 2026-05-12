print("------------------------------------")
print("--- Community Pool Safety System ---")
print("------------------------------------")
temp = float(input("Enter the water temperature (in celsius): "))
chlevel = float(input("Enter the Chlorine level (on a scale of 1.0 to 10.0): "))
if temp > 25 and chlevel >= 3 and chlevel <=7:
    print("RESULT: SAFE. You may open the pool.")
else:
    print("RESULT: DANGER. The pool must remain closed.")
    if temp <= 25 and chlevel < 3 or chlevel > 7:
        print("REASON: Water is too cold and Chlorine levels are unbalanced.")
    elif temp <= 25:
        print("REASON: Water is too cold.") 
    else:
        print("REASON: Chlorine levels are unbalanced.")