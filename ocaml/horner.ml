#!/usr/bin/env ocaml

(* Horner algorithm to compute the value of a polynomial function. The function
 * is represented as a list of coefficients, where the first element is
 * the coefficient for x^(deg p), the second element for x^(deg p-1), etc., and
 * the last element is the coefficient for x^0
 * Returns f(x)
 *)
let rec horner (p, x: float list * float) : float =
    match p with
    | [] -> 0.
    | c::[] -> c
    | c1::c2::q -> horner ((x *. c1 +. c2::q), x)

