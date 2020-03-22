#lang racket

; i m 2 dumb 2 no how 2 memoize in raket :(
; so dis is just dumb unoptimized :(

(define (collatz n)
    (match n
        [1 1]
        [_ (+ 1 (if (equal? (modulo n 2) 0)
                (collatz (/ n 2))
                (collatz (+ 1 (* n 3)))))]))
    
; (define (max l)
;     (cond
;         [(empty? (rest l)) (first l)]
;         [else 
;             (if (> (first l) (max (rest l)))
;                 (first l)
;                 (max (rest l)))]))

(define (all-collatz n)
    (cond
        [(= n 0) empty]
        [else (cons (collatz n) (all-collatz (- n 1)))]))

(define (arg-max-collatz n)
    (cond
        [(= n 1) 1]
        [else 
            (let ([argmax (arg-max-collatz (- n 1))])
                (if (> (collatz n) (collatz argmax))
                    n
                    argmax))]))

(arg-max-collatz 1000000)