from find_cap import func_test

i = 0
while i < 100:
    try:
        func_test()
        i += 1
    except Exception as e:
        print(e)
        continue
