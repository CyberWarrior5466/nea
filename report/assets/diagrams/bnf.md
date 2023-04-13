```aqa
program        => declarations EOF

declarations => (variable_declaration | statement)*

statement      => printStatement | ifStatement |
                  whileStatement | forStatement

variable_declaration        => IDENTIFIER "<-" expression

end => "END" | "ENDIF" | "ENDWHILE" | "ENDFOR"

printStatement => ( PRINT | OUTPUT ) expression

ifStatement
   => IF expression ( THEN | ":" )?
          declarations
    ( ELSE 
          declarations )?
    end

whileStatement 
   => WHILE expression ( DO | ":" )?
         declarations
    end

forStatement
   => FOR variable_declaration TO expression ( STEP expression )?
         declarations
    end
    
# expression syntax
expression  =>  logic_or
logic_or    =>  logic_and ( OR logic_and )*
logic_and   =>  equality ( AND equality )*
equality    =>  comparison ( ( "==" | "!=" ) comparison )*
comparison  =>  term ( ( ">" | ">=" | "<" | "<=" ) term )*
term        =>  factor ( ( "-" | "+" ) factor )*
factor      =>  unary ( ( "/" | "*" ) unary )*
unary       =>   ( NOT | "-" ) unary |  primary
primary     =>   INTEGER | REAL | STRING | None |
                 True | False | "(" expression ")"
```