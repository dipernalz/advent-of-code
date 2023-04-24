open Core
open Stdio

let grid_size = 128

let hex_to_bin =
  [ '0', "0000"
  ; '1', "0001"
  ; '2', "0010"
  ; '3', "0011"
  ; '4', "0100"
  ; '5', "0101"
  ; '6', "0110"
  ; '7', "0111"
  ; '8', "1000"
  ; '9', "1001"
  ; 'a', "1010"
  ; 'b', "1011"
  ; 'c', "1100"
  ; 'd', "1101"
  ; 'e', "1110"
  ; 'f', "1111"
  ]
  |> Map.of_alist_exn (module Char)
;;

let get_hex input =
  List.range 0 grid_size
  |> List.map ~f:(fun n -> input ^ "-" ^ Int.to_string n)
  |> List.map ~f:Knot_hash.hash
  |> List.map ~f:String.to_list
  |> List.map ~f:(List.map ~f:(Map.find_exn hex_to_bin))
;;

let f input =
  get_hex input
  |> List.map ~f:(List.map ~f:(String.count ~f:(fun b -> Char.equal b '1')))
  |> List.map ~f:(List.fold ~f:( + ) ~init:0)
  |> List.fold ~f:( + ) ~init:0
;;

let g input =
  let grid = Array.make_matrix ~dimx:grid_size ~dimy:grid_size false in
  get_hex input
  |> List.map ~f:String.concat
  |> List.iteri ~f:(fun r row ->
       String.iteri row ~f:(fun c b -> grid.(r).(c) <- Char.equal b '1'));
  let neighbors r c =
    [ -1, 0; 0, -1; 0, 1; 1, 0 ]
    |> List.filter_map ~f:(fun (dr, dc) ->
         if r + dr >= 0 && r + dr < grid_size && c + dc >= 0 && c + dc < grid_size
         then Some (r + dr, c + dc)
         else None)
  in
  let rec delete_region (r, c) =
    if grid.(r).(c)
    then (
      grid.(r).(c) <- false;
      neighbors r c |> List.iter ~f:delete_region)
  in
  let regions = ref 0 in
  for r = 0 to grid_size - 1 do
    for c = 0 to grid_size - 1 do
      if grid.(r).(c)
      then (
        regions := !regions + 1;
        delete_region (r, c))
    done
  done;
  !regions
;;

let () =
  let input = List.nth_exn (Input.read_lines "input.txt") 0 in
  f input |> printf "%d\n";
  g input |> printf "%d\n"
;;
