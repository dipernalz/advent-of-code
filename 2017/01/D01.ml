open Core
open Stdio

let rec f s i n g =
  let len = String.length s in
  if i = len
  then n
  else (
    let c0 = String.get s i in
    let c1 = String.get s (g s i % len) in
    let char_to_int c = Char.to_int c - 0x30 in
    f s (i + 1) (n + if Char.equal c0 c1 then char_to_int c0 else 0) g)
;;

let () =
  let input = List.nth (Input.read_lines "input.txt") 0 |> Option.value ~default:"" in
  printf "%d\n" (f input 0 0 (fun _ i -> i + 1));
  printf "%d\n" (f input 0 0 (fun s i -> i + (String.length s / 2)))
;;
