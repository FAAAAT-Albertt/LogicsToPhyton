import time
import requests
import json


TOKEN = "6015170757:AAF6Ns49I1gl6AjNn6mwvq3HYK37-KTW-YM"
id_channel = "-1001526787759"

check_num = {
    'num1': ""
}

check = {"2.5 Б": [0, 0],
            "2.5 М": [0, 0],
            "3.5 Б": [0, 0],
            "3.5 М": [0, 0],
            "4.5 Б": [0, 0],
            "4.5 М": [0, 0],
            "5.5 Б": [0, 0],
            "5.5 М": [0, 0],
            "6.5 Б": [0, 0],
            "6.5 М": [0, 0],
            "7.5 Б": [0, 0],
            "7.5 М": [0, 0],
            "iter": 0}

check_htree = {
    "YES" : [0, 0],
    "NO" : [0, 0],
    "iter" : 0
}

check_odd = {
    "YES" : [0, 0],
    "NO" : [0, 0],
    "iter" : 0
}


check_suit = {
    "P" : [0, 0, '♠️'],
    "T" : [0, 0, '♣️'],
    "B" : [0, 0, '♦️'],
    "CH" : [0, 0, '♥️'],
    "iter" : 0
}


check_who = {
    "W1" : [0, 0],
    "W2" : [0, 0],
    "D" : [0, 0],
    "iter" : 0

}

check_odd_not = {
    "2/2" : [0, 0],
    "3/2" : [0, 0],
    "2/3" : [0, 0],
    "3/3" : [0, 0],
    "iter" : 0

}

check_res_payer = {
    "2" : ["Двойка", 0, 0],
    "3" : ["Тройка", 0, 0],
    "4" : ["Четверка", 0, 0],
    "5" : ["Пятерка" , 0, 0],
    "6" : ["Шестерка", 0, 0],
    "7" : ["Семерка", 0, 0],
    "8" : ["Восьмерка", 0, 0],
    "9" : ["Девятка", 0, 0],
    "10" : ["Десятка", 0, 0],
    "11" : ["Валет", 0, 0],
    "12" : ["Дама", 0, 0],
    "13" : ["Король", 0, 0],
    "14" : ["Туз", 0, 0],
    "iter": 0
}

def main():
    main_url = get_main_url()
    while True:
        try:
            get_matches(main_url)
            time.sleep(3)
        except:
            main_url = get_main_url()
            time.sleep(3)
            continue

def get_main_url():

    req = requests.get('https://1xbetting.world/link/?domain=https://refpa1364493.top')
    url = req.url
    url = url.split('/')
    main_url = url[0] + '//' + url[2]
    return main_url

def get_matches(main_url):

    url = main_url + "/service-api/LiveFeed/GetSportsShortZip?sports=236&champs=2050671&gr=285&country=1&virtualSports=true&groupChamps=true"
    req = requests.get(url).json()

    find_baccara(req)

def find_baccara(js):

    for game in js['Value']:
        if game['I'] == 236:
            with open("data.json", "w") as file:
                json.dump(game, file)
    processing_games(file)

def processing_games(file):

    with open ("data.json", "r", encoding="utf-8") as file:
        file_js = json.load(file)
    games = file_js['L'][0]['G'][0]

    try:
        number = games['DI']
        data_player = games['SC']['S'][0]['Value']
        data_bankir = games['SC']['S'][1]['Value']
        winner = games['SC']['S'][2]['Value']
        status = games['SC']['I']
        try:
            total_sum = games['SC']['FS']['S1']
        except:
            total_sum = 0
        if check_num['num1'] != number:

            if status == "Игра завершена":
                check_num['num1'] = number
                math_total(total_sum, check, number)
                three_of_cards(data_player)
                odd_card(total_sum)
                suit_card(data_player)
                who_is_win(winner)
                odd_or_not(data_player, data_bankir)
                res_player(data_player)
                get_tg(TOKEN, id_channel)


    except Exception as ex:
        print(ex)

def total(total_sum):
    result = []
    if total_sum == 0 or total_sum == 1 or total_sum == 2:
        result = ['2.5 М', '3.5 М', '4.5 М', '5.5 М', '6.5 М', '7,5 М']

    elif total_sum == 3:
        result = ['3.5 М', '4.5 М', '5.5 М', '6.5 М', '7.5 М', '2.5 Б']

    elif total_sum == 4:
        result = ['4.5 М', '5.5 М', '6.5 М', '7.5 М', '2.5 Б', '3.5 Б']

    elif total_sum == 5:
        result = ['5.5 М', '6.5 М', '7.5 М', '2.5 Б', '3.5 Б', '4.5 Б']

    elif total_sum == 6:
        result = ['6.5 М', '7.5 М', '2.5 Б', '3.5 Б', '4.5 Б', '5.5 Б']

    elif total_sum == 7:
        result = ['7.5 М', '2.5 Б', '3.5 Б', '4.5 Б', '5.5 Б', '6.5 Б']

    elif total_sum == 8 or total_sum == 9:
        result = ['2.5 Б', '3.5 Б', '4.5 Б', '5.5 Б', '6.5 Б', '7.5 Б']

    return result

def three_of_cards(data_player):
    mas_line = ["3 КАРТЫ ИГРОКА\n"]
    k = 0
    data_player = data_player.split("}")
    for data in data_player:
        if "S" in data or "R" in data:
            k += 1
    # print(f"ЧИСЛО КАРТ: {k}")
    if check_htree['iter'] == 0:
        if k == 3:
            check_htree['YES'][0] = 0
            check_htree['YES'][1] = 0
            mas_line.append(f"ДА не было {check_htree['YES'][0]}[Макс {check_htree['YES'][1]}]")
            check_htree['NO'][0] += 1
            check_htree['NO'][1] += 1
            mas_line.append(f"НЕТ не было {check_htree['NO'][0]}[Макс {check_htree['NO'][1]}]")
        else:
            check_htree['YES'][0] += 1
            check_htree['YES'][1] += 1
            mas_line.append(f"ДА не было {check_htree['YES'][0]}[Макс {check_htree['YES'][1]}]")
            check_htree['NO'][0] = 0
            check_htree['NO'][1] = 0
            mas_line.append(f"НЕТ не было {check_htree['NO'][0]}[Макс {check_htree['NO'][1]}]")
    else:
        if k == 3:
            check_htree['NO'][0] += 1
            if check_htree['NO'][1] < check_htree['NO'][0]:
                check_htree['NO'][1] = check_htree['NO'][0]

            check_htree['YES'][0] = 0

            mas_line.append(f"ДА не было {check_htree['YES'][0]}[Макс {check_htree['YES'][1]}]")
            mas_line.append(f"НЕТ не было {check_htree['NO'][0]}[Макс {check_htree['NO'][1]}]")
        else:
            check_htree['YES'][0] += 1
            if check_htree['YES'][1] < check_htree['YES'][0]:
                check_htree['YES'][1] = check_htree['YES'][0]

            check_htree['NO'][0] = 0

            mas_line.append(f"ДА не было {check_htree['YES'][0]}[Макс {check_htree['YES'][1]}]")
            mas_line.append(f"НЕТ не было {check_htree['NO'][0]}[Макс {check_htree['NO'][1]}]")

    check_htree['iter'] += 1

    load(mas_line)

def odd_card(total_sum):
    mas_line = ["НЕЧЁТНОЕ ЧИСЛО ИГРОКА\n"]
    print(total_sum)
    if check_odd['iter'] == 0:

        if total_sum % 2 != 0:

            check_odd['YES'][0] = 0
            check_odd['YES'][1] = 0
            mas_line.append(f"ДА не было {check_odd['YES'][0]}[Макс {check_odd['YES'][1]}]")

            check_odd['NO'][0] += 1
            check_odd['NO'][1] += 1
            mas_line.append(f"НЕТ не было {check_odd['NO'][0]}[Макс {check_odd['NO'][1]}]")

        else:

            check_odd['YES'][0] += 1
            check_odd['YES'][1] += 1
            mas_line.append(f"ДА не было {check_odd['YES'][0]}[Макс {check_odd['YES'][1]}]")

            check_odd['NO'][0] = 0
            check_odd['NO'][1] = 0
            mas_line.append(f"НЕТ не было {check_odd['NO'][0]}[Макс {check_odd['NO'][1]}]")

    else:
        if total_sum % 2 != 0:
            check_odd['NO'][0] += 1

            if check_odd['NO'][1] < check_odd['NO'][0]:
                check_odd['NO'][1] = check_odd['NO'][0]

            check_odd['YES'][0] = 0

            mas_line.append(f"ДА не было {check_odd['YES'][0]}[Макс {check_odd['YES'][1]}]")
            mas_line.append(f"НЕТ не было {check_odd['NO'][0]}[Макс {check_odd['NO'][1]}]")

        else:
            check_odd['YES'][0] += 1

            if check_odd['YES'][1] < check_odd['YES'][0]:
                check_odd['YES'][1] = check_odd['YES'][0]

            check_odd['NO'][0] = 0

            mas_line.append(f"ДА не было {check_odd['YES'][0]}[Макс {check_odd['YES'][1]}]")
            mas_line.append(f"НЕТ не было {check_odd['NO'][0]}[Макс {check_odd['NO'][1]}]")

    check_odd['iter'] += 1
    load(mas_line)

def suit_card(data_player):
    mas_line = ['МАСТЬ ИГРОКА\n']
    suit_test = ["P", "T", "B", "CH"]
    suit_mas = []
    data_player = data_player.split(":")
    for data in range(len(data_player)):
        if data % 2 != 0:
            if "0" in data_player[data]:
                suit_mas.append("P")
            if "1" in data_player[data]:
                suit_mas.append("T")
            if "2" in data_player[data]:
                suit_mas.append("B")
            if "3" in data_player[data]:
                suit_mas.append("CH")

    for elem in suit_test:
        if check_suit['iter'] == 0:

            if elem not in suit_mas:
                check_suit[elem][0] += 1
                check_suit[elem][1] += 1

                mas_line.append(f"{check_suit[elem][2]} не было {check_suit[elem][0]}[Макс {check_suit[elem][1]}]")
            else:

                mas_line.append(f"{check_suit[elem][2]} не было {check_suit[elem][0]}[Макс {check_suit[elem][1]}]")
        else:
            if elem not in suit_mas:
                check_suit[elem][0] += 1
                if check_suit[elem][1] < check_suit[elem][0]:
                    check_suit[elem][1] = check_suit[elem][0]

                mas_line.append(f"{check_suit[elem][2]} не было {check_suit[elem][0]}[Макс {check_suit[elem][1]}]")
            else:
                check_suit[elem][0] = 0

                mas_line.append(f"{check_suit[elem][2]} не было {check_suit[elem][0]}[Макс {check_suit[elem][1]}]")

        check_suit['iter'] += 1

    load(mas_line)

def who_is_win(winner):

    mas_test = ["W1", "W2", "D"]
    mas_line = ['ПОБЕДА1/НИЧЬЯ/ПОБЕДА2\n']
    result = ""
    if winner == "Draw":
        result = "D"
    if winner == "Win1":
        result = "W1"
    if winner == "Win2":
        result = "W2"
    print(f"ПОБЕДИЛ : {result}")
    for elem in mas_test:
        if check_who['iter'] == 0:

            if elem not in result:
                check_who[elem][0] += 1
                check_who[elem][1] += 1

                mas_line.append(f"{elem} не было {check_who[elem][0]}[Макс {check_who[elem][1]}]")

            else:
                check_who[elem][0] = 0
                check_who[elem][1] = 0
                mas_line.append(f"{elem} не было {check_who[elem][0]}[Макс {check_who[elem][1]}]")
        else:
            if elem not in result:
                check_who[elem][0] += 1
                if check_who[elem][1] < check_who[elem][0]:
                    check_who[elem][1] = check_who[elem][0]

                mas_line.append(f"{elem} не было {check_who[elem][0]}[Макс {check_who[elem][1]}]")
            else:
                check_who[elem][0] = 0

                mas_line.append(f"{elem} не было {check_who[elem][0]}[Макс {check_who[elem][1]}]")

        check_who['iter'] += 1
    load(mas_line)

def odd_or_not(data_player, data_bankir):
    mas_test = ['2/2', '3/2', '2/3', '3/3']
    mas_line = ['ТОТАЛ КАРТ\n']
    odd_result = ""
    k1 = 0
    k2 = 0
    data_player = data_player.split(':')
    data_bankir = data_bankir.split(':')
    if len(data_player) == 3:
        k1 = 1
    elif len(data_player) == 5:
        k1 = 2
    elif len(data_player) == 7:
        k1 = 3

    if len(data_bankir) == 3:
        k2 = 1
    elif len(data_bankir) == 5:
        k2 = 2
    elif len(data_bankir) == 7:
        k2 = 3

    odd_result = str(k1) + "/" + str(k2)
    for elem in mas_test:
        if check_odd_not['iter'] == 0:
            if elem not in odd_result:
                check_odd_not[elem][0] += 1
                check_odd_not[elem][1] += 1

                mas_line.append(f"{elem} не было {check_odd_not[elem][0]}[Макс {check_odd_not[elem][1]}]")
            else:
                mas_line.append(f"{elem} не было {check_odd_not[elem][0]}[Макс {check_odd_not[elem][1]}]")
        else:
            if elem not in odd_result:
                check_odd_not[elem][0] += 1
                if check_odd_not[elem][1] < check_odd_not[elem][0]:
                    check_odd_not[elem][1] = check_odd_not[elem][0]

                mas_line.append(f"{elem} не было {check_odd_not[elem][0]}[Макс {check_odd_not[elem][1]}]")
            else:
                check_odd_not[elem][0] = 0


                mas_line.append(f"{elem} не было {check_odd_not[elem][0]}[Макс {check_odd_not[elem][1]}]")
        check_odd_not['iter'] += 1
    load(mas_line)

def res_player(data_player):
    mas_test = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    mas_res_num = []
    mas_line = []
    data_player = data_player.split(':')
    mas_line = ["ЗНАЧЕНИЯ ИГРОКА\n"]
    for data in range(len(data_player)):
        if data == 0:
            continue
        elif data % 2 == 0:
            data_player[data] = data_player[data].replace('"S"', '').replace('"R"', '').replace(",", "").replace("{", "").replace("}", "").replace("]", "")
            mas_res_num.append(data_player[data])

    print(mas_res_num)
    for elem in mas_test:
        if check_res_payer["iter"] == 0:
            if elem not in mas_res_num:
                check_res_payer[elem][1] += 1
                check_res_payer[elem][2] += 1

                mas_line.append(f"{check_res_payer[elem][0]} не было {check_res_payer[elem][1]}[Макс {check_res_payer[elem][2]}]")
            else:
                mas_line.append(f"{check_res_payer[elem][0]} не было {check_res_payer[elem][1]}[Макс {check_res_payer[elem][2]}]")
        else:
            if elem not in mas_res_num:
                check_res_payer[elem][1] += 1
                if check_res_payer[elem][2] < check_res_payer[elem][1]:
                    check_res_payer[elem][2] = check_res_payer[elem][1]

                mas_line.append(f"{check_res_payer[elem][0]} не было {check_res_payer[elem][1]}[Макс {check_res_payer[elem][2]}]")
            else:
                check_res_payer[elem][1] = 0

                mas_line.append(f"{check_res_payer[elem][0]} не было {check_res_payer[elem][1]}[Макс {check_res_payer[elem][2]}]")


        check_res_payer["iter"] += 1



    load(mas_line)

def math_total(total_sum, check, number):

    mas_line = []
    mas_test = ["2.5 Б", "2.5 М", "3.5 Б", "3.5 М", "4.5 Б", "4.5 М", "5.5 Б", "5.5 М","6.5 Б", "6.5 М", "7.5 Б", '7.5 М']
    ts = total(total_sum)
    for item in mas_test:
        if check['iter'] == 0:
            if item not in ts:
                check[item][0] += 1
                check[item][1] += 1
                mas_line.append(f"👉{item} не было {check[item][0]}[Макс {check[item][1]}]")
            else:

                mas_line.append(f"👉{item} не было {check[item][0]}[Макс {check[item][1]}]")
        else:
            if item not in ts:
                check[item][0] += 1
                if check[item][1] < check[item][0]:
                    check[item][1] = check[item][0]

                mas_line.append(f"👉{item} не было {check[item][0]}[Макс {check[item][1]}]")
            else:
                check[item][0] = 0
                mas_line.append(f"👉{item} не было {check[item][0]}[Макс {check[item][1]}]")
    mas_line.insert(0, f"Текущая игра: {number}\n")
    check['iter'] += 1
    st = ""

    load(mas_line)

def load(mas_line):
    with open('totals.txt', 'a', encoding="UTF-8") as file:
        for line in mas_line:
            file.write(line + "\n")
        file.write('\n')

def get_tg(token, id_channel):
    with open('totals.txt', 'r', encoding="UTF-8") as file:
        try:
            text = file.read()

            #url_user = f"https://api.telegram.org/bot{token}/getUpdates"
            url = f"https://api.telegram.org/bot{token}/editMessageText?chat_id={id_channel}&message_id=3&text={text}"
            #url =f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id_channel}&text={text}"
            res = requests.get(url)
            i = res.json()

        except:
            file.close()
    with open('totals.txt', 'w', encoding="UTF-8") as file:
        file.write("")


if __name__ == "__main__":
    main()
