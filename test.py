"""
このファイルに解答コードを書いてください
"""

"""
実行方法：
ubuntu:
cat input.txt | python3  ./test.py

"""

import sys


def main():

    input_list = []
    #input 
    for el in sys.stdin:
        input_list.append(el)

    num_str = {}
    for i in range(len(input_list) - 1):
        query = input_list[i].split(':')
        number = int(query[0])
        string = query[1].replace('\n', '')
        num_str[number] = string

    target_num = int(input_list[-1])

    keys = sorted(list(num_str.keys()))

    output = ""

    for key in keys:
        if target_num % key == 0:
            output += num_str[key]

    print(output)

if __name__ == "__main__":
    main()
