# examples/get_stocks_by_market_example.py

import amistock

def example_get_stocks_by_market():
    market = 'HOSE'  # Tên mã thị trường, ví dụ 'HOSE'
    api_key = 'your_api_key'  # Thay thế bằng API key hợp lệ
    stocks = amistock.get_stocks_by_market(market, api_key)
    print(stocks)

if __name__ == '__main__':
    example_get_stocks_by_market()
