def ones_digit_to_word(digit):
    return ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][digit]
def tens_digit_to_word(digit):
    return 'null null twenty thirty forty fifty sixty seventy eighty ninety'.split()[digit]
def teens_to_word(digit):
    return 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()[digit]
def num_to_words(n):
    ans = ''
    if n == 1000:
        return 'onethousand'
    if n >= 100:
        ans += ones_digit_to_word(n//100)
        ans += 'hundred'
        if n%100 > 0:
            ans += 'and'
    if n%100 < 10:
        ans += ones_digit_to_word(n%10)
    elif n%100 < 20:
        ans += teens_to_word(n%10)
    else:
        ans += tens_digit_to_word((n%100)//10)
        ans += ones_digit_to_word(n%10)
    return ans

ans = 0
for i in range(1,1001):
    print(num_to_words(i))
    ans += len(num_to_words(i))
print(ans)