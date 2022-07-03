# summary table draw

| from location | to location | count | command/chars                                       |
|:-------------:|:-----------:|:-----:|:---------------------------------------------------:|
| 0             | 51          | 51    | a-z and A-Z                                         |
|               |             |       | sympols                                             |
|               |             |       | char nums "0-9"                                     |
|               |             |       | arabic chars with special symbols and special chars |
|               |             |       | spical chars (functions without parameter)          |
| 150           |             |       | spical func ( use byte as parameter)                |
|               |             |       | num byte                                            |



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

## arabic char
| chars                                                     | count | from | to |
|:---------------------------------------------------------:|:-----:|:----:|:--:|
| ، َ  ِ  ً  ٍ  ُ  ٌ  ّ  ْ ؛                                |       |      |    |
| ـ ؟ أ إ آ ﻷ ﻹ ة ﻻ ﻵ ؤ ء ئ ||||
|  ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ  ف ق ك ل م ن ه و ي |       |      |    |
|                                                           |       |      |    |

# byte fucntions

## without parameters
| name of func       | key for func | how its work | keys        | use case                           |
|:------------------:|:------------:|:------------:|:-----------:|:----------------------------------:|
| go_next_table      | G            | XXGXX        | X=Byte char | go to next table                   |
| go_back_table      | B            | XXBXX        | X=Byte char | go to back table                   |
| use_previous_table | P            | XXPXX        | X=Byte char | go to previouse table if chage it  |
|                    |              |              |             |                                    |

## with one parameters
| name of func        | key for func          | parameter range                         | how its work | keys        | use case                                                                |
|:-------------------:|:---------------------:|:---------------------------------------:|:------------:|:-----------:|:-----------------------------------------------------------------------:|
| char_num ( Byte )   | C ( B )               | 0 <= B >= 255                           | XXCBXX       | X=Byte char | when find string num convert to byte num if more than tow string num    |
| go table ( Num )    | G ( N )               | 0 <= N >= 255                           | XXGNXX       | X=Byte char | go table num that found in tables file                                  |
| num repeat ( Char ) | N is [0,50] , N ( C ) | 0 <= C >= 255, C can be other same func | XXNC, XXNNC  | X=Byte char | that byte use like num 5a that mean a 5 times, 55a that mean a 55 times |
|                     |                       |                                         |              |             |                                                                         |

## with tow parameters
| name of func                              | key for func | parameter range                                    | how its work (no spaces)                         | keys        | use case                                                              |
|:-----------------------------------------:|:------------:|:--------------------------------------------------:|:------------------------------------------------:|:-----------:|:---------------------------------------------------------------------:|
| repeat_char_num_byte ( Byte, char )       | R ( B , C )  | 0 <= B >= 255 or repeat func , C byte char or func | XX RBC XX                                        | X=Byte char | repeat char C , B times                                               |
| char_escape_2_bytes ( Byte1, Byte2 )      | E (Y, Z)     | 0 <= Y,Z >= 255                                    | XX EYZ XX                                        | X=Byte char | when use unicode char (utf8)                                          |
| remember table no ( Num, Char )           | T ( N, C)    | 0 <= N >= 255 , C byte char or func                | XX TNC XX, in second time without N -> XX TC XX  | X=Byte char | use char from other table and remember the num of it to after use     |
| use char in table ( Num of table , Char ) | U ( N, C)    | 0 <= N >= 255 , C byte char or func                | XX UNC XX                                        | X=Byte char | if found char in other table or can use escape tow bytes (same coast) |
|                                           |              |                                                    |                                                  |             |                                                                       |
