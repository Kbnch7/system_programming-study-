import threading
import time


# Функция для имитации скачивания данных
def load_data(source, load_duration=2):
    print(f'Загружаем данные с {source}')
    time.sleep(load_duration)
    print(f'Загрузка данных с {source} завершена')

# Функция, возвращающая поток
def create_thread(thread_name, load_duration):
    return threading.Thread(target=load_data, name=thread_name, args=(thread_name, load_duration))

if __name__ == '__main__':
    # Создаем 3 потока с разной длительностью
    th1 = create_thread('server1', 1)
    th2 = create_thread('server2', 2)
    th3 = create_thread('server3', 3)

    # Запускаем все 3 потока
    th1.start()
    th2.start()
    th3.start()

    # Заставляем наш вызываюший поток ждать, пока дочерние потоки умрут :(
    th1.join()
    th2.join()
    th3.join()

    # Выводим сообщение в основном потоке. 
    # Если оно вывелось после 6 сообщений - победа (основной поток дождался выполнения 3-х дочерних)
    print('load ended')

    '''
    Загружаем данные с server1
    Загружаем данные с server2
    Загружаем данные с server3
    Загрузка данных с server1 завершена
    Загрузка данных с server2 завершена
    Загрузка данных с server3 завершена
    load ended
    '''