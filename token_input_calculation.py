#pip install coinbase
from coinbase.wallet.client import Client

def coin_spot_price(coin, currency):
    api_key = "organizations/1d87c8de-839b-4ef5-b73a-d6dca9bc9988/apiKeys/23fe4062-96b9-438c-b14f-e4b088fa8417"
    api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEINMjhjFpmI1H+BJ4Vrq51mwomQtiZuaVLOV9jrsmYA++oAoGCCqGSM49\nAwEHoUQDQgAE/erXjwh+7HVnEdL4RjHb3Au6iCORFxA3SqvJDG6EpDxFDEtqtUtr\nWxl2NmPUaFK10tuPb6gvodjDZswH5aJKBw==\n-----END EC PRIVATE KEY-----\n"
    client = Client(api_key, api_secret)
    coinPair = coin + "-" + currency
    priceData = client.get_spot_price(currency_pair = coinPair)
    return priceData #return Dict

if __name__ == "__main__":
    
    inputKRW = 5000000  
    
    KRW_USD = coin_spot_price("KRW","USD")
    USD_KRW = coin_spot_price("USD","KRW")
    USD = float(USD_KRW["amount"])
    
    convertARTC = inputKRW * float(KRW_USD["amount"]) * 10
    
    print(f"요청(KRW) : {inputKRW} KRW")
    print(f"달러 환율 : {USD:.0f} KRW")
    print(f"ARTC 변환 : {convertARTC:.0f} ARTC")
    
    