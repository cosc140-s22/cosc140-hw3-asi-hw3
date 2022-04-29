#######################################################
#Asianna Sample
# COSC 140 Homework 3: ghost
#
#######################################################
import sys 
def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

def main():
  words = load_wordlist()
  print(f"{len(words)} words loaded.")
  players = [1,2]
  list = len(players)
  wordlist = load_wordlist()
  for i in range(list):
    print ("Welcome to the game Player", players[i] ) 
  switch = True
  created_word =''
  while switch == True:
    player_loop = ['1','2']
    list = len(player_loop)
    for i in range(list):
      letter = input("Player "+(player_loop[i])+" Choose your letter:")
      created_word += letter
      created_word = created_word.upper() 
      print ("Current word combination:",created_word)
      counter = 0
      if len(created_word) > 1:
        for word in wordlist: 
          if created_word == word[0:len(created_word)]:
            if len(created_word) == 3:
              if created_word == word in wordlist:
                print('Player ' + (player_loop[i]) + ' "' +created_word+ '" is a three letter complete word, you lose.')
                switch = False
                sys.exit()
            
            if len(created_word) > 3:
              if created_word == word in wordlist:
                print('You have won! great job nerd 🧠')
                switch = False
                sys.exit()
          else:
            counter += 1 
            if counter == len(wordlist):
              print("The word you are creating is not a real word, sorry you're not a material gowrl👩🏼‍🎤")
              switch = False
              sys.exit()
          # if created_word[2:len(created_word)] != word[2:len(created_word)] in wordlist:
          #   switch = False
          #   print("this is not a real word")
#If the created word is equal to the beginning letters of a word in the dictionary 
 
#Check if those letter equal to a word, then if the first three equal a word then that player loses   
            #   switch = False
            # if created_word != word[0:len(created_word)]:
              
              # switch = False 
          # if created_word != word in wordlist[0:len(created_word)]: 
          #   print ('Player ' + (player_loop[i]) + ' "' +created_word+ '"" is not a real word, you lose.')
    
    #creation += letter
  #   if creation
    #while it is true as the player for their letter
    #Add on the letter to a string; check if the string is a real word?
    #Check if the string can be a word 
    #If the string is 4 letters long and a word the player loses 
    
    
    
    
    

    # you can start your code here, inside main
  
    
main()
