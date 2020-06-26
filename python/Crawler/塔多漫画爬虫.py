from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import time

def Pic_save(path,url):
    respone = requests.get(url)
    with open(path,'wb') as f:
        f.write(respone.content)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def each(url,path_z,name):
    os.mkdir(path_z + name)
    path_s = path_z + name + '\\'
    
    url_pic = []
    
    browser = webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(3)

    html_each = requests.get(url)
    soup = BeautifulSoup(html_each.content,'lxml')

    pageNum_s = (soup.find('span',attrs={'class':'manga-page'})).get_text()
    # print(pageNum_s)
    pageNum_st = ''
    flag = 0
    for i in range(len(pageNum_s)):
        if is_number(pageNum_s[i]) == False:
            flag = 0
        if flag == 1:
            pageNum_st = pageNum_st + pageNum_s[i]
        if pageNum_s[i] == '/':
            flag = 1
    # print(pageNum_st)
    pageNum = int(pageNum_st)
    # print(pageNum)

    for i in range(pageNum):
        # print(i)
        if i + 1 < 10:
            pageNum_c = '000' + str(i + 1)
        else:
            pageNum_c = '00' + str(i + 1)
        page_url = url + '?page=' + str(i + 1)
        browser.get(page_url)
        browser.implicitly_wait(3)
        pic_url = browser.find_element_by_xpath("//div[@class='manga-box']/img").get_attribute('src')
        # print(pic_url)
        Pic_save(path_s + pageNum_c + '.jpg',pic_url)

    print(name + '保存完毕！')

    browser.quit()

def mulu(base_url,path_a):
    url_list = []
    name_list = []
    
    html = requests.get(base_url);
    soup = BeautifulSoup(html.content,'lxml')
    liTag = soup.find('div',attrs={'class':'chapter-list'})
    liTags = liTag.find_all('li')
    name_a = (soup.find('h1')).get_text()
    
    os.mkdir(path_a + name_a)
    path_z = path_a + name_a + '\\'
    
    i = 0
    for li in liTags:
        url_list.append("http://m.taduo.net" + li.find('a')['href'])
        name_list.append(li.find('a')['title'])
        i = i + 1
    
    print("各章节地址获取完成！共" + str(i) + "话")
    '''
    for j in range(i):
        # print(url_list[j])
        # print(name_list[j])
        each(url_list[j],path_z,name_list[j])
'''
    j = i - 1
    while j >= 0:
        each(url_list[j],path_z,name_list[j])
        print(j)
        j = j - 1
    
def main():
    base_url = str(input('请输入漫画首页地址： \n'))
    path_a = 'f:\\ACG\\Comic\\'
    mulu(base_url,path_a)

if __name__ == '__main__':
    main()
