Token                 Lexeme                          Line#  Column#
INT                   int                             21     1      
IDENTIFIER            printf                          21     5      
L_PAREN               (                               21     11     
CHAR                  char                            21     12     
IDENTIFIER            s                               21     17     
L_SQBR                [                               21     18     
INT_CONSTANT          20                              21     19     
R_SQBR                ]                               21     21     
COMMA                 ,                               21     22     
INT                   int                             21     23     
IDENTIFIER            a                               21     27     
R_PAREN               )                               21     28     
SEMI_COLON            ;                               21     29     
INT                   int                             22     1      
IDENTIFIER            printf1                         22     5      
L_PAREN               (                               22     12     
CHAR                  char                            22     13     
IDENTIFIER            s                               22     18     
L_SQBR                [                               22     19     
INT_CONSTANT          20                              22     20     
R_SQBR                ]                               22     22     
R_PAREN               )                               22     23     
SEMI_COLON            ;                               22     24     
INT                   int                             23     1      
IDENTIFIER            scanf                           23     5      
L_PAREN               (                               23     10     
CHAR                  char                            23     11     
IDENTIFIER            s                               23     16     
L_SQBR                [                               23     17     
INT_CONSTANT          20                              23     18     
R_SQBR                ]                               23     20     
COMMA                 ,                               23     21     
INT                   int                             23     22     
MULTIPLY              *                               23     26     
IDENTIFIER            a                               23     27     
R_PAREN               )                               23     28     
SEMI_COLON            ;                               23     29     
INT                   int                             25     1      
IDENTIFIER            fibonacci                       25     5      
L_PAREN               (                               25     14     
INT                   int                             25     15     
IDENTIFIER            n                               25     19     
R_PAREN               )                               25     20     
L_BRACES              {                               25     21     
IF                    if                              26     5      
L_PAREN               (                               26     7      
IDENTIFIER            n                               26     8      
LESS_EQUALS           <=                              26     10     
INT_CONSTANT          1                               26     12     
R_PAREN               )                               26     13     
RETURN                return                          26     15     
IDENTIFIER            n                               26     22     
SEMI_COLON            ;                               26     23     
RETURN                return                          27     5      
IDENTIFIER            fibonacci                       27     12     
L_PAREN               (                               27     21     
IDENTIFIER            n                               27     22     
SUBSTRACT             -                               27     23     
INT_CONSTANT          1                               27     24     
R_PAREN               )                               27     25     
ADD                   +                               27     26     
IDENTIFIER            fibonacci                       27     27     
L_PAREN               (                               27     36     
IDENTIFIER            n                               27     37     
SUBSTRACT             -                               27     38     
INT_CONSTANT          2                               27     39     
R_PAREN               )                               27     40     
SEMI_COLON            ;                               27     41     
R_BRACES              }                               28     1      
INT                   int                             30     1      
IDENTIFIER            main                            30     5      
L_PAREN               (                               30     9      
R_PAREN               )                               30     10     
L_BRACES              {                               30     11     
INT                   int                             31     5      
IDENTIFIER            n                               31     9      
SEMI_COLON            ;                               31     10     
IDENTIFIER            scanf                           32     5      
L_PAREN               (                               32     10     
STR_CONSTANT          "%ld"                           32     11     
COMMA                 ,                               32     16     
BITWISE_AND           &                               32     17     
IDENTIFIER            n                               32     18     
R_PAREN               )                               32     19     
SEMI_COLON            ;                               32     20     
IF                    if                              33     5      
L_PAREN               (                               33     7      
IDENTIFIER            n                               33     8      
LESS                  <                               33     10     
INT_CONSTANT          0                               33     12     
R_PAREN               )                               33     13     
L_BRACES              {                               33     14     
IDENTIFIER            printf1                         34     9      
L_PAREN               (                               34     16     
STR_CONSTANT          "Enter a postive number\n"      34     17     
R_PAREN               )                               34     43     
SEMI_COLON            ;                               34     44     
RETURN                return                          35     9      
INT_CONSTANT          0                               35     16     
SEMI_COLON            ;                               35     17     
R_BRACES              }                               36     5      
IDENTIFIER            printf                          37     5      
L_PAREN               (                               37     11     
STR_CONSTANT          "%ld\n"                         37     12     
COMMA                 ,                               37     19     
IDENTIFIER            fibonacci                       37     20     
L_PAREN               (                               37     29     
IDENTIFIER            n                               37     30     
R_PAREN               )                               37     31     
R_PAREN               )                               37     32     
SEMI_COLON            ;                               37     33     
RETURN                return                          38     5      
INT_CONSTANT          0                               38     12     
SEMI_COLON            ;                               38     13     
R_BRACES              }                               39     1      
