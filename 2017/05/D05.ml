open Core
open Stdio

let f jump_list g =
  let jump_array = List.map jump_list ~f:ref |> List.to_array in
  let rec jump i c =
    if i >= Array.length jump_array
    then c
    else (
      let j = i + !(jump_array.(i)) in
      g !(jump_array.(i)) jump_array.(i);
      jump j (c + 1))
  in
  jump 0 0
;;

let () =
  let input = Input.read_lines "input.txt" |> List.map ~f:int_of_string in
  printf "%d\n" (f input (fun _ -> Int.incr));
  printf "%d\n" (f input (fun x -> if x >= 3 then Int.decr else Int.incr))
;;
