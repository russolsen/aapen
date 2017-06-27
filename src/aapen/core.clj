(ns aapen.core
  (:require [clojure.pprint :as pp])
  (:require [clojure.tools.analyzer :as ana])
  (:require [clojure.tools.analyzer.env :refer [with-env]]))

(defrecord AAVar [nspace nm])


(def foo-def "hello world")

(def context {:context    :ctx/expr
              :locals     {}
              :ns         'user})

(def the-env (atom {
                    :namespaces
                    {'user {:mappings (into (ns-map 'clojure.core)
                                            {'foo #'foo-def})
                            :aliases {'bar 'foo}
                            :ns      'user}
                     'clojure.core {:mappings (ns-map 'clojure.core)
                                    :aliases {}
                                    :ns      'clojure.core}}}))

(def vars (atom #{}))

(defn create-var [sym env]
  (println "creatvar:" sym)
  (println "createvar:" env))

(defn is-var? [sym]
  (println "is var:" sym)
  (instance? AAVar sym))

(def is-var? var?)

(defn me-1 [form env]
  (macroexpand-1 form))

(defn ast [form]
  (with-env the-env
    (binding [ana/macroexpand-1 me-1
              ana/create-var    create-var
              ana/parse         ana/-parse
              ana/var?          is-var?]
      (ana/analyze form context))))


