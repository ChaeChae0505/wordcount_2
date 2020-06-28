from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    text=request.GET['fulltext']
    text_split=text.split(' ')
    word_dic = {} #현재 사전에 아무것도 없음 

    for word in text_split:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1
#단어가 있으면 숫자 추가 없으면 단어를 추가

    #print(text_split[5]) #띄어쓰기 단위로 list형태로 저장한것중 5번째 값가져옴
    return render(request, 'count.html', {
                                            'length': len(text_split), 
                                            'full' : text_split,
                                            'text' : text,
                                            'dic': word_dic}) # full이라는 변수에 text_split의 값을 대응되게 전달 (딕셔너리 형태)