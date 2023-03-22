open Core
open Stdio

let f ns =
  let max = List.fold_left ~f:Int.max ~init:Int.min_value ns in
  let min = List.fold_left ~f:Int.min ~init:Int.max_value ns in
  max - min
;;

let rec g ns =
  match ns with
  | [] -> 0
  | n :: t ->
    let s =
      List.map ~f:(fun x -> if x % n = 0 then x / n else if n % x = 0 then n / x else 0) t
      |> List.fold_left ~f:Int.max ~init:0
    in
    if s = 0 then g t else s
;;

let () =
  let input =
    Input.read_lines "input.txt"
    |> List.map ~f:(fun s -> String.split ~on:'\t' s |> List.map ~f:int_of_string)
  in
  printf "%d\n" (List.sum (module Int) ~f input);
  printf "%d\n" (List.sum (module Int) ~f:g input)
;;
