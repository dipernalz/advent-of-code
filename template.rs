use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::read_to_string;

fn main() {
    use std::time::Instant;
    let now = Instant::now();

    let file = read_to_string("input.txt").unwrap();
    let inpt: Vec<&str> = file.trim().split("\n").collect();

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}
