# 부트스트랩 페이지 연결하기  
# 

import csv
import random
 
f = open('ddareng.csv', 'r')
rdr = csv.reader(f)
wedo = []
keungdo = []
for line in rdr:
    wedo.append(float(line[9]))
    keungdo.append(float(line[10]))
    

f.close()

# 플라스크 모듈 불러오기
from flask import Flask, render_template, request

# app 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def hello_world():
    return render_template('tvtvtv.html', wedo=wedo)

@app.route("/abcd/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def grape():
    
    return render_template('parkpark.html')

@app.route('/map/', methods=['POST'])
def apple():

    maping = request.form['maping']
    
   
    return render_template('jidopage.html', maping=maping, wedo=wedo, keungdo=keungdo)

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)
