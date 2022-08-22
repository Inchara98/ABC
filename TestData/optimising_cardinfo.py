import requests

from utilities.readProperties import ReadConfig


class API_Responses:

    @staticmethod
    def test_get_card_details():
        value_on_card = []
        info_on_card = []
        tooltip_on_card = []
        data = ReadConfig()
        api_url = data.getApplicationURL() + "api/metrics/getVanityMetrics/national/nishtha"
        response = requests.get(api_url)
        nishtha_cardinfo = response.json()

        for i in range(5):
            value_on_card.append(nishtha_cardinfo['result'][i]['value'])
            info_on_card.append(nishtha_cardinfo['result'][i]['name'])
            tooltip_on_card.append(nishtha_cardinfo['result'][i]['tooltip'])

        # print("Values in the Cards ", value_on_card)
        # print("Info in the cards ", info_on_card)
        # print("Tooltip in the cards ", tooltip_on_card)

        # to get first card values
        print(value_on_card[0], info_on_card[0], tooltip_on_card[0])
        return value_on_card, info_on_card, tooltip_on_card
