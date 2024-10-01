def my_func_2():
    print("Сейчас отдам число")
    yield 1
    print("Сейчас отдам ещё число")
    yield 2
    print("Больше ничего нету!")


a = my_func_2()
print(next(a))
