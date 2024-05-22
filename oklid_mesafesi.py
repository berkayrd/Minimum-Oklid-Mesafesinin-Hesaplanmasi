import math

# Noktaların Tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]


# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def oklidMesafesi(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


# Mesafelerin Hesaplanması
mesafe = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = oklidMesafesi(points[i], points[j])
        mesafe.append(dist)


# Minimum Mesafenin Bulunması
min_mesafe = min(mesafe)
print("Minimum Mesafe:", min_mesafe)

