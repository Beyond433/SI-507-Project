import csv

from selenium.webdriver import Chrome, ActionChains
import time
from selenium.webdriver.chrome.options import Options


opt=Options()
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")
driver = Chrome(options=opt)
url = 'https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc'

# header = ["POS","GP","MIN","PTS","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","REB","AST","STL","BLK","TO","DD2","TD3","PER"]
# f=open("nba.csv",mode="w",newline="")
# csvwriter_1=csv.writer(f)
# csvwriter_1.writerow(header)

f=open("nba_name.csv",mode="w",newline="")
csvwriter_2=csv.writer(f)


def scrolldown(driver,begin,step,times):
    scroll_y = begin
    for i in range(times):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,{})".format(scroll_y))
        scroll_y += step


def main():
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn=driver.find_element("xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a')
    show_more_btn.click()
    time.sleep(2)
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn = driver.find_element ( "xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a')
    show_more_btn.click ()

    time.sleep ( 2 )
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn = driver.find_element ( "xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a' )
    show_more_btn.click ()

    time.sleep ( 2 )
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn = driver.find_element ( "xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a' )
    show_more_btn.click ()

    time.sleep ( 2 )
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn = driver.find_element ( "xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a' )
    show_more_btn.click ()

    time.sleep ( 2 )
    scrolldown ( driver, 1000, 600, 2 )
    show_more_btn = driver.find_element ( "xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a' )
    show_more_btn.click ()

    names=[]
    names=get_name(driver,names,csvwriter_2)#得到人名的数组

    # get_other_info(driver,csvwriter_1)



def get_name(driver,names,csvwriter_2):
    tbody=driver.find_element("xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div/div/table/tbody')
    trs=tbody.find_elements("xpath",'./tr')
    for tr in trs:
        name=tr.find_element("xpath",'./td/div/a').text
        print(name)
        csvwriter_2.writerow([name])

        names.append(name)
    return names

def get_other_info(driver,csvwriter_1):
    tbody=driver.find_element("xpath",'//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div/div/div/div[2]/table/tbody')
    trs=tbody.find_elements("xpath",'./tr')
    i=0
    for tr in trs:
        POS=tr.find_element("xpath",'./td[1]/div').text
        GP=tr.find_element("xpath",'./td[2]').text
        MIN=tr.find_element("xpath",'./td[3]').text
        PTS=tr.find_element("xpath",'./td[4]').text
        FGM=tr.find_element("xpath",'./td[5]').text
        FGA=tr.find_element("xpath",'./td[6]').text
        FG=tr.find_element("xpath",'./td[7]').text
        threePM=tr.find_element("xpath",'./td[8]').text
        threePA=tr.find_element("xpath",'./td[9]').text
        threeP=tr.find_element("xpath",'./td[10]').text
        FTM=tr.find_element("xpath",'./td[11]').text
        FTA=tr.find_element("xpath",'./td[12]').text
        FT=tr.find_element("xpath",'./td[13]').text
        REB=tr.find_element("xpath",'./td[14]').text
        AST=tr.find_element("xpath",'./td[15]').text
        STL=tr.find_element("xpath",'./td[16]').text
        BLK=tr.find_element("xpath",'./td[17]').text
        TO=tr.find_element("xpath",'./td[18]').text
        DD_two=tr.find_element("xpath",'./td[19]').text
        TD_three=tr.find_element("xpath",'./td[20]').text
        PER=tr.find_element("xpath",'./td[21]').text
        i=i+1
        print(i,POS)
        csvwriter_1.writerow ( [POS,GP,MIN,PTS,FGM,FGA,FG,threePM,threePA,threeP,FTM,FTA,FT,REB,AST,STL,BLK,TO,DD_two,TD_three,PER] )

if __name__ == "__main__":
    main()