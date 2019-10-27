import requests
import os

alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
default_url = "https://github.githubassets.com/images/icons/emoji/unicode/1f3"
emoji_count = 0

"""
    
    Format 1 : 1f3<alphabet><hex>.png
    Github sets unicode for the emoji name, which begins from "1f3" followed by alphabet letter and hex value.
    and ends with extension .png
   
    
        Example: 1f3a0.png
                 1f3a1.png
                 1f3a2.png
                 .... 1f3a9...
                 for first set of emoji
        Then for second set , we have alphabet b,
        So we get : 1f3b0.png
                    1f3b1.png
                    1f3b2.png
                ......so on until f alphabet and hex 9
                i.e. 1f3f9.png
                
"""


def get_first_pack_emoji():
    global emoji_count
    for letter in alphabets:
        for i in range(0, 10):
            file_name = letter + str(i) + ".png"
            final_url = default_url+file_name
            try:
                req = requests.get(str(final_url))
                with open("first_pack/"+file_name, "wb") as f:
                    f.write(req.content)
                    emoji_count = emoji_count + 1
                    print("Writing emoji in first_pack...("+str(emoji_count)+")")
            except Exception as e:
                print(e+" [x] Emoji link borken")


"""    
    Format 2 : 1f3<hex><alphabet>.png
    Github sets another lists of emoji which name also beings with 1f3 followed by hex number and alphabet letter and 
    ends with .png extension
    
        Example: 1f31a.png
                 1f31b.png
                 1f31c.png
                 .........so on until hex 9 and alphabet f
                 i.e. 1f39f.png
                 
"""


def get_second_pack_emoji():
    global emoji_count
    for i in range(0, 10):
        for letter in alphabets:
            file_name = str(i) + letter + ".png"
            final_url = default_url+file_name
            try:
                req = requests.get(str(final_url))
                with open("second_pack/"+file_name, "wb") as f:
                    f.write(req.content)
                    emoji_count = emoji_count + 1
                    print("Writing emoji in second_pack...("+str(emoji_count)+")")
            except:
                print("[x] Emoji link borken")

"""
    Format 3: 1f3<number><number>.png
"""


def get_third_pack_emoji():
    global emoji_count
    for i in range(0, 10):
        for j in range(0, 10):
            file_name = str(i) + str(j) + ".png"
            final_url = default_url + file_name
            try:
                req = requests.get(str(final_url))
                with open("third_pack/" + file_name, "wb") as f:
                    f.write(req.content)
                    emoji_count = emoji_count + 1
                    print("Writing emoji in third_pack...(" +str(emoji_count)+ ")")
            except:
                print("[x] Emoji link borken")

"""
    Format 4 : 1f3<letter><letter>.png
"""


def get_fourth_pack_emoji():
    global emoji_count
    for i in alphabets:
        for j in alphabets:
            file_name = i + j + ".png"
            final_url = default_url + file_name
            try:
                req = requests.get(str(final_url))
                with open("fourth_pack/" + file_name, "wb") as f:
                    f.write(req.content)
                    emoji_count = emoji_count + 1
                    print("Writing emoji in fourth_pack...(" +str(emoji_count)+ ")")
            except:
                print("[x] Emoji link broken")


def make_dir():
    try:
        if not os._exists("first_pack"):
            os.mkdir("first_pack")
            print("first_pack folder created...")

        if not os._exists("second_pack"):
            os.mkdir("second_pack")
            print("second_pack folder created...")

        if not os._exists("third_pack"):
            os.mkdir("third_pack")
            print("third_pack folder created...")

        if not os._exists("fourth_pack"):
            os.mkdir("fourth_pack")
            print("fourth_pack folder created...")

    except FileExistsError:
        print("Folder already exists...")


make_dir()

get_first_pack_emoji()
get_second_pack_emoji()
get_third_pack_emoji()
get_fourth_pack_emoji()


