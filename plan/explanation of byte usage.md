how many byte use in prosses

not found char 

___

| use case                  | 1 | 2 | 3 | 4  | 5  | 6  | uses bytes after first | low coast | step low coast vs down           | sammary        |
|:-------------------------:|:-:|:-:|:-:|:--:|:--:|:--:|:----------------------:|:---------:|----------------------------------|----------------|
| ues alias escape          | 5 | 6 | 7 | 8  | 9  | 10 | 1                      | 1         |  step >4 with 2, step > 3 with 3 | if length >= 4 |
| use alias table           | 5 | 6 | 7 | 8  | 9  | 10 | 1                      | 1         |                                  |                |
| other table with remember | 3 | 5 | 7 | 9  | 11 | 13 | 2                      | 2         | step <2 with 1                   | if length <= 2 |
| other table               | 3 | 6 | 9 | 12 | 15 | 18 | 3                      | 3         | step <1 with 1 and 2             | if length      |
| escape char               | 3 | 6 | 9 | 12 | 15 | 18 | 3                      | 3         |                                  |                |
use alias alias key (1)+ not used char (1) + escape unicode char (1)+ tow byte (2)
5 byte in fest time then only one byte after

use alias alias key (1)+ not use char (1) + other table key (1)+ num of table (1)+ char (1)
5 chars in first  time

with use remember change table
on first key table (1)+ num table (1) + num of char (1)
on second key table(1) + num of char(1)

----

result 
with alias is best saving bytes if find bytes not used
then if not find the second choice is key remembers table number
	if no empty table key remember table number
		use change table or unicode key 
