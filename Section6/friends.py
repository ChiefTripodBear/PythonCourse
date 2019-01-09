# ask the user for a list of 3 friends
# for each friend, we'll tell the user whether they are nearby
# for each nearby friend, we'll save their name to 'nearby_friends.txt'
# hint: readlines()

users_friends_input = input('please type the names of 3 friends, separated with a comma')
users_friends = [line.strip() for line in users_friends_input.split(',')]

people = open('Section6/data/people.txt', 'r')
nearby_friends = [line.strip() for line in people.readlines()]
people.close()


users_friends_set = set(users_friends)
nearby_friends_set = set(nearby_friends)
friends_nearby = users_friends_set.intersection(nearby_friends_set)

nearby_friends_file = open('Section6/data/nearby_friends.txt', 'w')
for friend in friends_nearby:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

