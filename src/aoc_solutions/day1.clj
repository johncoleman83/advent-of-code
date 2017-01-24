(ns aoc-solutions.day1)

;--COMPASS--
; 1 north
; 2 east
; 3 south
; 4 west

(def compas 1)
(def coords [0 0])

(defn parse-string
  [x]
    (def input-vec (read-string (str "[" x "]")))
    (def instructions (vec (map #(str %) input-vec)))
)

(defn change-coords
  [dira numx]
  (cond
    (= compas 1) (if (= dira \R) (def coords (assoc coords 0 (+ (first coords) numx))) (def coords (assoc coords 0 (- (first coords) numx))))
    (= compas 2) (if (= dira \L) (def coords (assoc coords 1 (+ (last coords) numx))) (def coords (assoc coords 1 (- (last coords) numx))))
    (= compas 3) (if (= dira \L) (def coords (assoc coords 0 (+ (first coords) numx))) (def coords (assoc coords 0 (- (first coords) numx))))
    (= compas 4) (if (= dira \R) (def coords (assoc coords 1 (+ (last coords) numx))) (def coords (assoc coords 1 (- (last coords) numx))))
    :else nil
  )
)

(defn change-compas
  [dirb]
  (cond
    (= compas 1) (if (= dirb \R) (def compas 2) (def compas 4))
    (= compas 2) (if (= dirb \L) (def compas 1) (def compas 3))
    (= compas 3) (if (= dirb \L) (def compas 2) (def compas 4))
    (= compas 4) (if (= dirb \R) (def compas 1) (def compas 3))
    :else nil
  )
)

(defn find-destination
  [vec-x]
    (def instruction-count (count vec-x))
    (def index (atom 0))
    (while (< @index instruction-count)
    (println (str "coordinates:   " coords))
      (do
         (change-coords (first (nth vec-x @index)) (read-string (subs (nth vec-x @index) 1)))
	 (change-compas (first (nth vec-x @index)))
	)
	(swap! index (partial + 1))
    )
)

(defn answer
  "initial function to run solution to day 1"
  ; beginning coordinates (0, 0) facing north
  []
  (println "Reading input text file...")
  (def input-string (slurp "resources/day1input.txt"))
  (parse-string input-string)

  (find-destination instructions)

  (println (str "Final Coordinates: " coords))
  (println (str "Distance: " (+ (Math/abs (first coords)) (Math/abs (last coords)))))
  
)