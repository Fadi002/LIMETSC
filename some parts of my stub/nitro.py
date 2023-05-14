import random , string , time , os
os.system('cls')
def pinkred(text):
    os.system(""); faded = ""
    blue = 255
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded
print(pinkred('''            ___     ___   __  __    ___    _  _            
    o O O  |   \   | __| |  \/  |  / _ \  | \| |     o O O 
   o       | |) |  | _|  | |\/| | | (_) | | .` |    o      
  TS__[O]  |___/   |___| |_|__|_|  \___/  |_|\_|   TS__[O] 
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======| 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000' \n\nfastest way to get tokens'''))



ilosc = input("How many tokens to generate : ")
ilosc = int(ilosc)
write = input("Do you want to write the tokens to a file? (y/n) : ")
tim =  input("How many seconds to wait between each token : ")
tim = int(tim)

if write == "y" or write == "Y":
    for i in range(ilosc):
        x = token = "OD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        with open("tokens.txt", "a") as f:
            f.write(x+"\n")
            print(x)
            time.sleep(tim)
else:
    for i in range(ilosc):
        x = token = "OD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        print(x)
        time.sleep(tim)
print("done gen")
os.system('cls')
print(pinkred('''            ___     ___   __  __    ___    _  _            
    o O O  |   \   | __| |  \/  |  / _ \  | \| |     o O O 
   o       | |) |  | _|  | |\/| | | (_) | | .` |    o      
  TS__[O]  |___/   |___| |_|__|_|  \___/  |_|\_|   TS__[O] 
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======| 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000' \n\ndone gen tokens'''))
input()

