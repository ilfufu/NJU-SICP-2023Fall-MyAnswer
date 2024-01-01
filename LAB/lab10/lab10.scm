;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
      (if (f (car s))
          (cons-stream (car s) (filter-stream f (cdr-stream s)))
          (filter-stream f (cdr-stream s)))))


(define (slice s start end)
 (if(or (null? s) (<= end 0))
  nil
  (if(<= start 0)
  (cons (car s) (slice (cdr-stream s) (- start 1) (- end 1) ))
  (slice (cdr-stream s) (- start 1) (- end 1))
  ))
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)


(define (exp x)
  (cons-stream 1 (combine-with + (combine-with (lambda (a b)(/ (expt x b) a))
                               (cdr-stream factorials)
                               (naturals 1))
                               (exp x))
                               )
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (cond ((null? s) nil)
        ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
        (else (if (> (car s) (car (cdr-stream s)))
                  (cons-stream (list (car s)) (nondecrease (cdr-stream s)))
                  (let ((rest (nondecrease (cdr-stream s))))
                    (cons-stream (cons (car s) (car rest)) (cdr-stream rest))))))
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
