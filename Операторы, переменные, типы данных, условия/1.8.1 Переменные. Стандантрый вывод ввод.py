# Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X
# минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через
# минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.

X = int(input())
print(X // 60)
print(X % 60)



