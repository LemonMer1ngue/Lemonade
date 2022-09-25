ihateu = "aiueoAIUEO"
twitter = input("")
for vowels in twitter:
    if (vowels in ihateu):
        twitter = twitter.replace(vowels, "")
print(twitter)  