import threading
import time
import random


class Bank:
    def __init__(self, cashboxes, users):
        self.lock = threading.Lock()
        self.cashboxes = cashboxes
        self.users = users

    def start_process_client(self, client):
        def process_client():
            while self.cashboxes < 1:
                time.sleep(0.1)
            with self.lock:
                self.cashboxes -= 1
            print(f"start processing client №{client[0]}")
            time.sleep(random.uniform(0, 2))
            print(f"end processing client №{client[0]}")
            with self.lock:
                self.cashboxes += 1
        thread = threading.Thread(
            target=process_client,
            args=()
        )
        thread.start()

    def start_bank(self):
        sorted_users = sorted(self.users, key=lambda user: int(user[1]))[::-1]
        while sorted_users:
            thread = threading.Thread(
                target=self.start_process_client,
                args=(sorted_users[0],)
            )
            sorted_users.pop(0)
            thread.start()
            thread.join()

bank = Bank(2, [(0, True), (1, True), (2, False), (3, True), (4, False), (5, True), (6, False)])
bank.start_bank()