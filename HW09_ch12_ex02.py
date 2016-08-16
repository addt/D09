#def build_anagrams():
    #list_words = []
    #ana_dict = dict()
    #ana_dict[('a','a')] = "aa" 
    #fin = open('words.txt')
    #lines = fin.readlines()
    #for i in lines:
        #for j in ana_dict.keys():
            #if len(tuple(i.split()[0])) == len(j):
                #for z in tuple(i):
                    #if z in j:
                        #continue
                    #else:
                        #ana_dict[tuple(i.split()[0])] = ana_dict.get(tuple(i.split()[0]),[]) + [i.split()[0]]
                        #break
                #else:
                    #ana_dict[j] = ana_dict.get(j,[]) + [i.split()[0]]
                    #break
                #break
            #else:
                #ana_dict[tuple(i.split()[0])] = ana_dict.get(tuple(i.split()[0]),[]) + [i.split()[0]]
                #break
    #fin.close()
    #print(ana_dict)

#DO NOT RUN THE PROGRAM ON THE ENTIRE WORD.txt

def build_anagrams():
    list_words = []
    ana_dict = dict()
    ana_dict[('a','z')] = "aa" 
    fin = open('words.txt')
    lines = fin.readlines()
    for i in lines:
        for j in ana_dict.keys():
            if sorted(tuple(i.split()[0])) == sorted(j):
                print(i)
                ana_dict[j] = ana_dict.get(j,[]) + [i.split()[0]]
                break
        else:
            ana_dict[tuple(i.split()[0])] = ana_dict.get(tuple(i.split()[0]),[]) + [i.split()[0]] 
    #fin.close()
    #f = open("ana.txt", 'w')
    #f.write(str(ana_dict))
    #f.close()
    print(ana_dict)


def compare_words(s,n):
    pass


def main():
    build_anagrams()

if __name__ == '__main__':
    main()
