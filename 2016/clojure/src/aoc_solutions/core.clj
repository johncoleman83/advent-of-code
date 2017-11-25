(ns aoc-solutions.core
  (require [aoc-solutions.day1 :as day1])
  (require [aoc-solutions.day3 :as day3])
  (:gen-class))

(defn -main
  "Main function"
  [& args]
   (cond
	(= (first args) "1") (day1/answer)
   	(= (first args) "3") (day3/answer)
	:else (println "no solution yet.")))