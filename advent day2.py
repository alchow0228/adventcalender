popen = open("C:/users/cala/Documents/pwords.txt")
plist = popen.readlines()

correctpword = 0
def part1(pw):
    pwstring = pw.split(':')
    policy = pwstring[0]
    return policy
def part2(pw):
    pwstring = pw.split(':')
    pword = pwstring[1]
    return pword
def part3(po, pw, valid):
    postring = po.split(' ')
    numpo = postring[0]
    numpostring = numpo.split('-')
    pomin = int(numpostring[0])
    pomax = int(numpostring[1])
    polett = postring[1]
    corr = 0
    for i in pw:
        if i == polett:
            corr = corr + 1
    if corr >= pomin and corr <= pomax:
        valid = valid + 1
    return valid
def part4(po, pw, valid):
    postring = po.split(' ')
    numpo = postring[0]
    numpostring = numpo.split('-')
    po1 = int(numpostring[0])
    po2 = int(numpostring[1])
    polett = postring[1]
    corr = 0
    x=0
    for i in pw:
        x=x+1
        if i == polett and x == po1:
            print(polett, po1)
            if i == polett and x != po2:
                print(polett, po2)
                corr = corr + 1
            print(corr)
    if corr == 1:
        valid = valid + 1
    return valid
for i in plist:
    policy = part1(i)
    pword = part2(i)
    correctpword = part4(policy, pword, correctpword)
print(correctpword)
