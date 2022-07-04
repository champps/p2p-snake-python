# summary table draw
X = one byte 
bytes [0, 255] divided by the following

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
| chars               | count | from | to |
|:-------------------:|:-----:|:----:|:--:|
| & ^ % $ # @ ! ? \   |       |      |    |
| { } ( ) [ ] < > « » |       |      |    |
| / * - + = × ÷       |       |      |    |
| … _ – ~             |       |      |    |
| ’ ‘ ' " ` , . : ; ؛ |       |      |    |
| 0 1 2 3 4 5 6 7 8 9 |       |      |    |
|                     |       |      |    |

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
| name of func        | key for func         | parameter range                         | how its work | keys        |
|:-------------------:|:--------------------:|:---------------------------------------:|:------------:|:-----------:|
| char_num ( Byte )   | C ( B )              | 0 <= B >= 255                           | CB           | X=Byte char |
| go table ( Num )    | G ( N )              | 0 <= N >= 255                           | GN           | X=Byte char |
| num repeat ( Char ) | N is [0,?] , N ( C ) | 0 <= C >= 255, C can be other same func | NC, NNC      | X=Byte char |
|                     |                      |                                         |              |             |
### char_num ( Byte ) 
    when find string num convert to byte num if more than tow string num
    
#### example
  
    3 bytes -> 2 bytes 
    "123" -> char_num(123)
     
#### range
    from 0 to 255 one byte (256)
    
#### best use case
    when use 3 string number (3 bytes) use this func to use 2 bytes 
           


### go table ( Num )
    go table num that found in tables file
    
#### example
      char X found in table 3 with key(byte) 65
      go_table(3) then byte char 65
    
#### range
    from 0 to 255 one byte (256)
    
#### best use case
    when use sequential byte string with length ? (wont to study)
   




### num repeat ( Char )
        byte num after byte char 5x = xxxxx
        It can be combined with another repeat function
        
#### example
    5x = x 5 times
    33x = x 33 times
    
    depend to range num byte
    
    can use more than one func 
    
    55(55(55(x))) = 55*55*55 time x 
  
#### range
    from 0 to ?? determine depend the empty byte
    
#### best use case
    when use byte less than repeat fucn byte
   
  




## with tow parameters
| name of func                              | key for func  | parameter range                                              | how its work (no spaces)                        | keys        | use case                                                              |
|:-----------------------------------------:|:-------------:|:------------------------------------------------------------:|:-----------------------------------------------:|:-----------:|:---------------------------------------------------------------------:|
| repeat_char_num_byte ( \*Byte, char )     | R ( B , C )   | 0 <= B >= 255 , C byte char only                             | XX RBC XX, RB...C                               | X=Byte char | repeat char C , B.. times                                             |
| repeat_char_num_byte ( \*Byte, char*2 )   | R ( B , CC )  | 0 <= B >= 255 , CC tow bytes char or func with one parameter | XX RBCC XX, RB..CC                              | X=Byte char | repeat CC , B.. times                                                 |
| repeat_char_num_byte ( Byte, char*3 )     | R ( B , CCC ) | 0 <= B >= 255 , CCC 3 bytes char or func with tow parameter  | RB..CCC                                         | X=Byte char | repeat CCC , B.. times                                                |
| char_escape_2_bytes ( Byte1, Byte2 )      | E (Y, Z)      | 0 <= Y,Z >= 255                                              | XX EYZ XX                                       | X=Byte char | when use unicode char (utf8)                                          |
| remember table no ( Num, Char )           | T ( N, C)     | 0 <= N >= 255 , C byte char or func                          | XX TNC XX, in second time without N -> XX TC XX | X=Byte char | use char from other table and remember the num of it to after use     |
| use char in table ( Num of table , Char ) | U ( N, C)     | 0 <= N >= 255 , C byte char or func                          | XX UNC XX                                       | X=Byte char | if found char in other table or can use escape tow bytes (same coast) |
|                                           |               |                                                              |                                                 |             |                                                                       |
