import random

 words = ["python", "java", "javascript", "hangman", "programming", "computer"]

 word = random.choice(words).lower()
guessed = "_" * len(word)
guessed = list(guessed)
word_letters = set(word)

 used_letters = set()
tries = 6  

print("🎮 Welcome to Hangman!")
print("Guess the word:")

while tries > 0 and set(guessed) != word_letters:
    print("\nWord: ", " ".join(guessed))
    print(f"Used letters: {', '.join(used_letters)}")
    print(f"Remaining tries: {tries}")

    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("⚠️ You already used that letter.")
        continue

    if guess in word_letters:
        print("✅ Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        used_letters.add(guess)
    else:
        print("❌ Wrong guess.")
        used_letters.add(guess)
        tries -= 1
 
if "".join(guessed) == word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
