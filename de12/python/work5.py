


for i in range(1,4):print(i,"人目")
name=input("名前を教えてください。")
waist=float(input("腹囲は何センチですか？"))
age=int(input("いくつですか？"))
height=float(input("身長は？"))

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才,身長は",height,"ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")