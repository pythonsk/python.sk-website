import os

from flask_frozen import Freezer
from views import app
from os.path import isfile, join

LANGUAGES = (
    {'lang_code': 'sk'},
    {'lang_code': 'en'}
)
freezer = Freezer(app)


@freezer.register_generator
def blog_image():
    dir_path = join(os.getcwd(), "blog", "images")

    for filename in os.listdir(dir_path):
        yield {'image_url': filename}


@freezer.register_generator
def blog_detail_page():
    blog_dir_path = join(os.getcwd(), "blog")

    for filename in os.listdir(blog_dir_path):
        if filename.endswith(".md"):
            print(filename.split(".")[0])
            yield {'article_url': filename.split(".")[0]}


if __name__ == '__main__':
    freezer.freeze()
