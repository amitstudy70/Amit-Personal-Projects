from plyer import notification
import pandas as pd
import random
import os.path
import requests as re

path = "random_gre_vocab.csv"
check_file = os.path.isfile(path)
# print(check_file)

if check_file:
    df = pd.read_csv(path)
    df = pd.DataFrame(df)
    list1 = df.values.tolist()
    i = random.randint(0, len(list1) - 1)
    # i here is randomly chosen to as the list index and then the components of the lsot are displayed as a notification

    notification.notify(title=str(list1[i][1]), message=str(list1[i][2]), timeout=0)
else:
    # read the table from the url
    html_content = pd.read_html("https://www.graduateshotline.com/gre-word-list.html")
    html_content2 = pd.read_html(
        "https://www.graduateshotline.com/gre-word-list.html#x2"
    )
    html_content3 = pd.read_html(
        "https://www.graduateshotline.com/gre-word-list.html#x3"
    )
    html_content4 = pd.read_html(
        "https://www.graduateshotline.com/gre-word-list.html#x4"
    )
    html_content5 = pd.read_html(
        "https://www.graduateshotline.com/gre-word-list.html#x5"
    )

    # print(html_content)

    df1 = pd.DataFrame(html_content[0])
    df2 = pd.DataFrame(html_content2[0])
    df3 = pd.DataFrame(html_content2[0])
    df4 = pd.DataFrame(html_content2[0])
    df5 = pd.DataFrame(html_content2[0])
    words_and_meanings = pd.concat((df1, df2, df3, df4, df5))

    # print(f"\n\n\n\n\n\n\n\n {words_and_meanings}")
    list1 = []  # initialise an empty list
    list1 = (
        words_and_meanings.values.tolist()
    )  # a 2d list of words and meanings is created the [[words,meanings]]
    # print(list1)

    csv1 = pd.DataFrame(list1)
    csv1.to_csv("random_gre_vocab.csv")

    i = random.randint(0, len(list1) - 1)
    # i here is randomly chosen to as the list index and then the components of the lsot are displayed as a notification

    notification.notify(title=str(list1[i][0]), message=str(list1[i][1]), timeout=0)

    # * AUTOMATED THE TASK USING THE TASK SCHEDULER
