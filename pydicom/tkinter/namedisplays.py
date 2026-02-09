# DICOM standard definitions (VR): https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html
# Standard 2013

from pydicom.valuerep import PersonName

import tkinter

root = tkinter.Tk()

person_names = [
    PersonName.from_named_components(
        family_name='Yan',
        given_name='XiaoDong',
        encodings=['iso8859','UTF-8']
        )      

]

for person_name in person_names:
    label = tkinter.Label(text=person_name)
    label.pack()
root.mainloop()