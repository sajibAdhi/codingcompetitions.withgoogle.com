test_cases = int(input())

for i in range(test_cases):
    card_number = int(input())
    cards = []
    doller_amount = 0
    for j in range(card_number):
        cards.append(input())
        if j != 0:
            if cards[j] < cards[j-1]:
                doller_amount += 1
                cards.sort()
    print("Case #{}: {}".format(i+1, doller_amount))
