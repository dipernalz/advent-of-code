use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let inpt: Vec<&str> =
        include_str!("input.txt").trim().split("\n").collect();

    // Part 1
    let mut sum_2 = 0;
    let mut sum_3 = 0;
    for s in inpt.iter() {
        let mut count_2 = 0;
        let mut count_3 = 0;
        let mut counter = HashMap::new();
        for c in s.chars() {
            *counter.entry(c).or_insert(0) += 1;
            if counter[&c] == 2 {
                count_2 += 1;
            } else if counter[&c] == 3 {
                count_2 -= 1;
                count_3 += 1;
            } else if counter[&c] == 4 {
                count_3 -= 1;
            }
        }
        if count_2 > 0 {
            sum_2 += 1;
        }
        if count_3 > 0 {
            sum_3 += 1;
        }
    }
    println!("{}", sum_2 * sum_3);

    // Part 2
    let mut visited = HashSet::new();
    let mut found = false;
    for s in inpt.iter() {
        if found {
            break;
        }
        for i in 1..s.len() {
            let mut t = s.to_string();
            t.replace_range(i..i + 1, " ");
            if visited.contains(&t) {
                println!("{}", t.replace(" ", ""));
                found = true;
                break;
            }
            visited.insert(t);
        }
    }
}
