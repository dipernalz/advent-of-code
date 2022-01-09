use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let inpt: Vec<&str> = file.trim().split("\n").collect();

    let re = Regex::new(r"(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)").unwrap();
    let mut counter = HashMap::new();
    let mut squares: HashMap<u32, HashSet<(u32, u32)>> = HashMap::new();
    for s in inpt {
        let caps = re.captures(s).unwrap();
        let mut array: [u32; 5] = [0; 5];
        for i in 0..5 {
            array[i] = caps[i + 1].parse().unwrap();
        }
        let [id, x, y, w, h] = array;

        for r in y..y + h {
            for c in x..x + w {
                *counter.entry((r, c)).or_insert(0) += 1;
                squares.entry(id).or_insert(HashSet::new()).insert((r, c));
            }
        }
    }

    // Part 1
    println!("{}", counter.values().filter(|x| **x >= 2).count());

    // Part 2
    for (id, squares) in squares.iter() {
        let mut overlap = false;
        for s in squares {
            if counter[s] > 1 {
                overlap = true;
                break;
            }
        }
        if !overlap {
            println!("{}", id);
            break;
        }
    }
}
