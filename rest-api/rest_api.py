from copy import copy
import json 
from operator import itemgetter

def _clean_url(url: str) -> str :
    return url.removeprefix('/')

def get_keys(dict: dict):
    return list(map(itemgetter(0), dict.items()))


class RestAPI:
    def __init__(self, database: dict =None):
        database_copy = copy(database)
        if database_copy:
            for entry in database_copy['users']:
                possible_users = set(get_keys(entry.get('owes')) + get_keys(entry.get('owed_by'))) # This gets all unique users in that entry!
                for user in possible_users:
                    user_amount = entry.get('owes').get(user, 0) - entry.get('owed_by').get(user, 0) # We aggregate the debt of that user in the entry in one dict.
                    entry['owes'][user] = user_amount # We redo the owes dictionary
                    del entry['owed_by'] # We remove the unnecessary dictionary.
        self.valid_gets = ['users']
        self.database = database_copy 

    def get(self, url: str, payload: str = None):
        clean_url = _clean_url(url)
        if clean_url not in self.valid_gets:
             raise ValueError(f'Invalid request. GET only accepts the following requests: {self.valid_gets}.')
        if payload:
            payload = json.loads(payload)
            return json.dumps({'users': [self.__get_user(user) for user in payload['users']]})
        else:
            return json.dumps(self.database)
    
    def post(self, url: str, payload: str =None):
        url = _clean_url(url)
        if not payload:
            raise ValueError('Incorrect request. A POST method requires a payload.')
        payload = json.loads(payload)
        if url == 'add':
            return self.__add_user(payload)
        if url == 'iou':
            return self.__add_iou(payload)
        raise ValueError('Incorrect request passed to API. Valid POST methods are add, iou.')
            
    def __get_user(self, user_name: str) -> str:
        return [user for user in self.database['users'] if user['name'] == user_name][0]

    def __add_user(self, payload: str) -> str:
        users_list = self.database['users']
        new_user = payload['user']
        new_user_entry = {'name': new_user , 'owes': {}, 'balance': 0.0}
        return_new_user_entry = copy(new_user_entry)
        return_new_user_entry['owed_by'] = {}
        users_list.append(new_user_entry)
        return json.dumps(return_new_user_entry)
    
    def __add_iou(self, payload: str) -> str:
        # For the lender, we have to do:
        lender = payload['lender']
        borrower = payload['borrower']
        amount = payload['amount']
        lender_entry = self.__modify_user(lender, borrower, -amount)
        borrower_entry = self.__modify_user(borrower, lender, amount)
        
        return json.dumps({'users': sorted([lender_entry, borrower_entry], key = lambda x: x['name'])}) # The expected return is ordered by the name of the users in the IOU.   

    def parse_database_return(self, user: str) -> dict: 
        # This method exists because the output expects two dicts, one of owes and other of owed_by
        copy_user_entry = copy(self.__get_user(user))
        copy_user_entry['owed_by'] = {user: -amount for user, amount in copy_user_entry['owes'].items() if amount < 0} # Negative debt -> user is OWED BY, goes to new dict for output.
        copy_user_entry['owes'] = {user: amount for user, amount in copy_user_entry['owes'].items() if amount > 0} # Positive debt in owes -> stays
        return copy_user_entry 


    def __modify_user(self, lender: str, borrower: str, amount: float) -> dict:
        # This is a remodeling of the method I did, but this time assuming debt is a single dictionary.
        user = lender 
        other_guy = borrower 
        user_data = self.__get_user(user)
        user_data['balance'] -= amount # A new loan will always decrease your balance, either decreasing borrower by amount or decreasing lender by -amount (which is a net increase)
        current_debt = user_data['owes'].get(other_guy, 0) # The current debt is how much the user is owed by other guy
        total = current_debt + amount # We add the amount, regardless
        user_data['owes'][other_guy] = total # We update the dictionary
        parsed_user_data = self.parse_database_return(user) # Parse this due to the expected output.
        return parsed_user_data