from flask import Flask
from flask.templating import render_template
import random 

# 5번의 게임을 반복하는 반복문
app = Flask(__lotto__)

send_list = []
def lottostart():
    for h in range(5):

    # 0~44까지 번호가 나온 횟수를 담을 리스트 선언
        randomlist = [0 for i in range(0, 45)]
    # loop 숫자 만큼의 랜덤 번호를 생성함.
        loop = int(10)
        for i in range(loop):
            c = int(random.random()*45) # 1개의 번호 생성
            randomlist[c] += 1  # c는 랜덤리스트의 인덱스로 활용가능. 나온 횟수를 1 증가시킴 

        recommendlist = []
        for k in range(6):
            a = max(randomlist)
            b = randomlist.index(a)
            randomlist[b] = 0
            recommendlist.append(b+1)

        recommendlist.sort()
        send_list.append(recommendlist)

@LottoPythonVersion.route('/tmp', methods=['GET', 'Post'])
def tmp():
    value = send_list
    return render_template('lotto.html', value = value)
    



