import os

curl = """
curl "https://www.navily.com/region/next-page" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0" -H "Accept: */*" -H "Accept-Language: en-GB,en;q=0.5" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-CSRF-TOKEN: ajBIY2WZFVlSYxnvh11nVxQHbLBP8VQvTPNb87uz" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://www.navily.com" -H "Connection: keep-alive" -H "Referer: https://www.navily.com/region/sicily-anchorings-ports/317" -H "Cookie: XSRF-TOKEN=eyJpdiI6Ijc1bzRiekVnTU1Ma2Q2K2F3UkdQeEE9PSIsInZhbHVlIjoiT3E3djR6N0pqOFFubzJGRUI5OXNxdnl1akZQZ09YZU84aEJEbDBWZklvR1ZmZldsV2FnSkRhNHJYQmZsUmFJdSIsIm1hYyI6IjVjOTRjOTg0YWQ2ZGQ4OWUwMzRjMjY5N2MwMGM0YjA5OGE0ZjdiMTc2ZjIzYmFiZGIwYzgzNDUwOWEyMDE3NGYifQ"%"3D"%"3D; navily_webapp_session=eyJpdiI6Im4yZkFxNUdwQWdEMUxyODhpRk1aVXc9PSIsInZhbHVlIjoidks0Mldtd1wvZU5FaFoxTW1PdE1ISXFjcGx0N3dyanY1REJmSkVpcjZPXC9BaFB1QUlXbHZTSzBFXC9EOU1JRG1iRSIsIm1hYyI6IjRkMzNiMWZjNmU2MDNhNTBiZjNhZmRkMjk1YWM0NDBmYWE1OGFlYjI1ZTRiZDJiODVkNjc3OTg4MGY4NjMzZTEifQ"%"3D"%"3D; _ga=GA1.2.580859728.1577137865; _gid=GA1.2.46961634.1577137865; _fbp=fb.1.1577137865407.1944913650; CookieInfoScript=1; user_token=eyJpdiI6Ikg0dFQxQ0ZDUXhkMXFzOEExOEhBSVE9PSIsInZhbHVlIjoiZExZN0VZSEVrZUtYbVBvMVFFU095Zkd6OEg2Nk1TTkM2eE9RRTJlVE5lVnVnYVU4VXVqR2RnXC9OR05wQUx1cFwvZUduc3M3R09CQ2ZjdjJoYUJJSHBOVkFNdkx1MkFOTGVZNm1qb00yN2VqTT0iLCJtYWMiOiJkNTczYTY2MDc0NTE0NDI1YjFiZTNkODE3OTg2ZmJhY2Y3MzgxYmYxYWVmY2NkNWJmZTZmNzIyMmU4NDU1MTBiIn0"%"3D; crisp-client"%"2Fsession"%"2F0b8ed04d-fef2-4d38-94d9-1f27d5525ef1=session_d131ce75-5bb9-4900-acaa-2c2575b9ac29; crisp-client"%"2Fsession"%"2F0b8ed04d-fef2-4d38-94d9-1f27d5525ef1=session_55cc2549-9814-40cb-b5f5-cf4c2673b551" --data "id=317&pageNumber=1&filter=port"        
""" 

print (curl)

os.system(curl + " > out.txt")