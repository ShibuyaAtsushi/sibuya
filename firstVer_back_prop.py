
import pprint
import numpy as np
np.random.seed(42)  # 再現性のために乱数シードを設定

def set_network(w1,b1,w2,b2,w3,b3):
    network = [w1,b1,w2,b2,w3,b3] #listは中身何でもよし配列なので、arrayは数値の配列
    return network

def forward(network, in_x):
    W1, W2, W3 = np.array(network[0]), np.array(network[2]), np.array(network[4])
    # b1, b2, b3 = np.array(network[1]), np.array(network[3]), np.array(network[5])
    z1 = np.dot(in_x, W1) #+ b1
    fz1 = sigmoid(z1) #その層のすべてのニューロンの入力にシグモイド関数をかけて出力を作成する。
    z2 = np.dot(fz1, W2) #+ b2
    fz2 = sigmoid(z2)
    z3 = np.dot(fz2, W3) #+ b3
    fz3 = sigmoid (z3)
    print(fz3)
    Z_ALL = [z1, z2, z3]
    FZ_ALL = [in_x, fz1, fz2, fz3]
    return Z_ALL, FZ_ALL #xを入力したnetworkで順伝播して得られた出力結果

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):#恒等関数
    return x 

in_x = np.random.random([1,3])*1
teach = np.array([[0.5,0.7]])

# ニューロンの数を決める
IN = 3
W1 = 3
W2 = 3
W3 = 2

#初期の重みとバイアスを設定
#3つのニューロンから、8つのニューロンに出力する際の重み
w1 = np.random.random([IN,W1])
#バイアスを用意
b1 = np.random.random([1,W1])
 #8つのニューロンから5つのニューロンに出力する際の重み
w2 = np.random.random([W1,W2])
#5つのニューロンにたすバイアス
b2 = np.random.random([1,W2])
 #5つのニューロンから8つのニューロンに出力する際の重み
w3 = np.random.random([W2,W3])
b3 = np.random.random([1,W3])

W_ALL = [w1,w2,w3]# 重みパラメータを保存
layer_num = len(W_ALL)-1 #層の数用の変数　０スタートにするため１減らしている
print(layer_num)
# W_ALL.append(w1)
# W_ALL.append(w2)
# W_ALL.append(w3)
B_ALL = [b1,b2,b3]# バイアスパラメータを保存

print('W_ALL=')
pprint.pprint(W_ALL)
print('B_ALL=')
pprint.pprint(B_ALL)
                                                                                            # print('w1=')
                                                                                            # pprint.pprint(w1)
                                                                                            # print('b1=')
                                                                                            # pprint.pprint(b1)
                                                                                            # print('w2=')
                                                                                            # pprint.pprint(w2)
                                                                                            # print('b2=')
                                                                                            # pprint.pprint(b2)
                                                                                            # print('w3=')
                                                                                            # pprint.pprint(w3)
                                                                                            # print('b3=')
                                                                                            # pprint.pprint(b3)

Network = set_network(W_ALL[0], B_ALL[0], W_ALL[1], B_ALL[1], W_ALL[2],B_ALL[2],)
# z_all, fz_all = forward(Network, in_x)
# print('z_ALL=')
# pprint.pprint(z_all)
# print('fz_ALL=')
# pprint.pprint(fz_all)
                                                                                            # print('----------------')
                                                                                            # print('z1=')
                                                                                            # pprint.pprint(z1)
                                                                                            # print('z1t=')
                                                                                            # z1t = np.transpose(z1)
                                                                                            # pprint.pprint(z1t)
                                                                                            # print('z1shape=')
                                                                                            # print(z1.shape)
                                                                                            # print('z1tshape=')
                                                                                            # print(z1t.shape)
                                                                                            # print('fz1=')
                                                                                            # pprint.pprint(fz1)
                                                                                            # print('z2=')
                                                                                            # pprint.pprint(z2)
                                                                                            # print('fz2=')
                                                                                            # pprint.pprint(fz2)
                                                                                            # print('z3=')
                                                                                            # pprint.pprint(z3)
                                                                                            # print('fz3=')
                                                                                            # pprint.pprint(fz3_y)
                                                                                            # print('teach')
                                                                                            # pprint.pprint(teach)

                                                                                            # grad_list=[]










# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# square変更実験のコピー版＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃


from tqdm import trange
# ●マークのタイプの行列微分する関数
def grad_loss_and_y(layer_num, teach, Y):
    print("●の処理開始●●●●●●●●●●●●●●●●●●●●●●●●")
    circle = []
    for out in range(len(teach)): #出力の数つまり教師の数だけ(y-t)がでてくる
        loss = Y[out] - teach[out] #Y-ｔ
        circle.append(loss) #結果を一つずつ足しこんでいく
        # circle = np.transpose(circle) #偏微分計算によって転置行列になった
        print("サークル")
        print("Y:", Y, "Length:", len(Y))
        print("teach:", teach, "Length:", len(teach))
        print("●の処理終了＆結果↓●●●●●●●●●●●●●●●")
        pprint.pprint(circle)
    return circle


# 一番最初の▲マークのタイプの行列微分する関数(シグモイドの微分が出る)出力を見るから，layer_num+1番目
def first_grad_fz_and_z(layer_num, FZ, Z):
    print("最初の▲の処理開始▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    triangle = np.zeros((len(FZ[layer_num+1][0]), len(Z[layer_num][0]))) #その層のｆｚとｚの大きさの０だけ行列を作成
    pprint.pprint(triangle)
    for gyou in range(len(FZ[layer_num+1][0])):
        triangle[gyou, gyou] = (1-sigmoid(FZ[layer_num+1][0][gyou]))*sigmoid(FZ[layer_num+1][0][gyou]) #配列をnp.zerosで作って，その要素を指定場所に代入する
    # print("fin▲", triangle)
    print("最初の▲の処理終了▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    pprint.pprint(triangle)
    return triangle



# ▲マークのタイプの行列微分する関数(シグモイドの微分が出る)
def grad_fz_and_z(layer_num, FZ, Z):
    print("▲の処理開始▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    triangle = np.zeros((len(FZ[layer_num][0]), len(Z[layer_num][0]))) #その層のｆｚとｚの大きさの０だけ行列を作成
    pprint.pprint(triangle)
    for gyou in range(len(FZ[layer_num][0])):
        triangle[gyou, gyou] = (1-sigmoid(FZ[layer_num][0][gyou]))*sigmoid(FZ[layer_num][0][gyou]) #配列をnp.zerosで作って，その要素を指定場所に代入する
    # print("fin▲", triangle)
    print("▲の処理終了▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    pprint.pprint(triangle)
    return triangle


# ★マークのタイプの行列微分する関数(重みWが出る)．ここでは全パターン出る
def grad_z_and_fz(W_ALL,layer_num_loop,):
    print("★の処理開始★★★★★★★★★★★★")
    W = W_ALL[layer_num_loop+1] #今考えている（見ている）重みの値のセットを取り出す（何層目の重み層か）
    star =  np.transpose(W) #！！大事！！　W_ALLの定義の仕方と計算するやり方での違いを整えるため，転置行列にする　そのニューロンが次のニューロンに出力する値をひとまとまりにして，各ニューロンが出す出力のまとまりを1要素としてリストにしていたので（つまり行数はニューロンの数，列数は受け取るニューロンの数としていたので）それの逆で計算しないと計算がうまくいかないので，転地をすることでwを再定義することなく計算できるようにする．しかしこれはw_ALLの定義を帰ればしなくてもよい処理のはず
    print("★の処理終了＆結果★★★★★★★★★")
    pprint.pprint(star)
    return star


# square 編集中
# □マークのタイプの行列微分をする関数（fzがでる）．一度にすべて出すのではなく，行ごとに計算して，最後にそれらを足したい　！！！！完成！！！！
def grad_z_and_w(layer_num, FZ_ALL, W_ALL):
    print("■の処理開始■■■■■■■■■■■■■■■■■■■■■■■■■")
    KOUBAILIST = []
    for square_gyou in range(len(W_ALL[layer_num][0])):#その層の行数の数分繰り返す
        print("square_gyou =", square_gyou )
        print("0行列を作る(転置もしてる)結果↓")
        square = np.zeros((len(W_ALL[layer_num]), len(Z_ALL[layer_num][0]))) #その層のWとZの大きさの０だけ行列を作成つまりz行w列の０行列を作成
        square = np.transpose(square) #ゼロ行列を転置する　これら二つを使ってやればいい！？
        pprint.pprint(square)
        print("layer_num-square_gyouの値は")
        print(layer_num-square_gyou)
        print("FZ_ALLは")
        pprint.pprint(FZ_ALL)
        square[square_gyou] = FZ_ALL[layer_num] #FZ_ALLのlayer_num番目（つまり今見てる層のfz）を，ループごとに違うところに代入
        print("FZ_ALLのlayer_num番目（つまり今見てる層のfz）を，ループごとに違うところに代入")
        pprint.pprint(square)
        # square = np.transpose(square)
        # print("転置処理")
        # pprint.pprint(square)
        print("１掛ける３の勾配が出てるはず↓")
        pprint.pprint(np.dot(koubai, square))
        KOUBAILIST.append(np.dot(koubai, square)) #そして計算，すると勾配が１×３の形で出てくるので，それを一行ずつやりながらKOUBAILISTに入れていく
        print("これの結果をリストに保存したので，次の行に行きます．")
        #つまりいっぺんに計算せず，行ベクトルごとに取り出してそのつど計算し，結果を保存していくという処理をしている
    print("全ての勾配を計算してリストに保存し終わりました■■■■■＆結果↓")
    # 行列を連結する 例：（1×３の行列３つのリストを，３×３の行列に変換させる） ！！成功！！
    KOUBAILIST = np.concatenate(KOUBAILIST, axis=0)
    pprint.pprint(KOUBAILIST) #結果出力
    return KOUBAILIST



#微小量hを定義
h = 1e-2#0.0001
#学習率を定義
learning_rate = 0.6
#学習回数を定義
learn = 2500

loop_count = 0 #for文の中のfor文の繰り返し回数用変数
startriangle_count =0 #使わない
layer_num_loop2 = 0

Network = set_network(W_ALL[0], B_ALL[0], W_ALL[1], B_ALL[1], W_ALL[2],B_ALL[2],)#３層のネットワークを用意
COUNT=[]
LOSS=[]



#繰り返し処理
for LEARN in range (5): #適当 未定あとできめる　学習回数？？
    print("＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠学習", LEARN+1, "回目開始します＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠")
    Network = set_network(W_ALL[0], B_ALL[0], W_ALL[1], B_ALL[1], W_ALL[2],B_ALL[2],)#３層のネットワークを用意
    Z_ALL, FZ_ALL = forward(Network, in_x) #順伝播

    # 逆伝播
    layer_num_loop1 = layer_num #
    for layer_num_loop1 in range(layer_num, -1, -1):
        print("＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃いま，",layer_num_loop1, "層目を見ています＃＃＃＃＃＃＃＃＃＃＃＃＃＃" )
        # koubai = grad_loss_and_y(layer_num, teach, FZ_ALL[layer_num+1]) #●マークつまりy-tの計算 teachどうしよう，yも場所指定がむずい fz_all[layer_num]とは層数の数番目のfzつまり最後の層の出力を引数にとる
        koubai = grad_loss_and_y(layer_num, teach, FZ_ALL[-1]) #●マークつまりy-tの計算 teachどうしよう，yも場所指定がむずい fz_all[layer_num]とは層数の数番目のfzつまり最後の層の出力を引数にとる
        # layer_num_loop2 = layer_num_loop1
        triangle = first_grad_fz_and_z(layer_num, FZ_ALL, Z_ALL) #最初の▲計算　最初は出力を見るため，layer_num+1で三角をする必要があるため区別する　▲マークつまりシグモイド微分にｚを入れた値が出る計算 
        koubai = np.dot(koubai, triangle)#丸と三角の計算（最初必ず出るペア）

        # layer_num_loop2 = layer_num_loop1
        if loop_count != 0:
            print("これからforを回すぞ")
            for layer_num_loop2 in range(layer_num-1, layer_num-1-loop_count, -1): #watchi
                
                print("★▲繰り返しforを開始します．繰り返す数つまりlayer_num_loop2は ",layer_num-1, "から始まってひとつづつ減りながら", (layer_num-1)-(layer_num-1-loop_count), "回繰り返します．")
                star = grad_z_and_fz(W_ALL,layer_num_loop2) #★マークつまりi番目のｗの行列を返す
                print("star結果↓")
                pprint.pprint(star)
                print("これと↓の勾配")
                pprint.pprint(koubai)
                print("をかけると")
                koubai = np.dot(koubai, star)
                pprint.pprint(koubai)
                print("となる")
                triangle = grad_fz_and_z(layer_num_loop2, FZ_ALL, Z_ALL) #▲マークつまりシグモイド微分にｚを入れた値が出る計算 現在の層の情報が必要なためlayer_num_loop2も引数にとる
                koubai = np.dot(koubai, triangle)#★と▲の計算
                startriangle_count += 1
                # print("今から，▲と★を掛けます．▲は")
                # pprint.pprint(triangle)
                # print("で，★は")
                # pprint.pprint(star)
                # print("です．掛け算すると計算結果は")
                # pprint.pprint(W_ALL) 転地できてるか確認用
                # pprint.pprint(star)
                # pprint.pprint(koubai)
                # pprint.pprint(star)
                # pprint.pprint(koubai)
                # print("6r6666666666666666666")
                # print("fin=", layer_num_loop2)


        print("for文を抜けて，layer_num_loop2=", layer_num_loop2,"になりました．現在の行列は↓")
        pprint.pprint(koubai)
        print("です．さいごに□を一回やります")
        # print("計算前↑，計算後↓")
        # pprint.pprint(koubai)
        square_koubailist = grad_z_and_w(layer_num_loop1, FZ_ALL, W_ALL)
        # print("-----------")
        # print(layer_num_loop1)
        # print("-----------")
        # pprint.pprint(W_ALL[layer_num_loop1])
        print("square_koubailistつまりその層の勾配行列（全て）")
        pprint.pprint(square_koubailist)

        print("それを，全体のWである以下の")
        pprint.pprint(W_ALL)
        print("のうち，今回見てる層つまり", layer_num_loop1, "番目である")
        pprint.pprint(W_ALL[layer_num_loop1])
        print("に代入する．代入前に転置すると")
        square_koubailist = np.transpose(square_koubailist) #代入するために，W＿ALLの形と合わせるために転置する．これは理にかなっていて無理やり形合わせているわけではない
        pprint.pprint(square_koubailist)
        print("となり，Wと形が一致するので，学習率をかけて引くことでWの値を更新する")
        W_ALL[layer_num_loop1] -= square_koubailist*learning_rate #勾配に学習率を掛けたものを引くことで重みを更新し，「学習」する
        print("重みを更新しました.結果↓")
        pprint.pprint(W_ALL)

        loop_count += 1
    loop_count = 0
    
#学習後
pprint.pprint(W_ALL)



