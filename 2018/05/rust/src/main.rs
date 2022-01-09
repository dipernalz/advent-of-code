use std::cmp::min;
use std::collections::HashMap;
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let inpt = file.trim();

    let mut polymer = Vec::new();
    for c in inpt.chars() {
        polymer.push(c);
    }

    let mut adjacent = HashMap::new();
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    for c in alphabet.chars() {
        adjacent.insert(c, c.to_ascii_uppercase());
        adjacent.insert(c.to_ascii_uppercase(), c);
    }

    // Part 1
    let mut temp = polymer.clone();
    println!("{}", react(&mut temp, &adjacent));

    // Part 2
    let mut min_length = inpt.len() as u32;
    for c in alphabet.chars() {
        let mut temp = polymer.clone();
        temp.retain(|&a| a != c && a != c.to_ascii_uppercase());
        min_length = min(min_length, react(&mut temp, &adjacent));
    }
    println!("{}", min_length);
}

fn react(polymer: &mut Vec<char>, adjacent: &HashMap<char, char>) -> u32 {
    let (mut i, mut j, mut length) = (0, 1, polymer.len() as u32);
    let mut stack = Vec::new();
    while j < polymer.len() {
        if polymer[j] == adjacent[&polymer[i]] {
            length -= 2;
            match stack.pop() {
                Some(k) => {
                    i = k;
                }
                None => {
                    i = j + 1;
                    j += 1;
                }
            }
        } else {
            stack.push(i);
            i = j;
        }
        j += 1;
    }
    return length;
}
