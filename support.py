
p = {'crashed':'Are the drivers up to date?', 'blue':'Ah, the blue screen of death. And then what happened?', 'hacked':'You should consider installing anti-virus software.', 'bluetooth':'Have you tried mouthwash?', 'windows':'Ah, I think I see your problem. What version?', 'apple':'You do mean the computer kind?', 'spam':'You should see if your mail client can filter messages.', 'connection':'Contact Telkom.'}

    
def welcome():
        print('Welcome to the automated technical support system.')
        print('Please describe your problem:')
    
def get_input():
        return input().lower()
    
    
def main():
        welcome()
        query = get_input()
        while (not query =='quit'):
                if query == "crashed":
                        print(p['crashed'])
                elif query == "blue":
                        print(p['blue'])
                elif query == "hacked":
                        print(p['hacked'])
                elif query == "bluetooth":
                        print(p['bluetooth'])
                elif query == "windows":
                        print(p['windows'])
                elif query == "apple":
                        print(p['apple'])
                elif query == "spam":
                        print(p['spam'])
                elif query == "connection":
                        print(p['connection'])
                else:
                        print("Curious, tell me more.")
                query = get_input()
main()




