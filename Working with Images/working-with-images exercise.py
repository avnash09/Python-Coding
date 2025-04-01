from PIL import Image
import os

cwd = "c:/Users/Avinash_Anand/OneDrive - Dell Technologies/Documents/Learning/Python/Udemy/Notes & Learnings/Python-Coding/working-with-images exercise.py"

work_dir = "c:/Users/Avinash_Anand/OneDrive - Dell Technologies/Documents/Learning/Python/Udemy/Complete-Python-3-Bootcamp-master/14-Working-with-Images"

for files in os.listdir(work_dir):
    pass #print(files)

word_matrix = Image.open(work_dir+'/word_matrix.png')
mask = Image.open(work_dir+'/mask.png')

word_matrix.show()
mask.show()