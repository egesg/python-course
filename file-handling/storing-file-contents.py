import random

f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")

print(f_content_list)
# ['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']

print(random.choice(f_content_list))
# Gizmo