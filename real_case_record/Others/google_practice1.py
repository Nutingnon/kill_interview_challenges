#问题描述请见
# https://code.google.com/codejam/contest/3214486/dashboard
def split_the_string(input_string):
  m = input_string[0]
  outcome_list = input_string[2:].split()
  return (m,outcome_list)


def find_next_string(string):
    led = {'1111110': 0, '0110000': 1, '1101101': 2, '1111001': 3, '0110011': 4, '1011011': 5, '1011111': 6,
           '1110000': 7, '1111111': 8, '1111011': 9}
    led_reverse = dict(zip([l[1] for l in led.items()], [x[0] for x in led.items()]))
    if led[string] == 0:
        return '1111011'
    else:
        return led_reverse[led[string] - 1]

def judge_light(string_list):
    gd = [0,0,0,0,0,0,0]
    for i in string_list:
        for k in range(len(i)):
            if i[k] == '1':
                gd[k] = 1
    return gd

def final(input_string):
    led = {'1111110': 0, '0110000': 1, '1101101': 2, '1111001': 3, '0110011': 4, '1011011': 5, '1011111': 6,
           '1110000': 7, '1111111': 8, '1111011': 9}
    led_reverse = dict(zip([l[1] for l in led.items()],[x[0] for x in led.items()]))
    #print('led_reverse:',led_reverse)

    k = split_the_string(input_string)
    list_string = k[1]
    number_of_string = int(k[0])
    judge_light_outcome = judge_light(list_string)
    #print('judge_light_outcome:',judge_light_outcome)
    if judge_light_outcome == [0,0,0,0,0,0,0]:
        return 'ERROR!'
    if judge_light_outcome == [1,1,1,1,1,1,1]:
        if led[list_string[-1]] == 0:
            return '1111011'
        else:
            return led_reverse[led[list_string[-1]]-1]

    matched_list = list(led.keys())
    for i in list_string:
        temporary_list = matched_list
        record0 = []
        record1 = []
        for kk in range(len(i)):
            if judge_light_outcome[kk] == 1:
                if i[kk] == '0':
                    record0.append(kk)
                elif i[kk] == '1':
                    record1.append(kk)

        delete_records = []

        for index,l in enumerate(temporary_list):
            for j in record0:
                if l[j] != '0':
                    delete_records.append(l)
            for qq in record1:
                if l[qq] != '1':
                    delete_records.append(l)
        delete_records = list(set(delete_records))
        for k in delete_records:
            temporary_list.remove(k)

        matched_list = [find_next_string(xx) for xx in temporary_list]

        # print('temporary list:',temporary_list)
        # print('which means, the possible number is:',[led[qkk] for qkk in temporary_list])
        #
        # print('next matched_list:',matched_list)
        # print('which means, the possbile next value are:',[led[qkq] for qkq in matched_list])

    if len(matched_list) == 1:
        match=matched_list[0]
        # print('match',led[match])
        outcome = []
        for i in range(7):
            if judge_light_outcome[i] == 0:
                outcome.append('0')
            else:
                if match[i] == '0':
                    outcome.append('0')
                else:
                    outcome.append('1')
        outcome = ''.join(outcome)
        return outcome
    if len(matched_list) > 1:
        return 'ERROR!'



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  outcome_final=final(input()) # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, outcome_final))
#   # check out .format's specification for more formatting options