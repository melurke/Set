import random
import matplotlib.pyplot as plt

results = []
test = [0, 0, 0, 0, 0, 0, 0, 0]
num_of_tries = 100000

def set(cards):
    test = [0, 0, 0, 0]

    for i in range(4):
        for card in cards:
            test[i] += card[i]

    test = [test[0]%3, test[1]%3, test[2]%3, test[3]%3]

    if test == [0, 0, 0, 0]:
        return True
    return False

for ö in range(0, num_of_tries):
    if ö % (num_of_tries / 100) == 0:
        print(str(int((ö/num_of_tries)*100)) + "%")
    
    all_cards = []
    cards = []
    test1 = True
    no_cards_left = False

    for i in range(0, 3):
        for n in range(0, 3):
            for m in range(0, 3):
                for k in range(0, 3):
                    all_cards.append((i, n, m, k))
                    
    random.shuffle(all_cards)

    for i in range(12):
            cards.append(all_cards[-1])
            all_cards.pop()

    while test1:
        found_set = False
        counter = 0
        combinations = []

        for o in range(0, len(cards)):
            for i in range(0, len(cards)):
                for u in range(0, len(cards)):
                    if o != i and i != u and o != u:
                            combinations.append((o, i, u))

        for combination in combinations:
            pick = [cards[combination[0]], cards[combination[1]], cards[combination[2]]]
         
            if set(pick):
                for card in pick:
                    cards.remove(card)
                found_set = True
                counter += 1
                break
                
            if cards == []:
                no_cards_left == True
                break

        if not found_set and not no_cards_left:
            test1 = False
        elif not found_set:
            for i in range(3 * counter):
                try:
                    cards.append(all_cards[-1])
                    all_cards.pop()
                except:
                    no_cards_left = True
                    pass

    results.append(len(cards))

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
