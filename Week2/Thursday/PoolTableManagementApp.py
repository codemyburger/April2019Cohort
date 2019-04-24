import datetime


now = datetime.datetime.now()
"""print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)"""

dateOfRecord = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y')

filename = (str(dateOfRecord) + '.txt')
print(filename)


class PoolTable(object):
    def __init__(self, num):
        self.num = num
        self.available = "not occupied"

    def open_table(self):
        now = datetime.datetime.now()
        self.available = "occupied"
        self.hour_start = now.hour
        self.minute_start = now.minute

    def check_table(self):
        now = datetime.datetime.now()
        self.hour_current = now.hour
        self.minute_current = now.minute
        self.delta_minute_current = self.minute_current - self.minute_start
        self.delta_hour_current = self.hour_current - self.hour_start
        self.check_minute = self.delta_hour_current*60 + self.delta_minute_current

    def close_table(self):
        now = datetime.datetime.now()
        self.hour_end = now.hour
        self.minute_end = now.minute
        self.delta_hour = self.hour_end - self.hour_start
        self.delta_minute = self.minute_end - self.minute_start
        self.elapsed_minute = self.delta_hour*60 + self.delta_minute
        self.dollar_cost = self.elapsed_minute*.5
        self.available = "not occupied"
        with open(filename, 'a') as file_object:
            file_object.write("Pool Table " + str(self.num) + "\n")
            file_object.write("  start time " + str(self.hour_start) + ":" + str(self.minute_start).zfill(2) + "\n")
            file_object.write("  end time " + str(self.hour_end) + ":" + str(self.minute_end).zfill(2)+ "\n")
            file_object.write("  duration " + str(self.elapsed_minute) + " minutes\n")
            file_object.write("  cost is $" + str(self.dollar_cost) + "\n")

pool_table_01 = PoolTable(1)
pool_table_02 = PoolTable(2)
pool_table_03 = PoolTable(3)
pool_table_04 = PoolTable(4)
pool_table_05 = PoolTable(5)
pool_table_06 = PoolTable(6)
pool_table_07 = PoolTable(7)
pool_table_08 = PoolTable(8)
pool_table_09 = PoolTable(9)
pool_table_10 = PoolTable(10)
pool_table_11 = PoolTable(11)
pool_table_12 = PoolTable(12)

while True:
    cmd = raw_input("Enter table number (1 - 12), 's' for status, or 'q' to quit: ")
    if cmd == 's':
        print("Table 1: " + pool_table_01.available)
        if pool_table_01.available == "occupied":
            pool_table_01.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_01.hour_start, str(pool_table_01.minute_start).zfill(2), pool_table_01.check_minute))

        print("Table 2: " + pool_table_02.available)
        if pool_table_02.available == "occupied":
            pool_table_02.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_02.hour_start, str(pool_table_02.minute_start).zfill(2), pool_table_02.check_minute))

        print("Table 3: " + pool_table_03.available)
        if pool_table_03.available == "occupied":
            pool_table_03.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_03.hour_start, str(pool_table_03.minute_start).zfill(2), pool_table_03.check_minute))

        print("Table 4: " + pool_table_04.available)
        if pool_table_04.available == "occupied":
            pool_table_04.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_04.hour_start, str(pool_table_04.minute_start).zfill(2), pool_table_04.check_minute))

        print("Table 5: " + pool_table_05.available)
        if pool_table_05.available == "occupied":
            pool_table_05.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_05.hour_start, str(pool_table_05.minute_start).zfill(2), pool_table_05.check_minute))

        print("Table 6: " + pool_table_06.available)
        if pool_table_06.available == "occupied":
            pool_table_06.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_06.hour_start, str(pool_table_06.minute_start).zfill(2), pool_table_06.check_minute))

        print("Table 7: " + pool_table_07.available)
        if pool_table_07.available == "occupied":
            pool_table_07.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_07.hour_start, str(pool_table_07.minute_start).zfill(2), pool_table_07.check_minute))

        print("Table 8: " + pool_table_08.available)
        if pool_table_08.available == "occupied":
            pool_table_08.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_08.hour_start, str(pool_table_08.minute_start).zfill(2), pool_table_08.check_minute))

        print("Table 9: " + pool_table_09.available)
        if pool_table_09.available == "occupied":
            pool_table_09.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_09.hour_start, str(pool_table_09.minute_start).zfill(2), pool_table_09.check_minute))

        print("Table 10: " + pool_table_10.available)
        if pool_table_10.available == "occupied":
            pool_table_10.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_10.hour_start, str(pool_table_10.minute_start).zfill(2), pool_table_10.check_minute))

        print("Table 11: " + pool_table_11.available)
        if pool_table_11.available == "occupied":
            pool_table_11.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_11.hour_start, str(pool_table_11.minute_start).zfill(2), pool_table_11.check_minute))

        print("Table 12: " + pool_table_12.available)
        if pool_table_12.available == "occupied":
            pool_table_12.check_table()
            print("Start time: {0}:{1}   Current usage: {2} minutes".format(pool_table_12.hour_start, str(pool_table_12.minute_start).zfill(2), pool_table_12.check_minute))


    elif cmd == '1':
        print("Table 1 status is " + pool_table_01.available)
        if pool_table_01.available == "not occupied":
            cmdOpen = raw_input("Open table 1 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_01.open_table()
                print("Table 1 had been opened.")

        elif pool_table_01.available == "occupied":
            cmdClose = raw_input("Close table 1 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_01.close_table()
                print("Table 1 has been closed.")

    elif cmd == '2':
        print("Table 2 status is " + pool_table_02.available)
        if pool_table_02.available == "not occupied":
            cmdOpen = raw_input("Open table 2 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_02.open_table()
                print("Table 2 had been opened.")

        elif pool_table_02.available == "occupied":
            cmdClose = raw_input("Close table 2 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_02.close_table()
                print("Table 2 has been closed.")

    elif cmd == '3':
        print("Table 3 status is " + pool_table_03.available)
        if pool_table_03.available == "not occupied":
            cmdOpen = raw_input("Open table 3 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_03.open_table()
                print("Table 3 had been opened.")

        elif pool_table_03.available == "occupied":
            cmdClose = raw_input("Close table 3 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_03.close_table()
                print("Table 3 has been closed.")

    elif cmd == '4':
        print("Table 4 status is " + pool_table_04.available)
        if pool_table_04.available == "not occupied":
            cmdOpen = raw_input("Open table 4 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_04.open_table()
                print("Table 4 had been opened.")

        elif pool_table_04.available == "occupied":
            cmdClose = raw_input("Close table 4 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_04.close_table()
                print("Table 4 has been closed.")


    elif cmd == '5':
        print("Table 5 status is " + pool_table_05.available)
        if pool_table_05.available == "not occupied":
            cmdOpen = raw_input("Open table 5 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_05.open_table()
                print("Table 5 had been opened.")

        elif pool_table_05.available == "occupied":
            cmdClose = raw_input("Close table 5 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_05.close_table()
                print("Table 5 has been closed.")

    elif cmd == '6':
        print("Table 6 status is " + pool_table_06.available)
        if pool_table_06.available == "not occupied":
            cmdOpen = raw_input("Open table 6 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_06.open_table()
                print("Table 6 had been opened.")

        elif pool_table_06.available == "occupied":
            cmdClose = raw_input("Close table 6 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_06.close_table()
                print("Table 6 has been closed.")

    elif cmd == '7':
        print("Table 7 status is " + pool_table_07.available)
        if pool_table_07.available == "not occupied":
            cmdOpen = raw_input("Open table 7 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_07.open_table()
                print("Table 7 had been opened.")

        elif pool_table_07.available == "occupied":
            cmdClose = raw_input("Close table 7 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_07.close_table()
                print("Table 7 has been closed.")

    elif cmd == '8':
        print("Table 8 status is " + pool_table_08.available)
        if pool_table_08.available == "not occupied":
            cmdOpen = raw_input("Open table 8 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_08.open_table()
                print("Table 8 had been opened.")

        elif pool_table_08.available == "occupied":
            cmdClose = raw_input("Close table 8 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_08.close_table()
                print("Table 8 has been closed.")

    elif cmd == '9':
        print("Table 9 status is " + pool_table_09.available)
        if pool_table_09.available == "not occupied":
            cmdOpen = raw_input("Open table 9 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_09.open_table()
                print("Table 9 had been opened.")

        elif pool_table_09.available == "occupied":
            cmdClose = raw_input("Close table 9 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_09.close_table()
                print("Table 9 has been closed.")

    elif cmd == '10':
        print("Table 10 status is " + pool_table_10.available)
        if pool_table_10.available == "not occupied":
            cmdOpen = raw_input("Open table 10 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_10.open_table()
                print("Table 10 had been opened.")

        elif pool_table_10.available == "occupied":
            cmdClose = raw_input("Close table 10 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_10.close_table()
                print("Table 10 has been closed.")

    elif cmd == '11':
        print("Table 11 status is " + pool_table_11.available)
        if pool_table_11.available == "not occupied":
            cmdOpen = raw_input("Open table 11 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_11.open_table()
                print("Table 11 had been opened.")

        elif pool_table_11.available == "occupied":
            cmdClose = raw_input("Close table 11 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_11.close_table()
                print("Table 11 has been closed.")

    elif cmd == '12':
        print("Table 12 status is " + pool_table_12.available)
        if pool_table_12.available == "not occupied":
            cmdOpen = raw_input("Open table 12 (y/n)?: ")
            if cmdOpen == 'y':
                pool_table_12.open_table()
                print("Table 12 had been opened.")

        elif pool_table_12.available == "occupied":
            cmdClose = raw_input("Close table 12 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_12.close_table()
                print("Table 12 has been closed.")

        elif pool_table_12.available == "occupied":
            cmdClose = raw_input("Close table 12 (y/n)?: ")
            if cmdClose == 'y':
                pool_table_12.close_table()
                print("Table 12 has been closed.")

    elif cmd == 'q':
        break

    else:
        print("Invalid command.")


""" pool_table_01.open_table()
print(pool_table_01.available)
pool_table_01.close_table()
print("elapsed minutes for pool table 1: " + str(pool_table_01.elapsed_minute))
pool_table_02.hour_start = 10
pool_table_02.minute_start = 7
pool_table_02.close_table()
print("elapsed minutes for pool table 2: " + str(pool_table_02.elapsed_minute))
print(pool_table_01.available) """