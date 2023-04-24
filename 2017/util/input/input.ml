open Core

let read_lines file_name =
  In_channel.read_lines file_name |> List.filter ~f:(fun s -> not (String.is_empty s))
;;
