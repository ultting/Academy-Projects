# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Naver CLOVA Speech Api

# 형태소 분류 함수
def lemmatize(word):
    morphtags = Komoran().pos(word)
    if morphtags[0][1] == 'NNG' or morphtags[0][1] == 'NNP':
        return morphtags[0][0]


# +
# 라이브러리 및 모델 불러오기

from flask import Flask ,render_template,request, redirect

from konlpy.tag import Kkma,Okt, Twitter, Komoran # 형태소 분석 라이브러리
import kss # 텍스트 문장으로 바꾸는 라이브러리
from moviepy.editor import * # 영상을 오디오 파일로 변환
from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor as mp
from pytube import YouTube # 유튜브 영상 다운로드 또는 불러오기
import pytube
import tqdm as tq


import speech_recognition as sr # 오디오 파일 또는 음성을 텍스트로 변환
import pandas as pd
import numpy as np
# BOW = BAG of WORD : 단어가방, 단어모음, 단어사전
from sklearn.feature_extraction.text import CountVectorizer
# 위 도구는 빈도수 기반 벡터화 도구
import requests
import json


# +
# 형태소 분류 함수
def lemmatize(word):
    morphtags = Komoran().pos(word)
    if morphtags[0][1] == 'NNG' or morphtags[0][1] == 'NNP':
        return morphtags[0][0]
    
    
# naver CLOVA speech recognition API
class ClovaSpeechClient:
    # Clova Speech invoke URL
    invoke_url = ''
    # Clova Speech secret key
    secret = ''

    def req_url(self, url, completion, callback=None, userdata=None, forbiddens=None, boostings=None, wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'url': url,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/url',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_object_storage(self, data_key, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                           wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'dataKey': data_key,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/object-storage',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                   wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            'media': open(file, 'rb'),
            'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
        }
        response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
        return response

app = Flask(__name__)

@app.route('/post',methods=['POST','GET'])
def result():
    if request.method == 'POST' :
        result = request.form
        print(result)
        yt = pytube.YouTube(result.get('link'))
        print(yt.title)
        
        # 유튜브 영상 다운로드 후 저장
        stream = yt.streams.all()[0]
        stream.download(output_path='test/data')
        
        # 영상 제목
        title = yt.title
        
        # CLOVA Api 는 req관련 코드가 2개가 더 있음
        res = ClovaSpeechClient().req_upload(file='test/data/'+title+'.3gpp', completion='sync')
        #print(res.text)
        
        # 전체 텍스트를 json 타입 변수에 저장
        # 텍스트 추출
        text = json.loads(res.text)

        # kss 활용 텍스트 문장 화
        word_list = kss.split_sentences(text['text'])
        
        # 문장 끝 마침표 제거
        for i in range(len(word_list)):
            word_list[i]=word_list[i].replace('.','')
            
            
            # 명사만 가져오기 위한 삭제
        okt = Okt()
        headline = []
        stopwords = [ '의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','등','으로도']
        for sentence in word_list:
            temp = []
            # morphs() : 형태소 단위로 토큰화
            # stem = True : 형태소에서 어간을 추출
            temp = okt.morphs(sentence, stem = True)
            temp = [word for word in temp if not word in stopwords]
            headline.append(temp)

           # konlpy 트위터 이용 형태소 분류
        twitter = Twitter()
        sentences_tag_last=[]
        for word in headline:
            sentences_tag=[]
            for i in word :
                morph = twitter.pos(i)
                sentences_tag.append(morph)
            sentences_tag_last.append(sentences_tag)

        #  형태소 분류
        adj_list_last=[]
        for ko in sentences_tag_last:
            noun_adj_list=[]
            for i in ko:
                for word, tag in i:
                    if tag in ['Noun','Verb','Number','Adjective','Adverb','Alpha']:
                        noun_adj_list.append(word)
            adj_list_last.append(noun_adj_list)

        print(adj_list_last)
        # 형태소 분류 Komoran
        for i in range(len(adj_list_last)):
            for j in range(len(adj_list_last[i])):
                if lemmatize(adj_list_last[i][j]) != None :
                        adj_list_last[i][j] = lemmatize(adj_list_last[i][j])

        arr_list = adj_list_last

        wordCount=[]
        for i in range(len(arr_list)):
            for j in range(len(arr_list[i])):
                wordCount.append(arr_list[i][j])
        # 영상 합치기
        # 데이터프레임 
        wordData=pd.read_csv('Data_Deep/word_data.csv')

        # 데이터프레임에 있는 json 과 단어를 뽑아서 2차원 리스트로 만들기
        wordList = []
        for i in range(len(wordData)):
            jsonList=[]
            for j in range(1):
                jsonList.append(wordData.iloc[i,1])
                jsonList.append(wordData.iloc[i,2])
                jsontuple = tuple(jsonList)
            wordList.append(jsontuple)

        # 2차원 리스트 ( wordList )안에 샘플데이터 ( testList ) 가 있는지 확인
        jsonList2 = []
        for i in range(len(wordList)):
            if wordList[i][0] in wordCount:
                jsonList2.append(wordList[i][1]) # 맞는 번호의 json파일 

        jsonFileName=[]
        json_data=[]
        for i in range(len(jsonList2)):
            # 3. json파일 오픈
            jsonMovieData=[]
            for j in range(1):
                with open('Data_Deep/3000/'+jsonList2[i],'r',encoding='utf-8') as f:
                    json_data.append(json.load(f))
                    #print(json.dumps(json_data))
                    jsonMovieData.append(json_data[i]['metaData']['name'])
                    jsonMovieData.append(json_data[i]['data'][0]['start'])
                    jsonMovieData.append(json_data[i]['data'][0]['end'])
            jsonFileName.append(jsonMovieData)


        clips = []
        try:
            for i in range(len(jsonFileName)):
                mov = VideoFileClip('Data_Deep/Wordmp4/real_word_3000/'+jsonFileName[i][0]).subclip(jsonFileName[i][1],jsonFileName[i][2])
                mov = mov.resize(height=1080,width=1920) # 크기 맞추기
                clips.append(mov)
                print('성공')
        except:
            print('skip')
        print('last',clips)
        path = 'sua8.mp4'
        final_clip = concatenate_videoclips(clips, method='compose')
        final_clip.write_videofile('C:/Users/smhrd/git/BRIDGE_spring/Signal/src/main/webapp/WEB-INF/video/'+path)

        
        return redirect("http://localhost:8082/web/detailpage?link="+path)
    
if __name__ == '__main__':
    app.run(host= '61.80.106.115', port=3306)
# -

# # Google Cloud Speech To Text

# + endofcell="--"


# 유튜브 영상 다운로드 후 저장

stream = yt.streams.all()[0]
stream.download(output_path='C:/Users/smhrd/Desktop/Machine Learning/test/data') 

# 영상을 오디오 파일로 변환 
clip = mp.VideoFileClip("data/[파이썬 기초] NO3 변수.3gpp")
newsound = clip.subclip("00:00:10","00:01:00") # 20 sec
newsound.audio.write_audiofile("data/[파이썬 기초] NO3 변수.wav",16000,2,2000,'pcm_s16le')

# 오디오 파일 로드
filename = "data/[파이썬 기초] NO3 변수.wav"

# 오디오 파일 텍스트 추출
text = []
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data,language='ko-KR')
    # print(text)

# kss 활용 텍스트 문장 화
word_list = kss.split_sentences(text)

# 명사만 가져오기 위한 삭제
okt = Okt()
headline = []
stopwords = [ '의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','등','으로도']
for sentence in word_list:
    temp = []
    # morphs() : 형태소 단위로 토큰화
    # stem = True : 형태소에서 어간을 추출
    temp = okt.morphs(sentence, stem = True)
    temp = [word for word in temp if not word in stopwords]
    headline.append(temp)
    

# konlpy 트위터 이용 형태소 분류
twitter = Twitter()
sentences_tag = []
for word in headline:
    for i in word :
        morph = twitter.pos(i)
        sentences_tag.append(morph)
# print(sentences_tag)

# -

#  형태소 분류
noun_adj_list=[]
for i1 in sentences_tag:
    for word, tag in i1:
        if tag in ['Noun','Verb','Number','Adjective','Adverb','Alpha']:
            noun_adj_list.append(word)
# print(noun_adj_list)

# 형태소 분류
for i in range(len(noun_adj_list)):
    #print(lemmatize(noun_adj_list[i]))
    if lemmatize(noun_adj_list[i]) != None :
        noun_adj_list[i] = lemmatize(noun_adj_list[i])
        #print(noun_adj_list)

arr_list = noun_adj_list
print(arr_list)
# --

# +
# 구글 정확도
from google.cloud import speech_v1p1beta1 as speech

client = speech.SpeechClient()

speech_file = "data/hello.wav"

with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

# 현재 코드는 default값을 기준으로 실행시 에러여서 카운트 2가 부여되어 있음
# audio channel 관련 에러 시 채널 카운트를 2로 줄 것
config = speech.RecognitionConfig( 
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="ko-KR",
    enable_word_confidence=True,
    audio_channel_count = 2
)


response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print(u"Transcript: {}".format(alternative.transcript))
    print(
        u"First Word and Confidence: ({}, {})".format(
            alternative.words[0].word, alternative.words[0].confidence
        )
    )
    
## First Word and Confidence: (먼저, 0.8410878777503967)
# -

# # 수어 어순 알고리즘 (실패)

# +
last_new_word_list = [] # 수어 문장으로 정렬 하는 리스트
Noun_list=[] # 순서에 맞지 않았을때 값이 들어간 경우 
Verb_list = [] # 
del_list=[] # 활용가능성이 없는 단어들
for i in range(len(word_list_last)):
    for j in range(len(word_list_last[i])):
        if word_list_last[i][j][0][1]=='Noun':
            if len(word_list_last[i][j][0][0])==1:
                word_list_last[i].pop(j)
        elif word_list_last[i][j][0][1]=='Verb':
            if len(word_list_last[i][j][0][0])==1:
                word_list_last[i].pop(j)

for j in range(len(word_list_last)):
    new_word_list = [] # 수어 문장으로 정렬 하는 리스트
    for i in range(len(word_list_last[j])):
        if word_list_last[j][i][0][1]=='Noun':
            print(i)
            Noun_list.append(word_list_last[j][i][0][0])
            if len(new_word_list) < 3:  # 0,1,2
                if word_list_last[j][i][0][1]=='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1]=='Verb':
                    Verb_list.append(word_list_last[j][i][0][1])
            elif len(new_word_list) ==3:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 3 and len(new_word_list) < 7:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
            elif len(new_word_list) ==7:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 7 and len(new_word_list) < 11:
                if word_list_last[j][i][0][1] =='Noun':
                     new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                     Verb_list.append(word_list_last[j][i][0][0])

            elif len(new_word_list) ==11:
                 if word_list_last[j][i][0][1]=='Verb':
                        new_word_list.insert(i,word_list_last[j][i][0][0])
                        continue

            if len(new_word_list) > 11 and len(new_word_list) < 15:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])

            elif len(new_word_list) ==15:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 15 and len(new_word_list) < 19:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])

            elif len(new_word_list) ==19:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue        

        if word_list_last[j][i][0][1] == 'Verb':
            print(i)
            if len(new_word_list) < 3:  # 0,1,2
                if word_list_last[j][i][0][1]=='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1]=='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])
            elif len(new_word_list) ==3:
                if word_list_last[j][i][0][1]=='Noun':
                    if i == 1:
                        del_list.append(word_list_last[j][i][0][0])
                    else:
                        print('Verb')
                        Noun_list.append(word_list_last[j][i][0][0])
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 3 and len(new_word_list) < 7:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
            elif len(new_word_list) ==7:
                if word_list_last[j][i][0][1]=='Verb':
                    print(i)
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 7 and len(new_word_list) < 11:
                if word_list_last[j][i][0][1] =='Noun':   
                    new_word_list.insert(word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])
            elif len(new_word_list) ==11:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue

            if len(new_word_list) > 11 and len(new_word_list) < 15:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])

            elif len(new_word_list) ==15:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue     

            if len(new_word_list) > 15 and len(new_word_list) < 19:
                if word_list_last[j][i][0][1] =='Noun':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                elif word_list_last[j][i][0][1] =='Verb':
                    Verb_list.append(word_list_last[j][i][0][0])

            elif len(new_word_list) ==19:
                if word_list_last[j][i][0][1]=='Verb':
                    new_word_list.insert(i,word_list_last[j][i][0][0])
                continue
    
print(new_word_list)
print(Noun_list)
print(del_list)
print(Verb_list)
print('Noun / Noun / Verb / Noun / Noun / Verb / Noun / Noun / Verb')

# +
# 분류 및 정렬

SetNoun_list = set(Noun_list)
SetNew_word_list = set(new_word_list)

print(SetNoun_list.difference(SetNew_word_list))
print(new_word_list)
print(Noun_list)
print(Verb_list)


print(word_list_last[2])
print(new_word_list)

print(Noun_list)
print(Verb_list)
print('우리가 저번 시간까지 해서 매트릭스에 대해서 한번 배워봤는데 오늘 해볼 거는 데이터 프레임에 대해서 한번 배워보도록 하겠습니다')
# -

if len(new_word_list) > 14 and len(new_word_list) < 17:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==17:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 17 and len(new_word_list) < 20:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==20:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])
            
    if len(new_word_list) > 20 and len(new_word_list) < 23:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==23:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])
            
    if len(new_word_list) > 23 and len(new_word_list) < 26:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==26:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
    
    if len(new_word_list) > 26 and len(new_word_list) < 29:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==29:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 29 and len(new_word_list) < 32:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==32:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 32 and len(new_word_list) < 35:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==35:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 35 and len(new_word_list) < 38:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==38:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 38 and len(new_word_list) < 41:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==41:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 41 and len(new_word_list) < 44:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==44:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 44 and len(new_word_list) < 47:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==47:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
            
    if len(new_word_list) > 47 and len(new_word_list) < 50:
        if word_list_last[2][i][0][1] =='Noun':
            new_word_list.insert(i,word_list_last[2][i][0][0])
        elif word_list_last[2][i][0][1] =='Verb':
            Verb_list.append(word_list_last[2][i][0][0])
            
    if len(new_word_list) ==50:
        if word_list_last[2][i][0][1]=='Verb':
            new_word_list.insert(i,word_list_last[2][i][0][0])            
