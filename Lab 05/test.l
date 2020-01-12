%{
    #include <stdio.h>
    int yylex();
    int yyerror(char *s);
    extern int mylineno;
    extern FILE *yyin;
%}

%token ID 
%token COMMENT SPACES TABS
%token INT STRING DIGIT CONSTANT
%token SEMICOLON NEWLINE OTHER
%token EQEQ EQ
%token ILLEGAL_SIZE_OF_IDENTIFIER ILLEGAL_IDENTIFIER

%type <name> ID
%type <number> INT

%union {
    char name[20];
    int number;
}

%%
prog:
    stmts
;
stmts:
	| stmt SEMICOLON stmts

stmt:
    | COMMENT {printf("comment");}
    | SPACES {printf("spaces");}
    | TABS {printf("tabs");}
    | ID {printf("id: %s\n", $1);}
    | DIGIT {printf("digit: ");}
    | STRING {printf("string: ");}
    | INT {printf("integer: %d\n", $1);}
    | CONSTANT {printf("constant: ")}
    | ID SPACES EQ SPACES DIGIT {printf("assignment\n")}
    | ID SPACES EQ SPACES INT {printf("assignment\n")}
    | ILLEGAL_SIZE_OF_IDENTIFIER {printf("Illegal size of the identifier.\n");}
    | ILLEGAL_IDENTIFIER {printf("Illegal identifier.\n");}
    | OTHER
;
%%

int yyerror(char *s) {
    printf("Syntax error on line: %d\n", mylineno);
    return 0;
}

int yywrap() { 
    return 1;
}

int main(int argc, char **argv)
{
    int opened_file = 0, rparse;
    if ( argc > 0 ) {
        yyin = fopen( argv[1], "r" ); 
        opened_file = 1;
    }
    else {
        yyin = stdin; 
    }
    
    int ntoken, vtoken;

    rparse = yyparse();
    ntoken = yylex();
    while(ntoken && rparse == 0)
    {
        printf("%d\n", ntoken);
        if(ntoken == -1)
            return 0;
        rparse = yyparse();
        ntoken = yylex();
    }

    if(opened_file == 1) {
        fclose(yyin);
    }
    return 0;
}