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
int {return code25;}
char {return code26;}
while {return code27;}
if {return code28;}
else {return code29;}
read {return code30;}
write {return code31;}
main {return code32;}
_*|[A-Z]+|[a-z]+[0-9]* {return code0;}
[0-9] {return code1;}
%%

int yywrap()
{
return 1;
}