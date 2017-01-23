(ns aoc-solutions.core
  (require [aoc-solutions.day3 :as day3])
  (:gen-class))

(defn -main
  "Main function"
  [& args]
   (cond
   	(= (first args) "3") (day3/answer)
	:else (println "no solution yet.")))