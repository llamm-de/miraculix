"""
Example 1 - Making your own scripts with miraculix

This short script will guide you through the process of writing your own scripts using the
Miraculix framework. It covers the creation of an examination as well as the automated generation
of protocols etc.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""

""" 
1. Import all necessary packages
"""
from miraculix.exam import Exam
from miraculix.protocols import Protocol

""" 
2. Create a new exam object

After you have downloaded the list of participants from RWTHOnline, you can use this .csv file
to create your new exam.
"""
exam = Exam(r'D:\work\Lehre\MechanikAGW\participants.csv')

"""
3. Assign number of points per task

Besides the already imported information, you also have to assign the number of point which can
be achieved for each task.
"""
exam.Points_per_task = [63]

"""
4. Assign rooms for examination

Now you can assign the participants to the booked rooms. By default they will be assigned via
their matriculation number in ascending order. Rooms will be filled using an offset of 5 seats 
starting with the room of highest capacity. 
"""
exam.assign_participants()

"""
5. Create protocols and participant lists

This will automatically generate protocols and the associated participant list for every room.
Protocols are provided in Microsoft Word .docx format.
"""
protocol = Protocol(exam)
protocol.make_protocol(r'D:\work\Lehre\MechanikAGW\Protocol.docx')

"""
6. Create and export rating list

To record the points for every student, you can generate an easy to use .csv file for your exam.
After creating this file, you can open it in Microsoft Excel or Libre/OpenOffice to fill in the 
points achieved for every participant.
If you wish, you can also calculate the final grades within your spreadsheet software. Otherwise,
you can also use the build in functionality of Miraculix as will be described in example_2.py.
"""
exam.export_rating_list(r'D:\work\Lehre\MechanikAGW\Rating_list.csv')

"""
7. Save examination
"""
exam.save_exam(r'D:\work\Lehre\MechanikAGW\exam.json')