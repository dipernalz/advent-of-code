open Core
open Stdio

let build_graph lines =
  let process_line map line =
    let parsed_line = Str.split (Str.regexp " <-> ") line |> List.to_array in
    let node = parsed_line.(0) |> Int.of_string in
    let neighbors =
      parsed_line.(1)
      |> Str.split (Str.regexp ", ")
      |> List.map ~f:Int.of_string
      |> Set.of_list (module Int)
    in
    Map.set map ~key:node ~data:neighbors
  in
  List.fold lines ~init:(Map.empty (module Int)) ~f:process_line
;;

let find_group graph n =
  let rec bfs v =
    let add_unvisited_neighbors v' n' =
      match Map.find graph n' with
      | Some neighbors -> Set.union v' (Set.diff neighbors v)
      | None -> v'
    in
    let v' = Set.fold v ~init:(Set.empty (module Int)) ~f:add_unvisited_neighbors in
    if Set.is_empty v' then v else bfs (Set.union v v')
  in
  bfs (Set.singleton (module Int) n)
;;

let f graph = find_group graph 0 |> Set.length

let g graph =
  let rec g' v c =
    if Set.is_empty v
    then c
    else (
      let group = Set.min_elt_exn v |> find_group graph in
      g' (Set.diff v group) (c + 1))
  in
  g' (Set.of_map_keys graph) 0
;;

let () =
  let graph = Input.read_lines "input.txt" |> build_graph in
  f graph |> printf "%d\n";
  g graph |> printf "%d\n"
;;
