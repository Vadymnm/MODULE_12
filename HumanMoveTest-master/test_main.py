import main
import unittest


class MyMainTest(unittest.TestCase):

    def setUp(self):
        print('setup')

    @classmethod
    def setUpClass(cls):
        print('Megasetup')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_walk(self):
        for i in range(10):
            x = main.student_1.walk()
    #        print(i, main.student_1, x)
        print(main.student_1, x)
        if x < 50:
            print('Пройденный путь < 50 - ОООчень медленно !!!')
        else:
            print('Пройденный путь >= 50 - Молодец,',main.student_1,'хорошо  идешь !!!')
        self.assertGreaterEqual(x,50)

    def test_run(self):
        for i in range(10):
            x = main.student_2.run()
    #        print(i, main.student_2, x)
        print(main.student_2, x)
        #if x < 120:
        #     print('Пройденный путь < 120 - Можно было бы и быстрее !!!')
        # else:
        #     print('Пройденный путь >= 120 - Молодец, почти что спринтер !!!')
        self.assertLessEqual(x,115,'Пройденный путь < 120 - Можно было бы и быстрее !!!')
        print()

    def test_run_walk(self):
        for i in range(10):
            x = main.student_3.walk()
            y = main.student_4.run()
        print( main.student_3, 'walk:', x, ';', main.student_4, 'run:', y)
        if x < y:
            print('Действительно,', main.student_4, 'бежит быстрее, чем', main.student_3,'идет!')
        else:
            print(main.student_2, ',нужно таки бежать, а не идти !')
        print()

if __name__ == '__main__':
    # запускам автодискавер тестов
    unittest.main()
