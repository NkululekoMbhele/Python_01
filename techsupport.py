
p = {'crashed':'Are the drivers up to date?', 'blue':'Ah, the blue screen of death. And then what happened?', 'hacked':'You should consider installing anti-virus software.', 'bluetooth':'Have you tried mouthwash?', 'windows':'Ah, I think I see your problem. What version?', 'apple':'You do mean the computer kind?', 'spam':'You should see if your mail client can filter messages.', 'connection':'Contact Telkom.'}

    
def welcome():
        print('Welcome to the automated technical support system.')
        print('Please describe your problem:')
    
def get_input():
        return input().lower()
    
    
def main():
        welcome()
        value = get_input()
        while (not value =='quit'):
                l = value.split()
                if "crashed" in l:
                        print(p['crashed'])
                elif "blue" in l:
                        print(p['blue'])
                elif "hacked" in l:
                        print(p['hacked'])
                elif "bluetooth" in l:
                        print(p['bluetooth'])
                elif "windows" in l:
                        print(p['windows'])
                elif "apple" in l:
                        print(p['apple'])
                elif "spam" in l:
                        print(p['spam'])
                elif "connection" in l:
                        print(p['connection'])
                else:
                        print("Curious, tell me more.")              
                value = get_input()                                                 
                    
if __name__=='__main__':
        main()




