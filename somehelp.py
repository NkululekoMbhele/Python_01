#program that randomly select response
# Nkululeko Mbhele
# 07 April 2019


list = ["Have you tried it on a different operating system?", "Did you reboot it?", "What colour is it?", "You should consider installing anti-virus software.", "Contact Telkom.", "I should get that looked at if I were you."]

    
def welcome():
        print('Welcome to the automated technical support system.')
        print('Please describe your problem:')
    
def get_input():
        return input().lower()
    
    
def main():
        import random
        welcome()
        query = get_input()
        while (not query=='quit'):
                p = random.randint(0,5)
                print(list[p])
                query = get_input()    

if __name__=='__main__':
        main()





