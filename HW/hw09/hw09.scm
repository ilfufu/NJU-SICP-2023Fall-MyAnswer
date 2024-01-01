;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (reverse lst)  
    (if (null? lst)  
      '()  
      (append (reverse (cdr lst)) (list (car lst)))))

(define (make-change total biggest)

  (define (helper total biggest current)
  (if(= biggest 0)
    nil
    (if(= total 0)
  (list (reverse current))

  (if(> biggest total)
  (helper total total current)
  (
   append (helper (- total biggest) biggest (cons biggest current))
   (helper total (- biggest 1) current)
  )))))

  (helper total biggest '())
)


(define (find n lst)
  'YOUR-CODE-HERE
  (define (myfind n lst count)
  (if(= n (car lst))
  count
  (myfind n (cdr lst) (+ count 1)))
  )
  (myfind n lst 0)
)


(define (find-nest n sym)
  (define (helper lst expr)
    (if (pair? lst)
      (let ((r1 (helper (car lst) (list 'car expr))))
        (if (null? r1) (helper (cdr lst) (list 'cdr expr)) r1))
      (if (and (number? lst) (= n lst)) expr nil)))
  (helper (eval sym) sym)
)


(define-macro (my/or operands)
  (cond 
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
         (if t
             t
             (my/or ,(cdr operands))
             )))))



(define-macro (k-curry fn args vals indices)
  `(lambda ,(remove args indices 0) ,(cons fn (replace args vals indices 0)))
)

(define (remove lst indices curr)
  (cond ((or (null? lst) (null? indices)) lst)
        ((= curr (car indices)) (remove (cdr lst) (cdr indices) (+ 1 curr)))
        (else (cons (car lst) (remove (cdr lst) indices (+ 1 curr))))))

(define (replace lst vals indices curr)
  (cond ((or (null? lst) (null? indices)) lst)
        ((= curr (car indices)) 
          (cons (car vals) (replace (cdr lst) (cdr vals) (cdr indices) (+ 1 curr))))
        (else (cons (car lst) (replace (cdr lst) vals indices (+ 1 curr))))))



(define-macro (let* bindings expr)
  (if (null? bindings) `(let ,bindings ,expr)
    `(let (,(car bindings)) (let* ,(cdr bindings) ,expr)))) 



;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)