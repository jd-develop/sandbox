let rec split (l: int list) (poweroftwo: int) : (int list)*(int list) =
    match l with
    | [] -> [], []
    | x::q -> let l1, l2 = split q poweroftwo in
              if (x lsr poweroftwo) mod 2 = 0 then x::l1, l2
              else l1, x::l2

let rec lsdradix_powerof2 (l: int list) (poweroftwo: int) : int list =
    if poweroftwo > 32 then l else
    let l1, l2 = split l poweroftwo in
    match l2 with
    | [] -> l1
    | _ -> lsdradix_powerof2 (l1@l2) (poweroftwo+1)


let lsdradix (l: int list) : int list = lsdradix_powerof2 l 1

