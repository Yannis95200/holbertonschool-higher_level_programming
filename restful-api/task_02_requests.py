#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    responses = requests.get(url)
    print("Status Code: {}".format(responses.status_code))

    if responses.status_code == 200:
        post = responses.json()
        for index in post:
            print(index['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    responses = requests.get(url)

    if responses.status_code == 200:
        post = responses.json()

        with open('posts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ['id', 'title', 'body']
            writer.writerow(fields)
            for index_2 in post:
                writer.writerow([index_2['id'], index_2['title'],
                                 index_2['body']])
