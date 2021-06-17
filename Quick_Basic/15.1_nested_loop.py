# nested loop

print("---------------------------------------")
myDict2 = {"python": ["python is fast language ", "python is much more readable", "python has easy syntax"], "JS": [
    "js is good for front end ", "js is also easy to understand ", "js having very easy syntax"]}

for category in myDict2:
    print("info abut ", category)
    for key in myDict2[category]:
        print(key)
