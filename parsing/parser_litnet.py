import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://litnet.com/'
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response


def get_data(html):
    bs = BS4(html, 'html.parser')
    items = bs.find_all('div', class_='row book-item')
    litnet_list = []
    for item in items:

        title_tag = item.find('div', class_='bw-title-wr')
        title = title_tag.get_text(strip=True) if title_tag else "Название неизвестно"


        img_tag = item.find('div', class_='book-img transparent-marks')
        img_src = img_tag.find('img').get('src') if img_tag else None
        image = URL + img_src if img_src else "Нет изображения"

        litnet_list.append({
            'title': title,
            'image': image,
        })
    return litnet_list


def parsing():
    litnet_books = []
    try:
        for page in range(1, 3):
            response = get_html("https://litnet.com/ru/top/all", params={'page': page})
            litnet_books.extend(get_data(response.text))
        return litnet_books
    except Exception as e:
        print(f"Ошибка парсинга: {e}")
        return []


if __name__ == "__main__":
    books = parsing()
    for book in books:
        print(book)
