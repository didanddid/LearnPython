# Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи в H часов и
# M минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через
# X минут после того, как она ляжет спать.
# На стандартный ввод, каждое в своей строке, подаются значения X, H и M.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.#
X = int(input())
H = int(input())
M = int(input())
H2 = (H + X // 60) + ((M + X % 60) // 60)
M2 = (M + X % 60) - (((M + X % 60) // 60) * 60)
print(H2)
print(M2)

