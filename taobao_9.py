import time
import re
import urlname
from selenium import webdriver

# 等待浏览器加载数据的包
from selenium.webdriver.support.ui import WebDriverWait
time.sleep(3)

#
#
url_taobao='https://www.taobao.com'
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=http://121.226.3.109:4256')
chrome_options.add_argument(f'--window-position={217},{172}')
chrome_options.add_argument(f'--window-size={1200},{1000}')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#browser = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
browser = webdriver.Chrome(executable_path='/Applications/Google Chrome.app/Contents/MacOS/chromedriver')
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",})

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",})
wait = WebDriverWait(browser, 10)
browser.maximize_window()
    # 编写函数--类方法，函数有爬取数据的功能

#下拉页面函数
def down_page():
    for x in range(1, 11, 2):
        time.sleep(10)
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        browser.execute_script(js)
    time.sleep(10)


#登录界面及输入账号密码函数
def login_func(name_key):
    # 打开淘宝网首页,输入关键词
    browser.get(url_taobao)
    input_div = browser.find_element_by_id("q")
    input_div.send_keys(name_key)
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(5)
    if browser.find_element_by_xpath('//*[@id="fm-login-id"]'):
        user = browser.find_element_by_xpath('//*[@id="fm-login-id"]')
        user.send_keys(f'{user_name}')
        time.sleep(5)
    if browser.find_element_by_xpath('//*[@id="fm-login-password"]'):
        password= browser.find_element_by_xpath('//*[@id="fm-login-password"]')
        password.send_keys(f'{user_pass}')
    time.sleep(3)
    submit = browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button')
    submit.click()
    time.sleep(15)




    #将带有关键字的信息直接url方式get请求进行数据页面提取

def get_href():
    tbcc = browser.find_element_by_css_selector('tbcc').get_attribute('id')
    tbccimg = tbcc + '-imglink'
    tbccimg = tbccimg.replace('tbcc-c-', '')
    img = browser.find_elements_by_class_name(tbccimg)
    listurl = []
    for i in img:
        if i.get_attribute('title') == name_1:
            listurl.append(i.get_attribute('href'))
        else:
            pass
    return listurl
# 获取 符合条件的url链接
def get_data():
    time.sleep(25)
    #根据关键词+发货地+最高最低价格+排序规则等组成的url 进入链接
    browser.get(url)
    time.sleep(10)
    down_page()
    token = browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('(\d+)').search(token).group(1))
    if token == 1:
        list_no=get_href()
    elif token ==2 :
        list1=get_href()
        test = browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[8]/a')
        browser.execute_script("arguments[0].click();", test)
        down_page()
        list2=get_href()
        list_no=set(list1+list2)
    else:
        list1=get_href()
        test=browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[8]/a')
        browser.execute_script("arguments[0].click();", test)
        down_page()
        list2=get_href()
        test=browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[8]/a')
        browser.execute_script("arguments[0].click();", test)
        down_page()
        list3=get_href()
        list_no=set(list1+list2+list3)
        list_no=list(list_no)
    return list_no

#访问广告链接
def get_listurl(listurl_no):
    for j in listurl_no:
        browser.get(j)
        # 下拉页面
        down_page()
        time.sleep(10)
        browser.back()
        time.sleep(10)

def get_sousuo(xiao=0,city=0,price_min=0,price_max=0,pric_sort=0):
    '''
    xiao:0 不按照销售量排序，1 按照销售量排序
    city：0 不按照发货地，其余按照发货地（后期加入选择标签1- +&&）

    '''
    browser.find_element_by_id("q").clear()
    input_div = browser.find_element_by_id("q")
    input_div.send_keys(f'{name_2}')
    browser.find_element_by_xpath('//*[@id="J_SearchForm"]/button').click()
    #销量排序
    if xiao == 1:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[2]/a').click()
        time.sleep(5)
    else:
        pass
    #价格输入--最低--最高
    if price_max != 0 or price_min != 0:
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/div[1]/div[1]/div/ul/li[1]/input').send_keys(f'{price_min}')
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/div[1]/div[1]/div/ul/li[3]/input').send_keys(f'{price_max}')
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/div[1]/div[1]/div/ul/li[4]/button').click()
        time.sleep(5)
    else:
        pass

    #价格排序
    '''
    0：默认
    1：价格从低到高
    2：价格从高到低
    3：总价从低到高
    4：总价从高到低
    '''
    if pric_sort == 1:
        pass
    elif pric_sort==1:
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[4]/ul/li[1]/a').click()

    elif pric_sort == 2:
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[4]/ul/li[2]/a').click()
    elif pric_sort == 3:
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[4]/ul/li[3]/a').click()
    elif pric_sort == 4:
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[4]/ul/li[4]/a').click()
    else:
        pass


    if city == 1:
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/div[4]/div[1]').click()
        #//*[@id="J_relative"]/div[1]/div/div[4]/div[1]/div
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/div[4]/div[2]/div[2]/ul/li[2]/a').click()
    else:
        pass



#一共有几个账号
#dict1={'name_1':'','name_2':'','xiao':0,'city':0,'price_min':0,'price_max':0}
#账号for 遍历
no_i = len(namelist)
for i in range(no_i):
    user_name = namelist[i]
    user_pass = passlist[i]
    login_func('手表')
    list_no=urlname.list1
    len_no=len(list_no)

    #关键词遍历
    for i in range(len_no):
        name_1=list_no[i]['name_1']
        name_2=list_no[i]['name_2']
        xiao  =list_no[i]['xiao']
        city  =list_no[i]['city']
        price_min = list_no[i]['price_min']
        price_max = list_no[i]['price_max']
        pric_sort = list_no[i]['pric_sort']
        get_sousuo(xiao=xiao,city=city,price_min=price_min,price_max=price_max,pric_sort=pric_sort)
        down_page()






if __name__ == '__mai1n__':
    no_i = len(namelist)
    for i in   range(no_i):
        user_name = namelist[i]
        user_pass = passlist[i]
        login_func()
        no_j=len(url_list)
        for j in range(no_j):
            num_no=j+1
            num_no=str(num_no)
            url=url_list[j]
            print(f'第{num_no}个关键词组：{url}')
            print('第一次搜索')
            listurl_no=get_data()
            if len(listurl_no) == 0:
                print('第二次搜索')
                listurl_no1=get_data()
                if len(listurl_no1)==0:
                    print('第三次搜索')
                    listurl_no2=get_data()
                    if len(listurl_no2) == 0:
                        print(f"第{num_no}为匹配到符合条件的值")
                    else:
                        print(listurl_no2)
                        get_listurl(listurl_no2)
                else:
                    print(listurl_no1)
                    get_listurl(listurl_no1)
            else:
                print(listurl_no)
                get_listurl(listurl_no)
        browser.close()
'''
1.增加空list检测机制，谁是空就将谁重新执行一遍
2.

'''