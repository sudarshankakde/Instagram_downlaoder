import instaloader
from instaloader import Post as Ps

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# bot.login(user="Your_username",passwd="Your_password") #Use this code to log-in to your account.


def getBasicInfo():
    profileid = input('Enter the userid of the profile:\n')
    # Loading the profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, profileid)
    print("\nUsername: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    print("Bio: ", profile.biography)
    print("External URL: ", profile.external_url)
    print('\n')


def searchInformation():
    searchitem = input('Enter the search keyword:\n')
    # Provide the search query here
    search_results = instaloader.TopSearchResults(bot.context, searchitem)
    print('\n')
    # Iterating over the extracted usernames
    for username in search_results.get_profiles():
        print(username)

    print('\n')
    # Iterating over the extracted hashtags
    for hashtag in search_results.get_hashtags():
        print(hashtag)

    print('\n')


def downloadPost():
    useerid = input('Enter the userid of the profile:\n')
    # Loading a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, useerid)

    # Retrieving all posts in an object
    posts = profile.get_posts()
    count = 0
    # Iterating and downloading all the individual posts
    for index, post in enumerate(posts, 1):
        if count < 5:
            bot.download_post(
                post, target=f"{profile.username}_{index}")
            count += 1
        else:
            break


def downloadUrlPost():

    url = str(input("Enter Post Url:\n"))

    shorted_url = url[28:len(url)-1]

    post = Ps.from_shortcode(bot.context, shorted_url)

    bot.download_post(
        post, target="Instagram_downloader")


if __name__ == '__main__':
    option = '0'
    while option != '5':
        option = input(
            'Select YOur option\n1)Get Profile Info\n2)Download Post By Url\n3)Search For Top profiles and Hastags\n4)Download Profile Posts\n5)Exit\n')
        if option == '1':
            getBasicInfo()
        elif option == '2':
            downloadUrlPost()
        elif option == '3':
            searchInformation()
        elif option == '4':
            downloadPost()
        elif option == '5':
            exit
        else:
            print('Wrong Input Please Try Again\n')
