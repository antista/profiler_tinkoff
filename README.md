# Профилировщик
Объект, который может выступать в качестве декоратора и context менеджера. Выводит различные статистики по результату своей работы.

* Время работы;
* Кол-во и типы объектов с циклическими ссылками;
* Кол-во объектов собранных garbage collector'ом.

### Использование
* ***Context-manager***


    with Profiler():
        func(*args,**kwargs)
* ***Декоратор***


    @Profiler()
    def func(*args,**kwargs):
        pass
     

### Запуск тестов
* `python -m pytest`

### Запуск линтера
* `flake8 profiler/`

### Примеры вывода


             7 function calls in 2.000 seconds
          Ordered by: cumulative time
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.000    2.000 C:\Users\radish\python\courses\task-3\profiler\profiler.py:46(guu)
        1    2.000    2.000    2.000    2.000 {built-in method time.sleep}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 C:\Users\radish\python\courses\task-3\profiler\profiler.py:18(__exit__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects
    Overall time of work: 2.001061201095581 sec
    Count of collected objects by gc: 99
    Objects with circle links: 1 :
     <class 'list'> : 1
     
