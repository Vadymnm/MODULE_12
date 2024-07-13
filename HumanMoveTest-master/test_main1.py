import main1 as main


def test_run():
    for i in range(10):
        x = main.student_2.run()
#        print(i, main.student_2, x)
    print(main.student_2, x)
    if x < 130:
        print('Пройденный путь < 130 - Можно было бы и быстрее !!!')
    else:
        print('Пройденный путь >= 130 - Молодец,',main.student_2, ', почти что спринтер !!!')

def test_walk():
    for i in range(10):
        x = main.student_1.walk()
#        print(i, main.student_1, x)
    print(main.student_1, x)
    if x < 50:
        print('Пройденный путь < 50 - ОООчень медленно !!!')
    else:
        print('Пройденный путь >= 50 - Молодец',main.student_1, ', быстрый пешеход !!!')

def test_run_walk():

    for i in range(10):
        x = main.student_1.walk()
        y = main.student_2.run()
    print( main.student_1, 'walk:', x, ';', main.student_2, 'run:', y)
    if x < y:
        print('Действительно,', main.student_2, 'бежит быстрее, чем', main.student_1,'идет!')
    else:
        print(main.student_2, ',нужно таки бежать, а не идти !')
    print()

print('===========================')

print(main.student_1,main.student_1.walk())
print(main.student_2,main.student_2.run())

print('---------------------')
test_walk()
print('---------------------')
test_run()
print('---------------------')
test_run_walk()

