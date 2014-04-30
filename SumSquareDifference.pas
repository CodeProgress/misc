{
Find the difference between the sum of the squares 
and the square of the sum 
of the first one hundred natural numbers
}

Program SumSquareDifference;

var
    i, SumSqs, SqSum: LongInt;
    
begin

    SumSqs := 0;
    for i := 1 to 100 do 
      SumSqs := SumSqs + (i*i);
    
    SqSum := 0;
    for i := 1 to 100 do 
      SqSum:= SqSum+i;
      
    SqSum := SqSum * SqSum;
    
    WriteLn(SqSum - SumSqs);

end.

