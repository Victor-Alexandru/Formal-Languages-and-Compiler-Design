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
stmtlist: auxstmt  {printf("%s\n","yacc statement list ");};
auxstmt: stmt auxstmt | stmt {printf("%s\n","aux statement ");} ; 
stmt: declstmt | assignstmt | iostmt | whilestmt  | ifstmt  {printf("%s\n","yacc statement ");};
declstmt: vardeclstmt | arraydeclstmt {printf("%s\n","yacc decl statement ");};
vardeclstmt: type code0 code8 {printf("%s\n","variable statement ");};
arraydeclstmt: type code0 code2 code1 code3 code8 {printf("%s\n","array statement ");} ;
type: code33 | code34 {printf("%s\n","type statement ");};
assignstmt: varassignstmt | arrayassignstmt {printf("%s\n","assign statement ");} ;
varassignstmt: code0 code21 expresie code8 {printf("%s\n","varr asign statement ");};
arrayassignstmt: code0 code2 code1 code3 code21 expresie code8 {printf("%s\n","array assign statement ");};
iostmt: input | output {printf("%s\n","IO statement ");};
input: code39 code6 code0 code7 code8 {printf("%s\n","input statement ");};
output: code38 code6 expresie code7 code8 {printf("%s\n","output statement ");};
whilestmt: code35 code6 conditie code7 code4 stmtlist code5 {printf("%s\n","while statement ");};
ifstmt: code36 code6 conditie code7 code4 stmtlist code5 | code36 code6 conditie code7 code4 stmtlist code5 code37 code4 stmtlist code5 {printf("%s\n","if statement ");} ;
varmodifystmt: varindentstmt | vardecrementstmt {printf("%s\n","varmodif statement ");};
varindentstmt: code0 code31 {printf("%s\n","varindentstmt statement ");};
vardecrementstmt: code0 code30 {printf("%s\n","vardecrement statement ");};
conditie: expresie {printf("%s\n","conditie ");};
expresie: expresie operatie expresie | term {printf("%s\n"," expresie ");} ;
operatie: code14 | code15 | code16 | code17 | code18  {printf("%s\n"," operatie ");};
term: code0 | code1 {printf("%s\n"," term  ");};
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
    printf( "%s\n","I can't open prg.cpp file !");
    return -1;
  }
  // Set Flex to read from it instead of defaulting to STDIN:
  yyin = myfile;
  
  // Parse through the input:
  yyparse();
  
}