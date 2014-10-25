double x	= x + x
quadruple x 	= double (double x)
factorial n	= product [1..n]
average ns	= sum ns `div` length ns -- x `f` y is short for f x y

-- type ":reload" (no quotes) in ghci prompt to reload file

-- functions and param names must start with a lower case letter
-- types and identifiers start with upper case
-- if a param ends in 's' that means a list, 'ss' is a list of lists
-- white space is significant, make sure things line up
-- haskell programers like brevity

{- 
Commands	Meaning

:load name	load script name
:reload		reload current script
:edit name	edit script name
:type expr	show type of expr
:?    		show all commands
:quit		quit GHCi

-}