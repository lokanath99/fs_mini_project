def filewrite_with_index(dataobject):
    source_file = open('./Files/covid_data_keys.txt','a+')
    index_file = open('./Files/index.txt','a+')
    pos = source_file.tell()
    key = dataobject.get_key()
    data = dataobject.get_data()
    source_file.write(data)
    index_file.write(str(pos)+"|"+key+"\n")
    source_file.close()
    index_file.close()

def search_key(key):
    key = key+"\n"
    index_file = open('./Files/index.txt', 'r+')
    line = index_file.readline()
    pos = -1
    while line :
        data = line.split("|")
        # if data[0][1] == "*":
        #     line = index_file.readline()
        if data[1] == key:
            pos = data[0]
            return  pos
        else:
            line = index_file.readline()
    index_file.close()
    return pos


def print_data(r_data):
    p_data = r_data.split("|")
    print('case_type :'+p_data[1]+"\n"+'Cases = '+p_data[2]+"\n"+'Difference = '+p_data[3]+"\n"+'Date = '+p_data[4]+"\n"+'Country_Region ='+ p_data[5]+"\n"+'Province_State = '+p_data[6]+"\n"+'FIPS ='+ p_data[7]+"\n")


def read_file_at_pos(pos):
    source_file = open('./Files/covid_data_keys.txt', 'r')
    source_file.seek(pos)
    data = source_file.readline()
    source_file.close()
    return data

def write_modified(cases, difference, pos):
    source_file = open('./Files/covid_data_keys.txt', 'r')
    posi= int(pos)
    source_file.seek(posi)
    line = source_file.readline()
    stripped_line = line.strip()
    data = line.split("|")
    # print(data)
    old_data = "|"+data[2]+"|"+data[3]
    new_data = "|"+cases+"|"+difference
    new_line = stripped_line.replace(old_data, new_data)
    new_file_content = ""
    new_file_content += new_line
    source_file.close()

    source_file = open('./Files/covid_data_keys.txt', 'r+')
    source_file.seek(posi)
    source_file.write(new_file_content)
    source_file.close()
    print('record modified')


def find_index_pos(key):
    index_file = open('./Files/index.txt', 'r+')
    pos = int(index_file.tell())
    keyf = key+"\n"
    line = index_file.readline()
    while line :
        data = line.split("|")
        # if data[0][1] == "*":
        #     pos = index_file.tell()
        #     line = index_file.readline()
        if data[1]==keyf:
            return int(pos)
        else:
            pos = index_file.tell()
            line = index_file.readline()
    return -1


def delete_data(pos ,key):
    source_file = open('./Files/covid_data_keys.txt', 'r')
    new_file_content = ''
    posi = int(pos)
    source_file.seek(posi)
    line = source_file.readline()
    # print(data)
    old_data = line
    new_data = "*"+line[1:]
    new_line = line.replace(old_data, new_data)
    new_file_content += new_line
    source_file.close()

    source_file = open('./Files/covid_data_keys.txt', 'r+')
    source_file.seek(posi)
    source_file.write(new_file_content)
    source_file.close()
    print('record modified in Files')

    #erasing index
    source_file = open('./Files/index.txt', 'r')
    new_file_content = ''
    posi = find_index_pos(key)
    source_file.seek(posi)
    line = source_file.readline()
    # print(data)
    old_data = line
    new_data = "*"+line[1:]
    new_line = line.replace(old_data, new_data)
    new_file_content += new_line
    source_file.close()

    source_file = open('./Files/index.txt', 'r+')
    source_file.seek(posi)
    source_file.write(new_file_content)
    source_file.close()
    print('record modified in index')