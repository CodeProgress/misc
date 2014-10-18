sqrt(25)		-- 5.0

head [1,2,3,4,5] 	-- 1

tail [1,2,3,4,5] 	-- [2,3,4,5]

[1,2,3,4,5] !! 2 	-- 2 ( select index 2, O(n) performance)

take 3 [1,2,3,4,5] 	-- [1,2,3]

tail [1,2,3,4,5] 	-- [2,3,4,5]

length [1,2,3,4,5] 	-- 5  ( O(n) performance)

sum [1,2,3,4,5] 	-- 15

product [1,2,3,4,5] 	-- 120

[1,2,3] ++ [4,5] 	-- [1,2,3,4,5]

reverse [1,2,3,4,5]	-- [5,4,3,2,1]



--function syntax examples:
f x   			-- f(x)
f x y			-- f(x, y)
f (g x)			-- f(g(x))
f x (g y)		-- f(x, g(y))
f x * g y		-- f(x) * g(y)

f a b + c*d		-- python equivalent:  f(a, b) + c*d

f a + b			-- f(a) + b , functions bind stronger

