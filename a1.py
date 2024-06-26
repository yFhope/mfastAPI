import requests

url = "https://www.y2mate.com/mates/analyzeV2/ajax"

payload = "k_query=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DNyVSJbDjXm0&k_page=home&hl=en&q_auto=1"
headers = {
  'accept': '*/*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.y2mate.com',
  'referer': 'https://www.y2mate.com/youtube/NyVSJbDjXm0',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
