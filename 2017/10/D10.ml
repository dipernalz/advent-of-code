open Core
open Stdio

let f input =
  match
    String.split ~on:',' input |> List.map ~f:Int.of_string |> Knot_hash.sparse_hash
  with
  | a :: b :: _ -> a * b
  | _ -> 0
;;

let g = Knot_hash.hash
(*   let multiply_list list' n = *)
(*     let rec multiply_list' acc n' = *)
(*       if n' = 0 then acc else multiply_list' (List.append acc list') (n' - 1) *)
(*     in *)
(*     multiply_list' [] n *)
(*   in *)
(*   let list = input |> String.to_list |> List.map ~f:Char.to_int in *)
(*   multiply_list (List.append list [ 17; 31; 73; 47; 23 ]) 64 |> Knot_hash.hash *)
(* ;; *)

let () =
  let input = List.nth_exn (Input.read_lines "input.txt") 0 in
  f input |> printf "%d\n";
  g input |> printf "%s\n"
;;
