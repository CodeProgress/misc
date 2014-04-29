//If we list all the natural numbers below 10 that are multiples of 3 or 5, 
//we get 3, 5, 6 and 9. The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.

Program SumRangeDivBy;

var
  Total, i, limit: LongInt;
  
begin
  Total := 0;
  limit := 999;
  
  for i := 1 to limit do
  begin
    if (i mod 3 = 0) Or (i mod 5 = 0)
    then
      begin
      Total := Total + i;
      end
  end;
  
  WriteLn(Total);

end.
