import time
import covid_data as cd
import file_handler as fh

con = "2"
while con != "5":
    print('\nEnter the Option:')
    print('1.Insert')
    print('2.search')
    print('3.modify')
    print('4.delete')
    print('5.exit')

    option = int(input())

    if option == 1:
        date = input('enter the date in form of mm/dd/yyyy')
        country = input('enter the country')
        state = input('enter the state')
        fips = input('enter Postal code or Fips')

        for i in range(0, 2):

            if i == 1:
                print('enter the deaths info :')
                cases = input('enter the cases')
                diff = input('enter the difference')
                d1 = cd.covid_data('Deaths', cases, diff, date, country, state, fips)
                fh.filewrite_with_index(d1)

            if i == 0:
                print('enter the Confirmed info :')
                cases = input('enter the cases')
                diff = input('enter the difference')
                d2 = cd.covid_data('Confirmed', cases, diff, date, country, state, fips)
                fh.filewrite_with_index(d2)


    elif option == 2:
        print('2 selected')
        key = input('enter the key to search')
        print('searching')
        s_time = time.time()
        pos = fh.search_key(key)
        if pos != -1:
            print('found at '+pos)
            data = fh.read_file_at_pos(int(pos))
            fh.print_data(data)
        else:
            print('not found')
        e_time = time.time()
        print('time taken to process is ' + str(e_time - s_time))


    elif option == 3:
        key = input('enter the key to modify')
        print('searching')
        s_time = time.time()
        pos = fh.search_key(key)
        if pos != -1:
            print('found at ' + pos)
            data = fh.read_file_at_pos(int(pos))
            print(data)
            cases = input('enter the casses rate')
            difference = input('enter the difference rate')
            fh.write_modified(cases,difference,pos)
        else:
            print('not found')
        e_time = time.time()
        print('time taken to process is '+str(e_time-s_time))

    elif option == 4:
        key = input('enter the key to delete')
        print('searching')
        s_time = time.time()
        pos = fh.search_key(key)
        if pos != -1:
            print('found at ' + pos)
            data = fh.read_file_at_pos(int(pos))
            print(data)
            print('deleting...')
            fh.delete_data(pos,key)
        else:
            print('not found')
        e_time = time.time()
        print('time taken to process is ' + str(e_time - s_time))

    elif option == 5:
        exit(0)

    else:
        print('*****enter the correct option*****.\nTo continue enter any thing\nto exit enter 5\nOr restart program')
        con = input()