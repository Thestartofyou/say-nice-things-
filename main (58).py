import time

while True:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"It's currently {current_time}. Remember to say nice things to people!")
    time.sleep(3600)  # wait for one hour (3600 seconds)
