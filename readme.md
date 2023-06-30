# 3bitの2進数を１０進数に分類するニューラルネットワーク
## 作戦
・パラメータのリストをランダムに作成→→ニューラルネットワークの構造を作る（Network）   
・順伝播する  
・そのニューラルネットワークと同じものを複製する（Network1）  
・複製したネットワークのパラメータ１つを少し増やして順伝播して、誤差（損失）を取得(loss1)   
・もう一つ複製して、今度はパラメータの１つを少し減らして順伝播して、誤差（損失）を取得  (loss2)
・得た２つの誤差loss1,loss2を利用して、微小区間の変化量を求めてそこから損失関数の傾きを求める(つまり微分)  
・その傾き×学習率の値だけ、パラメータを調整する

各パラメータの微分値（勾配）を、１つずつリスト（koubai_list）に入れていく。 
完成したら、現在のパラメータのリストと、微分して求めた値のリスト（koubai_list）は同じ形なので、更新するところで引き算すれば、新たなパラメータのリストができる。  
そのリストでニューラルネットを作り、  
順伝播して・・  

を繰り返す  

## 失敗リスト
・関数「bibun_numerical_gradient」の引数の順番を逆にしていたため、勾配を降下せず上ってしまっていた  
・Pythonのリストとnp.arrayの違いがわかってなかった（listはどんな型でも並べられる。np.arrayは数値で、高速計算ができて、しかも要素全体に対する計算などを楽に書ける）  
・配列の形を整えず計算していたため変な結果が出た  
・パラメータを更新する部分がちゃんとできていなかった  
等

## 今後
・誤差逆伝播の実装による勾配計算の高速化、通常と速度がどのくらい違うか検証
