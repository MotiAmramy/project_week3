import requests




def get_api_players(year):
    response = requests.request("GET", f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=10")
    return response.json()

