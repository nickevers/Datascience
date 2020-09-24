import pandas
import numpy as py
import matplotlib.pyplot as plt

seq = "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
quality = "!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"

wat_is_dit = ""

# 1)Lees het bestand. Kan ik het bestand raadplegen? Hoe doe ik dat efficiënt?
# 2)Retourneer een sequentie op basis van een sequentie ID.
# 3)Bereken de Phredscore voor iedere Read (gebruik het gemiddelde in alle vragen).
# 4)Retourneer de sequentie met hoogste / laagste PhredScore.
# 5)Filter het bestand op basis van een PhredScore (Threshold>9, of hoger).
# 6)Sorteer het bestand op basis van PhredScore.
# 7)Plotdedistributie van alle gevonden PhredScores in een histogram.