Token                 Lexeme                          Line#  Column#
INT                   int                             31     1      
IDENTIFIER            printf                          31     5      
L_PAREN               (                               31     11     
CHAR                  char                            31     12     
IDENTIFIER            s                               31     17     
L_SQBR                [                               31     18     
INT_CONSTANT          20                              31     19     
R_SQBR                ]                               31     21     
COMMA                 ,                               31     22     
INT                   int                             31     23     
IDENTIFIER            a                               31     27     
R_PAREN               )                               31     28     
SEMI_COLON            ;                               31     29     
INT                   int                             32     1      
IDENTIFIER            printf1                         32     5      
L_PAREN               (                               32     12     
CHAR                  char                            32     13     
IDENTIFIER            s                               32     18     
L_SQBR                [                               32     19     
INT_CONSTANT          20                              32     20     
R_SQBR                ]                               32     22     
R_PAREN               )                               32     23     
SEMI_COLON            ;                               32     24     
VOID                  void                            33     1      
MULTIPLY              *                               33     6      
IDENTIFIER            malloc                          33     7      
L_PAREN               (                               33     13     
INT                   int                             33     14     
IDENTIFIER            size                            33     18     
R_PAREN               )                               33     22     
SEMI_COLON            ;                               33     23     
INT                   int                             36     1      
IDENTIFIER            main                            36     5      
L_PAREN               (                               36     9      
R_PAREN               )                               36     10     
L_BRACES              {                               36     11     
INT                   int                             37     5      
MULTIPLY              *                               37     9      
MULTIPLY              *                               37     10     
IDENTIFIER            ptr                             37     11     
ASSIGNMENT            =                               37     15     
L_PAREN               (                               37     17     
INT                   int                             37     18     
MULTIPLY              *                               37     21     
MULTIPLY              *                               37     22     
R_PAREN               )                               37     23     
IDENTIFIER            malloc                          37     24     
L_PAREN               (                               37     30     
SIZEOF                sizeof                          37     31     
L_PAREN               (                               37     37     
INT                   int                             37     38     
MULTIPLY              *                               37     42     
R_PAREN               )                               37     43     
MULTIPLY              *                               37     44     
INT_CONSTANT          5                               37     45     
R_PAREN               )                               37     46     
SEMI_COLON            ;                               37     47     
INT                   int                             38     5      
IDENTIFIER            i                               38     9      
COMMA                 ,                               38     10     
IDENTIFIER            j                               38     11     
SEMI_COLON            ;                               38     12     
FOR                   for                             39     5      
L_PAREN               (                               39     8      
IDENTIFIER            i                               39     9      
ASSIGNMENT            =                               39     10     
INT_CONSTANT          0                               39     11     
SEMI_COLON            ;                               39     12     
IDENTIFIER            i                               39     13     
LESS                  <                               39     14     
INT_CONSTANT          5                               39     15     
SEMI_COLON            ;                               39     16     
IDENTIFIER            i                               39     17     
INCREMENT             ++                              39     18     
R_PAREN               )                               39     20     
L_BRACES              {                               39     21     
IDENTIFIER            ptr                             40     9      
L_SQBR                [                               40     12     
IDENTIFIER            i                               40     13     
R_SQBR                ]                               40     14     
ASSIGNMENT            =                               40     16     
L_PAREN               (                               40     18     
INT                   int                             40     19     
MULTIPLY              *                               40     22     
R_PAREN               )                               40     23     
IDENTIFIER            malloc                          40     24     
L_PAREN               (                               40     30     
SIZEOF                sizeof                          40     31     
L_PAREN               (                               40     37     
INT                   int                             40     38     
R_PAREN               )                               40     41     
MULTIPLY              *                               40     42     
INT_CONSTANT          5                               40     43     
R_PAREN               )                               40     44     
SEMI_COLON            ;                               40     45     
FOR                   for                             41     9      
L_PAREN               (                               41     12     
IDENTIFIER            j                               41     13     
ASSIGNMENT            =                               41     15     
INT_CONSTANT          0                               41     17     
SEMI_COLON            ;                               41     18     
IDENTIFIER            j                               41     19     
LESS                  <                               41     20     
INT_CONSTANT          5                               41     21     
SEMI_COLON            ;                               41     22     
IDENTIFIER            j                               41     23     
INCREMENT             ++                              41     24     
R_PAREN               )                               41     26     
L_BRACES              {                               41     27     
IDENTIFIER            ptr                             42     13     
L_SQBR                [                               42     16     
IDENTIFIER            i                               42     17     
R_SQBR                ]                               42     18     
L_SQBR                [                               42     19     
IDENTIFIER            j                               42     20     
R_SQBR                ]                               42     21     
ASSIGNMENT            =                               42     23     
IDENTIFIER            i                               42     25     
MULTIPLY              *                               42     26     
INT_CONSTANT          10                              42     27     
ADD                   +                               42     29     
IDENTIFIER            j                               42     30     
SEMI_COLON            ;                               42     31     
R_BRACES              }                               43     9      
R_BRACES              }                               44     5      
FOR                   for                             46     5      
L_PAREN               (                               46     8      
IDENTIFIER            i                               46     9      
ASSIGNMENT            =                               46     10     
INT_CONSTANT          0                               46     11     
SEMI_COLON            ;                               46     12     
IDENTIFIER            i                               46     13     
LESS                  <                               46     14     
INT_CONSTANT          5                               46     15     
SEMI_COLON            ;                               46     16     
IDENTIFIER            i                               46     17     
INCREMENT             ++                              46     18     
R_PAREN               )                               46     20     
L_BRACES              {                               46     21     
FOR                   for                             47     9      
L_PAREN               (                               47     12     
IDENTIFIER            j                               47     13     
ASSIGNMENT            =                               47     15     
INT_CONSTANT          0                               47     17     
SEMI_COLON            ;                               47     18     
IDENTIFIER            j                               47     19     
LESS                  <                               47     20     
INT_CONSTANT          5                               47     21     
SEMI_COLON            ;                               47     22     
IDENTIFIER            j                               47     23     
INCREMENT             ++                              47     24     
R_PAREN               )                               47     26     
L_BRACES              {                               47     27     
IDENTIFIER            printf                          48     13     
L_PAREN               (                               48     19     
STR_CONSTANT          "%ld "                          48     20     
COMMA                 ,                               48     26     
IDENTIFIER            ptr                             48     27     
L_SQBR                [                               48     30     
IDENTIFIER            i                               48     31     
R_SQBR                ]                               48     32     
L_SQBR                [                               48     33     
IDENTIFIER            j                               48     34     
R_SQBR                ]                               48     35     
R_PAREN               )                               48     36     
SEMI_COLON            ;                               48     37     
R_BRACES              }                               49     9      
IDENTIFIER            printf1                         50     9      
L_PAREN               (                               50     16     
STR_CONSTANT          "\n"                            50     17     
R_PAREN               )                               50     21     
SEMI_COLON            ;                               50     22     
R_BRACES              }                               51     5      
R_BRACES              }                               53     1      
