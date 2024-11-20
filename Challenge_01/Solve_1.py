def unlock(initial_d, moves):
    digits = [int(x) for x in initial_d]

    pos = 0
    for i in moves:
        if i == 'U':
            if digits[pos] != 9:
                digits[pos] += 1
            else:
                digits[pos] = 0
        if i == 'D':
            if digits[pos] != 0:
                digits[pos] -= 1
            else:
                digits[pos] = 9
        if i == 'R':
            if pos == len(digits)-1:
                pos = 0
            else:
                pos += 1

            digits[pos] = digits[pos]
        if i == 'L':
            pos -= 1

            digits[pos] = digits[pos]

    final_digits = [str(y) for y in digits]
    password = ''.join(final_digits)
    return password

if __name__ == '__main__':
    print(unlock('528934712834', 'URDURUDRUDLLLLUUDDUDUDUDLLRRRR'))

    