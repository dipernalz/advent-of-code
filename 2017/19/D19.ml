open Core
open Stdio

let parse_input () =
  In_channel.read_lines "input.txt" |> List.map ~f:String.to_array |> List.to_array
;;

let f grid =
  let rec f' r c d s letters =
    let next_letters =
      if Char.is_uppercase grid.(r).(c) then grid.(r).(c) :: letters else letters
    in
    match grid.(r).(c) with
    | ' ' -> List.rev next_letters |> String.of_char_list, s
    | '+' ->
      (match d with
       | 'U' | 'D' ->
         if Char.equal grid.(r).(c - 1) '-' || Char.is_uppercase grid.(r).(c - 1)
         then f' r (c - 1) 'L' (s + 1) next_letters
         else f' r (c + 1) 'R' (s + 1) next_letters
       | _ ->
         if Char.equal grid.(r - 1).(c) '|' || Char.is_uppercase grid.(r - 1).(c)
         then f' (r - 1) c 'U' (s + 1) next_letters
         else f' (r + 1) c 'D' (s + 1) next_letters)
    | _ ->
      let dr, dc =
        match d with
        | 'U' -> -1, 0
        | 'D' -> 1, 0
        | 'L' -> 0, -1
        | _ -> 0, 1
      in
      f' (r + dr) (c + dc) d (s + 1) next_letters
  in
  let start_c, _ =
    Array.findi grid.(0) ~f:(fun _ c -> Char.equal c ' ' |> not) |> Option.value_exn
  in
  f' 0 start_c 'D' 0 []
;;

let () =
  let input = parse_input () in
  let p, s = f input in
  printf "%s\n%d\n" p s
;;
