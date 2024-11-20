def count_steps(trace):
    steps = 0
    pos = 0
    if int(trace[pos]) < 0:
        return 1
    while pos < len(trace) and pos > -1:
        current = trace[pos]
        trace[pos] += 1
        pos += current
        steps += 1
    return steps


traces_list = [['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['1', '2', '3', '4', '-1'], ['0', '0', '1', '1', '1'], ['2', '-1', '0', '2', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['-1', '0', '1', '-2', '2'], ['1', '2', '4', '1', '-2'], ['0', '1', '2', '3', '-1'], ['0', '1', '1', '1'], ['0', '1', '0', '1'], ['3', '0', '-2', '1'], ['1', '1', '1', '1', '1', '1'], ['1', '0', '1', '0', '1', '0', '1', '0', '1', '4', '5', '6', '7', '8']]
int_traces_list =[[int(num) for num in x] for x in traces_list]
if __name__ == '__main__':
    total = 0
    last = 0
    for x in int_traces_list:
        plus = count_steps(x)
        total += plus
        if x == int_traces_list[-1]:
            last = plus

    print(f'{total}-{last}')

