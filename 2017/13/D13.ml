open Core
open Stdio

let parse_input () =
  let parse_line line =
    let a =
      Str.split (Str.regexp ": ") line |> List.map ~f:Int.of_string |> List.to_array
    in
    a.(0), a.(1)
  in
  List.map (Input.read_lines "input.txt") ~f:parse_line
;;

let f layers =
  List.fold layers ~init:0 ~f:(fun s (d, r) ->
    s + if d % ((r - 1) * 2) = 0 then d * r else 0)
;;

let g layers =
  let rec g' delay =
    if List.find layers ~f:(fun (d, r) -> (d + delay) % ((r - 1) * 2) = 0)
       |> Option.is_some
    then g' (delay + 1)
    else delay
  in
  g' 0
;;

let () =
  let layers = parse_input () in
  f layers |> printf "%d\n";
  g layers |> printf "%d\n"
;;
