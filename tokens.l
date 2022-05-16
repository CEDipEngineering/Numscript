%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}

%%

[ \t\n]                 ;
"$"[0-9_]*              SAVE_TOKEN; return TIDENTIFIER;
[0-9]+                  SAVE_TOKEN; return TINTEGER;
"="                     return TOKEN(TEQUAL);
"$_436_0"        	    return TOKEN(TIF);        	                        
"$_436_1"       	    return TOKEN(TELSE);          	                    
"$_436_2"       	    return TOKEN(TWHILE)      	                        
"$_436_3"       	    return TOKEN(TPRINTF);      	                        
"$_436_5"       	    return TOKEN(TRETURN);
"=="                    return TOKEN(TCEQ);
"!="                    return TOKEN(TCNE);
"<"                     return TOKEN(TCLT);
"<="                    return TOKEN(TCLE);
">"                     return TOKEN(TCGT);
">="                    return TOKEN(TCGE);
"("                     return TOKEN(TLPAREN);
")"                     return TOKEN(TRPAREN);
"{"                     return TOKEN(TLBRACE);
"}"                     return TOKEN(TRBRACE);
","                     return TOKEN(TCOMMA);
"&&"                    return TOKEN(TAND);
"||"                    return TOKEN(TOR);
"!"                     return TOKEN(TNOT);
"+"                     return TOKEN(TPLUS);
"-"                     return TOKEN(TMINUS);
"*"                     return TOKEN(TMUL);
"/"                     return TOKEN(TDIV);
.                       printf("Unknown token!n"); yyterminate();

%%