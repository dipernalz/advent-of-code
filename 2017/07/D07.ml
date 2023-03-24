open Core
open Stdio

let parse_input () =
  let parse_line line =
    let from_data = List.nth_exn line 0 |> String.split ~on:' ' in
    let parent = List.nth_exn from_data 0 in
    let weight_string = List.nth_exn from_data 1 in
    let weight =
      String.sub weight_string ~pos:1 ~len:(String.length weight_string - 2)
      |> int_of_string
    in
    let children =
      match List.nth line 1 with
      | Some c -> Some (Str.split (Str.regexp ", ") c)
      | None -> None
    in
    parent, weight, children
  in
  Input.read_lines "input.txt"
  |> List.map ~f:(Str.split (Str.regexp " -> "))
  |> List.map ~f:parse_line
;;

let generate_tree input =
  let tree = Hashtbl.create (module String) in
  let add_node (parent, weight, children) =
    Hashtbl.set tree ~key:parent ~data:(weight, children)
  in
  List.iter input ~f:add_node;
  tree
;;

let f tree =
  let parent_set = Hash_set.create (module String) in
  let children_set = Hash_set.create (module String) in
  Hashtbl.iter_keys tree ~f:(fun parent ->
    Hash_set.add parent_set parent;
    let _, children = Hashtbl.find_exn tree parent in
    match children with
    | Some c -> List.iter c ~f:(fun child -> Hash_set.add children_set child)
    | None -> ());
  List.nth_exn (Hash_set.diff parent_set children_set |> Hash_set.to_list) 0
;;

let g tree root =
  let weights = Hashtbl.create (module String) in
  let rec g' node =
    let weight, children = Hashtbl.find_exn tree node in
    match children with
    | Some c ->
      let child_weights = List.sum (module Int) ~f:g' c in
      Hashtbl.set weights ~key:node ~data:(weight + child_weights);
      weight + child_weights
    | None ->
      Hashtbl.set weights ~key:node ~data:weight;
      weight
  in
  let _ = g' root in
  let correct_weight, wrong_child, wrong_weight =
    Hashtbl.keys weights
    |> List.filter_map ~f:(fun node ->
         let _, children = Hashtbl.find_exn tree node in
         match children with
         | Some children ->
           Some
             (List.map children ~f:(fun child -> child, Hashtbl.find_exn weights child))
         | None -> None)
    |> List.filter_map ~f:(fun child_list ->
         match List.all_equal child_list ~equal:(fun (_, w) (_, w') -> w = w') with
         | Some _ -> None
         | None -> Some child_list)
    |> List.map ~f:(fun child_list ->
         let correct_weight =
           List.map child_list ~f:(fun (_, w) -> w)
           |> List.find_a_dup ~compare:(fun w w' -> w - w')
           |> Option.value_exn
         in
         let wrong_child, wrong_weight =
           List.nth_exn (List.filter child_list ~f:(fun (_, w) -> w <> correct_weight)) 0
         in
         correct_weight, wrong_child, wrong_weight)
    |> List.min_elt ~compare:(fun (w, _, _) (w', _, _) -> w - w')
    |> Option.value_exn
  in
  let weight, _ = Hashtbl.find_exn tree wrong_child in
  weight + correct_weight - wrong_weight
;;

let () =
  let tree = parse_input () |> generate_tree in
  let root = f tree in
  printf "%s\n" root;
  printf "%d\n" (g tree root)
;;
