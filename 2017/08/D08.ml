open Core
open Stdio

type condition =
  { var : string
  ; amt : int
  ; op : int -> int -> bool
  }

type instruction =
  { var : string
  ; amt : int
  ; op : int -> int -> int
  ; cond : condition
  }

let parse_line i =
  let cond =
    let condition_input = List.nth i 1 |> Option.value_exn |> String.split ~on:' ' in
    let var = List.nth condition_input 0 |> Option.value_exn in
    let amt = List.nth condition_input 2 |> Option.value_exn |> int_of_string in
    let op =
      match List.nth condition_input 1 |> Option.value_exn with
      | ">" -> ( > )
      | "<" -> ( < )
      | "==" -> ( = )
      | "!=" -> ( <> )
      | ">=" -> ( >= )
      | _ -> ( <= )
    in
    { var; amt; op }
  in
  let instruction_input = List.nth i 0 |> Option.value_exn |> String.split ~on:' ' in
  let var = List.nth instruction_input 0 |> Option.value_exn in
  let amt = List.nth instruction_input 2 |> Option.value_exn |> int_of_string in
  let op =
    match List.nth instruction_input 1 |> Option.value_exn with
    | "inc" -> ( + )
    | _ -> ( - )
  in
  { var; amt; op; cond }
;;

let f instruction_list =
  let var_table = Hashtbl.create (module String) in
  let get_val var =
    match Hashtbl.find var_table var with
    | Some v -> v
    | None -> 0
  in
  let eval_cond ({ var; amt; op } : condition) = op (get_val var) amt in
  let exec_op var amt op =
    let res = op (get_val var) amt in
    Hashtbl.set var_table ~key:var ~data:res;
    res
  in
  let max_val =
    List.fold_left
      instruction_list
      ~f:(fun max ({ var; amt; op; cond } : instruction) ->
        let res = if eval_cond cond then exec_op var amt op else Int.min_value in
        Int.max max res)
      ~init:Int.min_value
  in
  let max_final_val =
    Hashtbl.data var_table
    |> List.max_elt ~compare:(fun v v' -> v - v')
    |> Option.value_exn
  in
  max_final_val, max_val
;;

let parse_input () =
  Input.read_lines "input.txt"
  |> List.map ~f:(Str.split (Str.regexp " if "))
  |> List.map ~f:parse_line
;;

let () =
  let input = parse_input () in
  let max_final_val, max_val = f input in
  printf "%d\n%d\n" max_final_val max_val
;;
