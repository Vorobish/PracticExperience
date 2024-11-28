import fnmatch
import os

import pandas as pd


class PriceMachine():
    price_all = None
    directory = 'C:/Users/nasty/Desktop/Практическое задание/PracticExperience/'

    def load_prices(self, file_path=directory + 'folder/'):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        filtered_files = fnmatch.filter(os.listdir(file_path), '*price*')
        for file in filtered_files:
            f = pd.read_csv(file_path + file)
            list_product_price_weight = self._search_product_price_weight(f.columns.tolist())
            if list_product_price_weight:
                product = f.columns.tolist()[list_product_price_weight[0]]
                price = f.columns.tolist()[list_product_price_weight[1]]
                weight = f.columns.tolist()[list_product_price_weight[2]]
                df = f[[product, price, weight]]
                df = df.rename(columns={product: 'Наименование', price: 'цена', weight: 'вес'})
                df['файл'] = file
                df['цена за кг.'] = (df['цена'] / df['вес']).round(1)
                if PriceMachine.price_all is None:
                    PriceMachine.price_all = df
                else:
                    PriceMachine.price_all = pd.concat([PriceMachine.price_all, df], ignore_index=True)

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''
        product = None
        price = None
        weight = None
        i = 0
        for c in headers:
            if c == 'товар' or c == 'название' or c == 'наименование' or c == 'продукт':
                product = i
            if c == 'розница' or c == 'цена':
                price = i
            if c == 'вес' or c == 'масса' or c == 'фасовка':
                weight = i
            i += 1
        if not product is None and not price is None and not weight is None:
            return [product, price, weight]

    def export_to_html(self, df=price_all, fname=directory + 'output.html'):
        with open(fname, 'w') as fo:
            fo.write(df.to_html())

    def find_text(self, text):
        df = PriceMachine.price_all[PriceMachine.price_all['Наименование'].str.contains(text, case=False)]
        df = df.sort_values('цена за кг.', ascending=True)
        df.index = range(1, len(df) + 1, 1)
        df.index.name = '№'
        print(df)
        pm.export_to_html(df.sort_values('цена за кг.', ascending=True))


pm = PriceMachine()
pm.load_prices()
user_input = ''

while user_input != 'exit':
    pm.find_text(user_input)
    user_input = input('Введите название товара \n')
else:
    print('работа закончена')
    exit()
