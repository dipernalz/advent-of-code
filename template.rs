use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    use std::time::Instant;
    let now = Instant::now();

    let inpt: Vec<&str> =
        include_str!("input.txt").trim().split("\n").collect();
    let inpt: Vec<i32> = include_str!("input.txt")
        .trim()
        .split("\n")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}
