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



### spical chars 

- go_next_table
\#if no next table go to first one

- go_back_table

- use_previous_table
\# can use it after change table


### spical func (use byte or more after use it) 

- repeat_chars_num [2..10] X
\#2-10 = 8 chars 
\# func use num then X (char)
\# not use one because u can use char directly without add more bytes :|

- func char_num X \#chose num from 0 to 255 
\# for save string char num to byte char num 
\# "1"+"2"+"3"= B+B+B vs char_num 123 = B+B

- func repeat_char_num_byte X  # x from 11 to 267
\# we use already have reapeat num from 2 to 10

- func char_escape_char_2_byte XY \#scape unicode char
\#that not use unless all char in table are used and no char to replce with it

- func go_table_num X
\#if there more than one can change it

- func remember table table_no no_of_char
\# table no only in first time then use with no_of_char_only

- func use_table_num X with char Y
/# best use with alias


\# fuction can use other func as X

/# total 158

-----
### Compression process steps
- find all not use table chars in string(byte list)
- specifies the number of times a char is repeated in the text in a dict {X:1, Y:5...}

- if find char not in this table 
    - search it in other table and save the result in dict {table_num:num_char=char ..}
    - save the not found in the table in dict {X:BB, Y:BB1} :- B is Byte. y is uincode char
    
- find repetition
    - use byte repeat num (one byte)
    - use func repeat with num (2 bytes)
 
choosing the best case in each case
