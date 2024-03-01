import random
print("作ります")
print("")


f = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'w')
f.write('''
<mujoco model="maze">
<worldbody>
    <!--ヘッダー-->
    <body name="base_plate" pos="0.8999999999999999 0.72 0.012">
    <geom type="plane" mass="0.1" size="0.9059999999999999 0.726 0.006" rgba="0.2 0.2 0.2 1" friction="0.0 0.0 0.0"/>
    </body>
        
    <!-- Column 1-->
    <body pos="0.0 0.0 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 2-->
    <body pos="0.18 0.0 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 3-->
    <body pos="0.36 0.0 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    

    <!-- Column 12-->
    <body pos="0.0 0.18 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 13-->
    <body pos="0.18 0.18 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 14-->
    <body pos="0.36 0.18 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 15-->
    <body pos="0.54 0.18 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    


    <!-- Column 24-->
    <body pos="0.18 0.36 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 25-->
    <body pos="0.36 0.36 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 26-->
    <body pos="0.54 0.36 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 27-->
    <body pos="0.72 0.36 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 36-->
    <body pos="0.36 0.54 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 37-->
    <body pos="0.54 0.54 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 38-->
    <body pos="0.72 0.54 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 39-->
    <body pos="0.8999999999999999 0.54 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    

    <!-- Column 48-->
    <body pos="0.54 0.72 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 49-->
    <body pos="0.72 0.72 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 50-->
    <body pos="0.8999999999999999 0.72 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 51-->
    <body pos="1.08 0.72 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>


    <!-- Column 60-->
    <body pos="0.72 0.8999999999999999 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 61-->
    <body pos="0.8999999999999999 0.8999999999999999 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 62-->
    <body pos="1.08 0.8999999999999999 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 63-->
    <body pos="1.26 0.8999999999999999 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    

    <!-- Column 72-->
    <body pos="0.8999999999999999 1.08 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 73-->
    <body pos="1.08 1.08 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 74-->
    <body pos="1.26 1.08 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 75-->
    <body pos="1.44 1.08 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    

    <!-- Column 84-->
    <body pos="1.08 1.26 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 85-->
    <body pos="1.26 1.26 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 86-->
    <body pos="1.44 1.26 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 87-->
    <body pos="1.6199999999999999 1.26 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 88-->
    <body pos="1.7999999999999998 1.26 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>


    <!-- Column 96-->
    <body pos="1.26 1.44 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 97-->
    <body pos="1.44 1.44 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 98-->
    <body pos="1.6199999999999999 1.44 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>

    <!-- Column 99-->
    <body pos="1.7999999999999998 1.44 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>
''')
f.close() #わざわざ閉じる必要はなさそう？

#ヘッダーを書いたから次は壁を書く

f2 = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'a')



# 50%の確率で壁を作る
if random.random() < 0.65:
  f2.write('''
    <body pos="0.09 0.0 0.037">
        <body pos="0 0 -0.0005">
            <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
        </body>
        
        <body pos="0 0 0.0245">
            <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
        </body>
    </body>
          ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.27 0.0 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
            <body pos="0.09 0.18 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.44999999999999996 0.18 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.27 0.36 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.63 0.36 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.44999999999999996 0.54 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.8099999999999999 0.54 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.63 0.72 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.9899999999999999 0.72 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.8099999999999999 0.8999999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.1700000000000002 0.8999999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.9899999999999999 1.08 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.35 1.08 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.1700000000000002 1.26 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.53 1.26 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.71 1.26 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.35 1.44 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.53 1.44 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.71 1.44 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.0 0.09 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.36 0.09 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.18 0.27 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.54 0.27 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.36 0.44999999999999996 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.72 0.44999999999999996 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.54 0.63 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.8999999999999999 0.63 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.72 0.8099999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.08 0.8099999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="0.8999999999999999 0.9899999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.26 0.9899999999999999 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.08 1.1700000000000002 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.44 1.1700000000000002 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.26 1.35 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
        ''')

if random.random() < 0.65:
  f2.write('''
  <body pos="1.7999999999999998 1.35 0.037">
      <body pos="0 0 -0.0005">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
      </body>
      
      <body pos="0 0 0.0245">
          <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
      </body>
  </body>
      ''')

f2.close()

f3 = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'a')
f3.write(
'''  </worldbody>
</mujoco>
''')

f3.close()

print("出力しました")



def random_wall_create():
    print("作ります")
    print("")


    f = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'w')
    f.write('''
    <mujoco model="maze">
    <worldbody>
        <!--ヘッダー-->
        <body name="base_plate" pos="0.8999999999999999 0.72 0.012">
        <geom type="plane" mass="0.1" size="0.9059999999999999 0.726 0.006" rgba="0.2 0.2 0.2 1" friction="0.0 0.0 0.0"/>
        </body>
            
        <!-- Column 1-->
        <body pos="0.0 0.0 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 2-->
        <body pos="0.18 0.0 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 3-->
        <body pos="0.36 0.0 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        

        <!-- Column 12-->
        <body pos="0.0 0.18 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 13-->
        <body pos="0.18 0.18 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 14-->
        <body pos="0.36 0.18 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 15-->
        <body pos="0.54 0.18 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        


        <!-- Column 24-->
        <body pos="0.18 0.36 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 25-->
        <body pos="0.36 0.36 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 26-->
        <body pos="0.54 0.36 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 27-->
        <body pos="0.72 0.36 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 36-->
        <body pos="0.36 0.54 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 37-->
        <body pos="0.54 0.54 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 38-->
        <body pos="0.72 0.54 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 39-->
        <body pos="0.8999999999999999 0.54 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        

        <!-- Column 48-->
        <body pos="0.54 0.72 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 49-->
        <body pos="0.72 0.72 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 50-->
        <body pos="0.8999999999999999 0.72 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 51-->
        <body pos="1.08 0.72 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>


        <!-- Column 60-->
        <body pos="0.72 0.8999999999999999 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 61-->
        <body pos="0.8999999999999999 0.8999999999999999 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 62-->
        <body pos="1.08 0.8999999999999999 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 63-->
        <body pos="1.26 0.8999999999999999 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        

        <!-- Column 72-->
        <body pos="0.8999999999999999 1.08 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 73-->
        <body pos="1.08 1.08 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 74-->
        <body pos="1.26 1.08 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 75-->
        <body pos="1.44 1.08 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        

        <!-- Column 84-->
        <body pos="1.08 1.26 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 85-->
        <body pos="1.26 1.26 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 86-->
        <body pos="1.44 1.26 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 87-->
        <body pos="1.6199999999999999 1.26 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 88-->
        <body pos="1.7999999999999998 1.26 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>


        <!-- Column 96-->
        <body pos="1.26 1.44 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 97-->
        <body pos="1.44 1.44 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 98-->
        <body pos="1.6199999999999999 1.44 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>

        <!-- Column 99-->
        <body pos="1.7999999999999998 1.44 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>
    ''')
    f.close() #わざわざ閉じる必要はなさそう？

    #ヘッダーを書いたから次は壁を書く

    f2 = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'a')



    # 50%の確率で壁を作る
    if random.random() < 0.65:
      f2.write('''
        <body pos="0.09 0.0 0.037">
            <body pos="0 0 -0.0005">
                <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
            </body>
            
            <body pos="0 0 0.0245">
                <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
            </body>
        </body>
              ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.27 0.0 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
                <body pos="0.09 0.18 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.44999999999999996 0.18 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.27 0.36 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.63 0.36 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.44999999999999996 0.54 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.8099999999999999 0.54 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.63 0.72 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.9899999999999999 0.72 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.8099999999999999 0.8999999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.1700000000000002 0.8999999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.9899999999999999 1.08 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.35 1.08 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.1700000000000002 1.26 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.53 1.26 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.71 1.26 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.35 1.44 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.53 1.44 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.71 1.44 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.0 0.09 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.36 0.09 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.18 0.27 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.54 0.27 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.36 0.44999999999999996 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.72 0.44999999999999996 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.54 0.63 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.8999999999999999 0.63 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.72 0.8099999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.08 0.8099999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="0.8999999999999999 0.9899999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.26 0.9899999999999999 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.08 1.1700000000000002 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.44 1.1700000000000002 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.26 1.35 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
            ''')

    if random.random() < 0.65:
      f2.write('''
      <body pos="1.7999999999999998 1.35 0.037">
          <body pos="0 0 -0.0005">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0245" rgba="1 1 1 1"/>
          </body>
          
          <body pos="0 0 0.0245">
              <geom type="box" mass="0.01" size="0.006 0.093 0.0005" rgba="1 0 0 1"/>
          </body>
      </body>
          ''')

    f2.close()

    f3 = open('c:/Users/atusi/anaconda3/envs/gymenv/Lib/site-packages/gymnasium/envs/mujoco/assets/my_xmls/randomwall_gen.xml', 'a')
    f3.write(
    '''  </worldbody>
    </mujoco>
    ''')

    f3.close()

    print("出力しました")

