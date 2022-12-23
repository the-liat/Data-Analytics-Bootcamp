# Reading Comic Book Data
import os 
impoer csv
csvpath = os.path.join('C:', 'Users', 'liats', 'git', 'UCD-VIRT-DATA-PT-12-2022-U-LOLC', '03-Python',
'2', 'Activities', '09-Stu_ReadComicBooksCSV', 'Resources', 'comic_books.csv')
with open(csvpath) as csvfile:
    csvreadr = csv.reader(csvfile, delimiter = ',')
    
## Instructions

* Prompt the user for the book title they’d like to search.
find_book = input("Which book title would you like to find? ")

* Search through the `comic_books.csv` to find the user's book.

* If the CSV contains the user's title, then print out the title, the publisher name, and the year it was published.

  * For example: `"Alien was published by DC Comics in 2015"`.

* If the CSV does not contain the user's title, then print out a message telling them that their book could not be found.

    * Set a variable to `False` to check if we found the comic book.

    * In the `for` loop, change the variable to confirm that the comic book is found.

## References

Data modified from "Comic books CSV" Updated April 2021. Initially released in 2014 to accompany the British Library's exhibition Comics Unmasked. [https://www.bl.uk/collection-metadata/downloads](https://www.bl.uk/collection-metadata/downloads)

—

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
