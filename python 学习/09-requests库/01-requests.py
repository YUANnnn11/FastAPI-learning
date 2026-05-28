
import requests

url = "http://httpbin.org"
parmas = {"user":"admin","password":"admin123"}
headers = {"User-Agent":"Python/3.13"}

# 发送get 请求（带参数+请求头）
res_get = requests.get(url=url+"/get",params=parmas,headers=headers)
print(res_get,type(res_get))

texl_html = res_get.text
print(f"[text]:{texl_html}")

res_headers = res_get.headers
print(f"[headers]:{res_headers}")

res_json = res_get.json()
print(f"[json]:{res_json}")

# post
res_post = requests.post(url=url+"/post",params=parmas,headers=headers)
print(res_post)
print(f"[post]:{res_post.status_code},{res_post.url}")

# delete
res_delete = requests.delete(url=url+"/delete",params=parmas,headers=headers)
print(res_delete)

# put
res_put = requests.put(url=url+"/put",params=parmas,headers=headers)
print(res_put)
