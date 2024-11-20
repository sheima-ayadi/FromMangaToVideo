def chapter_links(url) -> dict:
    pass


def main():
    url=input("enter the url of the manga")
    print("url"+url)

    chapters= chapter_links(url)
    for chapter in chapters:
        print(chapter + ": " + chapters[chapter])
        y= input
