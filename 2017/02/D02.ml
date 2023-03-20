open Core
open Stdio

let file_name = "input.txt"

let s_to_ns s =
  String.split_on_chars ~on:[' '; '\t'; '\n'] s
    |> List.filter ~f:(fun s -> not (String.is_empty s))
    |> List.map ~f:int_of_string

let f ns =
  match ns with
  | [] -> 0
  | _ ->
    let max = List.fold_left ~f:Int.max ~init:Int.min_value ns in
    let min = List.fold_left ~f:Int.min ~init:Int.max_value ns in
    max - min

let rec g ns =
  match ns with
  | [] -> 0
  | h :: t ->
    let n =
      List.map ~f:(fun x ->
        if x % h = 0 then x / h else
        if h % x = 0 then h / x else 0) t
      |> List.fold_left ~f:Int.max ~init:0 in
    match n with
    | 0 -> g t
    | x -> x

let () =
  let lines = In_channel.read_lines file_name in
  let lines = List.map ~f:s_to_ns lines in
  printf "%d\n" (List.fold_left ~f:(+) ~init:0 (List.map ~f:f lines));
  printf "%d\n" (List.fold_left ~f:(+) ~init:0 (List.map ~f:g lines));
