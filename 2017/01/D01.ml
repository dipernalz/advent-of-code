open Core
open Stdio

let file_name = "input.txt"

let char_to_int c = (Char.to_int c) - 0x30

let rec f s n =
  let len = String.length s in
  match len with
  | 0 | 1 -> n
  | _ ->
    let c0 = String.get s 0 in
    let c1 = String.get s 1 in
    f (String.sub s ~pos:1 ~len:(len - 1))
      (n + if Char.equal c0 c1 then char_to_int c0 else 0)

let rec g s i n =
  let len = String.length s in
    if i = len then n else 
      let c0 = String.get s i in
      let c1 = String.get s ((i + len / 2) % len) in
      g s (i + 1) (n + if Char.equal c0 c1 then char_to_int c0 else 0)

let () =
  let file = In_channel.create file_name in
  let line = In_channel.input_line file in
  match line with
  | Some s ->
    let s = String.strip s in
    let c0 = String.get s 0 in
    let c1 = String.get s (String.length s - 1) in
    let n = if Char.equal c0 c1 then char_to_int c0 else 0 in
    printf "%d\n" (f s n);
    printf "%d\n" (g s 0 0);
  | None -> printf("Error\n")
