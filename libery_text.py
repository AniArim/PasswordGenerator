import random

libery_text = """ A Palestinian child mourns over the death of his father and brother
who were killed kakamsgmduring Israeli sdefghijklmnopqrastuwvxyzairstrike yesterday in Gaza What fictional character 
should have been hit with a hugelawsuit at the end of the story million people sign up for Affordable Care Act 
coverage after Biden regragagjlqrerokejkmxfawhjkolsopens exchangemoneyintendedfor nature and environment projects 
disappeared into the pockets of Romanian politiciansIf your opposed to public money being spent on a 
oyal yacht please sign and shareestimated this yacht could costabsdefghijklmnopqrastuwvxyz
""".lower()
libery_text = libery_text.lower()
libery_text = libery_text.replace(" ", "")
libery_text_final = libery_text.replace("\n", "")

libery_numbers_final = []
for i in range(100):
    libery_numbers_final.append(random.randint(0,9))

libery_numbers_final = "".join(str(libery_numbers_final))
libery_numbers_final = libery_numbers_final.strip('[]')
libery_numbers_final = libery_numbers_final.replace(" ", "")
libery_numbers_final = libery_numbers_final.replace(",", "")

libery_symbol = [r'_', '-', '!', '#', '$', '%', '&', '*', '+', '-', '.',  '/', ':', '@', '^', '~']





