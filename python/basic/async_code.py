import time

async def main(func):
    await time.sleep(3)
    func()


def callback_func():
    print("the sql excute success!")


if __name__ == '__main__':
    try:
        main(callback_func).send(None)
    except StopIteration as e:
        print(e)
    print("I love Python.")
    

