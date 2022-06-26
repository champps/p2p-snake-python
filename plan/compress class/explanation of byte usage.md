# not found char in txt
with alias and without alias (other table and utf-8 char)

how many byte use in prosses

| use case                              | 1 | 2 | 3 | 4  | 5  | 6  | first coast | coast after first | best case for all | plan to use |
|:-------------------------------------:|:-:|:-:|:-:|:--:|:--:|:--:|:-----------:|:-----------------:|:-----------------:|:-----------:|
| ues alias escape or table             | 5 | 6 | 7 | 8  | 9  | 10 | 5           | 1                 | if length >= 4    | lenght >= 3 |
| other table with remember             | 3 | 5 | 7 | 9  | 11 | 13 | 3           | 2                 | if length <= 2    | lenght <= 2 |
| use other table one char or utf8 char | 3 | 6 | 9 | 12 | 15 | 18 | 3           | 3                 | if lenght = 1     |             |

la\# dont count alias func because it called one time at end of string

utf-8 + alias
not used char (1) + escape unicode char (1)+ tow byte (2)
4 byte in first time then only one byte after

table + alias
 char in txt (1) /not use char (1) + other table key (1)+ num of table (1)+ char (1)
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

# repeat chars
there is three ways
- use repeat num (xxx = 3x)
    - first use add Byte and remove duplicate
    - use case from 2 char to 
- use repeat key with num (xxx = R3x)