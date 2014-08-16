(define (sumFirstNHelper n total)
  (if (< n 1) total (sumFirstNHelper (- n 1) (+ total n))))
  
  
(define (sumFirstN n)
  (sumFirstNHelper n 0))

(define (sumFirstNClosedForm n)
  (/ (* n (+ n 1)) 2))

;n^2 run time (tests 1..n, ..., 1..3, 1..2, 1..1)
(define (testSumFirstNFunctions n func1 func2)
  (if (< n 1) #t 
      (if (= (func1 n) (func2 n)) (testSumFirstNFunctions (- n 1) func1 func2) #f)))


(define a 100)

(testSumFirstNFunctions a sumFirstN sumFirstNClosedForm)

