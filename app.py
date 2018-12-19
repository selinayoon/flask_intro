from flask import Flask,render_template
app = Flask(__name__)

import random

###한줄 띄우기
@app.route("/")
def hello():
    return "<h1>안녕하세요</h1>" #리턴 값이 화면에 출력
    
###여러 줄 띄우기    
@app.route("/html_tag")
#이 경로로 들어가려면 http://python-selinayoon.c9users.io:8080/주소에 html_tag만 더해주면 된다.
def html_tag():
    return """
    <h1>첫 번째 줄</h1>
    <h2>두 번째 줄</h2>
    """

###파일 띄우기
#flask_intro 폴더 안에 templates 폴더를 생성해둔다.
#그 안에는 html_file.html파일을 생성한다.
@app.route("/html_file")
#http://python-selinayoon.c9users.io:8080/html_file
def html_file():
    return render_template("html_file.html")

###변수로 string 데이터 받아 html로 전달하기
#templates 폴더 안에 welcome.html파일 생성한다. 
@app.route("/welcome/<string:name>")#/뒤에 모든 문자를 name이라는 변수로 받아줌
def welcome(name):
    #http://python-selinayoon.c9users.io:8080/welcome/쓰고싶은 말
    #name의 값을 people에 담아줌. 이제 people은 html에서 사용 가능하다.
    return render_template("welcome.html",people = name)
    
###변수로 int 데이터 받아 html로 전달하기
#입력 받은 숫자 세제곱 000의 세제곱은 000입니다 형식으로 띄우기
@app.route("/cube/<int:num>")
#http://python-selinayoon.c9users.io:8080/cube/5
def cube(num):
    triple = num * num * num
    return render_template("cube.html",triple = triple, number = num)
    #이때 triple과 두번째 triple과 다르다.

@app.route('/lunch')
def lunch():
    #점심메뉴를 추천해주는 코드 작성 
    #import random 해주기
    menu = ['짬뽕','피자','지코바','컵밥','삼겹살','라면','된장찌개','김치찌개','돼지국밥','돈까스']
    choice = random.choice(menu)
    print(choice)
    
    return render_template("lunch.html",choice = choice)
    
#라우팅:주소를 들어가야 함수가 실행된다.    
@app.route('/lotto') 
#컨트롤러: 조작 하는 역할
def lotto():
    #로또 번호 추천해주는 코드 작성
    #import random 해주기
    num = list(range(1,46))
    lottonum = random.sample(num,6)
    print(lottonum)
    
    #숫자들을 오름차순정렬 하는 함수sorted()
    spick = sorted(lottonum)
    print(spick)
    return render_template("lotto.html",spick= spick)   
    
@app.route('/search')
def search():
    #대신 네이버에 검색해주는 html 연결
    return render_template("search.html")