from locust import HttpLocust, TaskSet



def index(l):
    file = open('urls.txt', 'r')
    urls = file.readlines()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    for url in urls:
        try:
            l.client.get(url.split('https://staging.metals4u.co.uk')[1].strip(),headers=headers)
            print(url.split('https://staging.metals4u.co.uk')[1].strip())
        except:
            continue



class UserBehavior(TaskSet):
    tasks = {index:    1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
