# Task: Code an bacon seller which sells bacon stacks for 75 cent's.
# It only accepts 50, 25, 10 & 5 cent coins

print("Amount needed: 75 cents")

amount_needed = 75
coin_added = 0

while True:
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 50 or insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_needed -= insert_coin
        coin_added += insert_coin
    
    if coin_added == 75:
        print(f"Have a good one! {coin_added - 75}")
        break
    elif coin_added >= 75:
        print(f"You get back: {coin_added - 75} cents, have a good Day!")
        break
    else:
        print(f"Amount needed: {amount_needed}")
 
