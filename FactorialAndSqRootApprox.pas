program Factorial;

//Recursive factorial function

function Fact(Num: SmallInt): Extended;
begin
  if Num < 1 then Fact := 1
  else Fact := Num * Fact(Num - 1);
end;
 

//Approximating Square Root function

function SqRoot(Num, Tol: Real): Real;
var
  Guess: Real;
begin
  Guess := 1.0;
  while ABS((Guess*Guess) - Num) > Tol do
    begin
    Guess := (Guess + (Num/Guess)) / 2;
    end;
SqRoot := Guess;
end;


begin
  WriteLn(Fact(0));
  WriteLn(Fact(10));
  WriteLn(Fact(100));
  WriteLn(Fact(1000));
  
  WriteLn(SqRoot(2, 0.0001));
  WriteLn(SqRoot(64, 0.0001));
  WriteLn(SqRoot(10000, 0.0001));

end.
