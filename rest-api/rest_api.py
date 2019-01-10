import json
import operator


class RestAPI(object):
    def __init__(self, database=None):
        if database:
            self.__users = database['users']
            self.__database = database.copy()

    def get(self, url, payload=None):
        if payload:
            users = json.loads(payload)
            user_names = set(users['users'])
            return json.dumps({'users':
                               [x for x in
                                sorted(self.__users,
                                       key=operator.itemgetter('name'))
                                if x['name'] in user_names]})

        return json.dumps({'users': self.__users})

    def post(self, url, payload=None):
        if not payload:
            return None

        if url == '/add':
            user_name = json.loads(payload)
            new_user = {
                'name': user_name['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0
            }

            self.__users.append(new_user)
            return json.dumps(new_user)
        elif url == '/iou':
            loan = json.loads(payload)
            lender = [i for i, j in enumerate(self.__users)
                      if j['name'] == loan['lender']][0]
            borrower = [i for i, j in enumerate(self.__users)
                        if j['name'] == loan['borrower']][0]

            self.__users[lender]['balance'] += loan['amount']
            self.__users[borrower]['balance'] -= loan['amount']

            # Add the records if they don't already exist.
            if loan['borrower'] not in self.__users[lender]['owed_by'].keys():
                self.__users[lender]['owed_by'].update({loan['borrower']: 0})
            if loan['lender'] not in self.__users[borrower]['owes'].keys():
                self.__users[borrower]['owes'].update({loan['lender']: 0})

            # Update the records with the borrowed amount.
            self.__users[lender]['owed_by'][loan['borrower']] += loan['amount']
            self.__users[borrower]['owes'][loan['lender']] += loan['amount']

            # If a previous borrower is making a loan to a lender,
            # consider it a repayment and update accordingly.
            if loan['lender'] in self.__users[borrower]['owed_by'].keys():
                self.__users[borrower]['owed_by'][loan['lender']] -= loan['amount']
                self.__users[lender]['owed_by'].pop(loan['borrower'])
                self.__users[lender]['owes'][loan['borrower']] -= loan['amount']
                self.__users[borrower]['owes'].pop(loan['lender'])

                # Remove record if a loan has been repaid.
                if self.__users[borrower]['owed_by'][loan['lender']] == 0:
                    self.__users[borrower]['owed_by'].pop(loan['lender'])
                elif self.__users[borrower]['owed_by'][loan['lender']] < 0:
                    (self.__users[lender]['owes']
                     .update({loan['borrower']: self.__users[borrower]['owed_by'][loan['lender']] * -1}))
                    self.__users[borrower]['owed_by'].pop(loan['lender'])

                if self.__users[lender]['owes'][loan['borrower']] == 0:
                    self.__users[lender]['owes'].pop(loan['borrower'])
                elif self.__users[lender]['owes'][loan['borrower']] < 0:
                    (self.__users[borrower]['owed_by']
                     .update({loan['lender']: self.__users[lender]['owes'][loan['borrower']] * -1}))
                    self.__users[lender]['owes'].pop(loan['borrower'])

            return json.dumps({'users':
                               [x for x in
                                sorted(self.__users,
                                       key=operator.itemgetter('name'))
                                if x['name'] == loan['lender'] or
                                x['name'] == loan['borrower']]})
