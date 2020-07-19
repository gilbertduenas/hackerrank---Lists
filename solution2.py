# learn 2 f-strings and eval....
if __name__ == '__main__':
    answer = []
    N = int(input())

    for i in range(N):
        task = input().split()
        cmd = task[0]
        args = task[1:]

        if cmd !='print':
            eval(f'answer.{cmd}({",".join(args)})')
        else:
            print(answer)
