Token                 Lexeme                          Line#  Column#
INT                   int                             28     1      
IDENTIFIER            printf                          28     5      
L_PAREN               (                               28     11     
CHAR                  char                            28     12     
IDENTIFIER            s                               28     17     
L_SQBR                [                               28     18     
INT_CONSTANT          20                              28     19     
R_SQBR                ]                               28     21     
COMMA                 ,                               28     22     
INT                   int                             28     23     
IDENTIFIER            a                               28     27     
R_PAREN               )                               28     28     
SEMI_COLON            ;                               28     29     
INT                   int                             29     1      
IDENTIFIER            printf1                         29     5      
L_PAREN               (                               29     12     
CHAR                  char                            29     13     
IDENTIFIER            s                               29     18     
L_SQBR                [                               29     19     
INT_CONSTANT          20                              29     20     
R_SQBR                ]                               29     22     
R_PAREN               )                               29     23     
SEMI_COLON            ;                               29     24     
INT                   int                             30     1      
IDENTIFIER            scanf                           30     5      
L_PAREN               (                               30     10     
CHAR                  char                            30     11     
IDENTIFIER            s                               30     16     
L_SQBR                [                               30     17     
INT_CONSTANT          20                              30     18     
R_SQBR                ]                               30     20     
COMMA                 ,                               30     21     
INT                   int                             30     22     
MULTIPLY              *                               30     26     
IDENTIFIER            a                               30     27     
R_PAREN               )                               30     28     
SEMI_COLON            ;                               30     29     
INT                   int                             33     1      
IDENTIFIER            main                            33     5      
L_PAREN               (                               33     9      
R_PAREN               )                               33     10     
L_BRACES              {                               33     11     
INT                   int                             34     5      
IDENTIFIER            n                               34     9      
SEMI_COLON            ;                               34     10     
IDENTIFIER            scanf                           35     5      
L_PAREN               (                               35     10     
STR_CONSTANT          "%ld"                           35     11     
COMMA                 ,                               35     16     
BITWISE_AND           &                               35     17     
IDENTIFIER            n                               35     18     
R_PAREN               )                               35     19     
SEMI_COLON            ;                               35     20     
IF                    if                              36     5      
L_PAREN               (                               36     7      
IDENTIFIER            n                               36     8      
LESS                  <                               36     10     
INT_CONSTANT          0                               36     12     
R_PAREN               )                               36     13     
L_BRACES              {                               36     14     
IDENTIFIER            printf1                         37     9      
L_PAREN               (                               37     16     
STR_CONSTANT          "Enter a postive number\n"      37     17     
R_PAREN               )                               37     43     
SEMI_COLON            ;                               37     44     
RETURN                return                          38     9      
SUBSTRACT             -                               38     16     
INT_CONSTANT          1                               38     17     
SEMI_COLON            ;                               38     18     
R_BRACES              }                               39     5      
IF                    if                              40     5      
L_PAREN               (                               40     8      
IDENTIFIER            n                               40     9      
GREATER               >                               40     11     
INT_CONSTANT          50                              40     13     
R_PAREN               )                               40     15     
L_BRACES              {                               40     16     
IDENTIFIER            printf1                         41     9      
L_PAREN               (                               41     16     
STR_CONSTANT          "Number is too large\n"         41     17     
R_PAREN               )                               41     40     
SEMI_COLON            ;                               41     41     
RETURN                return                          42     9      
SUBSTRACT             -                               42     16     
INT_CONSTANT          1                               42     17     
SEMI_COLON            ;                               42     18     
R_BRACES              }                               43     5      
INT                   int                             44     5      
IDENTIFIER            fib                             44     9      
L_SQBR                [                               44     12     
INT_CONSTANT          51                              44     13     
R_SQBR                ]                               44     15     
SEMI_COLON            ;                               44     16     
IDENTIFIER            fib                             45     5      
L_SQBR                [                               45     8      
INT_CONSTANT          0                               45     9      
R_SQBR                ]                               45     10     
ASSIGNMENT            =                               45     12     
INT_CONSTANT          0                               45     14     
SEMI_COLON            ;                               45     15     
IDENTIFIER            fib                             46     5      
L_SQBR                [                               46     8      
INT_CONSTANT          1                               46     9      
R_SQBR                ]                               46     10     
ASSIGNMENT            =                               46     12     
INT_CONSTANT          1                               46     14     
SEMI_COLON            ;                               46     15     
INT                   int                             47     5      
IDENTIFIER            i                               47     9      
SEMI_COLON            ;                               47     10     
FOR                   for                             48     5      
L_PAREN               (                               48     8      
IDENTIFIER            i                               48     9      
ASSIGNMENT            =                               48     11     
INT_CONSTANT          2                               48     13     
SEMI_COLON            ;                               48     14     
IDENTIFIER            i                               48     15     
LESS_EQUALS           <=                              48     16     
IDENTIFIER            n                               48     18     
SEMI_COLON            ;                               48     19     
IDENTIFIER            i                               48     20     
INCREMENT             ++                              48     21     
R_PAREN               )                               48     23     
L_BRACES              {                               48     24     
IDENTIFIER            fib                             49     9      
L_SQBR                [                               49     12     
IDENTIFIER            i                               49     13     
R_SQBR                ]                               49     14     
ASSIGNMENT            =                               49     16     
IDENTIFIER            fib                             49     18     
L_SQBR                [                               49     21     
IDENTIFIER            i                               49     22     
SUBSTRACT             -                               49     23     
INT_CONSTANT          1                               49     24     
R_SQBR                ]                               49     25     
ADD                   +                               49     26     
IDENTIFIER            fib                             49     27     
L_SQBR                [                               49     30     
IDENTIFIER            i                               49     31     
SUBSTRACT             -                               49     32     
INT_CONSTANT          2                               49     33     
R_SQBR                ]                               49     34     
SEMI_COLON            ;                               49     35     
R_BRACES              }                               50     5      
IDENTIFIER            printf                          51     5      
L_PAREN               (                               51     11     
STR_CONSTANT          "%ld\n"                         51     12     
COMMA                 ,                               51     19     
IDENTIFIER            fib                             51     20     
L_SQBR                [                               51     23     
IDENTIFIER            n                               51     24     
R_SQBR                ]                               51     25     
R_PAREN               )                               51     26     
SEMI_COLON            ;                               51     27     
RETURN                return                          52     5      
INT_CONSTANT          0                               52     12     
SEMI_COLON            ;                               52     13     
R_BRACES              }                               53     1      
