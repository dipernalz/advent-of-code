open Core
open Stdio

let f memory_list g =
  let cache = Hashtbl.create (module String) in
  let memory_array = List.to_array memory_list in
  let key () =
    Array.to_list memory_array |> List.map ~f:string_of_int |> String.concat ~sep:" "
  in
  let update () : unit =
    let len = List.length memory_list in
    let i =
      List.fold
        ~init:0
        ~f:(fun a b -> if memory_array.(b) > memory_array.(a) then b else a)
        (List.range 0 len)
    in
    let rec update' j a b =
      let j' = j % len in
      memory_array.(j') <- (memory_array.(j') + a + if b > 0 then 1 else 0);
      if i <> j' then update' (j' + 1) a (b - 1)
    in
    let v = memory_array.(i) in
    memory_array.(i) <- 0;
    update' (i + 1) (v / len) (v % len)
  in
  let rec f' c =
    match Hashtbl.find cache (key ()) with
    | Some c' -> g c c'
    | None ->
      Hashtbl.set cache ~key:(key ()) ~data:c;
      update ();
      f' (c + 1)
  in
  f' 0
;;

let () =
  let input =
    List.nth (Input.read_lines "input.txt") 0
    |> Option.value ~default:""
    |> String.split ~on:'\t'
    |> List.map ~f:int_of_string
  in
  printf "%d\n" (f input (fun c _ -> c));
  printf "%d\n" (f input (fun c c' -> c - c'))
;;
