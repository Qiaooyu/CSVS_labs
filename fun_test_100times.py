from find_cap import func_test

i = 0
while i < 100:
    try:
        func_test()
        result = func_test()
        print("result: ", result)
        i += 1
    except Exception as e:
        print(e)
        continue
