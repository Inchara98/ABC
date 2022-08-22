import requests

from utilities.readProperties import ReadConfig

data = ReadConfig()

api_url = data.getApplicationURL()+"api/metrics/getVanityMetrics/national/nishtha"
response = requests.get(api_url)
nishtha_cardinfo = response.json()

#   Total state/UT's Participating
total_state_count = nishtha_cardinfo['result'][0]['value']
state_info = nishtha_cardinfo['result'][0]['name']
state_tooltip = nishtha_cardinfo['result'][0]['tooltip']

# Total Enrollment
total_enrollment_count = nishtha_cardinfo['result'][1]['value']
enrollment_info = nishtha_cardinfo['result'][1]['name']
enrollment_tooltip = nishtha_cardinfo['result'][1]['tooltip']

# Total Completion
total_completion_count = nishtha_cardinfo['result'][2]['value']
completion_info = nishtha_cardinfo['result'][2]['name']
completion_tooltip = nishtha_cardinfo['result'][2]['tooltip']

# Total Certification's
total_certification_count = nishtha_cardinfo['result'][3]['value']
certification_info = nishtha_cardinfo['result'][3]['name']
certification_tooltip = nishtha_cardinfo['result'][3]['tooltip']

# Total Mediums
total_medium_count = nishtha_cardinfo['result'][4]['value']
medium_info = nishtha_cardinfo['result'][4]['name']
medium_tooltip = nishtha_cardinfo['result'][4]['tooltip']

print("State Card Details : ", total_state_count, " ", state_info, ' ', state_tooltip)
print("Enrollment Card Details : ", total_enrollment_count, " ", enrollment_info, ' ', enrollment_tooltip)
print("Completion Card Details : ", total_certification_count, " ", completion_info, ' ', completion_tooltip)
print("Certification Card Details : ", total_certification_count, " ", certification_info, ' ', certification_tooltip)
print("Medium Card Details : ", total_medium_count, " ", medium_info, ' ', medium_tooltip)
