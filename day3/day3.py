import re
product = 0
with open('input2.txt','r') as file:
    for line in file.readlines():
        while re.search(r"mul\(\d{1,3},\d{1,3}\)",line):
            string = re.search(r"mul\(\d{1,3},\d{1,3}\)",line).group(0)
            first_num, second_num = re.search(r'(\d{1,3},\d{1,3})',string).group(0).split(',')
            product += int(first_num) * int(second_num)
            line = line.replace(string,"",1)
        print(product)
print(product)


# part two 
product = 0
with open('input2.txt','r') as file:
    do = True
    for line in file.readlines():
        while re.search(r"mul\(\d{1,3},\d{1,3}\)",line):
            dont_index_start, dont_index_end = re.search(r"don't()",line).pos, re.search(r"don't()",line).endpos
            do_index_start, do_index_end = re.search(r"do()",line).pos, re.search(r"do()",line).endpos

            # search for don't 
            mult_index_start , mult_index_end = re.search(r"mul\(\d{1,3},\d{1,3}\)",line).pos, re.search(r"mul\(\d{1,3},\d{1,3}\)",line).endpos
            string = re.search(r"mul\(\d{1,3},\d{1,3}\)",line).group(0)
            mult = {string:mult_index_start, "index":mult_index_start}
            dont = {re.search(r"don't()",line).group(0):dont_index_start,"index":dont_index_start}
            do_map = {re.search(r"do()",line).group(0):do_index_start,"index":do_index_start}
            maps = [mult,dont,do_map]
            maps = sorted(maps,key= lambda x : x['index'])
            for item in maps:
                print(item)
                if "do()" in item:
                    do = True
                if "don't()" in item:
                    do = False
                if do and string in item:
                    first_num, second_num = re.search(r'(\d{1,3},\d{1,3})',string).group(0).split(',')
                    product += int(first_num) * int(second_num)
                    line = line.replace(string,"",1).replace("don't()","",1).replace("do()","",1)
            if not do:
                line = line.replace(string,"",1)
print(product)