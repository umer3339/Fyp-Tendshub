from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import  HttpResponse
import pandas as pd
from django.core.paginator import Paginator
# Create your views here.
import itertools
import time
from django.contrib import messages
from datetime import datetime
from .models import Feedback,ContactForm


def Data(items):

    uniqueValues = list(items[' Post No'].values())
    print(uniqueValues)
    newListLen = []

    for i in uniqueValues:
        newListLen.append(int(i))

    post_no_dl = []
    post_user_name_dl = []
    post_time_and_date_dl = []
    post_user_status_dl = []
    post_like_dl = []
    post_comment_dl = []
    post_share_dl = []
    post_image_dl = []
    comment_dl = []
    comment_user_name_dl = []
    post_id_dl = []
    for i in newListLen:

        post_no = []
        post_id=[]
        post_user_name = []
        post_time_and_date = []
        post_user_status = []
        post_like = []
        post_comment = []
        post_share = []
        post_image = []
        comment = []
        comment_user_name = []

        for key, value in items[' Post No'].items():

            if i == int(value):
                post_no.append(int(items[' Post No'][int(key)]))
                post_user_name.append(items['Post User Name'][int(key)])
                post_time_and_date.append(items['Post Time And Date'][int(key)])
                post_user_status.append(items['Post User Status'][int(key)])
                post_like.append(items['Post Like'][int(key)])
                post_comment.append(items['Post Comment'][int(key)])
                post_share.append(items['Post Share'][int(key)])
                post_image.append(items['Post Image'][int(key)])
                post_id.append(int(items['Post_ID'][int(key)]))
                #comment.append(items['Comment'][int(key)])
                #comment_user_name.append(items['Comment User Name'][int(key)])
                break
        post_no_dl.append(post_no)
        post_user_name_dl.append(post_user_name)
        post_time_and_date_dl.append(post_time_and_date)
        post_user_status_dl.append(post_user_status)
        post_like_dl.append(post_like)
        post_comment_dl.append(post_comment)
        post_share_dl.append(post_share)
        post_image_dl.append(post_image)
        post_id_dl.append(post_id)
        #comment_dl.append(comment)
        #comment_user_name_dl.append(comment_user_name)
    data = zip(post_no_dl, post_user_name_dl, post_time_and_date_dl, post_user_status_dl, post_like_dl, post_comment_dl,
               post_share_dl, post_image_dl,post_id_dl)#,comment_dl, comment_user_name_dl
               #)
    dataList = list(data)
    post_no_dl2=[]
    for i in newListLen:
        post_no_dl2.append(items[' Post No'])
        comment_dl.append(items['Comment'])
        comment_user_name_dl.append(items['Comment User Name'])
        break

    #print(post_no_dl2,comment_dl,comment_user_name_dl)
    data2 = zip(post_no_dl2, comment_dl, comment_user_name_dl)  #
    dataList2 = list(data2)
    #print(dataList2, "DDDDDDDDDDDDDDDDDDDDd")
    return dataList,dataList2


def reddit_data(items):
    temp = 0
    uniqueValues = list(items['Post Title'].values())
    newListLen = []

    for i in uniqueValues:
        newListLen.append(i)

    post_user_name_dl = []
    post_title_dl = []
    post_text_dl = []
    post_time_and_date_dl = []
    post_like_dl = []
    post_comment_dl = []
    post_picture_dl = []
    post_id_dl = []
    for i in newListLen:
        post_title = []
        post_user_name = []
        post_time_and_date = []
        post_text = []
        post_like = []
        post_comment = []
        post_picture = []
        post_id=[]
        for key, value in items['Post Title'].items():
            if i == value:
                post_title.append(items['Post Title'][key])
                post_user_name.append(items['Post User Name'][key])
                post_time_and_date.append(items['Post Time And Date'][key])
                post_text.append(items['Post Text'][key])
                post_like.append(items['Post Like #'][key])
                post_comment.append(items['Post Comment #'][key])
                post_picture.append(items['Post Picture'][key])
                post_id.append(int(items['Post_ID'][int(key)]))
                break
        post_title_dl.append(post_title)
        post_user_name_dl.append(post_user_name)
        post_time_and_date_dl.append(post_time_and_date)
        post_text_dl.append(post_text)
        post_like_dl.append(post_like)
        post_comment_dl.append(post_comment)
        post_picture_dl.append(post_picture)
        post_id_dl.append(post_id)
        # comment_dl.append(comment)
        # comment_user_name_dl.append(comment_user_name)

    data = zip(post_title_dl, post_user_name_dl, post_time_and_date_dl, post_text_dl, post_like_dl, post_comment_dl,
               post_picture_dl,post_id_dl
               )
    dataList = list(data)

    post_title_dl = []
    comment_dl = []
    comment_user_name_dl = []
    for i in newListLen:
        print(i)
        post_title_dl.append(items['Post Title'])
        comment_dl.append(items['Comment'])
        comment_user_name_dl.append(items['Comment User Name'])
        break

    data2 = zip(post_title_dl, comment_dl, comment_user_name_dl)  #
    dataList2 = list(data2)


    return dataList, dataList2


def fashion(request,type,filename):#Fashion
    try:
        try:
            df = pd.read_pickle("static/pickleData/fashion/1/" + str(filename) + ".pkl")
            #df=pd.read_pickle("C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\fashion\\1\\" + str(filename) + ".pkl")
        except:
            error(request)

        indexes = []
        x = 0
        indexes.append(x)
        for i in range(0, len(df[' Post No'])):
            for j in range(0, len(df[' Post No']) - 1):
                try:
                    if df[' Post No'][x] == df[' Post No'][x + 1]:
                        x = x + 1
                    else:
                        indexes.append(x + 1)
                        temp = x
                        x = temp + 1
                        break
                except Exception as e:
                    break
        try:
            del df['emojiOnly']
            del df['textOnly']
        except:
            pass

        df = df.fillna("")

        items = df.to_dict()
        data1, data2 = Data(items)

        username_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            print(data2)
            print(data2[0][2],"....................................")
            for key, val in data2[0][2].items():
                if key < indexes[i + 1] and temp <= key:
                    # print(val)
                    firstList.append(val)
                    temp = key

            username_dl.append(firstList)

        comment_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][1].items():
                if key < indexes[i + 1] and temp <= key:
                    firstList.append(val)
                    temp = key

            comment_dl.append(firstList)

        mainList = []
        one = 1

        for i in range(0, len(comment_dl)):
            for j in range(0, len(comment_dl[i])):
                mainList.append((one, username_dl[i][j], comment_dl[i][j]))
                one = one + 1

        aikrList = []
        for i in indexes:
            aikrList.append(data1[i])
        indexes.remove(0)
        new_data = []
        c = 0
        for j in indexes:
            data = []
            for i in range(0, len(mainList)):
                if j > c:
                    data.append(mainList[c])
                    c = c + 1
            new_data.append(data)

        indexes.insert(0, 0)
        # print(indexes)

        data = zip(aikrList, new_data)

        length_of_mainList = len(mainList)
        feedback=Feedback.objects.all()
        return render(request, "category/fashon.html",
                      {"indexes": indexes, "data1": data1, "mainList": mainList, "length_of_mainList": length_of_mainList
                          , "zero": 0, "data": data,"feedback":feedback})
    except:
        return error(request)


def news(request,type,filename):
    try:
        try:
            df = pd.read_pickle("static/pickleData/news/1/" + str(filename) + ".pkl")
        except:
            error(request)
        #df = pd.read_pickle(
        #   "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\news\\1\\" + str(
        #        filename) + ".pkl")

        #if filename == 'g-top12' or filename == 'p-top14':
        #    print("CSV")
        #    df = pd.read_csv(
        #    "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\news\\1\\" + str(filename) + ".csv")
        indexes = []
        x = 0
        indexes.append(x)
        my_list = list(df[' Post No'])
        for i in range(0, len(df[' Post No'])):
            for j in range(0, len(df[' Post No']) - 1):
                try:
                    if my_list[x] == my_list[x + 1]:
                        x = x + 1
                    else:
                        indexes.append(x + 1)
                        temp = x
                        x = temp + 1
                        break
                except Exception as e:
                    break
        print(indexes,len(indexes),my_list)
        try:
            del df['emojiOnly']
            del df['textOnly']
        except:
            pass

        df = df.fillna("")

        items = df.to_dict()
        data1, data2 = Data(items)

        username_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []

            for key, val in data2[0][2].items():
                if key < indexes[i + 1] and temp <= key:
                    # print(val)
                    firstList.append(val)
                    temp = key

            username_dl.append(firstList)

        comment_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][1].items():
                if key < indexes[i + 1] and temp <= key:
                    firstList.append(val)
                    temp = key

            comment_dl.append(firstList)

        mainList = []
        one = 1

        for i in range(0, len(comment_dl)):
            for j in range(0, len(comment_dl[i])):
                mainList.append((one, username_dl[i][j], comment_dl[i][j]))
                one = one + 1

        aikrList = []
        for i in indexes:
            aikrList.append(data1[i])
        indexes.remove(0)
        new_data = []
        c = 0
        for j in indexes:
            data = []
            for i in range(0, len(mainList)):
                if j > c:
                    try:
                        data.append(mainList[c])
                        c = c + 1
                    except:
                        pass
            new_data.append(data)

        indexes.insert(0, 0)
        # print(indexes)

        data = zip(aikrList, new_data)

        length_of_mainList = len(mainList)
        feedback = Feedback.objects.all()
        return render(request, "category/news.html",
                      {"indexes": indexes, "data1": data1, "mainList": mainList, "length_of_mainList": length_of_mainList
                          , "zero": 0, "data": data,"feedback":feedback})
    except:
        return error(request)
    #return render(request,"category/news.html")

def tourism(request,type,filename):
    try:
        try:
            df = pd.read_pickle("static/pickleData/tourism/1/" + str(filename) + ".pkl")
        except:
            error(request)
        #df = pd.read_pickle(
        #    "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\tourism\\1\\" + str(
        #        filename) + ".pkl")

        #if filename == 'g-top12' or filename == 'p-top14':
        #    print("CSV")
        #    df = pd.read_csv(
        #    "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\tourism\\1\\" + str(filename) + ".csv")

        indexes = []
        x = 0
        indexes.append(x)
        my_list = list(df[' Post No'])

        for i in range(0, len(df[' Post No'])):
            for j in range(0, len(df[' Post No']) - 1):
                try:

                    if my_list[x] == my_list[x + 1]:
                        x = x + 1

                    else:
                        indexes.append(x + 1)
                        temp = x
                        x = temp + 1
                        break
                except Exception as e:
                    pass
        try:
            del df['emojiOnly']
            del df['textOnly']
        except:
            pass

        df = df.fillna("")

        items = df.to_dict()
        data1, data2 = Data(items)

        username_dl = []
        temp = 0
        print(indexes)
        for i in range(0, len(indexes) - 1):
            firstList = []

            for key, val in data2[0][2].items():

                if key < indexes[i + 1] and temp <= key:
                    firstList.append(val)
                    temp = key

            username_dl.append(firstList)
        comment_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][1].items():
                if key < indexes[i + 1] and temp <= key:
                    firstList.append(val)
                    temp = key

            comment_dl.append(firstList)
        mainList = []
        one = 1

        for i in range(0, len(comment_dl)):
            for j in range(0, len(comment_dl[i])):
                mainList.append((one, username_dl[i][j], comment_dl[i][j]))
                one = one + 1

        aikrList = []
        for i in indexes:
            aikrList.append(data1[i])
        indexes.remove(0)
        new_data = []
        c = 0
        for j in indexes:
            data = []
            for i in range(0, len(mainList)):
                if j > c:
                    try:
                        data.append(mainList[c])
                        c = c + 1
                        print(c)
                    except:
                        pass
            new_data.append(data)

        indexes.insert(0, 0)
        # print(indexes)

        data = zip(aikrList, new_data)
        #print(df['Comment'])
        #print(username_dl, "username")
        #print(comment_dl, "comments")

        length_of_mainList = len(mainList)
        # print(data1)
        feedback = Feedback.objects.all()
        #print(mainList, "... Where")
        return render(request, "category/enterteinment.html",
                      {"indexes": indexes, "data1": data1, "mainList": mainList, "length_of_mainList": length_of_mainList
                          , "zero": 0, "data": data,"feedback":feedback})
    except:
        return error(request)

#return render(request,"category/enterteinment.html")

def health(request,type,filename):
    try:
        try:
            df=pd.read_pickle("static/pickleData/health/1/"+str(filename)+".pkl")
        except:
            error(request)
        #df = pd.read_pickle(
        #    "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\health\\1\\" + str(
        #        filename) + ".pkl")

        #if filename == 'g-top8' or filename == 'p-top12':
        #    print("CSV")
        #    df = pd.read_csv("static/pickleData/health/1/" + str(filename) + ".csv")
            #df = pd.read_csv(
            #"C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\health\\1\\" + str(filename) + ".csv")

        indexes = []
        x = 0
        indexes.append(x)
        my_list = list(df[' Post No'])

        for i in range(0, len(df[' Post No'])):
            for j in range(0, len(df[' Post No']) - 1):
                try:

                    if my_list[x] == my_list[x + 1]:
                        x = x + 1

                    else:
                        indexes.append(x + 1)
                        temp = x
                        x = temp + 1
                        break
                except Exception as e:
                    pass
        try:
            del df['emojiOnly']
            del df['textOnly']
        except:
            pass

        df = df.fillna("")

        items = df.to_dict()
        data1, data2 = Data(items)

        username_dl = []
        temp = 0
        print(indexes)
        for i in range(0, len(indexes) - 1):
            firstList = []

            for key, val in data2[0][2].items():

                if key < indexes[i + 1] and temp <= key:

                    firstList.append(val)
                    temp = key

            username_dl.append(firstList)
        #print(username_dl,"username")
        comment_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][1].items():
                if key < indexes[i + 1] and temp <= key:
                    firstList.append(val)
                    temp = key

            comment_dl.append(firstList)
        #print(comment_dl, "comments")
        mainList = []
        one = 1

        for i in range(0, len(comment_dl)):
            for j in range(0, len(comment_dl[i])):
                mainList.append((one, username_dl[i][j], comment_dl[i][j]))
                one = one + 1

        aikrList = []
        for i in indexes:
            aikrList.append(data1[i])
        indexes.remove(0)
        new_data = []
        c = 0
        for j in indexes:
            data = []
            for i in range(0, len(mainList)):
                if j > c:

                    data.append(mainList[c])
                    c = c + 1
            new_data.append(data)

        indexes.insert(0, 0)
        # print(indexes)

        data = zip(aikrList, new_data)

        length_of_mainList = len(mainList)
        #print(data1)
        print(len(mainList),"...")
        feedback=Feedback.objects.all()
        return render(request, "category/health.html",
                      {"indexes": indexes, "data1": data1, "mainList": mainList, "length_of_mainList": length_of_mainList
                          , "zero": 0, "data": data,"feedback":feedback})
    except:
        return error(request)


def about(request):
    return render(request,"about-us.html")

def contact(request):
    try:
        if request.method == "POST":
            name =request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            details="Name :"+ name + "\nEmail :"+email+ "\nSubject :"+str(subject)+ "\nMessege :" +message
            send_mail("TrendsHUB :CONTACT US", details, "temptesting135@gmail.com", ["yassarfarooq13@gmail.com"])
            ContactForm.objects.create(name=name, email=email, subject=subject, message=message)
            info=messages.add_message(request, messages.INFO,
                                 'Form Successfully Submitted our Representative will Contact you soon.')


            return render(request, "contact.html",{"message":info})
        else:
            return render(request,"contact.html")
    except:
        return error(request)
def index(request):
    return render(request,"home.html")

def reddit(request,filename):

    try:
        news=['news','teaching',"Teachers","worldnews","top100"]
        health = ['Health', 'HealthAnxiety', "healthcare", "healthIT",'publichealth',"top23","top"]
        fashion=['fashion','femalefashion','FrugalFemaleFashion','frugalmalefashion','malefashionadvice','streetwear',"top31"]
        tourism=['CozyPlaces','pakistan','travel','top_30']

        fash=False
        heal=False
        tour=False
        news_false=False
        print(filename)
        if filename in news:
            news_false=True
            print("news")
            path="news/1/"+str(filename)
        if filename in health:
            heal=True
            print("health")
            path = "health/1/" + str(filename)
        if filename in fashion:
            fash=True
            print("fashion")
            path = "fashion/1/" + str(filename)
        if filename in tourism:
            tour=True
            print("tourism")
            path = "tourism/1/" + str(filename)
        #path = "pickleData/reddit/tourism/" + str(filename)
        #print(path)
        try:
            df = pd.read_csv("static/pickleData/reddit/"+ str(path) + ".csv")
        except:
            error(request)
        #df = pd.read_csv(""
        #    "C:\\Users\\yassa\\OneDrive\\Desktop FYP folder\\FYP\\TrendsHUB\\algo\\pickleData\\reddit\\" + str(path)  + ".csv")
        # start_time = time.time()
        indexes = []
        x = 0
        indexes.append(x)
        for i in range(0, len(df['Post Title'])):
            for j in range(0, len(df['Post Title']) - 1):
                try:
                    if df['Post Title'][x] == df['Post Title'][x + 1]:
                        x = x + 1
                    else:
                        indexes.append(x + 1)
                        temp = x
                        x = temp + 1
                        break
                except Exception as e:
                    break
        try:
            del df['emojiOnly']
            del df['textOnly']
        except:
            pass

        df = df.fillna("")

        items = df.to_dict()
        data1, data2 = reddit_data(items)

        username_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][2].items():
                if key < indexes [i + 1] and temp <= key:
                    #print(val)
                    firstList.append(val)
                    temp = key

            username_dl.append(firstList)


        comment_dl = []
        temp = 0
        for i in range(0, len(indexes) - 1):
            firstList = []
            for key, val in data2[0][1].items():
                if key < indexes[i + 1] and temp <= key:

                    firstList.append(val)
                    temp = key

            comment_dl.append(firstList)

        mainList = []
        one=1

        for i in range(0, len(comment_dl)):
            for j in range(0, len(comment_dl[i])):
                mainList.append((one, username_dl[i][j], comment_dl[i][j]))
                one = one + 1

        aikrList = []
        for i in indexes:
            aikrList.append(data1[i])
        indexes.remove(0)
        new_data = []
        c = 0
        for j in indexes:
            data = []
            for i in range(0, len(mainList)):
                if j > c:
                    data.append(mainList[c])
                    c = c + 1
            new_data.append(data)

        indexes.insert(0,0)

        data = zip(aikrList, new_data)

        length_of_mainList=len(mainList)
        feedback=Feedback.objects.all()
        return render(request,"category/reddit.html",{"indexes":indexes,"data1":data1,"mainList":mainList,"length_of_mainList":length_of_mainList
                                             ,"zero":0,"data":data,"tour":tour,"fash":fash,"news_false":news_false,"heal":heal,"feedback":feedback})
    except:
        return error(request)


def feedback(request):
    if request.method=='POST':
        post_id=int(request.POST.get('post_id'))
        feedback_comment=request.POST.get('feedback_comment')
        print(post_id,feedback_comment,request.user.username)

        f=Feedback()
        f.post_id=post_id
        f.feedback_comment=feedback_comment
        f.username=str(request.user.username)
        f.save()
        return redirect("/")
    
def error(request):
    return render(request,"error.html")