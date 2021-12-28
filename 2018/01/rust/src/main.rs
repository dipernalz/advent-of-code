use std::collections::HashSet;

fn main() {
    let inpt: Vec<i32> = include_str!("input.txt")
        .trim()
        .split("\n")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    // Part 1
    let freq: i32 = inpt.iter().sum();
    println!("{}", freq);

    // Part 2
    let mut visited = HashSet::new();
    let mut freq = 0;
    let mut found = false;
    while !found {
        for i in inpt.iter() {
            visited.insert(freq);
            freq += i;
            if visited.contains(&freq) {
                println!("{}", freq);
                found = true;
                break;
            }
        }
    }
}
