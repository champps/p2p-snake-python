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

## 

in function put num byte function can take char or other num byte as 30(30(x)) = 3030x that range wase so wide compared to use one byte repeat func (this is note for me dot in docs)