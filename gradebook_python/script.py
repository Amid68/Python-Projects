last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "history", "poetry"]
grades = [98, 90, 96, 100]

gradebook = [
    ["physics", 98],
    ["calculus", 90],
    ["history", 96],
    ["poetry", 100]
]


gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] += 5
gradebook[3].remove(100)
gradebook[3].append("Pass")

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
