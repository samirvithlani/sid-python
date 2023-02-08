try:
    greet = "morning"
    amount = 100
    print(greet+amount)
except TypeError:
    print("Invalid operation")    
else:
    print("Hello ",greet)
    print("Amount is ",amount)
finally:
    greet=""
    amount=0    
        