## compress class

how its work 
Replace Unicode characters with a one-byte character in the table

### sympols
[48] -> english chars

sympols
49 chars
```
 / ‘ * - + = - _ { } ( ) [ ] & ^ % $ # @ ! ~ \\ \"  < > , . ? ؟ : ; × ` ÷ ؛ ، … – « » |  َ  ِ  ً  ٍ  ُ  ٌ  ّ 
 ```
 
 
nums
10 chars
 
arabic chars
28 + "ـ" 
```
أ إ آ ﻷ ﻹ ة ﻻ ﻵ ؤ ء ئ
```
28+ 1+ 11 = 40 chars
 
 
48+49+10+40 = 147 chars


-----
### spical chars

- repeat_chars_num
\#2-10 = 8 chars 

- func char_num X \#chose num from 0 to 255 

- func repeat_char_num_byte X  # x from 0 to 255

- func char_escape_char_2_byte X \#scape unicode char
\#that not use unless all char in table are used and no char to replce with it

- func go_table_num X
\#if there more than one can change it

- go_next_table
\#if no next table go to first one

- go_back_table

- func use_table_num X with char Y
/# all empty bytes use this , and this with remember X
/# if you dont use byte can alias it to other chars 
/# use x only in first time then use it without 
/# best use with alias

- use_previous_table
\# can use it after change table

/# total 158

### using fuctions
can use repeat_char_num_byte(char_esape_char CHAR)

if char repeat more than one time to ten times use repeat_chars_num if more than 10 use func repeat_char_num_byte X

hixxxxxxxxxx = hix10
hixxxxxxxxxxx = hi repeat_char_num_byte(11, x) = hiC11x

if use char out of table and there is chars in table not used and it replce it with not use char in this message only 


-----
### Compression process steps
- find all not use table chars in string(byte list)

- if not find char in this table 
    - search it in other table then go to other table if exsist 3 or more chars in same table if chars is consecutive
    - if not fond use escape unicode char then tow byte 

- find characters that do not exist in the current table
    - find location of this char
        - search other table
        - if not found set unicode tow bytes

    

4- if find 3 or more consecutive chars in other table go_to_table X then return to previous table after end connected chars

2 - Replace the repetition with the repetition numbers or the repetition function

3 - Searching for 2 bytes that are the same, 3 bytes that are the same, and 
4 bytes that are the same, repeated more than once and replace bytes with one char(byte) not use in message exsist in table

if not find chars free, do nothing
