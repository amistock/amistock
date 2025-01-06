# examples/get_key_info_example.py

import amistock

def example_get_key_info():
    api_key = 'your_api_key'  # Thay thế bằng API key hợp lệ
    stocks = amistock.get_key_info(api_key)
    print(stocks)

if __name__ == '__main__':
    example_get_key_info()
