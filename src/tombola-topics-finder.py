from lxml import html
import requests
import re

page = requests.get('https://itunes.apple.com/se/podcast/tombola-podcast/id1095020110?l=en')
tree = html.fromstring(page.content)

episode_name = tree.xpath('//tr/@preview-title')

'''
saveFile = open("tombola-topics.txt", "w", encoding='utf-8')
for name in episode_name:
    saveFile.write(name + '\n')
saveFile.close()
'''

#episode_name = open("tombola-topics.txt", "r", encoding='utf-8').readlines()

topics = []
for name in episode_name:
    name = name[name.find(" "):].strip()
    if '(' in name:
       name = name[:name.find('(')]
    if '&' in name:
        #name = name[name.find(" "):].strip()
        split_str = [x.strip() for x in name.split('&')]
        for i in split_str:
            topics.append(i.lower())
    elif 'och' in name:
        #name = name[name.find(" "):].strip()
        split_str = [x.strip() for x in name.split('och')]
        for i in split_str:
            topics.append(i.lower())

    else:
        topics.append(name.lower())


def find_topic(str_to_find):
    print(f'\nTopics including "{str_to_find}":')
    for topic in topics:
        if str_to_find in topic:
            print(topic)
    print('\n')


def print_all_topics():
    for topic in topics:
        print(topic)
    print(f'Number of topics: {len(topics)} ')


def main():
    print('''
TOMBOLA TOPIC FINDER
Skriv "all_topics" för att visa alla ämnen.
Annars skriv ämnet du söker.
Använd bara små bokstäver i din sökning, annars kommer ämnet inte hittas.
Om inga ämnen dyker upp i din sökning betyder det att de ej finns.
Skriv "exit" för att avsluta programmet.
    ''')
    while(1):
        user_input = input("Skriv ett ämne/ord att söka efter (skriv 'exit' för att avsluta programmet): ").strip()
        if user_input == 'all_topics':
            print_all_topics()
        if user_input == 'exit':
            print("Exiting")
            exit()
        else:
            find_topic(user_input)

if __name__ == '__main__':
    main()
