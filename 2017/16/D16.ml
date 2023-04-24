open Core
open Stdio

let spin a _ state =
  let state_array = List.to_array state in
  let a' = Int.of_string a in
  let n = Array.length state_array in
  Array.append (Array.slice state_array (n - a') n) (Array.slice state_array 0 (n - a'))
  |> Array.to_list
;;

let exchange a b state =
  let state_array = List.to_array state in
  let a' = Int.of_string a in
  let b' = Int.of_string b in
  let temp = state_array.(a') in
  state_array.(a') <- state_array.(b');
  state_array.(b') <- temp;
  Array.to_list state_array
;;

let partner a b list =
  let state_array = List.to_array list in
  let a' = String.nget a 0 in
  let b' = String.nget b 0 in
  let find_index x =
    let rec find_index' i =
      if Char.equal state_array.(i) x then i else find_index' (i + 1)
    in
    find_index' 0
  in
  let pos_a = find_index a' in
  let pos_b = find_index b' in
  let temp = state_array.(pos_a) in
  state_array.(pos_a) <- state_array.(pos_b);
  state_array.(pos_b) <- temp;
  Array.to_list state_array
;;

let parse_input () =
  let parse_move move =
    let n = String.length move in
    let args = String.sub move ~pos:1 ~len:(n - 1) in
    let split_args = String.split args ~on:'/' |> List.to_array in
    match String.nget move 0 with
    | 's' -> spin args ""
    | 'x' -> exchange split_args.(0) split_args.(1)
    | _ -> partner split_args.(0) split_args.(1)
  in
  List.nth_exn (Input.read_lines "input.txt") 0
  |> String.split ~on:','
  |> List.map ~f:parse_move
;;

let f start_state moves =
  let rec f' state moves' =
    match moves' with
    | [] -> state
    | m :: t -> f' (m state) t
  in
  f' start_state moves |> String.of_char_list
;;

let g start_state moves =
  let rec g' state state_list =
    let state = f state moves in
    match List.find state_list ~f:(fun x -> String.equal x state) with
    | Some _ ->
      let state_array = List.rev state_list |> List.to_array in
      let n = Array.length state_array in
      state_array.(1_000_000_000 % n)
    | None -> g' (String.to_list state) (state :: state_list)
  in
  g' start_state [ String.of_char_list start_state ]
;;

let () =
  let moves = parse_input () in
  let start_state = String.to_list "abcdefghijklmnop" in
  f start_state moves |> printf "%s\n";
  g start_state moves |> printf "%s\n"
;;
