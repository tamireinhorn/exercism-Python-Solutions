from copy import deepcopy
import json 


def _clean_url(url: str) -> str :
    return url.removeprefix('/')


VALID_GETS = ['users']
class RestAPI:
    def __init__(self, database: dict=None):
        new_database = {}
        if database:
            for entry in database['users']:
                new_entry = {}
                possible_users = set(entry.get('owes').keys()).union(set(entry.get('owed_by'))) # This gets all unique users in that entry!
                for user in possible_users:
                    user_amount = entry.get('owes').get(user, 0) - entry.get('owed_by').get(user, 0) # We aggregate the debt of that user in the entry in one dict.
                    new_entry[user] = user_amount # We redo the owes dictionary
                new_database[entry['name']] = new_entry # The database is a dictionary whose keys are the names of the people in it.
        self.database = new_database

    def get(self, url: str, payload: dict=None):
        clean_url = _clean_url(url)
        if clean_url not in VALID_GETS:
             raise ValueError(f'Invalid request. GET only accepts the following requests: {VALID_GETS}.')
        if payload:
            payload = json.loads(payload)
            return json.dumps({'users': [self.parse_database_return(user) for user in payload['users']]})
        else:
            return json.dumps({'users': list(self.database)})
    
    def post(self, url: str, payload: str):
        url = _clean_url(url)
        payload = json.loads(payload)
        if url == 'add':
            return self.__add_user(payload)
        if url == 'iou':
            return self.__add_iou(payload)
        raise ValueError('Incorrect request passed to API. Valid POST methods are add, iou.')

    def __add_user(self, payload: dict) -> str:
        new_user = payload['user']
        self.database[new_user] = {}
        return_new_user_entry = self.parse_database_return(new_user)
        return json.dumps(return_new_user_entry)
    
    def __add_iou(self, payload: dict) -> str:
        # For the lender, we have to do:
        lender, borrower, amount = payload['lender'], payload['borrower'], payload['amount']
        lender_entry = self.__modify_user(lender, borrower, -amount)
        borrower_entry = self.__modify_user(borrower, lender, amount)
        return json.dumps({'users': sorted([lender_entry, borrower_entry], key=lambda x: x['name'])}) # The expected return is ordered by the name of the users in the IOU.   

    def parse_database_return(self, user: str) -> dict: 
        # This method exists because the output expects two dicts, one of owes and other of owed_by
        user_entry = self.database.get(user)
        copy_user_entry = {'balance':-sum(user_entry.values())}
        copy_user_entry['owed_by'] = {user: -amount for user, amount in user_entry.items() if amount < 0} # Negative debt -> user is OWED BY, goes to new dict for output.
        copy_user_entry['owes'] = {user: amount for user, amount in user_entry.items() if amount > 0} # Positive debt in owes -> stays
        copy_user_entry['name'] = user
        return copy_user_entry 

    def __modify_user(self, user: str, other_guy: str, amount: float) -> dict:
        # This is a remodeling of the method I did, but this time assuming debt is a single dictionary. 
        user_data = self.database.get(user)
        user_data[other_guy] = user_data.get(other_guy, 0) + amount # We update the dictionary, adding the amount to the current debt.
        parsed_user_data = self.parse_database_return(user) # Parse this due to the expected output.
        return parsed_user_data