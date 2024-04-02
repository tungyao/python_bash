import urllib.request
import json
import os
url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf-8"))
image_url = data["images"][0]["url"]
image_filename = image_url.split("/")[-1]
image_url = "https://cn.bing.com" + image_url
save_dir = "./tmp"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
with open(os.path.join(save_dir, "everydata.jpg"), "wb") as f:
  f.write(urllib.request.urlopen(image_url).read())
print("图片已保存到", os.path.join(save_dir, "everydata.jpg"))
