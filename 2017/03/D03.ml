open Core
open Stdio

let next_pos i r c =
  if r = -i && c = +i
  then i + 1, r, c + 1
  else if r = +i && c = +i
  then i, r, c - 1
  else if r = +i && c = -i
  then i, r - 1, c
  else if r = -i && c = -i
  then i, r, c + 1
  else if c = +i
  then i, r + 1, c
  else if c = -i
  then i, r - 1, c
  else if r = +i
  then i, r, c - 1
  else i, r, c + 1
;;

let f n =
  let rec f' n (i, r, c) =
    match n with
    | 1 -> abs r + abs c
    | _ -> f' (n - 1) (next_pos i r c)
  in
  f' n (0, 0, 0)
;;

let g n =
  let cache = Hashtbl.create (module String) in
  let key r c = Printf.sprintf "%d %d" r c in
  let neighbor_sum r c =
    let sum =
      match r, c with
      | 0, 0 -> 1
      | _ ->
        let r's = List.range ~stop:`inclusive (r - 1) (r + 1) in
        let c's = List.range ~stop:`inclusive (c - 1) (c + 1) in
        List.sum
          (module Int)
          ~f:(fun (r', c') -> Hashtbl.find cache (key r' c') |> Option.value ~default:0)
          (List.cartesian_product r's c's)
    in
    Hashtbl.set cache ~key:(key r c) ~data:sum;
    sum
  in
  let rec g' (i, r, c) =
    let s = neighbor_sum r c in
    if s > n then s else g' (next_pos i r c)
  in
  g' (0, 0, 0)
;;

let () =
  let input =
    List.nth (Input.read_lines "input.txt") 0 |> Option.value ~default:"" |> int_of_string
  in
  printf "%d\n" (f input);
  printf "%d\n" (g input)
;;
