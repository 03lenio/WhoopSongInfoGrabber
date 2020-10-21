import glob
import os
import time

from mp3_tagger import MP3File


def search_for_song(filename):
    import mp3_tagger
    from selenium import webdriver
    webdriver = webdriver.Chrome()
    webdriver.get("https://genius.com/search?q=" + file_query[0])
    time.sleep(5)
    webdriver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
    correct = input("Is the displayed song correct? (Y/n) ")


    if correct == "Y":
        try:
            webdriver.find_element_by_xpath("/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div[2]/search-result-section/div/div[2]/search-result-items/div[1]/search-result-item/div/mini-song-card/a").click()

            song_name = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[3]/div/h1').text
            artist = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[3]/div/a').text
            try:
                if webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[1]/p').text == "Featuring":
                    featuring_artist = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[1]/a').text
                    song_name = song_name + " (feat. " + featuring_artist + ")"

                print(song_name + " by " + artist)
            except:
                print(song_name + " by " + artist)

            mp3 = MP3File("songs/" + filename[0] + ".mp3")
            mp3.song = song_name
            mp3.artist = artist
            mp3.save()

            print("Set tags!")
         

        except:
            time.sleep(3)
            song_name = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/h1').text
            artist = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/h2/span/a').text

            try:
                if webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/ng-transclude/metadata/h3[1]/expandable-list/div/span[1]').text == "Featuring":
                    featuring_artist = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/ng-transclude/metadata/h3[1]/expandable-list/div/span[2]/span/a').text
                    song_name = song_name + " (feat. " + featuring_artist + ")"

                print(song_name + " by " + artist)
            except:
                print(song_name + " by " + artist)

            mp3 = MP3File("songs/" + filename[0] + ".mp3")
            mp3.song = song_name
            mp3.artist = artist
            mp3.save()

            print("Set tags!")
         


    else:
        song_query_manual = input("Please enter your query: ")
        webdriver.get("https://genius.com/search?q=" + song_query_manual)
        time.sleep(5)
        webdriver.find_element_by_xpath("/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div[2]/search-result-section/div/div[2]/search-result-items/div[1]/search-result-item/div/mini-song-card/a").click()

        try:
            song_name = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[3]/div/h1').text
            artist = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[3]/div/a').text

            try:
                if webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[1]/p').text == "Featuring":
                    featuring_artist = webdriver.find_element_by_xpath('//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[1]/a').text
                    song_name = song_name + " (feat. " + featuring_artist + ")"

                print(song_name + " by " + artist)
            except:
                print(song_name + " by " + artist)

            mp3 = MP3File("songs/" + filename[0] + ".mp3")
            mp3.song = song_name
            mp3.artist = artist
            mp3.save()

            print("Set tags!")
         

        except:
            time.sleep(3)
            song_name = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/h1').text
            artist = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/h2/span/a').text
            
            
            try:
                try:
                    if webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/ng-transclude/metadata/h3[1]/expandable-list/div/span[1]').text == "Featuring":
                        featuring_artist = webdriver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/header-with-cover-art/div/div/div[1]/div[2]/div/ng-transclude/metadata/h3[1]/expandable-list/div/span[2]/span/a').text
                        song_name = song_name + " (feat. " + featuring_artist + ")"

                    print(song_name + " by " + artist)
                except:
                    print(song_name + " by " + artist)
                mp3 = MP3File("songs/" + filename[0] + ".mp3")
                mp3.song = song_name
                mp3.artist = artist
                mp3.save()

                print("Set tags!")
             


            except:
                print(song_name + " by " + artist)

                mp3 = MP3File("songs/" + filename[0] + ".mp3")
                mp3.song = song_name
                mp3.artist = artist
                mp3.save()

                print("Set tags!")
             


for file_path in glob.iglob(r'songs\*.mp3'):
    file_query = os.path.basename(file_path)
    print(file_query)
    file_query = file_query.split(".mp3")
    print(file_query[0])
    search_for_song(file_query)
