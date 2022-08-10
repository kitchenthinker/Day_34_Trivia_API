import requests


class TriviaApi:

    def __init__(self):
        self.API = "https://opentdb.com/api.php"
        self.params = {"amount": 10, "type": "boolean"}

    def set_params(self, number_of_question: str = 10):
        if self.params['amount'] != number_of_question:
            self.params = {
                "amount": number_of_question,
                "type": "boolean",
            }

    def get_questions_data(self):
        try:
            response = requests.get(url=self.API, params=self.params)
        except:
            return None
        else:
            return response.json()['results']
