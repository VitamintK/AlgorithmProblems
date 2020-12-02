for i in range(1,1234567890):
    if i%10000 == 0:
        print(i)
    for j in range(1,21):
        if i%j != 0:
            break
    else:
        print(i)
        break
