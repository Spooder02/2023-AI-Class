grade = ["A", "B", "C", "D", "E", "F"]

score = int(input("점수를 입력하세요: "))
for i in range(0, len(grade)):
    scoreRange = (9-i)*10
    if (score < 59):
        print("당신의 성적은 F입니다.")
        break
    if (score >= scoreRange):
        print("당신의 성적은 "+ grade[i] +"입니다")
        break
    else:
        continue
