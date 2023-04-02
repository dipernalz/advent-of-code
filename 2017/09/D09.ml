open Core
open Stdio

let f stream =
  let rec parse l d g score sum =
    if g
    then (
      match l with
      | [] -> score, sum
      | '!' :: _ :: t -> parse t d true score sum
      | '>' :: t -> parse t d false score sum
      | _ :: t -> parse t d true score (sum + 1))
    else (
      match l with
      | [] -> score, sum
      | '{' :: t -> parse t (d + 1) false score sum
      | '}' :: t -> parse t (d - 1) false (score + d) sum
      | '<' :: t -> parse t d true score sum
      | _ :: t -> parse t d false score sum)
  in
  parse (String.to_list stream) 0 false 0 0
;;

let () =
  let input = Input.read_lines "input.txt" in
  let score, sum = List.nth_exn input 0 |> f in
  printf "%d\n%d\n" score sum
;;
