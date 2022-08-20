# -*- coding: utf-8 -*-
SEPARATOR_DICT = {'en_US': ['.', ','], 'nl_NL': [',', '.']}
CURRENCY_DICT = {'USD': '$', 'EUR': '€'}
HEADER_DICT = {'en_US': ['Date', 'Description', 'Change'], 'nl_NL': ['Datum', 'Omschrijving', 'Verandering']}

class LedgerEntry:
    def __init__(self, date: str, description: str, change):
        # No reason parameters can't come in the init, modifying outside of scopes without setters is weird.
        self.date = date
        self.description = description
        self.change = change


def create_entry(date: str, description: str, change) -> LedgerEntry:

    return LedgerEntry(date =  date, 
                        description = description, change = change)


def format_header(locale: str) -> str:
    """Creates a header for the ledger table based on the locale.

    Args:
        locale (str): The locale of the ledger, hence dictating the name of the columns.

    Returns:
        str: Returns the header of the table as a string.
    """
    h1, h2, h3 = HEADER_DICT[locale]
    return f"{h1.ljust(11)}| {h2.ljust(26)}| {h3.ljust(13)}"


def format_description(description: str) -> str:
    """Receives a description from an entry and then formats it to not exceed 25 chars.

    Args:
        description (str): A description from a ledger entry.

    Returns:
        str: The processed description so as to truncate it nicely to the 25 char limit.
    """
    processed_entry = description
    if len(processed_entry) > 25:
            processed_entry = processed_entry[:22].ljust(25, '.')
    else:
        processed_entry = processed_entry.ljust(25)
    processed_entry += ' | '
    return processed_entry


def format_date(locale: str, date: str) -> str:
    """Formats the date to the locale appropriate format.

    Args:
        locale (str): The string specifying the locale.
        date (str): The date string to be formated. Should be in format: '%Y-%m-%d'

    Returns:
        str: Formatted date to be put into ledger.
    """
    year, month, day = date.split('-')
    if locale == 'en_US':
        date_str = f"{month.rjust(2, '0')}/{day.rjust(2, '0')}/{year.rjust(4, '0')}"
    elif locale == 'nl_NL':
        date_str = f"{day.rjust(2, '0')}-{month.rjust(2, '0')}-{year.rjust(4, '0')}"
    else:
        raise ValueError("Location not recognized.")
    return date_str


def find_next_entry(entries: list[LedgerEntry]) -> int:
    min_entry_index = -1
    for i in range(len(entries)):
        entry = entries[i]
        if min_entry_index < 0:
            min_entry_index = i
            
        min_entry = entries[min_entry_index]
        if entry.date < min_entry.date:
            min_entry_index = i
            
        elif (
            entry.date == min_entry.date and
            entry.change < min_entry.change
        ):
            min_entry_index = i
            
        elif (
            entry.date == min_entry.date and
            entry.change == min_entry.change and
            entry.description < min_entry.description
        ):
            min_entry_index = i
    return min_entry_index

def format_currency(entry_change: int, locale: str, currency: str):
    # function just for locale, for now. Seems easier.
    # Or maybe for the cents part idk
    cents_separator, decimal_separator = SEPARATOR_DICT[locale]
    currency_str = str(entry_change).removeprefix('-')
    # Pad the cents part:
    if abs(entry_change) <= 10:
        if entry_change < 0:
            size = 3
        else:
            size = 2
        currency_str = currency_str.rjust(size, '0')
    currency_list = list(currency_str)
    currency_list.insert(-2, cents_separator) # Add cent separator.
    number_of_commas = (len(str(abs(entry_change))) // 3) - 1
    for i in range(number_of_commas): # This inserts the decimal separator every 3 characters from the right. (not counting cents)
        currency_list.insert(-3 -3*(i+1), decimal_separator)
    currency_symbol = CURRENCY_DICT[currency]
    if locale == 'nl_NL': # This locale pads the currency symbol.
        currency_symbol = currency_symbol.ljust(2)
    if currency_list[0] == '.':
        currency_list.insert(0, '0')
    currency_list.insert(0, currency_symbol)
    currency_ledger = ''.join(currency_list)
    if entry_change < 0:
        if locale == 'en_US':
            currency_ledger = f'({currency_ledger})'
        elif locale == 'nl_NL':
            pass
    else:
        currency_ledger += ' '
    currency_ledger = currency_ledger.rjust(13)
    return currency_ledger


def format_entries(currency, locale: str, entries: list[LedgerEntry]):
    if locale == 'en_US':
        # Generate Header Row
        table = format_header(locale)
        while len(entries) > 0:
            table += '\n'
            min_entry_index = find_next_entry(entries)
            entry =  entries.pop(min_entry_index)
            table += format_date(locale, entry.date) # Simplify date processing to another function, tidier as well.
            table += ' | '
            table += format_description(entry.description)
            table += format_currency(entry.change, locale, currency)
    elif locale == 'nl_NL':
        table = format_header(locale)
        while len(entries) > 0:
            table += '\n'
            min_entry_index = find_next_entry(entries)
            entry = entries.pop(min_entry_index)
            table += format_date(locale, entry.date)
            table += ' | '
            table += format_description(entry.description)
            
            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while len(euro_parts) > 0:
                        change_str += euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
    return table
