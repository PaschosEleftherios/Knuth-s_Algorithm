# Eleftherios Pashos, A.M. 4151
import string
K = []
K_all = []  # all combinations, never remove from this list



# ============ INITIATION ============
def initiate_k():
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    K.append("%s%s%s%s" % (i, j, k, l))
                    K_all.append("%s%s%s%s" % (i, j, k, l))


# ============ PLAY ============
def check_the_guess(guess, secret_code):
    response = []
    guess_list = list(guess)
    secret_code_list = list(secret_code)

    i = 0
    while i<len(guess_list):
        if guess_list[i] == secret_code_list[i]:
            response.append('o')
            guess_list.pop(i)
            secret_code_list.pop(i)
        else:
            i += 1

    i = 0
    for i in range(len(guess_list)):
        if guess_list[i] in secret_code_list:
            response.append('x')
            secret_code_list.remove(guess_list[i])

    return ''.join(response)


def make_a_guess(guess, attempt):
    global K

    print("-----------------")
    print("Attempt %s: %s" % (attempt, guess))
    response = input("Please give your Feedback :")
    while True:
        answers = ['oooo', 'ooo', 'oo', 'oox', 'ooxx', 'o', 'ox', 'oxx', 'oxxx', '', 'x', 'xx', 'xxx', 'xxxx']
        if response in answers :
            break
        else:
            response= input("Please enter correct Feedback :")
    print('Feedback: %s' % response)
    if response == 'oooo':  # The guess was correct
        print("Ha! I found it in %s attempts!" % attempt)
    else:
        # Remove from K
        K.append("end")
        i = 0
        while K[i] != "end":
            k = K[i]
            if response != check_the_guess(guess, k):
                K.pop(i)
                i -= 1
            i += 1

    K.pop(-1)
    return response


def find_next_guess():
    global  K_all, K
    answers = ['oooo', 'ooo', 'oo', 'oox', 'ooxx', 'o', 'ox', 'oxx', 'oxxx', '', 'x', 'xx', 'xxx', 'xxxx']

    scores = []
    max_score = 0

    for x in K_all:
        removes = []
        for a in answers:
            response = a
            cur_removes = 0
            for k in K:
                if response != check_the_guess(x, k):
                    cur_removes += 1
            removes.append(cur_removes)
        score = min(removes)

        if score > max_score:
            max_score = score
        scores.append(score)

    if len(K) == 1:
        return K[0]

    for i in range(len(scores)):
        if scores[i] == max_score:
            if K_all[i] in K:
                return K_all[i]

    for i in range(len(scores)):
        if scores[i] == max_score:
            return K_all[i]


def play():
    attempt = 1
    next_guess = "1122"
    for i in range(6):
        response = make_a_guess(next_guess, attempt)
        if response == 'oooo':  # The guess was correct
            break
        next_guess = find_next_guess()
        attempt += 1


initiate_k()
play()
