use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let inpt: Vec<&str> =
        include_str!("input.txt").trim().split("\n").collect();
    let inpt: Vec<i32> = include_str!("input.txt")
        .trim()
        .split("\n")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();
}
