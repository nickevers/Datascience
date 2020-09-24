import pandas
import numpy as py
import matplotlib.pyplot as plt
from itertools import islice


wat_is_dit = "D:/Downloads/watisdit.txt"


def calc_highest_lowest(_score, highest_score, lowest_score):
    highest_score = _score if _score > highest_score else highest_score
    lowest_score = _score if _score < lowest_score else lowest_score
    return highest_score, lowest_score


highest = 0
lowest = 999
quality_score = {}
seq_id = ""
seq = ""
quality = ""
with open(wat_is_dit, 'r') as file:
    i = 0
    # count = 0
    for line in file:
        if i == 0:
            seq_id = line
            i += 1
        elif i == 1:
            # seq = line
            i += 1
        elif i == 2:
            i += 1
        elif i == 3:
            quality = line
            score = py.mean([ord(ch) for ch in quality])
            highest, lowest = calc_highest_lowest(score, highest, lowest)
            quality_score[seq_id] = score
            i = 0
        # count += 1
        # Debug amount of lines to read from file
        # if count >= 8000000:
        #     break


print(f"Highest score is: {highest}")
print(f"Lowest score is: {lowest}")


# 2)Retourneer een sequentie op basis van een sequentie ID.
# 5)Filter het bestand op basis van een PhredScore (Threshold>9, of hoger).
# 6)Sorteer het bestand op basis van PhredScore.
# 7)Plotdedistributie van alle gevonden PhredScores in een histogram.

plt.hist(quality_score.values(), bins='auto')  # arguments are passed to np.histogram
plt.title("Score %")
plt.yscale('log', nonpositive='clip')
plt.show()

