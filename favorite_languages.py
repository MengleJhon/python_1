#-*-coding:utf-8-*-
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print("\n" + name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())