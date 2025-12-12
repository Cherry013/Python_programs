
with open("Hello.txt","w") as f:
    String = input() # For 1 line
    f.write(String)

with open('Hello.txt', 'r') as file:
    print(file.read())

with open("Hello.txt","a") as f:
    st = "Just appending the content"
    f.write(f"\n{st}")

with open('Hello.txt', 'r') as file:
    print(file.read())

with open("Hello.txt","w+") as f:
    # This overwrites a file by clearing the previous content and writes the new content like 'w' Permission
    # This is Read+Write('r'+'w') == 'w+' Permission
    # Note:- This can create a new file if not exists
    f.write("\nJust adding new content using 'w+' Permission")
    f.seek(0) # This is used set cursor position
    print(f.read())

with open("Hello.txt","a+") as f:
    # This Permission Just add new or append the content to the file
    # Note:- This can create New file if not existed
    f.write("\nJust adding new line using 'a+' Permission")
    f.seek(0)
    print(f.read())

with open("Hello.txt","r+") as f:
    # This overwrites the previous content and writes the new content from the current cursor position
    # This is Read+Write('r'+'w') == 'r+' Permission
    # Note:- This will not create a new file
    f.seek(100)
    f.write("\nJust adding new content using 'r+' Permission\n")
    f.seek(0)
    print(f.read())

with open('Hello.txt', 'rb') as f:
    print(f.read())

# 'wb' Write binary it can create and overwrite files
# 'ab' Append Binary it can create files but not overwrite files

with open('Hello.txt','wb') as f:
    f.write(b"Hello, Just adding new content using 'wb' \r\nthis is 1st line \x00 \nThis is 2nd line")

with open('Hello.txt','ab') as f:
    f.write(b"Hello, Just adding new content using 'ab' \r\nthis is 1st line \x00 \nThis is 2nd line")