open Core
open Stdio

let sort s =
  let rec s_to_char_list i =
    if i = String.length s then [] else String.get s i :: s_to_char_list (i + 1)
  in
  s_to_char_list 0
  |> List.sort ~compare:(fun a b -> Char.to_int a - Char.to_int b)
  |> String.of_char_list
;;

let f s =
  match List.find_a_dup ~compare:String.compare s with
  | Some _ -> 0
  | None -> 1
;;

let () =
  let input = Input.read_lines "input.txt" |> List.map ~f:(String.split ~on:' ') in
  printf "%d\n" (List.sum (module Int) ~f input);
  printf "%d\n" (List.sum (module Int) ~f:(fun p -> List.map ~f:sort p |> f) input)
;;
