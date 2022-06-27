# not found char in txt
with alias and without alias (other table and utf-8 char)

##  table vs remember vs unicode vs alias

how many byte use in prosses

| use case                              | 1 | 2 | 3 | 4  | 5  | 6  | first coast | coast after first | best case for all | range to use |
|:-------------------------------------:|:-:|:-:|:-:|:--:|:--:|:--:|:-----------:|:-----------------:|:-----------------:|:------------:|
| ues alias escape or table             | 5 | 6 | 7 | 8  | 9  | 10 | 5           | 1                 | if length >= 4    | lenght >= 3  |
| other table with remember             | 3 | 5 | 7 | 9  | 11 | 13 | 3           | 2                 | if length <= 2    | lenght <= 2  |
| use other table one char or utf8 char | 3 | 6 | 9 | 12 | 15 | 18 | 3           | 3                 | if lenght = 1     |              |

la\# dont count alias func because it called one time at end of string

## utf-8 + alias
not used char (1) + escape unicode char (1)+ tow byte (2)
4 byte in first time then only one byte after

## table + alias
not use char (1) + other table key (1)+ num of table (1)+ char (1)
4 chars in first  time


## with use remember change table
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
    - use case wiht 3 chars or more 
- use repeat fucn with num
    - (xxx = R3x) (R is repeat func num) (3 num of repetition) (x is char or func)
    - use case with 4 or more repetition char
-  use  repeat num with alias
    -  in first use ( xxxyxxxyxxx ) -> (mymymAm3x) (A alias key func) (m is char not used) (3 is num of repetition) (x is the char)
        -  in first use will take 3 bytes + (char in txt byte) = 4
        -  second use with take one byte only
- use reapeat func with alias
    - (xxxxAmR4x) = (A alias key func) (m is char not used) (R is repeat func key) (4 num of repetition) (x is the char)
        - alias(not_used_char, wont_to_alias_char)
        - alias(not_used_char, repeat_func(num, char) )
    - use case with 

## without aliasing
the numbers for num of repetition char repeated continuously (xxx not xxyxx Connected Similar Chars) in first time 

| use case                 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 70 | 260 | lower coast                | best case can use (len char continuously) |
|:------------------------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:---:|:--------------------------:|:-----------------------------------------:|
| use raw chars            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 70 | 260 | one byte for each char     | open                                      |
| ues repeat num           |   |   | 2 | 2 | 2 | 2 | 2 | 2 | 2  |     | 2 bytes in range (3,90)    | lenght >= 3 if range in (3,90)            |
| use repeat func with num |   |   |   | 3 | 3 | 3 | 3 | 3 | 3  | 3   | 3 bytes in range (90, 260) | lenght > 90 if range in (90 , 260)        |

we can use repetition byte num to repeat with tow byte range( 0, 9090)

## with aliasing
numbers now after first use 

| use case                            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 70 | 260 | lower coast | coast after first | best range can use                 |
|:-----------------------------------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:---:|:-----------:|:-----------------:|:----------------------------------:|
| use raw chars                       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 70 | 260 | 1           |                   | open                               |
| ues repeat num with alias           |   |   |   |   | 4 | 4 | 4 | 4 | 4  |     | 4           | 1                 | lenght >= 5 if range in (3,90)     |
| use repeat func with num with alias |   |   |   |   |   |   |   |   |    | 5   | 5           | 1                 | lenght > 90 if range in (90 , 260) |

## unicode with repeat

| use case                 | 1 | 2 | 3 | 4  | 5  | 6  | 7  | 8  | 70  | 260 | lower coast                | best case can use (len char continuously) |
|:------------------------:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:--------------------------:|:-----------------------------------------:|
| with raw unicode         | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 210 | 780 | three byte for each char   |                                           |
| with unicode num repeat  |   | 4 | 4 | 4  | 4  | 4  | 4  | 4  | 4   |     | 4 bytes in range (3,90)    |                                           |
| with unicode func repeat |   | 5 | 5 | 5  | 5  | 5  | 5  | 5  | 5   | 5   | 5 bytes in range (90, 260) |                                           |

## unicode with aliasing

| use case                            | 1 | 2 | 3 | 4  | 5  | 6  | 7  | 8  | 70  | 260 | lower coast | coast after first | best range can use                 |
|:-----------------------------------:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:-----------:|:-----------------:|:----------------------------------:|
| with raw unicode                    | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 210 | 780 |             |                   |                                    |
| with unicode num repeat with alias  |   | 4 | 4 | 4  | 4  | 4  | 4  | 4  | 4   |     | 4           | 1                 | lenght >= 3 if range in (3,90)     |
| with unicode func repeat with alias |   |   |   |    |    |    |    |    |     | 5   | 5           | 1                 | lenght > 90 if range in (90 , 260) |


## repeat with num vs repeat func
numbers for num of bytes 


| uese case                         | 1 | 2   | 3     | 4     | 5     | 6     | 7     | 8     | coast               | lower coast | example   | best case to use |
|:---------------------------------:|:-:|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-------------------:|:-----------:|:---------:|:----------------:|
| num repeat fucn                   |   | 100 | 100^2 | 100^3 | 100^4 | 100^5 | 100^6 | 100^7 | len(num)+char       | 2 byte      | 554x      |                  |
| func repeat with num byte (0,255) |   |     | 255   | 255^2 | 255^3 | 255^4 | 255^5 | 255^6 | len(func byte)+char | 3 byte      | R255R255x |                  |



char num to num byte ot use repetition