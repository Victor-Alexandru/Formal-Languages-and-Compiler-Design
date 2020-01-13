%{

#include <stdio.h>
#include "viena.tab.h"

%}

%%
[\t]
[\n]
[\r]
[ ]
\[ {return code2;}
\] {return code3;}
\{ {return code4;}
\} {return code5;}
\( {return code6;}
\) {return code7;}
; {return code8;}
, {return code10;}
\<{2} {return code11;}
\>{2} {return code12;}
# {return code13;}
\+ {return code14;}
\- {return code15;}
\* {return code16;}
\/ {return code17;}
% {return code18;}
\< {return code19;}
\<\= {return code20;}
\= {return code21;}
\>\= {return code22;}
\> {return code23;}
\=\= {return code24;}
\+{2} {return code31;}
\-{2} {return code30;}
int {return code33;}
char {return code34;}
while {return code35;}
if {return code36;}
else {return code37;}
read {return code38;}
write {return code39;}
main {return code42;}
_*|[A-Z]+|[a-z]+[0-9]* {return code0;}
[0-9] {return code1;}
. {return code49;}
%%

int yywrap()
{
return 1;
}