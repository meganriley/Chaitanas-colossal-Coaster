def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue

def find_my_friend(queue, friend_name):
    index = queue.index(friend_name)
    return index


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue



def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    count = queue.count(person_name)
    return count


def remove_the_last_person(queue):
    last_person = queue[-1]
    queue.remove(queue[-1])
    return last_person


def sorted_names(queue):
    queue.sort()
    return queue
