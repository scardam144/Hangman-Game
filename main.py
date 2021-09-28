# The Hangman game
import random
import stages_seen
import words
from replit import clear
print(stages_seen.logo)

random_word = list(random.choice(words.game_words))
final_word = ['_']*len(random_word)
end_of_game = False
live = 6
while not end_of_game and live >= 0:
    temp = 0
    guess_word = input("Guess a letter:").lower()
    clear()
    for i in range(0, len(random_word)):
        if random_word[i] == guess_word:
            final_word[i] = guess_word
            temp = 1
    print(final_word)

    if temp == 0:
        print(f"you choose a letter {guess_word}, its not in a word, you loose a life.")
        print(stages_seen.stages[live])
        live -= 1
    if '_' not in final_word:
        end_of_game = True
        print("You Won.")
    elif live == -1 and '_' in final_word:
        print("You Loose.")

