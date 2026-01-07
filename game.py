import time
import random

sentences = [
    "Python makes coding fun and powerful.",
    "Artificial intelligence is changing the world.",
    "Typing fast requires practice and focus.",
    "Code is like poetry written for machines.",
    "Debugging is twice as hard as writing code."
]

sentence = random.choice(sentences)

print("\n🔥 TYPING SPEED TEST 🔥")
print("Type the following sentence exactly:\n")
print(f'"{sentence}"\n')

input("Press ENTER when you're ready...")

start_time = time.time()
user_input = input("\nStart typing:\n")
end_time = time.time()

time_taken = end_time - start_time
words = len(sentence.split())
wpm = (words / time_taken) * 60

# Accuracy calculation
correct_chars = sum(1 for a, b in zip(sentence, user_input) if a == b)
accuracy = (correct_chars / len(sentence)) * 100

print("\n📊 RESULTS")
print(f"⏱ Time Taken: {time_taken:.2f} seconds")
print(f"⚡ Speed: {wpm:.2f} WPM")
print(f"🎯 Accuracy: {accuracy:.2f}%")

if accuracy > 90:
    print("🔥 Excellent typing!")
elif accuracy > 70:
    print("👍 Good job, keep practicing!")
else:
    print("💪 Practice makes perfect!")
