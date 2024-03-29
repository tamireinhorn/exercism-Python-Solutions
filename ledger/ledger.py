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
    return f'{date_str} | '


def find_next_entry(entries: list[LedgerEntry]) -> int:
    """Applies business rules to find the next ledger entry to be printed.

    Args:
        entries (list[LedgerEntry]): List of all ledger entries from which to select the next one.

    Returns:
        int: Index of the next ledger entry.
    """
    min_entry_index = -1
    for i in range(len(entries)):
        entry = entries[i]
        if min_entry_index < 0: # If it's the first iteration, the next entry is the one to be considered.
            min_entry_index = i
            
        min_entry = entries[min_entry_index]
        if entry.date < min_entry.date: # If the current entry is earlier, it's the next one.
            min_entry_index = i
            
        elif ( # If the date is tied, the smallest change is the tiebreaker.
            entry.date == min_entry.date and
            entry.change < min_entry.change
        ):
            min_entry_index = i
            
        elif ( # If all ties, the description is the next tie breaker.
            entry.date == min_entry.date and
            entry.change == min_entry.change and
            entry.description < min_entry.description
        ):
            min_entry_index = i
    return min_entry_index

def format_currency(entry_change: int, locale: str, currency: str) -> str:
    """Formats the ledger currency according to the locale rules.

    Args:
        entry_change (int): The ledger entry's value, without separators (10.00 becomes 1000)
        locale (str): The locale whose formatting we should follow.
        currency (str): The name of the currency whose symbol we should apply to the ledger.

    Returns:
        str: Formatted part of the currency ready for adding to ledger.
    """
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
    if currency_list[0] == '.': # If we just have cents, we need to add the 0 before it!
        currency_list.insert(0, '0')
    currency_ledger = ''.join(currency_list)
    if entry_change < 0:
        if locale == 'en_US':
            currency_ledger = f'({currency_symbol}{currency_ledger})'
        elif locale == 'nl_NL':
            currency_ledger = f'{currency_symbol}-{currency_ledger} '
    else:
        currency_ledger = f'{currency_symbol}{currency_ledger}'
        currency_ledger += ' '
    currency_ledger = currency_ledger.rjust(13)
    return currency_ledger


def format_entry(entry: LedgerEntry, locale: str, currency: str) -> str:
    """Formats entry using auxiliary functions for every part of a Ledger Entry.

    Args:
        entry (LedgerEntry): The entry to be formatted.
        locale (str): The locale whose formatting rules the entry should follow.
        currency (str): The currency to be used in the entry formatting.

    Returns:
        str: The formatted entry to be added to the ledger.
    """
    return f'{format_date(locale, entry.date)}{format_description(entry.description)}{format_currency(entry.change, locale, currency)}'


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    """Main function that generates the entire ledger.

    Args:
        currency (str): Chosen currency for the entire ledger.
        locale (str): Chosen locale for the entire ledger.
        entries (list[LedgerEntry]): All entries that need to be added to the ledger.

    Returns:
        str: The ledger in a string format.
    """
    table = format_header(locale)
    if entries:
        sorted_entries = sorted(entries, key = lambda x: (x.date, x.change, x.description)) # You only need to sort once.
        formatted_entries = [format_entry(entry, locale, currency) for entry in sorted_entries]
        rest_of_table = '\n' + '\n'.join(formatted_entries)
    else:
        rest_of_table = ''
    return table + rest_of_table
