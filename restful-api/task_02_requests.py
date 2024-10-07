import requests
import csv


def fetch_and_print_posts():
    reponses = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(reponses.status_code))

    if reponses.status_code == 200:
        post = reponses.json()
        for index in post:
            print(index['title'])


def fetch_and_save_posts():
    reponses = requests.get("https://jsonplaceholder.typicode.com/posts")

    if reponses.status_code == 200:
        post = reponses.json()

        with open('posts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ['id', 'title', 'body']
            writer.writerow(fields)
            for index in post:
                writer.writerow([index['id'], index['title'], index['body']])
