import play
import get_time

playtime = input("insert time(format: 00:00:00): ")


def get_timeMinusOne():
    timeMinusOne = f'{playtime.split(":")[0]}:{playtime.split(":")[1]}:{int(playtime.split(":")[2])}'

    if timeMinusOne.split(':')[1] == "00" and timeMinusOne.split(':')[2] == "0":
        timeMinusOne = f'{int(playtime.split(":")[0]) - 1}:59:59'

        if timeMinusOne.split(":")[0] == "-1":
            timeMinusOne = '11:59:59'

        if len(timeMinusOne.split(':')[0]) == 1:
            timeMinusOne = f'0{int(playtime.split(":")[0]) - 1}:{playtime.split(":")[1]}:0{playtime.split(":")[2]}'
    elif timeMinusOne.split(':')[2] == "0":

        timeMinusOne = f'{playtime.split(":")[0]}:{int(playtime.split(":")[1]) - 1}:59'

        if len(timeMinusOne.split(':')[1]) == 1:
            timeMinusOne = f'{playtime.split(":")[0]}:{playtime.split(":")[1]}:59'
    else:
        timeMinusOne = f'{playtime.split(":")[0]}:{playtime.split(":")[1]}:{int(playtime.split(":")[2]) - 1}'

        if len(timeMinusOne.split(':')[2]) == 1:
            timeMinusOne = f'{playtime.split(":")[0]}:{playtime.split(":")[1]}:0{int(playtime.split(":")[2]) - 1}'

    return timeMinusOne


while True:

    if get_time.time() == get_timeMinusOne():
        play.volumeUp()

    if get_time.time() == playtime:
        print("get somebody once'd lmao")
        play.play()
        continue
