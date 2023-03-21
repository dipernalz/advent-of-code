open Core
open Stdio

let file_name = "input.txt"

let f jump_list update =
  let jump_array =
    List.map jump_list ~f:ref
    |> List.to_array in
  let rec jump i c =
    if i >= Array.length jump_array then c else (
      let j = i + !(jump_array.(i)) in
      jump_array.(i) |> update !(jump_array.(i));
      jump j (c + 1)
    ) in
  jump 0 0
  
let () =
  let input =
    In_channel.read_lines file_name
    |> List.filter ~f:(fun s -> not (String.is_empty s))
    |> List.map ~f:int_of_string in
  printf "%d\n" (f input (fun _ -> Int.incr));
  printf "%d\n" (f input (fun x -> if x >= 3 then Int.decr else Int.incr));
