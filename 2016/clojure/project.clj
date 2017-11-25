(defproject aoc-solutions "0.1.0-SNAPSHOT"
  :description "My Advent of Code Solutions using Clojure"
  :url "https://github.com/johncoleman83/advent-of-code"
  :license {:name "MIT"
            :url "https://github.com/johncoleman83/advent-of-code/blob/master/LICENSE"}
  :dependencies [[org.clojure/clojure "1.8.0"]]
  :main ^:skip-aot aoc-solutions.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
