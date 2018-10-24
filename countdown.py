def countdown(seconds=None):
    import time

    while True:
        while not seconds or type(seconds) is not int:
            uin = input(">> ")
            try:
                seconds = abs(int(uin))
            except KeyboardInterrupt:
                break
            except:
                print("Not a number!")

        for second in reversed(range(seconds)):
            m, s = divmod(second, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) \
                + ":" + str(m).zfill(2) \
                + ":" + str(s).zfill(2)
            # '\r' helps to print over the same line
            print(time_left + "\r", end="")
            time.sleep(1)  # Pauses execution for 1 second so countdown works
        print()
        break

countdown()
