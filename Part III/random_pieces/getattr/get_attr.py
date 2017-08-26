class test:
    def __init__(self):
        self.value = 42

    def add(self, value):
        print(self.value + value)

    def sub(self, value):
        print(self.value - value)

    def run(self, cmd, value):
        getattr(self, cmd)(value)

    def hello(self):
        print('Without params')


t = test()

print(f'value: {t.value}')
getattr(t, 'sub')(2)
t.run('sub', 2)

print(f'value: {t.value}')
getattr(test(), 'add')(2)
t.run('add', 2)

getattr(t, 'hello')()
