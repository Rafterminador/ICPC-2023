string = input()
reverse = int(input())

#len_str = len(string)

first = string[:len(string)-reverse]
input = string[len(string)-reverse:]

rev = input[::-1]

print(rev+first)

#for i in range(reverse):
#    first = string[:len(string)-reverse]
#    string = string[len(string)-reverse:]
#    string = string + first
#
#print(string, reverse)