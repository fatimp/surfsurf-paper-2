(defpackage ellipses
  (:use #:cl)
  (:local-nicknames (:sera :serapeum)
                    (:diff :cl-forward-diff))
  (:export #:ellipses #:make-ellipses #:ellipsis))
(in-package :ellipses)

(sera:defconstructor ellipsis
  (x     double-float)
  (y     double-float)
  (ax    double-float)
  (ay    double-float)
  (axy   double-float))

(defun make-ellipses (n)
  (loop repeat n collect
        (let ((ax (+ 5d-1 (random 1d0)))
              (ay (+ 5d-1 (random 1d0))))
          (ellipsis (- (random 1d0) 5d-1)
                    (- (random 1d0) 5d-1)
                    ax ay
                    (random (sqrt (* ax ay)))))))

(sera:-> ellipsis-value
         (ellipsis list)
         (values diff:dual &optional))
(defun ellipsis-value (ellipsis coord)
  (declare (optimize (speed 3)))
  (destructuring-bind (x y) coord
    (declare (type diff:dual x y))
    (let ((x-center (diff:- x (ellipsis-x ellipsis)))
          (y-center (diff:- y (ellipsis-y ellipsis))))
      (diff:sqrt
       (diff:+
        (diff:* (diff:expt x-center 2) (ellipsis-ax ellipsis))
        (diff:* (diff:expt y-center 2) (ellipsis-ay ellipsis))
        (diff:* x-center y-center (ellipsis-axy ellipsis)))))))

(defun ellipses (ellipses)
  (declare (optimize (speed 3)))
  (lambda (coord)
    (reduce
     (lambda (acc ellipse)
       (declare (type diff:dual acc))
       (diff:min acc (ellipsis-value ellipse coord)))
     ellipses
     :initial-value (diff:make-dual most-positive-double-float 0d0))))
