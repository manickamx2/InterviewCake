import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list): # make new random list be the front of the input list to shuffle in place.

    # if the length of the list is 1 or 0, just return the list
    if len(the_list) <= 1:
        return the_list

    # loop through the list
    # choose a random element in the list and swap that with another element
    # that is after the list
    for i in range(0, len(the_list) - 1):
        random_index = get_random(i, len(the_list) - 1)
        if (random_index != i):
            the_list[random_index], the_list[i] = the_list[i], the_list[random_index]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
