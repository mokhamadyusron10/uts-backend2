list_Supermarket = ['Sembako', 'Minuman', 'Makanan']
list_Sembako = ['Beras', 'Minyak', 'Telur', 'Gula']
list_Minuman = ['Susu', 'Teh',
                     'Soda', 'Mineral']
list_Makanan = ['Roti', 'sosis',
                'Snack', 'Buah']
cart = []
while True:
    print('==================')
    for item in range(0, len(list_Supermarket)):
        print(f'{item + 1}. {list_Supermarket[item]} ')
    market = input('Silahkan Pilih Aneka Varian 1-3 ')
    if market == '1':
        for item_market in range(0, len(list_Sembako)):
            print(f'{item_market + 1}. {list_Sembako[item_market]} ')
        ulang = True
        while ulang:
            select_market = int(
                input(f'Silahkan Pilih Varian 1-{len(list_Sembako)} '))
            if select_market <= 0 or select_market > len(list_Sembako):
                print('silahkan masukan menu dengan benar')
                for item_market in range(0, len(list_Sembako)):
                    print(f'{item_market + 1}. {list_Sembako[item_market]} ')
                continue
            else:
                cart.append(list_Sembako[select_market - 1])
                print('==== list market ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                ulang = False
            continue
    elif market == '2':
        for item_market2 in range(0, len(list_Minuman)):
            print(f'{item_market2 + 1}. {list_Minuman[item_market2]} ')
        ulang = True
        while ulang:
            select_market = int(
                input(f'Silahkan Pilih Varian 1-{len(list_Minuman)} '))
            if select_market <= 0 or select_market > len(list_Minuman):
                print('silahkan masukan menu dengan benar')
                for item_market2 in range(0, len(list_Minuman)):
                    print(
                        f'{item_market2 + 1}. {list_Minuman[item_market2]} ')
            else:
                cart.append(list_Minuman[select_market - 1])
                print('==== list varian ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
                continue
    elif market == '3':
        for item_market3 in range(0, len(list_Makanan)):
            print(f'{item_market3 + 1}. {list_Makanan[item_market3]} ')
        ulang = True
        while ulang:
            select_market = int(
                input(f'Silahkan Pilih Varian 1-{len(list_Makanan)} '))
            if select_market <= 0 or select_market > len(list_Makanan):
                print('silahkan masukan menu dengan benar')
                for item_market3 in range(0, len(list_Makanan)):
                    print(f'{item_market3 + 1}. {list_Makanan[item_market3]} ')
            else:
                cart.append(list_Makanan[select_market - 1])
                print('==== list market ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
            continue
    else:
        print('varian tidak ditemukan')
        continue
    pilih = input('Apakah Pilih Lagi ?')
    if pilih == 'Y' or pilih == 'N':
        continue
    else:
        print('==== list market ====')

        for list_cart in range(0, len(cart)):
            print(f'{list_cart +1} . {cart[list_cart]}')
        print("terima kasih telah berkunjung")
        break