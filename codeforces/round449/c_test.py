n = 10
def make_string(n):
    if n == 0:
        return 'What are you doing at the end of the world? Are you busy? Will you save us?'
    m = make_string(n-1)
    return 'What are you doing while sending "' + m + '"? Are you busy? Will you send "' + m + '"?'
print(make_string(2))
