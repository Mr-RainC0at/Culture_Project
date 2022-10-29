import datetime
import os
import random
import time
from itertools import dropwhile, takewhile
import instaloader
import tkinter
from PIL import ImageTk, Image
from culture_class import *


# 인스타그램에서 포스트 스크래핑하기
def download_posts(username, save_image, days):
    for f in os.listdir(username):
        os.remove(os.path.join(username, f))

    class MyRateController(instaloader.RateController):
        def sleep(self, secs: 30):
            wait_time = random.uniform(30, 90)
            print(str(wait_time) + " seconds")
            time.sleep(wait_time)

        def count_per_sliding_window(self, query_type):
            return 20

    L = instaloader.Instaloader(rate_controller=lambda ctx: MyRateController(ctx),
                                download_videos=False, save_metadata=False, download_pictures=save_image,
                                max_connection_attempts=1)
    # L.login("no_bug_zone_", "nobugzone123")
    posts = instaloader.Profile.from_username(L.context, username).get_posts()

    SINCE = datetime.datetime.now()
    UNTIL = datetime.datetime.now() - datetime.timedelta(days=int(days))
    for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
        time.sleep(random.uniform(10, 40))
        L.download_post(post, username)


def image_preview(path):
    root = tkinter.Tk()  # Start window
    root.title("Instagram Image")  # Modify this to change the title
    rawimg = Image.open(path)  # Open image path

    rawimg = rawimg.resize(int(0.5 * s) for s in rawimg.size)

    img = ImageTk.PhotoImage(rawimg)  # Adapt the image to tkinter
    panel = tkinter.Label(root, image=img)  # Add image to the window
    panel.pack()  # Build window
    root.mainloop()


def print_data_instagram(username):
    for filename in os.listdir(username):
        path = username + '/' + filename
        if os.path.isfile(os.path.join(username, filename)) and os.path.splitext(filename)[-1].lower() == '.txt':
            with open(path, encoding='utf-8') as f:
                caption = f.read().replace('\n\n\n\n', '\n\n\n')
                print(caption)
                print("-" * 88)
        elif os.path.isfile(os.path.join(username, filename)) and os.path.splitext(filename)[-1].lower() == '.jpg':
            image_preview(path)


def instagram_extract(li):
    for i, x in enumerate(li):
        CultureClasses.append(CultureClass(x[1] + str(i), x))


def main():
    # download_posts('popupstorego', False, 14)
    # print_data_instagram('popupstorego')

    # download_posts('pops.official_', False, 14)
    # print_data_instagram('pops.official_')

    # download_posts('popuperspace', False, 14)
    # print_data_instagram('popuperspace')
    pass


if __name__ == '__main__':
    main()
