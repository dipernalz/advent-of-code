open Core
open Stdio

let parse_input () =
  let input =
    Input.read_lines "input.txt"
    |> List.map ~f:(String.split ~on:' ')
    |> List.map ~f:List.to_array
    |> List.to_array
  in
  Int.of_string input.(0).(4), Int.of_string input.(1).(4)
;;

let a_factor = 16807
let b_factor = 48271
let step_a a = a * a_factor % 2147483647
let step_b b = b * b_factor % 2147483647

let update_a a =
  let rec update_a' a' = if a' % 4 = 0 then a' else step_a a' |> update_a' in
  step_a a |> update_a'
;;

let update_b b =
  let rec update_b' b' = if b' % 8 = 0 then b' else step_b b' |> update_b' in
  step_b b |> update_b'
;;

let check_pairs a_start b_start f_a f_b n =
  let rec check_pairs' a b n s =
    let next_a = f_a a in
    let next_b = f_b b in
    match n, Int.bit_and next_a 0x0000FFFF = Int.bit_and next_b 0x0000FFFF with
    | 0, _ -> s
    | _, true -> check_pairs' next_a next_b (n - 1) (s + 1)
    | _ -> check_pairs' next_a next_b (n - 1) s
  in
  check_pairs' a_start b_start n 0
;;

let f a_start b_start = check_pairs a_start b_start step_a step_b 40_000_000
let g a_start b_start = check_pairs a_start b_start update_a update_b 5_000_000

let () =
  let a_start, b_start = parse_input () in
  f a_start b_start |> printf "%d\n";
  g a_start b_start |> printf "%d\n"
;;
