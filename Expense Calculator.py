from datetime import datetime
import ast


class ExpenseCalculator:
    def __init__(self):
        self.user_records = []
        self.p_type = ''

    def _create_record(self) -> None:
        with open('My Records.txt', 'a') as file:
            file.write(str(self.user_records))

    @staticmethod
    def _get_current_date():
        return datetime.now().strftime('%d:%m:%Y')

    def record(self) -> None:
        expense_dict = {'Items': None, 'Price': None, 'entry_date': self._get_current_date()}
        _items, _prices = [], []
        while True:
            item = input('Give Item Name/Write "end_session" To End\n:> ')
            if item.lower() == 'end_session':
                break
            price_tag = input('Give Item Price\n:> ')
            _items.append(item)
            _prices.append(price_tag)
        expense_dict['Items'] = _items
        expense_dict['Price'] = _prices
        self.user_records.append(expense_dict)
        self._create_record()
        print('Record Updated')
        return

    def _get_records(self) -> None:
        with open('My Records.txt', 'r') as file:
            contents = file.read().replace('][', ', ')
            self.user_records = ast.literal_eval(contents)

    def total_expense(self):
        _Currency = input('Give Your Currency\n:> ')
        total_expense = 0.00
        self._get_records()
        for cells in self.user_records:
            print('----------------------------------------------------------------------------')
            print('Items  Price')
            daily_expense = 0.00
            date = cells['entry_date']
            items = cells['Items']
            prices = cells['Price']
            for itm, val in zip(items, prices):
                print(f'{itm}: {val} {_Currency}')
                daily_expense += float(val)
                total_expense += float(val)
            print(f'Expense on {date} = {daily_expense} {_Currency}')
            print('----------------------------------------------------------------------------')
        print(f'\n######################### Total Expense = {total_expense} {_Currency} #########################')

    def expense_by_date(self) -> None:
        usr_date = input('Give Date in format "DD:MM::YYYY"\n:> ')
        usr_date = usr_date.replace(' ', ':')

        _Currency = input('Give Your Currency\n:> ')
        _expense = 0.00
        FOUND_FLAG = False
        self._get_records()
        for cells in self.user_records:
            date = cells['entry_date']
            if usr_date == date:
                FOUND_FLAG = True
                items = cells['Items']
                prices = cells['Price']
                for itm, val in zip(items, prices):
                    print(f'{itm}: {val} {_Currency}')
                    _expense += float(val)
        if FOUND_FLAG:
            print(f'Expense on {usr_date} = {_expense} {_Currency}')
        else:
            print(f'No Record Found On Date: {usr_date}')

if __name__ == '__main__':
    g = ExpenseCalculator()
    # g.total_expense()
    # g.record()
    g.expense_by_date()
