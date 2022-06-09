from copy import deepcopy
import json 


VALID_GETS = ['/users']
class RestAPI:
    def __init__(self, database: dict=None):
        new_database = {}
        if database:
            for entry in database['users']:
                new_entry = {user: entry['owes'][user] for user in entry.get('owes')}
                new_entry.update({user: -entry['owed_by'][user] for user in entry.get('owed_by')})
                new_database[entry['name']] = new_entry # The database is a dictionary whose keys are the names of the people in it.
        self.database = new_database

    def get(self, url: str, payload: dict=None):
        if url not in VALID_GETS:
             raise ValueError(f'Invalid request. GET only accepts the following requests: {VALID_GETS}.')
        if payload:
            payload = json.loads(payload)
            return json.dumps({'users': [self.parse_database_return(user) for user in payload['users']]})
        else:
            return json.dumps({'users': list(self.database)})
    
    def post(self, url: str, payload: str):
        payload = json.loads(payload)
        if url == '/add':
            return self.__add_user(payload)
        if url == '/iou':
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
        copy_user_entry = {
                        'name': user,
                        'balance': -sum(user_entry.values()),
                        'owed_by': {user: -amount for user, amount in user_entry.items() if amount < 0},
                        'owes': {user: amount for user, amount in user_entry.items() if amount > 0}
                        }
        return copy_user_entry 

    def __modify_user(self, user: str, other_guy: str, amount: float) -> dict:
        # This is a remodeling of the method I did, but this time assuming debt is a single dictionary. 
        user_data = self.database.get(user)
        user_data[other_guy] = user_data.get(other_guy, 0) + amount # We update the dictionary, adding the amount to the current debt.
        parsed_user_data = self.parse_database_return(user) # Parse this due to the expected output.
        return parsed_user_data