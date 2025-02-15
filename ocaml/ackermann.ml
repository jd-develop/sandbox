(* Function of Ackermann *)
let rec a (m, n : int*int) : int =
    if m = 0 then n+1
    else if n = 0 then a (m-1, 1)
    else a (m-1, a (m, n-1))

(* Same but with Continuation-Passing style *)
let rec a_cont ((m, n, k) : (int*int*(int -> int))) : int =
    if m = 0 then k (n+1)
    else if n = 0 then a_cont (m-1, 1, k)
    else a_cont (m, n-1, (fun r -> a_cont (m-1, r, k)))
    (* a_cont (m, n, k) = k(a(m-1, a(m, n-1))
                        = (r |-> k(a(m-1, r)))(a(m, n-1))
                        = a m, n-1, (r |-> k(a m-1 r))
     *)
