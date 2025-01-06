# examples/get_stock_data_example.py

import amistock

def example_get_stock_data():
    symbol = 'AAPL'  # Mã cổ phiếu bạn muốn lấy dữ liệu
    from_date = '2023-01-01'
    to_date = '2023-12-31'
    api_key = 'your_api_key'  # Thay thế bằng API key hợp lệ
    stock_data = amistock.get_stock_data(symbol, from_date, to_date, api_key)
    print(stock_data)

if __name__ == '__main__':
    example_get_stock_data()
