
(* 1 2 3 4 5)

(map inc (range 1 10))

(defn pow [base exp]
    (if (= exp 0)
    1N
    (* base (pow base (- exp 1)))))

(defn powFast [base exp]
    (if (= exp 0)
    1N
    (if (= (mod exp 2) 0)
    (* (powFast base (/ exp 2)) (powFast base (/ exp 2)))
    (* base (pow base (- exp 1))))))

(defn power [base exp]
    (reduce * (repeat exp base)))
