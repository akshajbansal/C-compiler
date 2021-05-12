import sys
import ply.lex as lex
import ply.yacc as yacc
import clexer as lexer
import argparse
import pygraphviz as pgv
import copy

def main():
    """Driver code for Abstract syntax tree 
    Generation"""

    #read source code provided by user
    arg_parser = argparse.ArgumentParser(description="Lexer for Source Language C")
    arg_parser.add_argument('source_code',help="source code file location")
    arg_parser.add_argument('-o',help="output file name", default="a.out")
    arg_parser.add_argument('-a',action='store_true',help="output ast")
    arg_parser.add_argument('-s',action='store_true',help="output symbol table")
    arg_parser.add_argument('-t',action='store_true',help="output 3 address code")
    arg_parser.add_argument('-d',action='store_true',help="output dot script")
    arg_parser.add_argument('-l',action='store_true',help="output lexeme table")
    arg_parser.add_argument('-stdc',action='store_true',help="output lexeme table")
    args = arg_parser.parse_args()

    try:
        # source_code = open(sys.argv[1],"r").read()
        source_code = open(args.source_code,"r").read()
    except FileNotFoundError:
        print("source file cannot be open/read.\nCheck the file name or numbers of arguments!!")
        sys.exit(-1)

    if args.l:
        print_lexeme(source_code)

    parser = yacc.yacc(debug=1)
    lexer.lexer.filename = args.source_code
    
    result = parser.parse(source_code, lexer = lexer.lexer)
    
    #print(sym_table)
    if len(Errors.get_all_error()):
        for error in Errors.get_all_error():
            print(error)
        return
    
    Graph = draw_ast(result)
    # print(args)
    if args.p:
        Graph.draw(args.f, format='png')
        print(Graph.string())
        return

    Graph.draw(args.f, format='png')

    file = open(args.o, 'w')
    file.write(Graph.string())
    file.close()
    
    # print(sym_table)
    # print(args.d)
    print_csv(sym_table = sym_table, filename = args.d)
    tac_code = result.code
    tac_code = remove_none(tac_code)
    #to remove redundant labels
    #can also add as args for optimization
    tac_code = remove_label(tac_code)
    print_code(tac_code, filename = args.t)
    # print(alloc)
    print_asm(tac_code)
if __name__ == "__main__":
    main()
