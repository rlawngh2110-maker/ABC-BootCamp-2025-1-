h=input("키를 입력하시오 : ")
w=input("몸무게를 입력하시오 : ")
height=float(h) / 100
weight=float(w)

bmi=weight/(height)**2
print(f"당신의 BMI 수치는 {bmi}입니다.")
