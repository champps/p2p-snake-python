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
   
  


***
## with tow parameters

key X = Byte char

| name of func                              | key for func | prameter range                    | nano example  |
|:-----------------------------------------:|:------------:|:---------------------------------:|:-------------:|
| char_escape_2_bytes ( Byte1, Byte2 )      | E (Y, Z)     | Y, Z [0,255]                      | EYZ           |
|                                           |              |                                   |               |
| remember table no ( Num, Char )           |  T ( N, C)   | N  [0,255] , C byte char or func  | 1> TNC 1+> TC |
| use char in table ( Num of table , Char ) | U ( N, C)    | N  [0,255] , C byte char or func  | UNC           |
|                                           |              |                                   |               |




|:-----------------------------------------:|:-------------:|:-----------------------------------------------------------:|:-----------------------------------------------:|:---------------------------------------------------------------------:|
| remember table no ( Num, Char )           | T ( N, C)     | 0 <= N >= 255 , C byte char or func                         | XX TNC XX, in second time without N -> XX TC XX | use char from other m other t and remember the num of it to after use     |
| use char in table ( Num of table , Char ) | U ( N, C)     | 0 <= N >= 255 , C byte char or func                         | XX UNC XX                                       | if found char in other table or can use escape tow bytes (same coast) |

repeat char
| name of func                                 | key for func  | parameter range | nano example | use byte |
|:--------------------------------------------:|:-------------:|:---------------:|:------------:|:--------:|
| repeat_char_num_byte ( Byte, char )          | R ( B , C )   | B, C [0,255]    | RBC          | 3        |
| repeat_char_num_byte ( Byte, char*2 )        | R ( B , CC )  | B, C [0,255]    | RBCC         | 4        |
| repeat_char_num_byte ( Byte, char*3 )        | R ( B , CCC ) | B [0,255]       | RBCCC        | 5        |
|                                              |               |                 |              |          |
| repeat_char_num_byte (NumOfByte, Byte ,Char) | R(N B C)      | N, B, C [0,255] | RNB..C       | 3+N      |
| repeat_char_num_byte (NumOfByte, Byte, )     | R(N B CC)     | N, B, C [0,255] | RNB..CC      | 4+N      |
| repeat_char_num_byte (NumOfByte, B,CC)       | R(N B CCC)    | N, B, C [0,255] | RNB..CC      | 5+N      |
|                                              |               |                 |              |          |
| repeat char e power( power, char )           | E(P, C)       | P, C [0,255]    | EPC          | 3        |
| repeat string e power( power, char*2 )       | E(P, CC)      | P, C [0,255]    | EPCC         | 4        |
| repeat string e power( power, char*3 )       | E(P, CCC)     | P, C [0,255]    | EPCCC        | 5        |
|                                              |               |                 |              |          |
| repeat string 2 power( power, char )         | T(P, C)       | P, C [0,255]    | TPC          | 3        |
| repeat string 2 power( power, char*2 )       | T(P, CC)      | P, C [0,255]    | TPCC         | 4        |
| repeat string 2 power( power, char*3 )       | T(P, CCC)     | P, C [0,255]    | TPCCC        | 5        |
|                                              |               |                 |              |          |
| repeat string N power(base, power, char )    | N(B, P, C)    | B, P, C [0,255] | NB..PC       | 3+N      |
| repeat string N power(base, power, char*2)   | N(B, P, CC)   | B, P, C [0,255] | NB..PCC      | 4+N      |
| repeat string N power(base, power, char*3)   | N(B, P, CCC)  | B, P, C [0,255] | NB..PCCC     | 6+N      | 

CCC 3 bytes char or func with tow param
CC 2byte char or func with one param

string char
| name of func                              | key for func | parameter range | nano example | use byte |
|:-----------------------------------------:|:------------:|:---------------:|:------------:|:--------:|
| char_num_byte ( Byte)                     | M ( B )      | B [0,255]       | MB           | 2        |
|                                           |              |                 |              |          |
| char_num_byte (NumOfByte, Byte)           | M(N, B..)    | N, B [0,255]    | MNB..        |          |
|                                           |              |                 |              |          |
| num string e power( power, char )         | E(P, C)      | P, C [0,255]    |              |          |
| num string e power( power, char*2 )       | E(P, CC)     | P, C [0,255]    |              |          |
| num string e power( power, char*3 )       | E(P, CCC)    | P, C [0,255]    |              |          |
|                                           |              |                 |              |          |
| num string 2 power( power, char )         | T(P, C)      | P, C [0,255]    |              |          |
| num string 2 power( power, char*2 )       | T(P, CC)     | P, C [0,255]    |              |          |
| num string 2 power( power, char*3 )       | T(P, CCC)    | P, C [0,255]    |              |          |
|                                           |              |                 |              |          |
| num string N power( base, power, char )   | N(B, P, C)   | B, P, C [0,255] |              |          |
| num string N power( base, power, char*2 ) | N(B, P, CC)  | B, P, C [0,255] |              |          |
| num string N power( base, power, char )   | N(B, P, CCC) | B, P, C [0,255] |              |          |

###  repeat_char_num_byte ( Byte, char )
    when find string num convert to byte num if more than tow string num
    
#### example
  
    3 bytes -> 2 bytes 
    "123" -> char_num(123)
     
#### range
    from 0 to 255 one byte (256)
    
#### best use case
    when use 3 string number (3 bytes) use this func to use 2 bytes 
