# examples/get_stock_info_example.py

import amistock

def example_get_stock_info():
    symbol = 'AAPL'  # Tên mã cổ phiếu bạn muốn lấy thông tin
    api_key = 'your_api_key'  # Thay thế bằng API key hợp lệ
    stock_info = amistock.get_stock_info(symbol, api_key)
    print(stock_info)

if __name__ == '__main__':
    example_get_stock_info()
