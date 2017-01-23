(ns aoc-solutions.day3)

(def total-tris (atom 0))
(def total-tris2 (atom 0))


(defn parse-string
  [x]
    (def input-vec (read-string (str "[" x "]")))
)

(defn is-triangle
  [x y z]
    (if
      (> (+ (nth (sort [x y z]) 0) (nth (sort [x y z]) 1)) (max x y z))
      1
      0
    )
)

(defn count-valid-tris2
  [vec-y]
    (def count-tris2 (count vec-y))
    (def index2 (atom 0))
    (while (< @index2 count-tris2)
      (do
        (if
          (= (is-triangle (nth vec-y @index2) (nth vec-y (+ @index2 3)) (nth vec-y (+ @index2 6))) 1)
	  (swap! total-tris2 inc)
	  nil
	)
      )
      (cond
        (= (mod (+ @index2 1) 3) 0) (swap! index2 (partial + 7))
	:else (swap! index2 (partial + 1))
      )
    )
)


(defn count-valid-tris
  [vec-x]
    (def count-tris (count vec-x))
    (def index (atom 0))
    (while (< @index count-tris)
      (do
        (if
	  (= (is-triangle (nth vec-x @index) (nth vec-x (+ @index 1)) (nth vec-x (+ @index 2))) 1)
	  (swap! total-tris inc)
	  nil)
	  )
	(swap! index (partial + 3))
    )
)

(defn answer
  "initial function to run solution to problem 3"
  []
  (println "Reading input text file...")
  (def input-string (slurp "resources/day3input.txt"))
  (parse-string input-string)
  (count-valid-tris input-vec)
  (println (str "Method #1: " @total-tris))
  (count-valid-tris2 input-vec)
  (println (str "Method #2: " @total-tris2))
)