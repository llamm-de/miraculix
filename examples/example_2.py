"""
Example 2 - Making your own scripts with miraculix

This examples shows you how to do simple automated evaluation of your examination.
To work on this example, you first need to run example_1.py.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""

""" 
1. Import all necessary packages
"""
from miraculix.exam import Exam
from miraculix.evaluator import Evaluator

""" 
2. Load examination from file and import ratings

After saving the examination from example_1 to a .json file, we can now load the stored data
into a new exam object. If you have already recorded the scores of each participant within the
exported list from example_1, you can also import these scores now.
"""
exam = Exam()
exam.load_exam('./Kontiklausur/exam.json')
exam.import_rating_list('./Kontiklausur/Ratings.csv')

"""
3. Evaluate your exam

If you did do the evaluation within your desired spreadsheet software, you can easily skip this
section. Otherwise, you can now use the build in evaluation tool to evaluate your examination.
All you need to provide is the scoring thresholds for your passing grade (4.0) and for the excellent
grade (1.0). By default, these values are set to 50% and 90%.
"""
eval = Evaluator(exam)
eval.evaluate(0.5, 0.9)

"""
4. Save examination
"""
exam.save_exam('./Kontiklausur/exam.json')

"""
5. Export data to RWTHOnline file

Finally, you can write the results of your examination to the file you downloaded from RWTHOnline.
Once this is done, you can easily upload this file in RWTHOnline and your examination process is 
done. Congratulations!
"""
exam.export_data_RWTHOnline(file='./Kontiklausur/Participants_RTWHOnline.csv')
