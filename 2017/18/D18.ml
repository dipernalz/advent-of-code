open Core
open Stdio

type instruction =
  { name : string
  ; x : string
  ; y : string
  }

type program =
  { i : int
  ; reg : (char, int, Char.comparator_witness) Map.t
  ; buf : int Queue.t
  ; dead : bool
  ; c : int
  }

let parse_input () =
  let parse_line line =
    let instr = String.split line ~on:' ' |> List.to_array in
    { name = instr.(0)
    ; x = instr.(1)
    ; y = (if Array.length instr = 3 then instr.(2) else "")
    }
  in
  Input.read_lines "input.txt" |> List.map ~f:parse_line
;;

let get_val reg x =
  let k = String.nget x 0 in
  if Char.is_lowercase k
  then (
    match Map.find reg k with
    | Some v -> v
    | None -> 0)
  else Int.of_string x
;;

let set_val reg x y = Map.set reg ~key:(String.nget x 0) ~data:y

let f input =
  let instructions = List.to_array input in
  let rec f' i last_sound reg =
    let { name; x; y } = instructions.(i) in
    match name with
    | "snd" -> f' (i + 1) (get_val reg x) reg
    | "set" -> f' (i + 1) last_sound (set_val reg x (get_val reg y))
    | "add" -> f' (i + 1) last_sound (set_val reg x (get_val reg x + get_val reg y))
    | "mul" -> f' (i + 1) last_sound (set_val reg x (get_val reg x * get_val reg y))
    | "mod" -> f' (i + 1) last_sound (set_val reg x (get_val reg x % get_val reg y))
    | "rcv" ->
      (match get_val reg x with
       | 0 -> f' (i + 1) last_sound reg
       | _ -> last_sound)
    | "jgz" -> f' (i + if get_val reg x > 0 then get_val reg y else 1) last_sound reg
    | _ -> 0
  in
  f' 0 0 (Map.empty (module Char))
;;

let g input =
  let instructions = List.to_array input in
  let new_program id =
    { i = 0
    ; reg = Map.singleton (module Char) 'p' id
    ; buf = Queue.create ()
    ; dead = false
    ; c = 0
    }
  in
  let rec run p p' =
    let { i; reg; _ } = p in
    let { name; x; y } = instructions.(i) in
    match name with
    | "snd" ->
      Queue.enqueue p'.buf (get_val reg x);
      run { p with i = i + 1; c = p.c + 1 } { p' with dead = false }
    | "set" -> run { p with i = i + 1; reg = set_val reg x (get_val reg y) } p'
    | "add" ->
      run { p with i = i + 1; reg = set_val reg x (get_val reg x + get_val reg y) } p'
    | "mul" ->
      run { p with i = i + 1; reg = set_val reg x (get_val reg x * get_val reg y) } p'
    | "mod" ->
      run { p with i = i + 1; reg = set_val reg x (get_val reg x % get_val reg y) } p'
    | "rcv" ->
      (match Queue.dequeue p.buf with
       | Some v -> run { p with i = i + 1; reg = set_val reg x v } p'
       | None -> { p with dead = true }, p')
    | "jgz" -> run { p with i = (i + if get_val reg x > 0 then get_val reg y else 1) } p'
    | _ -> p, p'
  in
  let rec g' (p, p') =
    match p.dead, p'.dead with
    | false, _ -> run p p' |> g'
    | _, false -> run p' p |> (fun (p', p) -> p, p') |> g'
    | true, true -> p'.c
  in
  g' (new_program 0, new_program 1)
;;

let () =
  let input = parse_input () in
  f input |> printf "%d\n";
  g input |> printf "%d\n"
;;
