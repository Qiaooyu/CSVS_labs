from all_code_new import func_test

i=0
while i <200:
    try:
        func_test()
        i += 1
    except Exception as e:
        print(e)
        break
