
#topic 1: probability

# Probability of rolling a 4 on a fair die

favorable = 1
total_outcomes = 6
probability = favorable / total_outcomes

print("Probability of rolling a 4 on a fair die =", probability) 
print("-" * 50)

p_rain =0.3
p_traffic =0.2
p_both = p_rain*p_traffic
print("probability of rain =",p_rain)
print("probability of traffic =",p_traffic)
print("probability of both rain and taffic=",p_both)
print("-" * 50)


#Task 1

import random

# Number of simulations
n = 1000
count_sum_7 = 0

for _ in range(n):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / n

print("Experimental Probability of sum = 7:", experimental_probability)


#Task 2

import random

total_trials = 10000
success_count = 0

for i in range(total_trials):
    
    coin = random.randint(0, 1)
    
    dice = random.randint(1, 6)
    
    if coin == 1 and dice == 6:
        success_count += 1

probability = success_count / total_trials

print("Experimental Probability (Heads AND 6):", probability)


# TASK 3

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)

