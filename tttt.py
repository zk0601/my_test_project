def func(kong_ping, gai):
    ping = kong_ping // 2 + gai // 4
    return ping, ping + kong_ping % 2, ping + gai % 4


def main(money):
    ping = money / 2
    result = ping
    kong_ping, gai = ping, ping
    while kong_ping >= 2 or gai >= 4:
        temp = func(kong_ping, gai)
        result += temp[0]
        kong_ping, gai = temp[1], temp[2]
    return result


if __name__ == '__main__':
    print(main(20))
