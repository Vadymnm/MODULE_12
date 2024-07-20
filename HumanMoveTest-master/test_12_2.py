import unittest
import rt_with_exceptions as main


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.first = main.Runner('Усэйн', 10)
        self.second = main.Runner('Андрей', 9)
        self.third = main.Runner('Ник', 3)
#        print('setup')

    @classmethod
    def setUpClass(cls):
        all_results = []
        last_finisher = []
        cls.all_results = all_results
        cls.last_finisher = last_finisher
#        print('Megasetup')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('--------------------------------------')
#        print('all results: ',cls.all_results)
#        print('last_finisher: ',cls.last_finisher)

        for i in range(1, len(cls.last_finisher)):
            if cls.last_finisher[i] == cls.last_finisher[i-1]:
                message = ['К сожалению,',cls.last_finisher[i],'всегда  последний!']
            else:
                message = [cls.last_finisher[i], 'He Всегда  последний']
        print(message)

    def test_Tournament_start_1(self):
        x = main.Tournament(101, self.first, self.third).start()
        print('1.',list(x.values()))
        self.all_results.append(x)
        last = list(x.values())[-1]
#        print('1 -',last)
        self.last_finisher.append(last)
#        print(self.last_finisher)


    def test_Tournament_start_2(self):
        x = main.Tournament(101,  self.second,self.third).start()
        print('2.',list(x.values()))
        self.all_results.append(x)
        last = list(x.values())[-1]
#        print('2 -',last)
        self.last_finisher.append(last)
#        print(self.last_finisher)


    def test_Tournament_start_3(self):
        x = main.Tournament(101, self.first, self.second, self.third).start()
        print('3.',list(x.values()))
        self.all_results.append(x)
        last = list(x.values())[-1]
#        print('3 -',last)
        self.last_finisher.append(last)
#        print(self.last_finisher)

if __name__ == '__main__':
    unittest.main()
