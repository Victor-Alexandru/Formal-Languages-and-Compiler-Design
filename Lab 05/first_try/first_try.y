  
%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token code0
%token code1
%token code2
%token code3
%token code4
%token code5
%token code6
%token code7
%token code8
%token code10
%token code11
%token code12
%token code13
%token code14
%token code15
%token code16
%token code17
%token code18
%token code19
%token code20
%token code21
%token code22
%token code23
%token code24
%token code25
%token code26
%token code27
%token code28
%token code29
%token code30
%token code31
%token code32
%token code33
%token code34
%token code35
%token code36
%token code37
%token code38
%token code39
%token code40
%token code41
%token code42
%token code43
%token code44
%token code45
%token code46
%token code47
%token code48
%token code49
%%


program: code33 code42 code6 code7 code4 stmtlist code5 {printf("%s\n","yacc  program statement ");};
stmtlist: auxstmt  {printf("%s\n","yacc statement ");};
auxstmt: stmt auxstmt | stmt ; 
stmt: declstmt | assignstmt | iostmt | whilestmt | forstmt | ifstmt ;
declstmt: vardeclstmt | arraydeclstmt ;
vardeclstmt: type code0 code8 {printf("%s\n","variable statement ");};
arraydeclstmt: type code0 code2 code1 code3 code8 ;
type: code33 | code34 ;
assignstmt: varassignstmt | arrayassignstmt ;
varassignstmt: code0 code21 expresie code8 ;
arrayassignstmt: code0 code2 code1 code3 code21 expresie code8 ;
iostmt: input | output ;
input: code39 code6 code0 code7 code8 ;
output: code38 code6 expresie code7 code8 ;
whilestmt: code35 code6 conditie code7 code4 stmtlist code5 ;
ifstmt: code36 code6 conditie code7 code4 stmtlist code5 | code36 code6 conditie code7 code4 stmtlist code5 code37 code4 stmtlist code5 ;
forstmt: code41 code6 varassignstmt code8 conditie code8 varmodifystmt code7 code4 stmtlist code5 ;
varmodifystmt: varindentstmt | vardecrementstmt ;
varindentstmt: code0 code31 ;
vardecrementstmt: code0 code30 ;
conditie: expresie ;
expresie: expresie operatie expresie | term ;
operatie: code14 | code15 | code16 | code17 | code18 | code26 | code25 ;
term: code0 | code1 ;
%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv) {
  // Open a file handle to a particular file:
  FILE *myfile = fopen("prg.cpp", "r");
  // Make sure it is valid:
  if (!myfile) {
    printf( "%s\n","I can't open a.snazzle.file!");
    return -1;
  }
  // Set Flex to read from it instead of defaulting to STDIN:
  yyin = myfile;
  
  // Parse through the input:
  yyparse();
  
}