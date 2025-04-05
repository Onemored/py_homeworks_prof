import requests

# response = requests.get('https://speedtest.selectel.ru/10GB')
# with open('10GB', 'wb') as file:
#     file.write(response.content)


def download(url):
    filename = url.split('/')[-1]
    with requests.get(url, stream=True) as response:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

download('https://speedtest.selectel.ru/10GB')