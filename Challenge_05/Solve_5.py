def is_prime(num):
    if num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    
    return True

def checks_conditions(num):
    if not is_prime(num):
        return False
    
    else:
        str_num = str(num)

        digits = [int(x) for x in str_num]

        if not is_prime(sum(digits)):
            return False
        
    return True

if __name__ == '__main__':
    # Obtained from challenge 4

    safe_nodes = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 155, 156, 157, 158, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 195, 196]

    hides = []

    for _ in safe_nodes:
        if checks_conditions(_):
            hides.append(_)

    print(f'{len(hides)}-{hides[2]}')