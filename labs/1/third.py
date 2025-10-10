import multiprocessing
from second import load_data # Функции из 2 и 3 задания делают +- одно и то же, поэтому я ее ивзял просто


# Функция, возвращающая процесс
def create_process(process_name):
    return multiprocessing.Process(target=load_data, args=(process_name,), name=process_name)

if __name__ == '__main__':
    # Создаем процессы
    process1 = create_process('process1')
    process2 = create_process('process2')

    # Запускаем процессы
    process1.start()
    process2.start()

    # Ждем, пока они завершатся
    process1.join()
    process2.join()

    # Выводим сообщение об окончании дочерних потоков
    # Аналогично 2 задаче, если этот принт последний = победа
    print('load ended')

    '''
    load ended
    Загружаем данные с process1
    Загружаем данные с process2
    Загрузка данных с process1 завершена
    Загрузка данных с process2 завершена
    '''