Token                 Lexeme                          Line#  Column#
BOOL                  bool                            31     1      
IDENTIFIER            is_odd                          31     6      
L_PAREN               (                               31     12     
INT                   int                             31     13     
IDENTIFIER            n                               31     17     
R_PAREN               )                               31     18     
SEMI_COLON            ;                               31     19     
BOOL                  bool                            32     1      
IDENTIFIER            is_even                         32     6      
L_PAREN               (                               32     13     
INT                   int                             32     14     
IDENTIFIER            n                               32     18     
R_PAREN               )                               32     19     
SEMI_COLON            ;                               32     20     
VOID                  void                            34     1      
IDENTIFIER            printf                          34     6      
L_PAREN               (                               34     12     
CHAR                  char                            34     13     
IDENTIFIER            s                               34     18     
L_SQBR                [                               34     19     
INT_CONSTANT          100                             34     20     
R_SQBR                ]                               34     23     
COMMA                 ,                               34     24     
INT                   int                             34     25     
IDENTIFIER            a                               34     29     
R_PAREN               )                               34     30     
SEMI_COLON            ;                               34     31     
VOID                  void                            35     1      
IDENTIFIER            scanf                           35     6      
L_PAREN               (                               35     11     
CHAR                  char                            35     12     
IDENTIFIER            s                               35     17     
L_SQBR                [                               35     18     
INT_CONSTANT          100                             35     19     
R_SQBR                ]                               35     22     
COMMA                 ,                               35     23     
INT                   int                             35     24     
MULTIPLY              *                               35     28     
IDENTIFIER            a                               35     29     
R_PAREN               )                               35     30     
SEMI_COLON            ;                               35     31     
INT                   int                             37     1      
IDENTIFIER            main                            37     5      
L_PAREN               (                               37     9      
R_PAREN               )                               37     10     
L_BRACES              {                               37     11     
INT                   int                             38     5      
IDENTIFIER            n                               38     9      
ASSIGNMENT            =                               38     11     
INT_CONSTANT          0                               38     13     
SEMI_COLON            ;                               38     14     
IDENTIFIER            scanf                           39     5      
L_PAREN               (                               39     10     
STR_CONSTANT          "%ld"                           39     11     
COMMA                 ,                               39     16     
BITWISE_AND           &                               39     17     
IDENTIFIER            n                               39     18     
R_PAREN               )                               39     19     
SEMI_COLON            ;                               39     20     
IF                    if                              40     5      
L_PAREN               (                               40     7      
IDENTIFIER            n                               40     8      
LESS                  <                               40     10     
INT_CONSTANT          0                               40     12     
R_PAREN               )                               40     13     
L_BRACES              {                               40     14     
IDENTIFIER            printf                          41     9      
L_PAREN               (                               41     15     
STR_CONSTANT          "Enter a positive number\n"     41     16     
COMMA                 ,                               41     43     
INT_CONSTANT          0                               41     44     
R_PAREN               )                               41     45     
SEMI_COLON            ;                               41     46     
RETURN                return                          42     9      
INT_CONSTANT          0                               42     16     
SEMI_COLON            ;                               42     17     
R_BRACES              }                               43     5      
IDENTIFIER            printf                          44     5      
L_PAREN               (                               44     11     
STR_CONSTANT          "%ld\n"                         44     12     
COMMA                 ,                               44     19     
IDENTIFIER            is_odd                          44     20     
L_PAREN               (                               44     26     
IDENTIFIER            n                               44     27     
R_PAREN               )                               44     28     
R_PAREN               )                               44     29     
SEMI_COLON            ;                               44     30     
R_BRACES              }                               45     1      
BOOL                  bool                            47     1      
IDENTIFIER            is_odd                          47     6      
L_PAREN               (                               47     12     
INT                   int                             47     13     
IDENTIFIER            n                               47     17     
R_PAREN               )                               47     18     
L_BRACES              {                               47     19     
IF                    if                              48     5      
L_PAREN               (                               48     7      
IDENTIFIER            n                               48     9      
EQUALS                ==                              48     11     
INT_CONSTANT          0                               48     14     
R_PAREN               )                               48     15     
RETURN                return                          48     17     
FALSE                 false                           48     24     
SEMI_COLON            ;                               48     29     
RETURN                return                          49     5      
IDENTIFIER            is_even                         49     12     
L_PAREN               (                               49     19     
IDENTIFIER            n                               49     20     
SUBSTRACT             -                               49     21     
INT_CONSTANT          1                               49     22     
R_PAREN               )                               49     23     
SEMI_COLON            ;                               49     24     
R_BRACES              }                               50     1      
BOOL                  bool                            52     1      
IDENTIFIER            is_even                         52     6      
L_PAREN               (                               52     13     
INT                   int                             52     14     
IDENTIFIER            n                               52     18     
R_PAREN               )                               52     19     
L_BRACES              {                               52     20     
IF                    if                              53     5      
L_PAREN               (                               53     7      
IDENTIFIER            n                               53     9      
EQUALS                ==                              53     11     
INT_CONSTANT          0                               53     14     
R_PAREN               )                               53     15     
RETURN                return                          53     17     
TRUE                  true                            53     24     
SEMI_COLON            ;                               53     28     
RETURN                return                          54     5      
IDENTIFIER            is_odd                          54     12     
L_PAREN               (                               54     18     
IDENTIFIER            n                               54     19     
SUBSTRACT             -                               54     20     
INT_CONSTANT          1                               54     21     
R_PAREN               )                               54     22     
SEMI_COLON            ;                               54     23     
R_BRACES              }                               55     1      
