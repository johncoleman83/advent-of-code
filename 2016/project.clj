(defproject aoc-solutions "0.1.0-SNAPSHOT"
  :description "My Advent of Code Solutions using Clojure"
  :url "https://github.com/johncoleman83/aoc-solutions"
  :license {:name "WTFPL"
            :url "http://www.wtfpl.net/"}
  :dependencies [[org.clojure/clojure "1.8.0"]]
  :main ^:skip-aot aoc-solutions.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
