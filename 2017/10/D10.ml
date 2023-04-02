open Core
open Stdio

let array_length = 256

let sparse_hash list =
  let array = List.range 0 array_length |> List.to_array in
  let next_pos i d = (i + d) % array_length in
  let prev_pos i d = (i - d + array_length) % array_length in
  let reverse_sublist i length =
    let rec reverse_sublist' l r d =
      if d >= 1
      then (
        let temp = array.(l) in
        array.(l) <- array.(r);
        array.(r) <- temp;
        reverse_sublist' (next_pos l 1) (prev_pos r 1) (d - 2))
    in
    reverse_sublist' i (next_pos i (length - 1)) (length - 1)
  in
  let rec sparse_hash' list' i skip =
    match list' with
    | [] -> ()
    | h :: t ->
      reverse_sublist i h;
      sparse_hash' t (next_pos i (h + skip)) (skip + 1)
  in
  sparse_hash' list 0 0;
  Array.to_list array
;;

let dense_hash list =
  let _, _, hash =
    List.fold_right
      list
      ~f:(fun n' (c, n, list') ->
        if c + 1 = 16
        then 0, 0, Int.bit_xor n n' :: list'
        else c + 1, Int.bit_xor n n', list')
      ~init:(0, 0, [])
  in
  hash
;;

let f list =
  match sparse_hash list with
  | a :: b :: _ -> a * b
  | _ -> 0
;;

let g list =
  let multiply_list list' n =
    let rec multiply_list' acc n' =
      if n' = 0 then acc else multiply_list' (List.append acc list') (n' - 1)
    in
    multiply_list' [] n
  in
  multiply_list (List.append list [ 17; 31; 73; 47; 23 ]) 64
  |> sparse_hash
  |> dense_hash
  |> List.map ~f:(Printf.sprintf "%02x")
  |> String.concat
;;

let () =
  let input = List.nth_exn (Input.read_lines "input.txt") 0 in
  input |> String.split ~on:',' |> List.map ~f:Int.of_string |> f |> printf "%d\n";
  input |> String.to_list |> List.map ~f:Char.to_int |> g |> printf "%s\n"
;;
