open Core
open Stdio

let file_name = "input.txt"

let sort s =
  let rec s_to_char_list s' =
    let len = String.length s' in
    match len with
    | 0 -> []
    | _ ->
      String.get s' 0 :: s_to_char_list (String.sub s' ~pos:1 ~len:(len - 1)) in
  String.of_char_list (List.sort (s_to_char_list s) ~compare:(fun a b -> (Char.to_int a) - (Char.to_int b)))

let f s =
  match List.find_a_dup ~compare:String.compare s with
  | Some _ -> 0
  | None   -> 1

let () =
  let lines = In_channel.read_lines file_name in
  let passwords =
    List.filter lines ~f:(fun s -> not (String.is_empty s))
    |> List.map ~f:(fun s -> String.split ~on: ' ' s) in
  let dupes = List.map ~f:f passwords in
  printf "%d\n" (List.fold_left dupes ~init:(0) ~f:(+));
  let dupes = List.map ~f:(fun p -> List.map ~f:sort p |> f) passwords in
  printf "%d\n" (List.fold_left dupes ~init:(0) ~f:(+));
