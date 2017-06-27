(ns aapen.scratch
  (:require [clojure.tools.analyzer.ast :as ast]
            [clojure.tools.analyzer :as ana]
            [clojure.tools.analyzer.env :as env]
            [clojure.tools.analyzer.jvm :as ana.jvm]
            [clojure.tools.analyzer.jvm :refer [analyze]]
            [clojure.repl :refer :all]))

(def trivialish
  '(+ 1 2))

(def trivialish
  '(+ 1 2 3))

(def branching
  '(if true
     true
     false))

(def macro-branching
  '(when true
     true))

(def non-trivial
  '(if (> 5 (+ 1 2 3))
     (do (println "test")
         true)
     (let [response false]
       response)))

(comment

  (let [analyzed (analyze trivial)]
    (ast/nodes analyzed))

  (ast/nodes (analyze '(+ 1 2))))
