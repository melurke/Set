import random
import matplotlib.pyplot as plt

results = []
test = [0, 0, 0, 0, 0, 0, 0, 0]
num_of_tries = 250
no_cards_left = False
test1 = True
found_set = False

def set(cards):
    test = [0, 0, 0, 0]

    for i in range(0, 4):
        for card in cards:
            test[i] += card[i]

    test = [test[0]%3, test[1]%3, test[2]%3, test[3]%3]

    if test == [0, 0, 0, 0]:
        return True
    return False

for ö in range(0, num_of_tries):
    if ö % 10 == 0:
        print(str((ö/num_of_tries)*100) + "%")
    
    counter = 0
    cool = True
    all_cards = []
    cards = []
    combinations = []
    num_of_cards = 12

    for i in range(0, 3):
        for n in range(0, 3):
            for m in range(0, 3):
                for k in range(0, 3):
                    all_cards.append((i, n, m, k))
    random.shuffle(all_cards)

    for i in range(0, 12):
            cards.append(all_cards[0])
            all_cards.remove(all_cards[0])

    while test1:
        num_of_cards = len(cards)
        found_set = False
        for o in range(0, num_of_cards):
            for i in range(0, num_of_cards):
                for u in range(0, num_of_cards):
                    if o != i and i != u and o != u:
                            combinations.append((o, i, u))

        for combination in combinations:
            pick = [cards[combination[0]], cards[combination[1]], cards[combination[2]]]
            
            if set(pick):
                for card in pick:
                    cards.remove(card)
                num_of_cards -= 3
                found_set = True
                counter += 1
                break
                
            if cards == []:
                no_cards_left == True
                break

        if not found_set and no_cards_left:
            test1 = False

        if not found_set:
            for i in range(0, 3 * counter):
                try:
                    cards.append(all_cards[i])
                    all_cards.remove(all_cards[0])
                    num_of_cards += 3
                except:
                    no_cards_left = True
                    pass

    results.append(len(cards))
    print(cards)

for result in results:
    test[int(result/3)] += 1

for i in range(0, len(test)-1):
    test[i] = test[i]/num_of_tries

print("")
print("")

for i in range(0, len(test)):
    print(str(3*i) + ": " + str(test[i]*100) + "%")

plt.bar([0, 3, 6, 9, 12, 15, 18, 21], test)
plt.show()
