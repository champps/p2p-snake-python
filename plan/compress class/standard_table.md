# summary table draw

| from location | to location | count | command/chars                                       |
|:-------------:|:-----------:|:-----:|:---------------------------------------------------:|
| 0             | 51          | 51    | a-z and A-Z                                         |
| 48            | 96          | 49    | sympols                                             |
| 97            | 106         | 10    | char nums "0-9"                                     |
| 107           | 146         | 40    | arabic chars with special symbols and special chars |
| 147           | 149         | 3     | spical chars (functions without parameter)          |
| 150           | 155         | 6     | spical func ( use byte as parameter)                |
| 156           | 256         | 100   | num byte                                            |



# byte chars

##  english chars
| chars                      | count | from | to |
|:--------------------------:|:-----:|:----:|:--:|
| abcdefghijklmnopqrstuvwxyz | 26    | 0    | 25 |
| ABCDEFGHIJKLMNOPQRSTUVWXYZ | 26    | 26   | 51 |
|                            |       |      |    |

## sympols
| chars                  | count | from | to |
|:----------------------:|:-----:|:----:|:--:|
|  | & ^ % $ # @ ! ? \ 
 |       |      |    |
| { } ( ) [ ] < > « »    |       |      |    |
|  / * - + = × ÷         |       |      |    |
| … _ – ~                |       |      |    |
| ’ ‘ ' " ` , . : ; ؛    |       |      |    |
| 0 1 2 3 4 5 6 7 8 9    |       |      |    |
|                        |       |      |    |

## arabic char
| chars                                                     | count | from | to |
|:---------------------------------------------------------:|:-----:|:----:|:--:|
| ، َ  ِ  ً  ٍ  ُ  ٌ  ّ  ْ ؛                                |       |      |    |
| ـ ؟ أ إ آ ﻷ ﻹ ة ﻻ ﻵ ؤ ء ئ 
                               |       |      |    |
|  ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ  ف ق ك ل م ن ه و ي |       |      |    |
|                                                           |       |      |    |

# byte fucntions

## without parameters
| name of func       | key for func | how its work | keys        | use case                           | from  | to  |
|:------------------:|:------------:|:------------:|:-----------:|:----------------------------------:|:-----:|:---:|
| go_next_table      | G            | XXGXX        | X=Byte char | go to next table                   |       |     |
| go_back_table      | B            | XXBXX        | X=Byte char | go to back table                   |       |     |
| use_previous_table | P            | XXPXX        | X=Byte char | go to previouse table if chage it  |       |     |
|                    |              |              |             |                                    |       |     |

## with one parameters
| name of func      | key for func | parameter range | how its work | keys        | use case                                                             | from | to |
|:-----------------:|:------------:|:---------------:|:------------:|:-----------:|:--------------------------------------------------------------------:|:----:|:--:|
| char_num ( Byte ) | C ( B )      | 0 <= B >= 255   | XXCBXX       | X=Byte char | when find string num convert to byte num if more than tow string num |      |    |
| go table ( Num )  | G ( N )      | 0 <= N >= 255   | XXGNXX       | X=Byte char | go table num that found in tables file                               |      |    |
|                   |              |                 |              |             |                                                                      |      |    |
- repeat_chars_num [2..10] X
\#2-10 = 8 chars 
\# func use num then X (char)
\# not use one because u can use char directly without add more bytes :|

<!-- - func char_num X \#chose num from 0 to 255 
\# for save string char num to byte char num 
\# "1"+"2"+"3"= B+B+B vs char_num 123 = B+B -->

<!-- - func repeat_char_num_byte X  # x from 11 to 267
\# we use already have reapeat num from 2 to 10 -->

<!-- - func char_escape_char_2_byte XY \#scape unicode char
\#that not use unless all char in table are used and no char to replce with it -->

<!-- - func go_table_num X
\#if there more than one can change it -->

<!-- - func remember table table_no no_of_char
\# table no only in first time then use with no_of_char_only -->

- func use_table_num X with char Y
/# best use with alias


\# fuction can use other func as X

/# total 158

## with tow parameters
| name of func                         | key for func | parameter range                                    | how its work (no spaces)                         | keys        | use case                          | from | to |
|:------------------------------------:|:------------:|:--------------------------------------------------:|:------------------------------------------------:|:-----------:|:---------------------------------:|:----:|:--:|
| repeat_char_num_byte ( Byte, char )  | R ( B , C )  | 0 <= B >= 255 or repeat func , C byte char or func | XX RBC XX                                        | X=Byte char | repeat char C , B times           |      |    |
| char_escape_2_bytes ( Byte1, Byte2 ) | E (Y, Z)     | 0 <= Y,Z >= 255                                    | XX EYZ XX                                        | X=Byte char | when use unicode char (utf8)      |      |    |
| remember table no ( Num, Char )      | T ( N, C)    | 0 <= N >= 255 , C byte char or func                | XX TNC XX, in second time without N -> XX TC XX  | X=Byte char | go to previouse table if chage it |      |    |
|                                      |              |                                                    |                                                  |             |                                   |      |    |


in function put num byte function can take char or other num byte as 30(30(x)) = 3030x that range wase so wide compared to use one byte repeat func (this is note for me dot in docs)