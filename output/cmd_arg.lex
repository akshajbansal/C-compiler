Token                 Lexeme                          Line#  Column#
VOID                  void                            16     1      
IDENTIFIER            puts                            16     6      
L_PAREN               (                               16     10     
CHAR                  char                            16     11     
MULTIPLY              *                               16     16     
IDENTIFIER            str                             16     17     
R_PAREN               )                               16     20     
SEMI_COLON            ;                               16     21     
VOID                  void                            17     1      
IDENTIFIER            printf                          17     6      
L_PAREN               (                               17     12     
CHAR                  char                            17     13     
MULTIPLY              *                               17     18     
IDENTIFIER            str                             17     19     
COMMA                 ,                               17     22     
INT                   int                             17     23     
IDENTIFIER            d                               17     27     
R_PAREN               )                               17     28     
SEMI_COLON            ;                               17     29     
VOID                  void                            18     1      
IDENTIFIER            printf1                         18     6      
L_PAREN               (                               18     13     
CHAR                  char                            18     14     
MULTIPLY              *                               18     19     
IDENTIFIER            str                             18     20     
COMMA                 ,                               18     23     
INT                   int                             18     24     
IDENTIFIER            d                               18     28     
COMMA                 ,                               18     29     
CHAR                  char                            18     31     
MULTIPLY              *                               18     35     
IDENTIFIER            s                               18     36     
R_PAREN               )                               18     37     
SEMI_COLON            ;                               18     38     
VOID                  void                            19     1      
IDENTIFIER            printfs                         19     6      
L_PAREN               (                               19     13     
CHAR                  char                            19     14     
MULTIPLY              *                               19     19     
IDENTIFIER            str                             19     20     
R_PAREN               )                               19     23     
SEMI_COLON            ;                               19     24     
INT                   int                             21     1      
IDENTIFIER            main                            21     6      
L_PAREN               (                               21     10     
INT                   int                             21     11     
IDENTIFIER            argc                            21     15     
COMMA                 ,                               21     19     
CHAR                  char                            21     21     
MULTIPLY              *                               21     25     
MULTIPLY              *                               21     26     
IDENTIFIER            argv                            21     28     
R_PAREN               )                               21     32     
L_BRACES              {                               21     33     
IDENTIFIER            printf                          23     5      
L_PAREN               (                               23     11     
STR_CONSTANT          "no of args: %ld\n"             23     12     
COMMA                 ,                               23     31     
IDENTIFIER            argc                            23     33     
R_PAREN               )                               23     37     
SEMI_COLON            ;                               23     38     
INT                   int                             24     5      
IDENTIFIER            i                               24     9      
ASSIGNMENT            =                               24     10     
INT_CONSTANT          0                               24     11     
SEMI_COLON            ;                               24     12     
FOR                   for                             25     5      
L_PAREN               (                               25     8      
IDENTIFIER            i                               25     9      
ASSIGNMENT            =                               25     10     
INT_CONSTANT          0                               25     11     
SEMI_COLON            ;                               25     12     
IDENTIFIER            i                               25     13     
LESS                  <                               25     14     
IDENTIFIER            argc                            25     15     
SEMI_COLON            ;                               25     19     
IDENTIFIER            i                               25     20     
INCREMENT             ++                              25     21     
R_PAREN               )                               25     23     
L_BRACES              {                               25     24     
IDENTIFIER            printf1                         26     9      
L_PAREN               (                               26     16     
STR_CONSTANT          "argument no.%ld is %s\n"       26     17     
COMMA                 ,                               26     42     
IDENTIFIER            i                               26     43     
ADD                   +                               26     44     
INT_CONSTANT          1                               26     45     
COMMA                 ,                               26     46     
IDENTIFIER            argv                            26     48     
L_SQBR                [                               26     52     
IDENTIFIER            i                               26     53     
R_SQBR                ]                               26     54     
R_PAREN               )                               26     55     
SEMI_COLON            ;                               26     56     
R_BRACES              }                               27     5      
RETURN                return                          28     5      
INT_CONSTANT          0                               28     12     
SEMI_COLON            ;                               28     13     
R_BRACES              }                               29     1      
