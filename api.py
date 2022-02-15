import requests as req 
res = req.get('https://animechan.vercel.app/api/quotes/character?name=saitama')

print(res.status_code)
print(res.json())