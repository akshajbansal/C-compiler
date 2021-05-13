Token                 Lexeme                          Line#  Column#
STRUCT                struct                          75     1      
IDENTIFIER            node                            75     8      
L_BRACES              {                               75     13     
INT                   int                             76     5      
IDENTIFIER            data                            76     9      
SEMI_COLON            ;                               76     13     
STRUCT                struct                          77     5      
IDENTIFIER            node                            77     12     
MULTIPLY              *                               77     16     
IDENTIFIER            left                            77     18     
SEMI_COLON            ;                               77     22     
STRUCT                struct                          78     5      
IDENTIFIER            node                            78     12     
MULTIPLY              *                               78     16     
IDENTIFIER            right                           78     18     
SEMI_COLON            ;                               78     23     
R_BRACES              }                               79     1      
SEMI_COLON            ;                               79     2      
VOID                  void                            81     1      
IDENTIFIER            printf                          81     6      
L_PAREN               (                               81     12     
CHAR                  char                            81     13     
IDENTIFIER            a                               81     18     
L_SQBR                [                               81     19     
INT_CONSTANT          100                             81     20     
R_SQBR                ]                               81     23     
COMMA                 ,                               81     24     
INT                   int                             81     26     
IDENTIFIER            b                               81     30     
R_PAREN               )                               81     31     
SEMI_COLON            ;                               81     32     
VOID                  void                            82     1      
IDENTIFIER            printfs                         82     6      
L_PAREN               (                               82     13     
CHAR                  char                            82     14     
IDENTIFIER            a                               82     19     
L_SQBR                [                               82     20     
INT_CONSTANT          100                             82     21     
R_SQBR                ]                               82     24     
R_PAREN               )                               82     25     
SEMI_COLON            ;                               82     26     
VOID                  void                            83     1      
MULTIPLY              *                               83     6      
IDENTIFIER            malloc                          83     7      
L_PAREN               (                               83     13     
INT                   int                             83     14     
IDENTIFIER            s                               83     18     
R_PAREN               )                               83     19     
SEMI_COLON            ;                               83     20     
STRUCT                struct                          85     1      
IDENTIFIER            node                            85     8      
MULTIPLY              *                               85     12     
IDENTIFIER            newNode                         85     14     
L_PAREN               (                               85     21     
INT                   int                             85     22     
IDENTIFIER            data                            85     26     
R_PAREN               )                               85     30     
L_BRACES              {                               86     1      
STRUCT                struct                          87     5      
IDENTIFIER            node                            87     12     
MULTIPLY              *                               87     16     
IDENTIFIER            node                            87     18     
ASSIGNMENT            =                               87     23     
L_PAREN               (                               87     25     
STRUCT                struct                          87     26     
IDENTIFIER            node                            87     33     
MULTIPLY              *                               87     37     
R_PAREN               )                               87     38     
IDENTIFIER            malloc                          87     39     
L_PAREN               (                               87     45     
SIZEOF                sizeof                          87     46     
L_PAREN               (                               87     52     
STRUCT                struct                          87     53     
IDENTIFIER            node                            87     60     
R_PAREN               )                               87     64     
R_PAREN               )                               87     65     
SEMI_COLON            ;                               87     66     
IDENTIFIER            node                            88     5      
ARROW                 ->                              88     9      
IDENTIFIER            data                            88     11     
ASSIGNMENT            =                               88     16     
IDENTIFIER            data                            88     18     
SEMI_COLON            ;                               88     22     
IDENTIFIER            node                            89     5      
ARROW                 ->                              89     9      
IDENTIFIER            left                            89     11     
ASSIGNMENT            =                               89     16     
NULL                  NULL                            89     18     
SEMI_COLON            ;                               89     22     
IDENTIFIER            node                            90     5      
ARROW                 ->                              90     9      
IDENTIFIER            right                           90     11     
ASSIGNMENT            =                               90     17     
NULL                  NULL                            90     19     
SEMI_COLON            ;                               90     23     
RETURN                return                          92     5      
L_PAREN               (                               92     12     
IDENTIFIER            node                            92     13     
R_PAREN               )                               92     17     
SEMI_COLON            ;                               92     18     
R_BRACES              }                               93     1      
VOID                  void                            95     1      
IDENTIFIER            printPostorder                  95     6      
L_PAREN               (                               95     20     
STRUCT                struct                          95     21     
IDENTIFIER            node                            95     28     
MULTIPLY              *                               95     32     
IDENTIFIER            node                            95     34     
R_PAREN               )                               95     38     
L_BRACES              {                               96     1      
IF                    if                              97     5      
L_PAREN               (                               97     8      
IDENTIFIER            node                            97     9      
EQUALS                ==                              97     14     
NULL                  NULL                            97     17     
R_PAREN               )                               97     21     
RETURN                return                          98     9      
SEMI_COLON            ;                               98     15     
IDENTIFIER            printPostorder                  99     5      
L_PAREN               (                               99     19     
IDENTIFIER            node                            99     20     
ARROW                 ->                              99     24     
IDENTIFIER            left                            99     26     
R_PAREN               )                               99     30     
SEMI_COLON            ;                               99     31     
IDENTIFIER            printPostorder                  101    5      
L_PAREN               (                               101    19     
IDENTIFIER            node                            101    20     
ARROW                 ->                              101    24     
IDENTIFIER            right                           101    26     
R_PAREN               )                               101    31     
SEMI_COLON            ;                               101    32     
IDENTIFIER            printf                          103    5      
L_PAREN               (                               103    11     
STR_CONSTANT          "%ld "                          103    12     
COMMA                 ,                               103    18     
IDENTIFIER            node                            103    20     
ARROW                 ->                              103    24     
IDENTIFIER            data                            103    26     
R_PAREN               )                               103    30     
SEMI_COLON            ;                               103    31     
R_BRACES              }                               104    1      
VOID                  void                            106    1      
IDENTIFIER            printInorder                    106    6      
L_PAREN               (                               106    18     
STRUCT                struct                          106    19     
IDENTIFIER            node                            106    26     
MULTIPLY              *                               106    30     
IDENTIFIER            node                            106    32     
R_PAREN               )                               106    36     
L_BRACES              {                               107    1      
IF                    if                              108    5      
L_PAREN               (                               108    8      
IDENTIFIER            node                            108    9      
EQUALS                ==                              108    14     
NULL                  NULL                            108    17     
R_PAREN               )                               108    21     
RETURN                return                          109    9      
SEMI_COLON            ;                               109    15     
IDENTIFIER            printInorder                    111    5      
L_PAREN               (                               111    17     
IDENTIFIER            node                            111    18     
ARROW                 ->                              111    22     
IDENTIFIER            left                            111    24     
R_PAREN               )                               111    28     
SEMI_COLON            ;                               111    29     
IDENTIFIER            printf                          112    5      
L_PAREN               (                               112    11     
STR_CONSTANT          "%ld "                          112    12     
COMMA                 ,                               112    18     
IDENTIFIER            node                            112    20     
ARROW                 ->                              112    24     
IDENTIFIER            data                            112    26     
R_PAREN               )                               112    30     
SEMI_COLON            ;                               112    31     
IDENTIFIER            printInorder                    113    5      
L_PAREN               (                               113    17     
IDENTIFIER            node                            113    18     
ARROW                 ->                              113    22     
IDENTIFIER            right                           113    24     
R_PAREN               )                               113    29     
SEMI_COLON            ;                               113    30     
R_BRACES              }                               114    1      
VOID                  void                            116    1      
IDENTIFIER            printPreorder                   116    6      
L_PAREN               (                               116    19     
STRUCT                struct                          116    20     
IDENTIFIER            node                            116    27     
MULTIPLY              *                               116    31     
IDENTIFIER            node                            116    33     
R_PAREN               )                               116    37     
L_BRACES              {                               117    1      
IF                    if                              118    5      
L_PAREN               (                               118    8      
IDENTIFIER            node                            118    9      
EQUALS                ==                              118    14     
NULL                  NULL                            118    17     
R_PAREN               )                               118    21     
RETURN                return                          119    9      
SEMI_COLON            ;                               119    15     
IDENTIFIER            printf                          121    5      
L_PAREN               (                               121    11     
STR_CONSTANT          "%ld "                          121    12     
COMMA                 ,                               121    18     
IDENTIFIER            node                            121    20     
ARROW                 ->                              121    24     
IDENTIFIER            data                            121    26     
R_PAREN               )                               121    30     
SEMI_COLON            ;                               121    31     
IDENTIFIER            printPreorder                   122    5      
L_PAREN               (                               122    18     
IDENTIFIER            node                            122    19     
ARROW                 ->                              122    23     
IDENTIFIER            left                            122    25     
R_PAREN               )                               122    29     
SEMI_COLON            ;                               122    30     
IDENTIFIER            printPreorder                   123    5      
L_PAREN               (                               123    18     
IDENTIFIER            node                            123    19     
ARROW                 ->                              123    23     
IDENTIFIER            right                           123    25     
R_PAREN               )                               123    30     
SEMI_COLON            ;                               123    31     
R_BRACES              }                               124    1      
INT                   int                             126    1      
IDENTIFIER            main                            126    5      
L_PAREN               (                               126    9      
R_PAREN               )                               126    10     
L_BRACES              {                               127    1      
STRUCT                struct                          128    5      
IDENTIFIER            node                            128    12     
MULTIPLY              *                               128    16     
IDENTIFIER            root                            128    18     
ASSIGNMENT            =                               128    23     
IDENTIFIER            newNode                         128    25     
L_PAREN               (                               128    32     
INT_CONSTANT          1                               128    33     
R_PAREN               )                               128    34     
SEMI_COLON            ;                               128    35     
IDENTIFIER            root                            129    5      
ARROW                 ->                              129    9      
IDENTIFIER            left                            129    11     
ASSIGNMENT            =                               129    16     
IDENTIFIER            newNode                         129    18     
L_PAREN               (                               129    25     
INT_CONSTANT          2                               129    26     
R_PAREN               )                               129    27     
SEMI_COLON            ;                               129    28     
IDENTIFIER            root                            130    5      
ARROW                 ->                              130    9      
IDENTIFIER            right                           130    11     
ASSIGNMENT            =                               130    17     
IDENTIFIER            newNode                         130    19     
L_PAREN               (                               130    26     
INT_CONSTANT          3                               130    27     
R_PAREN               )                               130    28     
SEMI_COLON            ;                               130    29     
IDENTIFIER            root                            131    5      
ARROW                 ->                              131    9      
IDENTIFIER            left                            131    11     
ARROW                 ->                              131    15     
IDENTIFIER            left                            131    17     
ASSIGNMENT            =                               131    22     
IDENTIFIER            newNode                         131    24     
L_PAREN               (                               131    31     
INT_CONSTANT          4                               131    32     
R_PAREN               )                               131    33     
SEMI_COLON            ;                               131    34     
IDENTIFIER            root                            132    5      
ARROW                 ->                              132    9      
IDENTIFIER            left                            132    11     
ARROW                 ->                              132    15     
IDENTIFIER            right                           132    17     
ASSIGNMENT            =                               132    23     
IDENTIFIER            newNode                         132    25     
L_PAREN               (                               132    32     
INT_CONSTANT          5                               132    33     
R_PAREN               )                               132    34     
SEMI_COLON            ;                               132    35     
IDENTIFIER            printfs                         134    5      
L_PAREN               (                               134    12     
STR_CONSTANT          "Preorder traversal of binary tree is \n"  134    13     
R_PAREN               )                               134    54     
SEMI_COLON            ;                               134    55     
IDENTIFIER            printPreorder                   135    5      
L_PAREN               (                               135    18     
IDENTIFIER            root                            135    19     
R_PAREN               )                               135    23     
SEMI_COLON            ;                               135    24     
IDENTIFIER            printfs                         137    5      
L_PAREN               (                               137    12     
STR_CONSTANT          "\nInorder traversal of binary tree is \n"  137    13     
R_PAREN               )                               137    55     
SEMI_COLON            ;                               137    56     
IDENTIFIER            printInorder                    138    5      
L_PAREN               (                               138    17     
IDENTIFIER            root                            138    18     
R_PAREN               )                               138    22     
SEMI_COLON            ;                               138    23     
IDENTIFIER            printfs                         140    5      
L_PAREN               (                               140    12     
STR_CONSTANT          "\nPostorder traversal of binary tree is \n"  140    13     
R_PAREN               )                               140    57     
SEMI_COLON            ;                               140    58     
IDENTIFIER            printPostorder                  141    5      
L_PAREN               (                               141    19     
IDENTIFIER            root                            141    20     
R_PAREN               )                               141    24     
SEMI_COLON            ;                               141    25     
IDENTIFIER            printfs                         142    5      
L_PAREN               (                               142    12     
STR_CONSTANT          "\n"                            142    13     
R_PAREN               )                               142    17     
SEMI_COLON            ;                               142    18     
RETURN                return                          144    5      
INT_CONSTANT          0                               144    12     
SEMI_COLON            ;                               144    13     
R_BRACES              }                               145    1      