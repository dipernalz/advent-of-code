open Core
open Stdio

let f steps =
  let rec insert buffer i x =
    match i, buffer with
    | 0, _ -> x :: buffer
    | _, head :: tail -> head :: insert tail (i - 1) x
    | _ -> []
  in
  let rec f' buffer i n =
    if n - 1 = 2017
    then buffer, i
    else (
      let j = ((i + steps) % List.length buffer) + 1 in
      f' (insert buffer j n) j (n + 1))
  in
  let buffer, i = f' [ 0 ] 0 1 in
  List.nth_exn buffer (i + 1)
;;

let g steps =
  let rec g' i n x =
    if n - 1 = 50_000_000
    then x
    else (
      let j = ((i + steps) % n) + 1 in
      let y = if j = 1 then n else x in
      g' j (n + 1) y)
  in
  g' 0 1 0
;;

let () =
  let input = List.nth_exn (Input.read_lines "input.txt") 0 |> Int.of_string in
  f input |> printf "%d\n";
  g input |> printf "%d\n"
;;
