open Core
open Stdio

let file_name = "input.txt"

let f n =
  let rec f' n i r c =
    match n with
    | 1 -> (abs r) + (abs c)
    | _ ->
      if r = -i && c = +i then f' (n - 1) (i + 1) (r    ) (c + 1) else
      if r = +i && c = +i then f' (n - 1) (i    ) (r    ) (c - 1) else
      if r = +i && c = -i then f' (n - 1) (i    ) (r - 1) (c    ) else
      if r = -i && c = -i then f' (n - 1) (i    ) (r    ) (c + 1) else
      if c = +i           then f' (n - 1) (i    ) (r + 1) (c    ) else
      if c = -i           then f' (n - 1) (i    ) (r - 1) (c    ) else
      if r = +i           then f' (n - 1) (i    ) (r    ) (c - 1) else
                               f' (n - 1) (i    ) (r    ) (c + 1) in
  f' n 0 0 0

let g n =
  let cache = Hashtbl.create (module Int) in
  let key r c = (r + 1000) * 1000 + (c + 1000) in
  let neighbor_sum r c =
    let sum = match r, c with
    | 0, 0 -> 1
    | _    ->
      let r_range = List.range ~stop:`inclusive (r - 1) (r + 1) in
      let c_range = List.range ~stop:`inclusive (c - 1) (c + 1) in
      let rec pairs l r =
        match r with
        | []     -> []
        | h :: t ->
          List.append (List.map r ~f:(fun x -> (h, x))) (pairs t l) in
      List.map (pairs r_range c_range) ~f:(fun p ->
        let a, b = p in 
        match Hashtbl.find cache (key a b) with
        | Some v -> v
        | None -> 0
      ) |> List.fold_left ~f:(+) ~init:0 in
    Hashtbl.set cache ~key:(key r c) ~data:sum;
    sum in
  let rec g' i r c =
    let s = neighbor_sum r c in
    if s > +n           then s                          else
    if r = -i && c = +i then g' (i + 1) (r    ) (c + 1) else
    if r = +i && c = +i then g' (i    ) (r    ) (c - 1) else
    if r = +i && c = -i then g' (i    ) (r - 1) (c    ) else
    if r = -i && c = -i then g' (i    ) (r    ) (c + 1) else
    if           c = +i then g' (i    ) (r + 1) (c    ) else
    if           c = -i then g' (i    ) (r - 1) (c    ) else
    if r = +i           then g' (i    ) (r    ) (c - 1) else
                             g' (i    ) (r    ) (c + 1) in
  g' 0 0 0

let () =
  let lines = In_channel.read_lines file_name in
  match List.nth lines 0 with
  | Some n ->
    printf "%d\n" (f (int_of_string n));
    printf "%d\n" (g (int_of_string n));
  | None -> printf("error")
