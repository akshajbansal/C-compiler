#!/usr/local/bin/python3
"""This Script for Syntax Analysis of C code
provided by user"""

import sys
import ply.lex as lex
import ply.yacc as yacc
import clexer as lexer
import argparse
import pygraphviz as pgv
import copy


from utils import draw_ast
from clexer import tokens,print_lexeme
from structure import Errors, Node
from structure import sym_table, BasicType, FunctionType, PointerType, Type
from structure import getMutliPointerType
from typecheck import *
from utils import print_csv, print_code
from threeaddr import *
from codegen import print_asm
#####################Grammar section #################
# print(temp_cnt)

start = 'program' #start action

#Node
def p_program(p):
    'program : translation_unit'
    p[0] = Node("program",children=p[1])
    for node in p[1]:
        if node != None:
            p[0].code += node.code

#List
def p_translation_unit(p):
    '''
    translation_unit : external_declaration
                     | translation_unit external_declaration
    '''
    p[0] = p[1] if len(p)==2 else p[1]+p[2]

#List
def p_external_declaration(p):
    '''
    external_declaration : function_definition
                         | declaration
    '''
    p[0] = p[1]

#List
# def p_external_declaration_1(p):
#     '''
#     external_declaration : function_declaration
#     '''
#     p[0] = []

#List
def p_function_definition(p):
    '''
    function_definition : type_specifier declarator func_scope parameter_type_list func_rparen_1 function_body pop_sym
                        | type_specifier declarator func_scope func_rparen_2 function_body pop_sym
    '''
    
    if len(p) == 8:
        p[0] = Node("function",p[2].value,children=[p[6]])
    else:
        p[0] = Node("function",p[2].value,children=[p[5]])
    p[0].code = [gen(op="label",place1=p[2].value,code=p[2].value+":")]
    p[0].code += [gen(op="BeginFunc",place1=p[2].value,code="BeginFunc")]
    if len(p) == 8:
        if has_break_continue(p[6].code):
            Errors(
                errorType='SyntaxError',
                errorText='invalid break/continue in function',
                token_object= p[2].data['token']
            )
        p[0].code += p[6].code
    else:
        if has_break_continue(p[5].code):
            Errors(
                errorType='SyntaxError',
                errorText='invalid break/continue in function',
                token_object= p[2].data['token']
            )
        p[0].code += p[5].code
    p[0].code += [gen(op="EndFunc",place1=p[2].value,code="EndFunc")]
    p[0] = [p[0]]

def p_function_definition_1(p):
    '''
    function_definition  : type_specifier declarator func_scope parameter_type_list R_PAREN SEMI_COLON pop_sym
                         | type_specifier declarator func_scope R_PAREN SEMI_COLON pop_sym
    '''
    p[0] = []
    #make unused sym = True
    # if len(p) == 8: p[7].unused = True
    # else: p[6].unused = True
    success = sym_table.look_up(name=p[2].value,token_object=p[2].data['token'],no_error=True)
    if success != None:
         Errors(
                errorType='DeclarationError',
                errorText='Function is already declared/defined',
                token_object= p[2].data['token']
            )
    else:
        if len(p) == 8:
            sym_table.add_entry(name=p[2].value,type=FunctionType(return_type=p[2].type,param_list=p[4],defined=False,symbol_table=p[7]))
        else:
            sym_table.add_entry(name=p[2].value,type=FunctionType(return_type=p[2].type,param_list=[],defined=False,symbol_table=p[6]))


def p_func_scope(p):
    '''
    func_scope : L_PAREN
    '''
    decl = p.stack[-1].value #getting function name and return type
    if decl.type.class_type == "PointerType" and len(decl.type.array_size) != 0:
        Errors(
                errorType='DeclarationError',
                errorText='Function cannot have array return type',
                token_object= p.slice[-1]
            )
       
    sym_table.start_scope(name=decl.value) #starting scope of function
    sym_table.add_entry(name='return',type=decl.type) #creating entry to check return type
    p[0] = (decl,FunctionType(return_type=decl.type,symbol_table=sym_table.curr_symbol_table)) #type of function


#with parameters
def p_func_rparen_1(p):
    '''
    func_rparen_1 : R_PAREN
    '''
    if p.stack[-2].value == "error":
        return
    func_name = p.stack[-2].value[0].value
    token = p.stack[-2].value[0].data['token']
    func_type = p.stack[-2].value[1]
    param_list = p.stack[-1].value
    func_type.add_param_list(param_list)
    #adding function to global table after creating paramlist
    success = sym_table.curr_symbol_table.parent._look_up(name=func_name,token_object=p.slice[-1],no_error=True)
    if success and success.type.class_type == "FunctionType":
        if success.type.defined == True:
            Errors(
                errorType='DeclarationError',
                errorText='Function is already defined',
                token_object= p.slice[-1]
            )
        #checking if same parameters
        elif func_type.is_same(success.type) == False:
            Errors(
                errorType='DeclarationError',
                errorText='Function is declared with different parameters/return type',
                token_object= p.slice[-1]
            )
        else:
            #removing sym table of decl
            success.type.symbol_table.unused = True
            success.type.symbol_table = sym_table.curr_symbol_table
            success.type.defined = True
    else:
        sym_table.curr_symbol_table.parent._add_entry(name=func_name,type=func_type,token_object=token)

#without parameters    
def p_func_rparen_2(p):
    '''
    func_rparen_2 : R_PAREN
    '''
    if p.stack[-2].value == "error":
        return
    func_name = p.stack[-1].value[0].value
    token = p.stack[-1].value[0].data['token']
    func_type = p.stack[-1].value[1]
    func_type.param_list = []
    success = sym_table.curr_symbol_table.parent._look_up(name=func_name,token_object=token,no_error=True)
    if success:
        if success.type.defined == True:
            Errors(
                errorType='DeclarationError',
                errorText='Function is already defined',
                token_object= p.slice[-1]
            )
        #checking if same parameters
        elif func_type.is_same(success.type) == False:
            Errors(
                errorType='DeclarationError',
                errorText='Function is declared with different parameters/return type',
                token_object= p.slice[-1]
            )
        else:
            success.type.symbol_table.unused = True
            success.type.symbol_table = sym_table.curr_symbol_table
    else:
        sym_table.curr_symbol_table.parent._add_entry(name=func_name,type=func_type,token_object=token)

    # sym_table.curr_symbol_table.parent._add_entry(name=func_name,type=func_type,token_object=token)




def p_primary_expression(p):
    '''
    primary_expression : IDENTIFIER
                       | COLON COLON IDENTIFIER
                       | INT_CONSTANT
                       | HEX_CONSTANT
                       | OCTAL_CONSTANT
                       | EXPONENT_CONSTANT
                       | REAL_CONSTANT
                       | CHAR_CONSTANT
                       | STR_CONSTANT
                       | L_PAREN expression R_PAREN
                       | TRUE
                       | FALSE
                       | NULL
    '''
    if p[1] == ":":
        success = sym_table._look_up(name=p[3],token_object=p.slice[-1])
        if success:
                p[0] = Node(name="id",value="global: "+p[3],type=success.type)
                p[0].place = p[3]+"|"+"global"
                if success.type.class_type == "PointerType" and success.type.is_array == True:
                    tmp = get_newtmp()
                    p[0].code += [gen(op="addr",place1=p[0].place,place3=tmp,code=tmp+" = "+"addr("+p[0].place+")")]
                    p[0].place = tmp
        else:
            p[0] = Node(name="id",type='error')
        return
    if len(p) == 2:
        if p.slice[-1].type == "IDENTIFIER":
            #looking for id
            success = sym_table.look_up(name=p[1],token_object=p.slice[-1])
            if success:
                p[0] = Node(name="id",value=p[1],type=success.type)
                p[0].place = p[1]+"|"+success.symbol_table.name
                if success.type.class_type == "PointerType" and success.type.is_array == True:
                    tmp = get_newtmp()
                    p[0].code += [gen(op="addr",place1=p[0].place,place3=tmp,code=tmp+" = "+"addr("+p[0].place+")")]
                    p[0].place = tmp
            else:
                p[0] = Node(name="id",type='error')
            return

        if p.slice[-1].type in ["INT_CONSTANT","HEX_CONSTANT","OCTAL_CONSTANT"]:
            if int(p[1]) <= (2**31 - 1) and int(p[1]) >= -(2**31 -1):
                p[0] = Node(name="constant",value=p[1],type=BasicType('int'))
            else:
                p[0] = Node(name="constant",value=p[1],type=BasicType('long'))
            p[0].constant = p[1]
                
        
        elif p.slice[-1].type in ["EXPONENT_CONSTANT","REAL_CONSTANT"]:
            p[0] = Node(name="constant",value=p[1],type=BasicType('float'))
            p[0].constant = p[1]
        
        elif p.slice[-1].type == "CHAR_CONSTANT":
            p[0] = Node(name="constant",value=p[1],type=BasicType('char'))
            p[0].constant = ord(remove_backslash(p[1][1]))

        elif p.slice[-1].type == "STR_CONSTANT":
            string = remove_backslash(p[1][1:-1])
            str_type = PointerType(type=BasicType('char'),array_size=[len(string)+1],array_type=BasicType('char'))
            p[0] = Node(name="constant",value=p[1],type=str_type)
            #string is assigned as tmp not const
            p[0].place = get_str_const(string)
            return
        elif p.slice[-1].type == "NULL":
            p[0] = Node(name="constant",value=p[1],type=PointerType(type=Type()))
            p[0].constant = 0
        else:
            p[0] = Node(name="constant",value=p[1],type=BasicType('bool'))
            p[0].constant = 1 if p[1] == "true" else 0
        p[0].place = get_const(const=p[0].constant,type=p[0].type)
        # p[0].code = [gen(op="eqc_"+p[0].type.stype,place1=str(p[0].constant),place3=p[0].place)]
    
    else:
        p[0] = p[2]

#Node
def p_postfix_expression(p):
    '''
    postfix_expression : primary_expression
                       | postfix_expression INCREMENT
                       | postfix_expression DECREMENT

    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        # p[1] = load_place(p[1])
        allowed_base = {'int','float','char','long'}
        allowed_class = {'PointerType'}
        if p[1].type == 'error':
            p[0] = p[1]
        elif 'const@' in p[1].place:
            Errors(
            errorType='TypeError',
            errorText=p[2] + " not valid on constant",
            token_object= p.slice[-1]
            )
            p[0] = Node(type="error")
        elif (p[1].type.class_type == 'BasicType' and p[1].type.type in allowed_base) or p[1].type.class_type in allowed_class:
            p[0] = Node(name="unary_op",value=str(p[1].type)+': p'+p[2],children=[p[1]],type=p[1].type)
            p[0].place = get_newtmp(type=p[1].type)
            # print(p[1].place+"1")
            node_assign = type_check_assign(p[0],copy.copy(p[1]),token=p.slice[-1])
            if node_assign.type == "error":
                p[0] = Node(type="error")
                return
            # print(p[1].place+"1")
            p[0].code = node_assign.code
            const_place = get_const(const=1,type=BasicType("long"))
            node_1 = Node(type=BasicType("long"))
            node_1.place = const_place
            p[1].code = list()
            node_op = type_check_assign_op(p[1],node_1,op=p[2][0]+"=",token=p.slice[-1])
            if node_op.type == "error":
                p[0] = Node(type="error")
                return
            p[0].code += node_op.code
            #print(p[0].code)
        
        # elif p[1].type.class_type == 'BasicType' and p[1].type.type in allowed_base:
        #     p[0] = Node(name="unary_op",value=str(p[1].type)+': p'+p[2],children=[p[1]],type=p[1].type)
        #     p[0].place = get_newtmp(type=p[1].type)
        #     p[0].code = p[1].code
        #     p[0].code += [gen(op=str(p[1].type)+"=",place1=p[1].place,place3=p[0].place)]
        #     #print(p[0].code)
        #     const_place = get_const(const=1,type=p[1].type,use=True)
        #     #add type conversion
        #     p[0].code += [gen(op=str(p[1].type)+p[2][0],place1=p[1].place,place2=const_place,place3=p[1].place)]
        #     #print(p[0].code)
        # elif p[1].type.class_type in allowed_class:
        #     p[0] = Node(name="unary_op",value=str(p[1].type)+': p'+p[2],children=[p[1]],type=p[1].type)
        #     p[0].place = get_newtmp(type=p[1].type)
        #     p[0].code = p[1].code
        #     p[0].code += [gen(op=str(p[1].type)+"=",place1=p[1].place,place3=p[0].place)]
        #     width = p[1].type.type_size
        #     const_place = get_const(const=width,type="long",use=True)
        #     p[0].code += [gen(op="long"+p[2][0],place1=p[1].place,place2=const_place,place3=p[1].place)]
        #     #print(p[0].code)
        else:
            p[0] = p[1]
            p[0].type = 'error'
            Errors(
                errorType='TypeError',
                errorText='increment/decrement not possible',
                token_object= p.slice[-1]
            )
        

def p_postfix_expression_1(p):
    # Array ref
    ''' 
    postfix_expression : postfix_expression L_SQBR constant_expression R_SQBR
    '''
    # p[3] = load_place(p[3])
    p[1] = load_place(p[1])
    allowed_class = {'BasicType'}
    allowd_base = {'int','long'}
    check1 = True
    check2 = True
    if "const@" in p[1].place:
        Errors(
            errorType='TypeError',
            errorText="array ref not valid on constant",
            token_object= p.slice[-1]
            )
        p[0] = Node(type="error")
        return
    if p[3].type == "error":
        check1 = False
        p[0] = Node(type="error")
    elif p[3].type.class_type not in allowed_class or p[3].type.type not in allowd_base:
        Errors(
            errorType='TypeError',
            errorText='wrong index type '+p[3].type.stype,
            token_object= p.slice[-1]
        )
        check1  = False
        p[0] = Node(type="error")

    allowed_class = {'PointerType'}
    if p[1].type == "error":
        check2 = False
        p[0] = Node(type="error")
    elif p[1].type.class_type not in allowed_class:
        Errors(
            errorType='TypeError',
            errorText='cannot reference type '+p[1].type.stype,
            token_object= p.slice[-1]
        )
        check2  = False
        p[0] = Node(type="error")

    if check1 and check2:
        #type_casting
        p[0] = Node(name="array_ref",value = "[]",type=p[1].type.type,children=[p[1],p[3]])
        p[0].code = p[1].code + p[3].code
        #when pointer
        if len(p[1].type.array_size) == 0:
            const_place = get_const(p[1].type.type_size,type="long")
            tmp,code = get_opcode(op="long*",place1=p[3].place,place2=const_place,type="long")
            p[0].code += [code]
            tmp,code = get_opcode(op="long+",place1=p[1].place,place2=tmp,type="long")
            p[0].place = "load$"+tmp
            p[0].code += [code]
        #when array
        else:
            p[0].type.array_size = p[1].type.array_size[1:]
            width = 1
            for i in p[1].type.array_size[1:]:
                width = width*i
            width = width*p[1].type.array_type.width
            const_place = get_const(width,type="long")
            tmp,code = get_opcode(op="long*",place1=p[3].place,place2=const_place,type="long")
            p[0].code += [code]
            # tmp1 = get_newtmp(BasicType("long"))
            #addr of array
            # if "load$" in p[1].place:
            #     addr = p[1].place.split("$")[1]
            # else:
            #     addr = get_newtmp(BasicType("long"))
            #     p[0].code += [gen(op="addr",place1=p[1].place,place3=addr)]
            # tmp,code = get_opcode(op="long+",place1=addr,place2=tmp,type="long")
            tmp,code = get_opcode(op="long+",place1=p[1].place,place2=tmp,type="long")
            if p[0].type.class_type == "PointerType" and p[0].type.is_array == True:
                p[0].place = tmp
            else:
                p[0].place = "load$"+tmp
            p[0].code += [code]




def p_postfix_expression_2(p):
    # function ref
    ''' 
    postfix_expression : postfix_expression L_PAREN R_PAREN
                       | postfix_expression L_PAREN argument_expression_list R_PAREN
    
    '''
    p[1] = load_place(p[1])
    if p[1].type == "error":
        p[0] = Node(type="error")
        return

    if p[1].type.class_type != "FunctionType":
        p[0] = Node(type="error")
        Errors(
            errorType='TypeError',
            errorText='not function type',
            token_object= p.slice[-1]
        )
        return

    param_list = p[1].type.param_list
    return_type = p[1].type.return_type

    if len(p) == 4:
        if len(param_list) != 0:
            p[0] = Node(type="error")
            Errors(
                errorType='TypeError',
                errorText='Function require more arguments',
                token_object= p.slice[-1]
            )
        else:
            p[0] = Node(name="func_call",type=return_type,children=[p[1]])
            p[0].code = p[1].code
            p[0].place = get_newtmp(type=return_type) if return_type.stype != "void" else "None"
            p[0].code += [gen(op="func_call",place1=p[1].value,place2 = list(),place3=p[0].place)]
    else:
        arg_list = p[3].children
        if len(arg_list) != len(param_list):
            p[0] = Node(type="error")
            Errors(
                errorType='TypeError',
                errorText='No of arguments is not matching',
                token_object= p.slice[-1]
            )
            return
        arg_places = []
        code = []
        push_code = []
        pop_code = []
        for i in range(len(arg_list)):
            if arg_list[i].type == "error" or param_list[i] == "error":
                p[0] = Node(type="error")
                return
            if arg_list[i].type.is_convertible_to(param_list[i]) == False:
                p[0] = Node(type="error")
                Errors(
                    errorType='TypeError',
                    errorText="cannot convert "+arg_list[i].type.stype+" to "+param_list[i].stype,
                    token_object= p.slice[-1]
                )
                return
            node = typecast(arg_list[i],param_list[i],p.slice[-1])
            if "sconst@" in node.place:
                tmp = get_newtmp(type=node.type)
                node.code += [gen(op="str=",place1=node.place,place3=tmp)]
                const_use(node.place,sconst=True)
                node.place = tmp
            arg_places.append(node.place)
            if "const@" in node.place:
                const_use(node.place)
            code += node.code
            push_code += [gen(op = "push",place1=node.place,code="push "+node.place)]
            pop_code += [gen(op = "pop",place1=node.place,code="pop "+node.place)]
        
        p[0] = Node(name="func_call",type=return_type,children=[p[1],p[3]])
        p[0].place = get_newtmp(type=return_type) if return_type.stype != "void" else "None"
        p[0].code = p[1].code+code+push_code + [gen(op="func_call",place1=p[1].value,place2=arg_places,place3=p[0].place)] + pop_code[::-1]

        
        



def p_postfix_expression_3(p):
    # struct ref
    ''' 
    postfix_expression : postfix_expression DOT IDENTIFIER

    '''
    if p[1].type == "error":
        p[0] = Node(type="error")
        return
    if p[1].type.class_type != "StructType":
        p[0] = Node(type="error")
        Errors(
            errorType='TypeError',
            errorText='not struct type',
            token_object= p.slice[-1]
        )
        return
    
    # arg_dict = p[1].type.arg_dict
    struct_sym = p[1].type.symbol_table
    success = struct_sym._look_up(p[3],token_object=p.slice[3],in_struct=True,no_error=True)
    # success = arg_dict.get(p[3])
    if success == None:
        Errors(
            errorType='DeclarationError',
            errorText='variable '+p[3]+' not declared in struct',
            token_object= p.slice[-1]
        )
        p[0] = Node(type="error")
        return
    p[3] = Node(name="id",value=p[3])
    p[0] = Node(name="struct ref",value=p[2],type=success.type,children=[p[1],p[3]])
    p[0].code = p[1].code
    # tmp = get_newtmp()
    # p[0].code += [gen(op="addr",place1=p[1].place,place3=tmp,code=tmp+" = "+"addr("+p[1].place+")")]
    #addr of struct
    if "load$" in p[1].place:
        addr = p[1].place.split("$")[1]
    else:
        addr = get_newtmp()
        p[0].code += [gen(op="addr",place1=p[1].place,place3=addr)]
    # print(success.offset)
    const_place = get_const(const=success.offset-success.width,type="long")
    tmp1,code = get_opcode(op="long+",place1=addr,place2=const_place,type="long")
    p[0].code += [code]
    p[0].place = "load$"+tmp1

    


def p_postfix_expression_4(p):
    # struct ref
    ''' 
    postfix_expression : postfix_expression ARROW IDENTIFIER
    
    '''
    p[1] = load_place(p[1])
    if p[1].type == "error":
        p[0] = Node(type="error")
        return
    if p[1].type.class_type != "PointerType" or p[1].type.type.class_type != "StructType":
        p[0] = Node(type="error")
        Errors(
            errorType='TypeError',
            errorText='not pointer of struct type',
            token_object= p.slice[-1]
        )
        return
    
    # arg_dict = p[1].type.type.arg_dict
    # success = arg_dict.get(p[3])
    struct_sym = p[1].type.type.symbol_table
    success = struct_sym._look_up(p[3],token_object=p.slice[3],in_struct=True,no_error=True)
    if success == None:
        Errors(
            errorType='DeclarationError',
            errorText='variable '+p[3]+' not declared in struct',
            token_object= p.slice[-1]
        )
        p[0] = Node(type="error")
        return
    p[3] = Node(name="id",value=p[3])
    p[0] = Node(name="struct ref",value=p[2],type=success.type,children=[p[1],p[3]])
    p[0].code = p[1].code
    const_place = get_const(const=success.offset-success.width,type="long")
    tmp,code = get_opcode(op="long+",place1=p[1].place,place2=const_place,type="long")
    p[0].code += [code]
    p[0].place = "load$"+tmp




#Node
def p_argument_expression_list(p):
    '''
    argument_expression_list : assignment_expression
	                         | argument_expression_list COMMA assignment_expression
    '''
    if len(p) == 2:
        # p[1] = load_place(p[1])
        p[0] = Node("argument_expression_list",children=[p[1]])
        p[0].data['args_type'] = [p[1].type]
        p[0].place = [p[1].place]
        p[0].code += p[1].code
    else:
        # p[3] = load_place(p[3])
        p[1].addChild(p[3])
        p[1].data['args_type'] += [p[3].type]
        p[1].code += p[3].code
        p[1].place += [p[3].place]
        p[0] = p[1]


#Node
def p_unary_expression(p):
    '''
    unary_expression : postfix_expression
    '''
    p[0] = p[1]

#Node
def p_unary_expression_1(p):
    '''
    unary_expression : INCREMENT unary_expression
                     | DECREMENT unary_expression
    '''
    # p[2] = load_place(p[2])
    p[0] = type_check_unary(node1=p[2],op=p[1],token=p.slice[1])

#Node
def p_unary_expression_2(p):
    '''
    unary_expression : unary_operator cast_expression
    '''    
    # p[2] = load_place(p[2]) 
    p[0] = type_check_unary(node1=p[2],op=p[1]['op'],token=p[1]['token'])

#Node
def p_unary_expression_3(p):
    '''
    unary_expression : SIZEOF unary_expression
                     | SIZEOF L_PAREN type_name R_PAREN
    '''
   
    if len(p) == 3:
        p[2] = load_place(p[2])
        p[0] = type_check_unary(node1=p[2],op=p[1],token=p.slice[1])
    else:
        p[0] = type_check_unary(node1=p[3],op=p[1],token=p.slice[1],is_typename=True)

#String
def p_unary_operator(p):
    '''
    unary_operator : BITWISE_AND
                   | MULTIPLY
                   | ADD
                   | SUBSTRACT
                   | BITWISE_ONE_COMPLEMENT
                   | LOGICAL_NOT
    '''
    p[0] = {'op':p[1],'token':p.slice[1]}

#Node
def p_cast_expression(p):
    '''
    cast_expression : unary_expression
	                | L_PAREN type_name R_PAREN cast_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2].type == 'error' or p[4].type == 'error':
            p[0] = Node(type='error')
        else:
            if p[4].type.is_convertible_to(p[2].type):
                p[0] = typecast(p[4],p[2].type,token=p.slice[1],hard=True)
            else:
                Errors(
                    errorType='TypeError',
                    errorText="cannot typecast "+p[4].types.stype+" to "+p[2].type.stype,
                    token_object= p.slice[1]
                )
                p[0] = Node(type='error')

#Node
def p_multiplicative_expression(p):
    '''
    multiplicative_expression : cast_expression
                              | multiplicative_expression MULTIPLY cast_expression
                              | multiplicative_expression DIVIDE cast_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_multi(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])

def p_multiplicative_expression_1(p):
    '''
    multiplicative_expression : multiplicative_expression MODULUS cast_expression
    '''
    p[1] = load_place(p[1])
    p[3] = load_place(p[3])
    p[0] = type_check_multi(node1=p[1],node2=p[3],op=p[2],token=p.slice[2],decimal=False)


#Node
def p_additive_expression(p):
    '''
    additive_expression : multiplicative_expression
                        | additive_expression ADD multiplicative_expression
                        | additive_expression SUBSTRACT multiplicative_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_add(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])

#Node
def p_shift_expression(p):
    '''
    shift_expression : additive_expression
                     | shift_expression LEFT_SHIFT additive_expression
                     | shift_expression RIGHT_SHIFT additive_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_bit(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])

#Node
def p_relational_expression(p):
    '''
    relational_expression : shift_expression
                          | relational_expression LESS shift_expression
                          | relational_expression GREATER shift_expression
                          | relational_expression LESS_EQUALS shift_expression
                          | relational_expression GREATER_EQUALS shift_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_relational(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])
        
#Node
def p_equality_expression(p):
    '''
    equality_expression : relational_expression
                        | equality_expression EQUALS relational_expression
                        | equality_expression NOT_EQUALS relational_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_relational(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])
#Node
def p_and_expression(p):
    '''
    and_expression : equality_expression
	               | and_expression BITWISE_AND equality_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_bit(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])

    

#Node
def p_exclusive_or_expression(p):
    '''
    exclusive_or_expression : and_expression
	                        | exclusive_or_expression BITWISE_XOR and_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_bit(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])



#Node
def p_inclusive_or_expression(p):
    '''
    inclusive_or_expression : exclusive_or_expression
	                        | inclusive_or_expression BITWISE_OR exclusive_or_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0] = type_check_bit(node1=p[1],node2=p[3],op=p[2],token=p.slice[2])


#Node
def p_logical_and_expression(p):
    '''
    logical_and_expression : inclusive_or_expression
	                       | logical_and_expression LOGICAL_AND inclusive_or_expression
    '''
    ### Implement typecasting logic
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0]=type_check_logical(node1 = p[1],node2=p[3],op=p[2],token=p.slice[2])

#Node
def p_logical_or_expression(p):
    '''
    logical_or_expression : logical_and_expression
	                      | logical_or_expression LOGICAL_OR logical_and_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[0]=type_check_logical(node1 = p[1],node2=p[3],op=p[2],token=p.slice[2])
        
    

#Node
def p_conditional_expression(p):
    '''
    conditional_expression : logical_or_expression
	                       | logical_or_expression QUES_MARK assignment_expression COLON conditional_expression
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1] = load_place(p[1])
        p[3] = load_place(p[3])
        p[5] = load_place(p[5])
        if p[1].type == "error" or p[3].type == "error" or p[5].type == "error":
            p[0] = Node(type="error")
            return
        allowed_class = {'BasicType'}
        allowed_base = {'int','long','char','bool','float'}
        if p[1].type.class_type not in allowed_class or p[1].type.type not in allowed_base:
            Errors(
                errorType='TypeError',
                errorText=p[2]+' not support type '+p[1].type.stype,
                token_object= p.slice[2]
            )
            p[0] = Node(type="error")
            return
        if p[3].type != p[5].type:
            Errors(
                errorType='TypeError',
                errorText='type should be same',
                token_object= p.slice[2]
            )
            p[0] = Node(type="error")
            return
        p[0] = Node("ternary_op",children = [p[1],p[3],p[5]],type=p[3].type)
        if "const@" in p[1].place:
            if get_const_value(p[1].place):
                p[0].place = p[3].place
                p[0].code = p[3].code
            else:
                p[0].place = p[5].place
                p[0].code = p[5].code
            return
        p[0].place = get_newtmp()
        label = get_newlabel()
        label1 = get_newlabel()

        p[0].code = p[1].code
        p[0].code += [gen(op='ifz', place1=p[1].place, place2 = label)]
        p[0].code += p[3].code
        p[0].code += [gen(op=get_type(p[0].place)+'=', place3 = p[0].place, place1 = p[3].place)]
        p[0].code += [gen(op='goto', place1=label1)]
        p[0].code += [gen(op = 'label', place1 = label)]
        p[0].code += p[5].code
        p[0].code += [gen(op=get_type(p[0].place)+'=', place3 = p[0].place, place1 = p[5].place)]
        p[0].code += [gen(op = 'label', place1 = label1)]


#Node
def p_assignment_expression(p):
    '''
    assignment_expression : conditional_expression
	                      | unary_expression assignment_operator assignment_expression
    '''

    if len(p) == 2:
        p[1] = load_place(p[1])
        p[0] = p[1]
    else:
        p[3] = load_place(p[3])
        p[0] = type_check_assign_op(node1=p[1],node2=p[3],op=p[2]['op'],token=p[2]['token'])


#String
def p_assignment_operator(p):
    '''
    assignment_operator : ASSIGNMENT
                        | MULTIPLY_ASSIGNMENT
                        | DIVIDE_ASSIGNMENT
                        | MODULUS_ASSIGNMENT
                        | ADD_ASSIGNMENT
                        | SUBSTRACT_ASSIGNMENT
                        | LEFT_SHIFT_ASSIGNMENT
                        | RIGHT_SHIFT_ASSIGNMENT
                        | BITWISE_AND_ASSIGNMENT
                        | BITWISE_XOR_ASSIGNMENT
                        | BITWISE_OR_ASSIGNMENT
    '''
    p[0] = {'op':p[1],'token':p.slice[1]}

# Node
def p_expression(p):
    '''
    expression : assignment_expression
	           | expression COMMA assignment_expression
    ''' 
    if len(p) == 2:
        p[0] = p[1]
        if "const@" in p[1].place:
            const_use(p[1].place)
    else:
        if p[1].type == "error" or p[3].type == "error":
            p[0] = Node(type="error")
        if isinstance(p[1],Node) and p[1].name == "expression":
            p[1].addChild(p[3])
            p[0] = p[1]
            p[0].code += p[3].code
        else:
            p[0] = Node(name="expression",children=[p[1],p[3]],type="ok")
            p[0].code = p[1].code + p[3].code
            p[0].place = p[1].place
#Node
def p_constant_expression(p):
    '''
    constant_expression : conditional_expression
    '''
    p[1] = load_place(p[1])
    p[0] = p[1]
    # if "const@" in p[1].place:
    #     const_use(p[1].place)


#List
def p_declaration(p):
    '''
    declaration : struct_specifier SEMI_COLON
	            | type_specifier init_declarator_list SEMI_COLON
                | AUTO auto_declarator_list SEMI_COLON
    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = [None]
    assert isinstance(p[0], list), "return object is not list"



# list (can be None)
def p_init_declarator_list(p):
    '''
    init_declarator_list : init_declarator
	                     | init_declarator_list COMMA init_declarator
    '''
    p[0] = p[1] if len(p) == 2  else p[1]+p[3]
    assert isinstance(p[0], list), "return object is not list, p[0] is:" + str(p[0])

# list (can be None)
def p_init_declarator(p):
    '''
    init_declarator : declarator
	                | declarator ASSIGNMENT assignment_expression
    '''
    if p[1].type == "error":
        p[0] = [None]
        return
    if len(p) == 2:
        success = sym_table.add_entry(name=p[1].value,type=p[1].type,token_object=p[1].data['token'])
        p[0] = [None]
        
    else:
        p[0] = [None]
        if p[3].type == "error":
            return
        if p[3].type.is_convertible_to(p[1].type) == False:
            Errors(
                errorType='TypeError',
                errorText="cannot assign "+p[3].type.stype+" to "+p[1].type.stype,
                token_object= p.slice[2]
            )
            return
        if p[1].type.class_type == "PointerType" and len(p[1].type.array_size) != 0:
            if len(p[1].type.array_size) > 1:
                Errors(
                    errorType='DeclarationError',
                    errorText="cannot initialize array with multiple dimension", 
                    token_object= p.slice[2]
                )
                return
            if p[1].type.array_type.stype != "char":
                Errors(
                    errorType='DeclarationError',
                    errorText="cannot initialize array of type "+p[1].type.array_type.stype, 
                    token_object= p.slice[2]
                )
                return
            if "sconst@" not in p[3].place:
                Errors(
                    errorType='DeclarationError',
                    errorText="cannot initialize array of type char with non-string value", 
                    token_object= p.slice[2]
                )
                return

        node = typecast(node1=p[3],type=p[1].type,token=p.slice[2])
        if node.type == "error":
            return
        if "sconst@" in node.place and len(p[1].type.array_size) == 0:
            string = node.place.split("@")[-1]
            p[1].type = PointerType(type=BasicType("char"),array_type=BasicType("char"),array_size=[len(string)+1])
        success = sym_table.add_entry(name=p[1].value,type=p[1].type,token_object=p[1].data['token'])
        if success:
            p[0] = Node(name="binary_op",value=p[1].type.stype+"=",children = [p[1],node],type="ok")
            p[0].code = node.code
            p[0].place = p[1].value+"|"+success.symbol_table.name
            if success.symbol_table.name == "global":
                if "const@" not in node.place:
                    Errors(
                        errorType='DeclarationError',
                        errorText="can declare global variable with only constant value",
                        token_object= p.slice[2]
                    )
                    p[0] = [None]
                    return 
                else:
                    if "sconst@" in  node.place:
                        alloc[p[0].place] = node.place.split("@")[-1]
                    else:
                        alloc[p[0].place] = get_const_value(node.place)   
                    p[0] = [p[0]]
                    return
            p[0].code += [gen(op=get_type(node)+"=",place1=node.place,place3=p[0].place)]
            if "const@" in node.place:
                const_use(node.place,sconst=True)
            p[0] = [p[0]]
        else:
            p[0] = [None]

#List
def p_auto_declarator_list(p):
    '''
    auto_declarator_list : auto_declarator
                         | auto_declarator_list COMMA auto_declarator
    '''
    p[0] = p[1] if len(p) == 2  else p[1]+p[3]

#List
def p_auto_declarator(p):
    '''
    auto_declarator : IDENTIFIER ASSIGNMENT assignment_expression
                    | IDENTIFIER
    '''
    p[0] = [None]
    if len(p) == 2:
        Errors(
                errorType='DeclarationError',
                errorText="cannot declare auto variable without initialization",
                token_object= p.slice[1]
        )
        return
    if p[3].type == "error":
        return
    if p[3].type.class_type == "PointerType" and p[3].type.is_array == True:
        Errors(
                errorType='DeclarationError',
                errorText="cannot declare auto variable with array",
                token_object= p.slice[1]
        )
        return
    if p[3].type.class_type == "FunctionType":
        Errors(
                errorType='DeclarationError',
                errorText="cannot declare auto variable with function",
                token_object= p.slice[1]
        )
        return
    success = sym_table.add_entry(name=p[1],type=p[3].type,token_object=p.slice[1])
    node = Node(name="id",value=p[1],type=p[3].type)
    if success:
        p[0] = Node(name="binary_op",value=p[3].type.stype+"=",children = [node,p[3]],type="ok")
        p[0].code = p[3].code
        p[0].place = p[1]+"|"+success.symbol_table.name
        if success.symbol_table.name == "global":
            if "const@" not in node.place:
                Errors(
                    errorType='DeclarationError',
                    errorText="can declare global variable with only global value",
                    token_object= p.slice[2]
                )
                p[0] = [None]
                return 
            else:
                if "sconst@" in  node.place:
                    alloc[p[0].place] = node.place.split("@")[-1]
                else:
                    alloc[p[0].place] = get_const_value(node.place)   
                p[0] = [p[0]]
                return
        p[0].code += [gen(op=get_type(p[3])+"=",place1=p[3].place,place3=p[0].place)]
        if "const@" in p[3].place:
                const_use(p[3].place)
        p[0] = [p[0]]

# Node
def p_type_specifier(p):
    '''
    type_specifier : VOID
                   | CHAR
                   | INT
                   | LONG
                   | FLOAT
                   | STRUCT IDENTIFIER
                   | BOOL
    '''

    if p[1] == 'struct':
        success = sym_table.look_up_struct(name = p[2],token_object=p.slice[-1])
        if success:
            p[0] = Node(type = success)
        else:
            p[0] = Node(type="error")
    else:
        if p[1] == 'void':
            p[0] = Node(type = Type())
        else:
            p[0] = Node(type = BasicType(type = p[1]))

    assert isinstance(p[0], Node), "return object is not Node"
    assert p[0].type == 'error' or isinstance(p[0].type, Type), "unexpected type attribute of return object"


# String
def p_struct_specifier(p):
    '''
    struct_specifier : STRUCT IDENTIFIER add_sym_struct struct_declaration_list pop_sym R_BRACES
    '''



def p_add_sym_struct(p):
    '''
    add_sym_struct : L_BRACES
    '''   
    name = p.stack[-1].value
    sym_table.start_scope(name)
    sym_table.curr_symbol_table.parent._add_struct_entry(name=name,symbol_table=sym_table.curr_symbol_table,token_object=p.slice[1])
# dict
def p_struct_declaration_list(p):
    '''
    struct_declaration_list : struct_declaration
	                        | struct_declaration_list struct_declaration
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].update(p[2])

# dict
def p_struct_declaration(p):
    '''
    struct_declaration : type_specifier struct_declarator_list SEMI_COLON
    '''
    p[0] = p[2]


# dict
def p_struct_declarator_list(p):
    '''
    struct_declarator_list : declarator
	                       | struct_declarator_list COMMA declarator
    '''
    success = None
    if len(p) == 2:
        if p[1].type == "error":
            p[0] = dict({})
            return
        # print(p[1].type.class_type,p[1].value)
        if p[1].type.class_type == "StructType" and p[1].type.name == sym_table.curr_symbol_table.name:
            Errors(
                    errorType='DeclarationError',
                    errorText='cannot declare variable with same struct type within same struct',
                    token_object= p[1].data['token']
            )
            p[0] = dict({})
            return
        success = sym_table.add_entry(name=p[1].value,type=p[1].type,token_object=p[1].data['token'])
        if success:
            p[0] = {p[1].value:p[1].type}
        else:
            p[0] = dict({})

    else:
        if p[3].type == "error":
            p[0] = p[1]
            return
        if p[3].type.class_type == "StructType" and p[3].type.name == sym_table.curr_symbol_table.name:
            Errors(
                    errorType='DeclarationError',
                    errorText='cannot declare variable with same struct type within same struct',
                    token_object= p[3].data['token']
            )
            p[0] = p[1]
            return
        success = sym_table.add_entry(name=p[3].value,type=p[3].type,token_object=p[3].data['token'])
        if success:
            p[0] = p[1]
            p[0].update({p[3].value:p[3].type})
        else:
            p[0] = p[1]

# Node
def p_declarator(p):
    '''
    declarator : pointer direct_declarator
	           | no_pointer direct_declarator
    '''
    p[0] = p[2]
    assert isinstance(p[0], Node), "return object is not Node"
    assert p[0].type == 'error' or isinstance(p[0].type, Type), "unexpected type attribute of return object"


# Node
def p_direct_declarator(p):
    '''
    direct_declarator : IDENTIFIER
                      | L_PAREN declarator R_PAREN
                      | direct_declarator L_SQBR INT_CONSTANT R_SQBR
    '''
    # | direct_declarator L_SQBR R_SQBR

    if len(p) == 2:
        p[0] = Node(value=p[1], type = p.stack[-1].value.type)
        p[0].data['token'] = p.slice[-1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = p[1]
        if p[0].type == "error":
            return
        if p[0].type.class_type != "PointerType" or len(p[0].type.array_size) == 0:
            p[0].type = PointerType(type = p[0].type,array_size=[p[3]],array_type=p[0].type)
        else:
            p[0].type = PointerType(type=p[0].type,array_size=p[0].type.array_size+[p[3]],array_type=p[0].type.array_type)
        # else:
        #     if p[0].type.class_type == "PointerType" and len(p[0].type.array_size) != 0:
        #         Errors(
        #             errorType='DeclarationError',
        #             errorText="left side size cannot be empty in array",
        #             token_object= p.slice[2]
        #         )
        #         p[0] = Node(type="error")
        #     else:   
        #         p[0].type = PointerType(type = p[0].type,array_size=[float('inf')],array_type=p[0].type)   

    
    assert isinstance(p[0], Node), "return object is not Node"
    assert p[0].type == 'error' or isinstance(p[0].type, Type), "unexpected type attribute of return object"

# Node
def p_pointer(p):
    '''
    pointer : MULTIPLY
            | pointer MULTIPLY
    '''
  
    if len(p) == 2:
        type_specifier_symbol = None
        for symbol in reversed(p.stack):
            if symbol.type in  ['type_specifier', 'pointer', 'no_pointer']:
                type_specifier_symbol = symbol
                break
        if type_specifier_symbol.value.type == "error":
            p[0] = Node(type="error")
        else:
            p[0] = Node(type = PointerType(type = type_specifier_symbol.value.type))
        #p[0] = Node(PointerType(type = p.stack[-1].value.type))
    else:
        p[0] = p[1]
        if p[0].type != "error":
            p[0].type = PointerType(type = p[1].type)
    
    assert isinstance(p[0], Node), "return object is not Node"
    assert p[0].type == 'error' or isinstance(p[0].type, Type), "unexpected type attribute of return object"


# Node

def p_no_pointer(p):
    '''
    no_pointer : 
    '''
    type_specifier_symbol = None
    for symbol in reversed(p.stack):
        if symbol.type in  ['type_specifier', 'pointer', 'no_pointer']:
            type_specifier_symbol = symbol
            break
    p[0] = Node(type = type_specifier_symbol.value.type)
    
    assert isinstance(p[0], Node), "return object is not Node"
    assert p[0].type == 'error' or isinstance(p[0].type, Type), "unexpected type attribute of return object"




#List
def p_parameter_type_list(p):
    '''
    parameter_type_list : parameter_declaration
	                    | parameter_type_list COMMA parameter_declaration
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+p[3]
    
# List
def p_parameter_declaration(p):
    '''
    parameter_declaration : type_specifier declarator
    '''
    if p[2].type.class_type == "PointerType" and len(p[2].type.array_size) !=0 :
        p[2].type.is_array = False
        p[2].type._width = 8
    success = sym_table.add_entry(name=p[2].value,type=p[2].type,token_object=p[2].data['token'])
    if success:
        p[0] = [p[2].type]
    else:
        p[0] = []



# Node
def p_type_name(p):
    '''
    type_name : type_specifier
	          | type_specifier pointer
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]




# Node
def p_statement(p):
    '''
    statement : compound_statement
	          | expression_statement
	          | selection_statement
	          | iteration_statement
	          | jump_statement
    '''
    p[0] = p[1]

# Node

def p_labeled_statement_list(p):
    '''
    labeled_statement_list : labeled_statement_list labeled_statement
                           | labeled_statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]+[p[2]]

def p_labeled_statement(p):
    '''
    labeled_statement : CASE constant_expression COLON statement
	                  | DEFAULT COLON statement
    '''
    
    if p.slice[1].type == 'CASE':
        if p[2].type == "error" or p[4].type == "error":
            p[0] = Node(type="error")
            return 
        if p[2].type.class_type != "BasicType":
            Errors(
                    errorType='TypeError',
                    errorText='invalid type ' + p[2].type.stype + ' in case',
                    token_object= p.slice[1]
                )
            p[0] = Node(type="error")
            return   

        p[0] = Node("case",children=[p[2],p[4]],type="ok")
        p[0].data['expr'] = p[2]
        if "const@" in p[2].place:
            const_use(p[2].place)
        p[0].data['stmt'] = p[4]
        p[0].data['token'] = p.slice[1]
    else:
        if p[3].type == "error":
            p[0] = Node(type="error")
            return 
        p[0] = Node("default",children=[p[3]],type="ok")
        p[0].data['expr'] = None
        p[0].data['stmt'] = p[3]
        p[0].data['token'] = p.slice[1]

# Node
def p_compound_statement(p):
    '''
    compound_statement : L_BRACES R_BRACES
	                   | L_BRACES add_sym block_item_list pop_sym R_BRACES
    '''
    if len(p) == 3:
        p[0] = Node("compound_statement","{}",type="ok")
    else:
        p[0] = Node("compound_statement","{}",children=p[3],type="ok")
        for node in p[3]:
            if node != None:
                p[0].code += node.code
    # print(p, p.__dict__, p[-1], p.stack[-1], p.stack[-1].__dict__)

def p_function_body(p):
    '''
    function_body : L_BRACES R_BRACES
	              | L_BRACES block_item_list R_BRACES
    '''
    if len(p) == 3:
        p[0] = Node("compound_statement","{}",type="ok")
    else:
        p[0] = Node("compound_statement","{}",children=p[2],type="ok")
        for node in p[2]:
            if node != None:
                assert isinstance(node.code,list), print(node.code)
                p[0].code += node.code

# List
def p_block_item_list(p):
    '''
    block_item_list : block_item
                   | block_item_list block_item
    '''
    p[0] = p[1] if len(p) == 2 else p[1]+p[2]

# List     
def p_block_item(p):
    '''
    block_item : statement
                | declaration
    '''
    if p.slice[1].type == "statement":
        p[0] = [p[1]]
    else:
        p[0] = p[1]
 


# Node
def p_expression_statement(p):
    '''
    expression_statement : SEMI_COLON
	                     | expression SEMI_COLON
    '''
    if len(p) == 2:
        p[0] = Node(value = p[1],type="ok")
    else:
        p[0] = p[1]

# Node
def p_selection_statement(p):
    '''
    selection_statement : IF L_PAREN expression R_PAREN statement
	                    | IF L_PAREN expression R_PAREN statement ELSE statement
	                    | SWITCH L_PAREN expression R_PAREN L_BRACES add_sym labeled_statement_list pop_sym R_BRACES
    '''
    if p[1] == "if":
        if len(p) == 6:
            if p[3].type=="error" or p[5].type=="error":
                p[0] = Node(type="error")
                return
            p[0] = Node(name="if",children=[p[3],p[5]],type="ok")

            label = get_newlabel()

            p[0].code = p[3].code
            p[0].code += [gen(op = 'ifz', place1=p[3].place, place2 = label)]
            p[0].code += p[5].code
            p[0].code += [gen(op = "label",place1=label)]

        else:
            if p[3].type=="error" or p[5].type=="error" or p[7].type=="error":
                p[0] = Node(type="error")
                return
            p[0] = Node(name="if_else",children=[p[3],p[5],p[7]],type="ok")

            label1 = get_newlabel()
            label2 = get_newlabel()

            p[0].code = p[3].code
            p[0].code += [gen(op = 'ifz', place1=p[3].place, place2 = label1)]
            p[0].code += p[5].code
            p[0].code += [gen(op="goto",place1=label2)]
            p[0].code += [gen(op = "label",place1=label1)]
            p[0].code += p[7].code
            p[0].code += [gen(op = "label",place1=label2)]

    else:
        p[0] = Node(type="error")
        if p[3].type=="error":
            return
        if p[3].type.class_type != "BasicType":
            Errors(
                    errorType='TypeError',
                    errorText='invalid type ' + p[3].type.stype + ' in switch',
                    token_object= p.slice[1]
                )
            return    
        label_list = Node(name="labeled list",children=p[7],type="ok")
        p[0] = Node(name="switch",children=[p[3],label_list],type="ok")
        label_list = p[7]
        p[0].code = p[3].code
        place = p[3].place
        end_label = get_newlabel()
        for labels in label_list:
            assert isinstance(labels,Node), "labels should be node"
            if labels.type == "error":
                p[0] = Node(type="error")
                return
            if labels.data['expr'] == None:
                p[0].code += labels.data["stmt"].code
            else:
                const = labels.data['expr']
                const = typecast(const,type=p[3].type)
                new_label = get_newlabel()
                p[0].code += const.code
                p[0].code += [gen(op="if_not_cmp_"+p[3].type.stype,place1=place,place2=const.place,place3=new_label,code="if "+place+" <> "+const.place+" goto "+new_label)]
                p[0].code += labels.data["stmt"].code
                p[0].code += [gen("label",place1=new_label)]
        p[0].code += [gen("label",place1=end_label)]
        code = break_only(p[0].code,break_label=end_label)
        if code == False:
            Errors(
                errorType='SyntaxError',
                errorText='invalid continue in switch case',
                token_object= p.slice[1],
            )
            p[0] = Node(type="error")
            return
        p[0].code = code

# Node
def p_iteration_statement(p):
    '''
    iteration_statement : WHILE L_PAREN expression R_PAREN statement
	                    | DO statement WHILE L_PAREN expression R_PAREN SEMI_COLON
	                    | FOR L_PAREN expression_statement expression_statement R_PAREN statement
	                    | FOR L_PAREN expression_statement expression_statement expression R_PAREN statement
    '''
    if p[1] == "while":
        if p[3].type=="error" or p[5].type=="error":
            p[0] = Node(type="error")
            return
        p[0] = Node(name="iteration_statement",value="while",children=[p[3],p[5]],type="ok")

        label1 = get_newlabel()
        label2 = get_newlabel()
        p[0].code = [gen(op = "label",place1=label1)]
        p[0].code += p[3].code
        p[0].code += [gen(op = 'ifz', place1 = p[3].place, place2  = label2)]
        code = break_continue(p[5].code,label2,label1)
        p[0].code += code
        p[0].code += [gen(op = "goto", place1 = label1)]
        p[0].code += [gen(op = "label",place1=label2)]

    elif p[1] == "do":
        if p[2].type=="error" or p[5].type=="error":
            p[0] = Node(type="error")
            return
        p[0] = Node(name="iteration_statement",value="do",children=[p[2],p[5]],type="ok")

        label1 = get_newlabel()
        label2 = get_newlabel()
        label3 = get_newlabel()

        p[0].code = [gen(op = "label", place1 = label1)]
        p[0].code += p[2].code
        p[0].code += [gen(op = "label", place1 = label2)]
        p[0].code += p[5].code
        p[0].code += [gen(op = 'ifnz', place1 = p[5].place, place2 = label1)]
        p[0].code += [gen(op = "label", place1 = label3)]
        p[0].code = break_continue(p[0].code, label3, label2)

    else:
        if len(p) == 7:
            if p[3].type=="error" or p[4].type=="error" or p[6].type=="error":
                p[0] = Node(type="error")
                return
            child = [p[3],p[4],p[6]]

            label1 = get_newlabel()
            label2 = get_newlabel()
            # label3 = get_newlabel()

            code = p[3].code
            code += [gen(op = "label", place1 = label1)]

            if p[4].code:
                code += p[4].code
                code += [gen(op = 'ifz', place1 = p[4].place, place2  = label2)]
               
            code += p[6].code
            code += [gen(op = "goto", place1 = label1)]
            code += [gen(op = "label", place1 = label2)]
            code = break_continue(code, label2, label1)

        else:
            if p[3].type=="error" or p[4].type=="error" or p[5].type=="error" or p[7].type=="error":
                p[0] = Node(type="error")
                return
            child = [p[3],p[4],p[5],p[7]]

            label1 = get_newlabel()
            label2 = get_newlabel()
            label3 = get_newlabel()
            # label4 = get_newlabel()

            code = p[3].code
            code += [gen(op = "label", place1 = label1)]

            if p[4].code:
                code += p[4].code
                code += [gen(op = 'ifz', place1 = p[4].place, place2  = label3)]
        
            code += p[7].code
            code += [gen(op = "label", place1 = label2)]
            code += p[5].code
            code += [gen(op = "goto", place1 = label1)]
            code += [gen(op = "label",place1 = label3)]

            code = break_continue(code, label3, label2)

        p[0] = Node(name="iteration_statement",value="for",children=child,type="ok")
        p[0].code = code
    
# Node
def p_jump_statement(p):
    '''
    jump_statement : CONTINUE SEMI_COLON
	               | BREAK SEMI_COLON
	                 
    '''
    
    p[0] = Node(name=p[1],type="ok")
    p[0].code = [gen(op = p[1], code = p[1])]

def p_jump_statement_1(p):
    '''
    jump_statement : RETURN SEMI_COLON
	               | RETURN expression SEMI_COLON      
    '''
    success = sym_table.look_up(name='return',token_object=p.slice[1],no_error=True)
    if success:
        if len(p) == 3:
            if success.type != Type():
                p[0] = Node(type="error")
                Errors(
                    errorType='TypeError',
                    errorText='return type not matching',
                    token_object= p.slice[2]
                )
                p[0].code = []
                return
            p[0] = Node(name="return",type="ok")
            p[0].code = [gen(op = 'return',code = 'return')]
    
        else:
            if p[2].type == "error":
                p[0] = Node(type="error")
                return
            if p[2].type.is_convertible_to(success.type):
                node = typecast(p[2],success.type)    
                p[0] = Node(name="return",type="ok",children=[node])
                p[0].code = node.code
                if "const@" in node.place:
                    const_use(node.place)
                p[0].code += [gen(op = 'return', place1 = node.place, code = 'return ' + node.place)]
                return

            p[0] = Node(type="error")
            Errors(
                errorType='TypeError',
                errorText='return type not matching',
                token_object= p.slice[2]
            )
    else:
        p[0] = Node(type="error")
        Errors(
            errorType='TypeError',
            errorText='Not Function',
            token_object= p.slice[2]
        )

def p_add_sym(p):
    '''
        add_sym :
    '''
    # print("start_scope", p, p.stack, p.slice)
    # name = None
    # if p.stack[-2].type == 'IDENTIFIER':
    #     name = p.stack[-2].value
    sym_table.start_scope()
    p[0] = None

def p_pop_sym(p):
    '''
        pop_sym :
    '''
    p[0] = sym_table.curr_symbol_table
    sym_table.close_scope()
    
def p_error(t):
    if t is None:
        print("End of File Reached. More Input required")    
    else:
        print("syntax error at line no.{0} in file {1}, erroneous lexeme:'{2}'".format(t.lineno, t.lexer.filename,t.value))
    exit(-1)

def get_grammar(code_file,source_code,debug=1):
    parser = yacc.yacc(debug=debug)
    lexer.lexer.filename = code_file
    result = parser.parse(source_code, lexer = lexer.lexer)
    return result


def main():
    """Driver code for Abstract syntax tree 
    Generation"""

    #read source code provided by user
    arg_parser = argparse.ArgumentParser(description="Lexer for Source Language C")
    arg_parser.add_argument('source_code',help="source code file location")
    arg_parser.add_argument('-o',help="take the name of dot script", default="ast.dot")
    arg_parser.add_argument('-f',help="take the name of png file", default="ast.png")
    arg_parser.add_argument('-d',help="take the name of csv file", default="dump.csv")
    arg_parser.add_argument('-t',help="take the name of 3ac file", default="3ac.3ac")
    arg_parser.add_argument('-p',action='store_true',help="output dot script to console")
    arg_parser.add_argument('-l',action='store_true',help="output lexeme table")
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


"""
#refrences: https://www.dabeaz.com/ply/ply.html
            https://www.lysator.liu.se/c/ANSI-C-grammar-y.html
"""
