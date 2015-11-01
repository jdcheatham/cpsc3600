"""dictionary parse
cpsc3600
JD Cheatham"""


def main():
    total = 0
    eight = 0
    seven = 0
    six = 0
    five = 0
    four = 0
    three = 0
    two = 0
    one = 0
    fout=open('word8','w')
    with open('words') as fin:
        for each in fin:
            total +=1
            if len(each.strip()) == 8:
                eight += 1
                fout.write(each+'\n')

            elif len(each.strip()) == 7:
                seven += 1
            elif len(each.strip()) == 6:
                six += 1
            elif len(each.strip()) == 5:
                five += 1
            elif len(each.strip()) == 4:
                four += 1
            elif len(each.strip()) == 3:
                three += 1
            elif len(each.strip()) == 2:
                two += 1
            elif len(each.strip()) == 1:
                one += 1

    fin.close()
    fout.close()
    print(total)
    print("one-", one)
    print("two -", two)
    print("three -", three)
    print("four-",four)
    print( "five-",five)
    print("six-", six)
    print("seven-", seven)
    print("eight or more-", eight)

if __name__ == "__main__":
    main()