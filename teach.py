# 將turtle模組導入這一個pytohn檔案
import turtle
# 將math模組放到這一個python檔案當中
import math
# 因為要做4個圖所以我分別使用4個筆,這樣就不用一直重置筆的狀態
# 因為我不喜歡看到箭頭，所以我會用ht來把箭頭隱藏用法為 t1.ht()當中的t1看要隱藏哪一隻做更改
t1 = turtle.Turtle()
t1.ht()
t2 = turtle.Turtle()
t2.ht()
t3 = turtle.Turtle()
t3.ht()
t4 = turtle.Turtle()
t4.ht()
# 定義Goto的功能，這樣當有需要將筆拿起放到對的位置之後再放下 可以使用這一個function
def Goto(t, x ,y):
    t.pu()
    t.goto(x,y)
    t.pd()
# 第一個題目,正六邊形且切成等分的三角形(t:哪一支筆，l:邊長)
def HexagonPie(t, l):
    # 將筆色設定為黑色，並將筆粗設定成1
    t.pencolor('black')
    t.pensize(1)
    # 藉由數學公式可以知道正六邊形可以分割成6個正三角形所以for j 的迴圈表示要會6個三角形，且因為開始繪圖的點都是中心，繪製完成會剛好轉一圈，所以會畫圖完成後要轉60度畫下一個
    for j in range(6):
        t.rt(60)
        # 三角形的畫法就是畫邊轉彎，注意到這邊對於筆來說是要轉外角，所以要用180-內角得到120度（正六邊形每一角120度，正三角形剛好是否角平分線）
        for i in range(3):
            t.rt(120)
            t.fd(l)
# 第二題是要繪製24個圓,且這些圓的圓心連起來剛好是一個圓的邊（t:哪一支筆,n:幾個圓組成,r：這些圓的半徑大小）
def RoundCircle(t, n, r):
    # 如上述所說要圍繞在同一個圓，所以每一次都要轉一個角度（根據n不同，角度不同，但是剛好會繞一圈，所以轉彎的ang = 360/n)
    ang = 360/n
    # 因為要畫n個圓所以for i 回圈當中的range()裡面的數字代表，所以用n
    for i in range(n):
        t.circle(r)
        # 畫圖完成每一個圓之後，要轉上面算的ang所以在這邊進行回圈。
        t.lt(ang)
# 第三個作業：繪製一個空心的綠色三葉(有其他解法e.g:畫6個60度的圓or不同起始點)
def ThreeLeaf(t, l):
    # 設定筆的顏色跟大小分別是綠色和5號大小
    t.pencolor('green')
    t.pensize(5)
    # 47~49是基於數學運算後，我將中心放在螢幕中心所以要調整起使位置可以不用做
    move_x = -l * math.sqrt(3) / 2
    move_y = -l/2
    Goto(t, move_x, move_y)
    # 因為我是從作下角開始畫圖，並且以畫三個120度的圓來完成，所以要先左轉60度
    t.lt(60)
    t.circle(l,120)
    # 畫3個120度半圓，因為筆面向右上，所以為負的圓（逆向）
    for i in range(3):
        t.circle(l,120)
        t.rt(120)
# 第四個作業：太極(t:哪一隻筆，r:整體的圓半徑)
def TaiChi(t, r):
    # 設定筆的大小為10號,顏色為黑色
    t.pensize(10)
    t.pencolor('black')
    # 我的作法是由最上面開始畫，所以使用Goto()去到圓的最上面
    Goto(t, 0, r)
    # 先畫右邊並且填滿黑色
    t.fillcolor('black')
    t.begin_fill()
    # 先畫右邊半圓，逆向
    t.circle(-r,180)
    # 中間分隔線的作法是分別做兩個半徑為原本圓一半的半圓且先左後右(下到上）65~72畫出來的部分剛好是右邊要填滿黑色的部分（起始點為下方）
    t.circle(-(r/2),180 )
    t.circle((r/2),180)
    t.end_fill()
    # 相同的方法做左邊的圓（外圈）,現在在上方，所以畫出左半圓（順向）
    t.circle(r,180)    
    # 最後需要使用到turtle當中的dot功能（在筆的位置畫一個實心圓）
    # 預測白點位置（個人偏好）
    Goto(t, 0 ,(-2* r/ 3))
    # 在筆的位置畫出尺寸為50的白點
    t.dot(50, 'white')
    # 預測黑點位置（個人偏好）
    Goto(t, 0, (2* r/3))
    # 在筆的位置畫出尺寸為50的黑點
    t.dot(50, 'black')

# 分別將每一個圖形展示出來
HexagonPie(t1,100)
# clear指令的用法是將該筆所畫出來的部分刪除
t1.clear()
# 以下都是畫一個圖然後刪除
RoundCircle(t2, 24, 100)
t2.clear()
ThreeLeaf(t3, 200)
t3.clear()
TaiChi(t4,200)
# 最後一個不要刪除定格


turtle.exitonclick()

