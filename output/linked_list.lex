Token                 Lexeme                          Line#  Column#
INT                   int                             76     1      
IDENTIFIER            printf                          76     5      
L_PAREN               (                               76     11     
CHAR                  char                            76     12     
IDENTIFIER            s                               76     17     
L_SQBR                [                               76     18     
INT_CONSTANT          20                              76     19     
R_SQBR                ]                               76     21     
COMMA                 ,                               76     22     
INT                   int                             76     23     
IDENTIFIER            a                               76     27     
R_PAREN               )                               76     28     
SEMI_COLON            ;                               76     29     
INT                   int                             77     1      
IDENTIFIER            printf1                         77     5      
L_PAREN               (                               77     12     
CHAR                  char                            77     13     
IDENTIFIER            s                               77     18     
L_SQBR                [                               77     19     
INT_CONSTANT          20                              77     20     
R_SQBR                ]                               77     22     
R_PAREN               )                               77     23     
SEMI_COLON            ;                               77     24     
INT                   int                             78     1      
IDENTIFIER            scanf                           78     5      
L_PAREN               (                               78     10     
CHAR                  char                            78     11     
IDENTIFIER            s                               78     16     
L_SQBR                [                               78     17     
INT_CONSTANT          20                              78     18     
R_SQBR                ]                               78     20     
COMMA                 ,                               78     21     
INT                   int                             78     22     
MULTIPLY              *                               78     26     
IDENTIFIER            a                               78     27     
R_PAREN               )                               78     28     
SEMI_COLON            ;                               78     29     
VOID                  void                            79     1      
MULTIPLY              *                               79     6      
IDENTIFIER            malloc                          79     7      
L_PAREN               (                               79     13     
INT                   int                             79     14     
IDENTIFIER            size                            79     18     
R_PAREN               )                               79     22     
SEMI_COLON            ;                               79     23     
STRUCT                struct                          81     1      
IDENTIFIER            Node                            81     8      
L_BRACES              {                               81     12     
INT                   int                             82     5      
IDENTIFIER            data                            82     9      
SEMI_COLON            ;                               82     13     
STRUCT                struct                          83     5      
IDENTIFIER            Node                            83     12     
MULTIPLY              *                               83     17     
IDENTIFIER            next                            83     18     
SEMI_COLON            ;                               83     22     
R_BRACES              }                               84     1      
SEMI_COLON            ;                               84     2      
STRUCT                struct                          86     1      
IDENTIFIER            Node                            86     8      
MULTIPLY              *                               86     13     
IDENTIFIER            head                            86     14     
ASSIGNMENT            =                               86     19     
NULL                  NULL                            86     21     
SEMI_COLON            ;                               86     25     
VOID                  void                            88     1      
IDENTIFIER            push                            88     6      
L_PAREN               (                               88     10     
INT                   int                             88     11     
IDENTIFIER            data                            88     15     
R_PAREN               )                               88     19     
L_BRACES              {                               88     20     
STRUCT                struct                          89     5      
IDENTIFIER            Node                            89     12     
MULTIPLY              *                               89     17     
IDENTIFIER            node                            89     18     
ASSIGNMENT            =                               89     23     
L_PAREN               (                               89     25     
STRUCT                struct                          89     26     
IDENTIFIER            Node                            89     33     
MULTIPLY              *                               89     37     
R_PAREN               )                               89     38     
IDENTIFIER            malloc                          89     39     
L_PAREN               (                               89     45     
SIZEOF                sizeof                          89     46     
L_PAREN               (                               89     52     
STRUCT                struct                          89     53     
IDENTIFIER            Node                            89     60     
R_PAREN               )                               89     64     
R_PAREN               )                               89     65     
SEMI_COLON            ;                               89     66     
IDENTIFIER            node                            90     5      
ARROW                 ->                              90     9      
IDENTIFIER            data                            90     11     
ASSIGNMENT            =                               90     16     
IDENTIFIER            data                            90     18     
SEMI_COLON            ;                               90     22     
IDENTIFIER            node                            91     5      
ARROW                 ->                              91     9      
IDENTIFIER            next                            91     11     
ASSIGNMENT            =                               91     16     
IDENTIFIER            head                            91     18     
SEMI_COLON            ;                               91     22     
IDENTIFIER            head                            92     5      
ASSIGNMENT            =                               92     10     
IDENTIFIER            node                            92     12     
SEMI_COLON            ;                               92     16     
R_BRACES              }                               93     1      
VOID                  void                            95     1      
IDENTIFIER            pop                             95     6      
L_PAREN               (                               95     9      
R_PAREN               )                               95     10     
L_BRACES              {                               95     11     
IF                    if                              96     5      
L_PAREN               (                               96     8      
IDENTIFIER            head                            96     9      
EQUALS                ==                              96     14     
NULL                  NULL                            96     17     
R_PAREN               )                               96     21     
L_BRACES              {                               96     22     
IDENTIFIER            printf1                         97     9      
L_PAREN               (                               97     16     
STR_CONSTANT          "linked list is empty\n"        97     17     
R_PAREN               )                               97     41     
SEMI_COLON            ;                               97     42     
RETURN                return                          98     9      
SEMI_COLON            ;                               98     15     
R_BRACES              }                               99     5      
IDENTIFIER            printf                          100    5      
L_PAREN               (                               100    11     
STR_CONSTANT          "removing node with data %ld\n"  100    12     
COMMA                 ,                               100    43     
IDENTIFIER            head                            100    44     
ARROW                 ->                              100    48     
IDENTIFIER            data                            100    50     
R_PAREN               )                               100    54     
SEMI_COLON            ;                               100    55     
IDENTIFIER            head                            101    5      
ASSIGNMENT            =                               101    10     
IDENTIFIER            head                            101    12     
ARROW                 ->                              101    16     
IDENTIFIER            next                            101    18     
SEMI_COLON            ;                               101    22     
R_BRACES              }                               102    1      
VOID                  void                            104    1      
IDENTIFIER            print_list                      104    6      
L_PAREN               (                               104    16     
R_PAREN               )                               104    17     
L_BRACES              {                               104    18     
IF                    if                              105    5      
L_PAREN               (                               105    8      
IDENTIFIER            head                            105    9      
EQUALS                ==                              105    14     
NULL                  NULL                            105    17     
R_PAREN               )                               105    21     
L_BRACES              {                               105    22     
IDENTIFIER            printf1                         106    9      
L_PAREN               (                               106    16     
STR_CONSTANT          "linked list is empty\n"        106    17     
R_PAREN               )                               106    41     
SEMI_COLON            ;                               106    42     
RETURN                return                          107    9      
SEMI_COLON            ;                               107    15     
R_BRACES              }                               108    5      
STRUCT                struct                          109    5      
IDENTIFIER            Node                            109    12     
MULTIPLY              *                               109    17     
IDENTIFIER            node                            109    18     
ASSIGNMENT            =                               109    23     
IDENTIFIER            head                            109    25     
SEMI_COLON            ;                               109    29     
WHILE                 while                           110    5      
L_PAREN               (                               110    10     
IDENTIFIER            node                            110    11     
NOT_EQUALS            !=                              110    16     
NULL                  NULL                            110    19     
R_PAREN               )                               110    23     
L_BRACES              {                               110    24     
IDENTIFIER            printf                          111    9      
L_PAREN               (                               111    15     
STR_CONSTANT          "%ld "                          111    16     
COMMA                 ,                               111    22     
IDENTIFIER            node                            111    23     
ARROW                 ->                              111    27     
IDENTIFIER            data                            111    29     
R_PAREN               )                               111    33     
SEMI_COLON            ;                               111    34     
IDENTIFIER            node                            112    9      
ASSIGNMENT            =                               112    14     
IDENTIFIER            node                            112    16     
ARROW                 ->                              112    20     
IDENTIFIER            next                            112    22     
SEMI_COLON            ;                               112    26     
R_BRACES              }                               113    5      
IDENTIFIER            printf1                         114    5      
L_PAREN               (                               114    12     
STR_CONSTANT          "\n"                            114    13     
R_PAREN               )                               114    17     
SEMI_COLON            ;                               114    18     
R_BRACES              }                               116    1      
VOID                  void                            118    1      
IDENTIFIER            search                          118    6      
L_PAREN               (                               118    12     
INT                   int                             118    13     
IDENTIFIER            a                               118    17     
R_PAREN               )                               118    18     
L_BRACES              {                               118    19     
IF                    if                              119    5      
L_PAREN               (                               119    8      
IDENTIFIER            head                            119    9      
EQUALS                ==                              119    14     
NULL                  NULL                            119    17     
R_PAREN               )                               119    21     
L_BRACES              {                               119    22     
IDENTIFIER            printf1                         120    9      
L_PAREN               (                               120    16     
STR_CONSTANT          "linked list is empty\n"        120    17     
R_PAREN               )                               120    41     
SEMI_COLON            ;                               120    42     
RETURN                return                          121    9      
SEMI_COLON            ;                               121    15     
R_BRACES              }                               122    5      
STRUCT                struct                          123    5      
IDENTIFIER            Node                            123    12     
MULTIPLY              *                               123    17     
IDENTIFIER            node                            123    18     
ASSIGNMENT            =                               123    23     
IDENTIFIER            head                            123    25     
SEMI_COLON            ;                               123    29     
WHILE                 while                           124    5      
L_PAREN               (                               124    10     
IDENTIFIER            node                            124    11     
NOT_EQUALS            !=                              124    16     
NULL                  NULL                            124    19     
R_PAREN               )                               124    23     
L_BRACES              {                               124    24     
IF                    if                              125    9      
L_PAREN               (                               125    11     
IDENTIFIER            node                            125    12     
ARROW                 ->                              125    16     
IDENTIFIER            data                            125    18     
EQUALS                ==                              125    23     
IDENTIFIER            a                               125    26     
R_PAREN               )                               125    27     
L_BRACES              {                               125    28     
IDENTIFIER            printf                          126    13     
L_PAREN               (                               126    19     
STR_CONSTANT          "Element %ld is present in linked list\n"  126    20     
COMMA                 ,                               126    61     
IDENTIFIER            a                               126    62     
R_PAREN               )                               126    63     
SEMI_COLON            ;                               126    64     
RETURN                return                          127    13     
SEMI_COLON            ;                               127    19     
R_BRACES              }                               128    9      
IDENTIFIER            node                            129    9      
ASSIGNMENT            =                               129    14     
IDENTIFIER            node                            129    16     
ARROW                 ->                              129    20     
IDENTIFIER            next                            129    22     
SEMI_COLON            ;                               129    26     
R_BRACES              }                               130    5      
IDENTIFIER            printf                          131    5      
L_PAREN               (                               131    11     
STR_CONSTANT          "Element %ld is not in linked list\n"  131    12     
COMMA                 ,                               131    49     
IDENTIFIER            a                               131    50     
R_PAREN               )                               131    51     
SEMI_COLON            ;                               131    52     
R_BRACES              }                               133    1      
INT                   int                             135    1      
IDENTIFIER            main                            135    5      
L_PAREN               (                               135    9      
R_PAREN               )                               135    10     
L_BRACES              {                               135    11     
INT                   int                             136    5      
IDENTIFIER            i                               136    9      
SEMI_COLON            ;                               136    10     
FOR                   for                             137    5      
L_PAREN               (                               137    8      
IDENTIFIER            i                               137    9      
ASSIGNMENT            =                               137    11     
INT_CONSTANT          0                               137    13     
SEMI_COLON            ;                               137    14     
IDENTIFIER            i                               137    15     
LESS                  <                               137    16     
INT_CONSTANT          10                              137    17     
SEMI_COLON            ;                               137    19     
IDENTIFIER            i                               137    20     
INCREMENT             ++                              137    21     
R_PAREN               )                               137    23     
IDENTIFIER            push                            137    25     
L_PAREN               (                               137    29     
IDENTIFIER            i                               137    30     
MULTIPLY              *                               137    31     
IDENTIFIER            i                               137    32     
R_PAREN               )                               137    33     
SEMI_COLON            ;                               137    34     
IDENTIFIER            print_list                      138    5      
L_PAREN               (                               138    15     
R_PAREN               )                               138    16     
SEMI_COLON            ;                               138    17     
IDENTIFIER            search                          139    5      
L_PAREN               (                               139    11     
INT_CONSTANT          49                              139    12     
R_PAREN               )                               139    14     
SEMI_COLON            ;                               139    15     
FOR                   for                             140    5      
L_PAREN               (                               140    8      
IDENTIFIER            i                               140    9      
ASSIGNMENT            =                               140    11     
INT_CONSTANT          0                               140    13     
SEMI_COLON            ;                               140    14     
IDENTIFIER            i                               140    15     
LESS                  <                               140    16     
INT_CONSTANT          5                               140    17     
SEMI_COLON            ;                               140    18     
IDENTIFIER            i                               140    19     
INCREMENT             ++                              140    20     
R_PAREN               )                               140    22     
IDENTIFIER            pop                             140    24     
L_PAREN               (                               140    27     
R_PAREN               )                               140    28     
SEMI_COLON            ;                               140    29     
IDENTIFIER            print_list                      141    5      
L_PAREN               (                               141    15     
R_PAREN               )                               141    16     
SEMI_COLON            ;                               141    17     
IDENTIFIER            search                          142    5      
L_PAREN               (                               142    11     
INT_CONSTANT          49                              142    12     
R_PAREN               )                               142    14     
SEMI_COLON            ;                               142    15     
FOR                   for                             143    5      
L_PAREN               (                               143    8      
SEMI_COLON            ;                               143    9      
IDENTIFIER            i                               143    10     
LESS_EQUALS           <=                              143    11     
INT_CONSTANT          10                              143    13     
SEMI_COLON            ;                               143    15     
IDENTIFIER            i                               143    16     
INCREMENT             ++                              143    17     
R_PAREN               )                               143    19     
IDENTIFIER            pop                             143    21     
L_PAREN               (                               143    24     
R_PAREN               )                               143    25     
SEMI_COLON            ;                               143    26     
RETURN                return                          144    5      
INT_CONSTANT          0                               144    12     
SEMI_COLON            ;                               144    13     
R_BRACES              }                               145    1      
