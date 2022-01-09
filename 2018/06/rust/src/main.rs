use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let inpt: Vec<&str> = file.trim().split("\n").collect();

    let mut coords = Vec::new();
    for i in inpt.iter() {
        let v: Vec<i16> = i.split(", ").map(|x| x.parse().unwrap()).collect();
        coords.push((v[0], v[1]));
    }

    let (mut min_x, mut max_x, mut min_y, mut max_y) =
        (i16::MAX, 0, i16::MAX, 0);
    for &(x, y) in coords.iter() {
        min_x = std::cmp::min(min_x, x);
        max_x = std::cmp::max(max_x, x);
        min_y = std::cmp::min(min_y, y);
        max_y = std::cmp::max(max_y, y);
    }

    let mut nearest = 0;
    let mut sizes = HashMap::new();
    let mut infinite = HashSet::new();
    for x in min_x - 1..=max_x + 1 {
        for y in min_y - 1..=max_y + 1 {
            let mut min_dist = i16::MAX;
            let mut min_coord = inpt.len();
            let mut duplicate = false;
            let mut total_dist = 0;
            for (i, &c) in coords.iter().enumerate() {
                let dist = manhattan(&(x, y), &c);
                if dist < min_dist {
                    min_dist = dist;
                    min_coord = i;
                    duplicate = false;
                } else if dist == min_dist {
                    duplicate = true;
                }
                total_dist += dist;
            }
            if min_x <= x && x <= max_x && min_y <= y && y <= max_y {
                if !duplicate {
                    *sizes.entry(min_coord).or_insert(0) += 1;
                }
                if total_dist < 10000 {
                    nearest += 1;
                }
            } else {
                infinite.insert(min_coord);
            }
        }
    }

    // Part 1
    println!(
        "{:?}",
        sizes
            .iter()
            .filter(|(i, _)| !infinite.contains(i))
            .max_by(|(_, &a), (_, &b)| a.cmp(&b))
            .map(|(_, v)| v)
            .unwrap()
    );

    // Part 2
    println!("{}", nearest);
}

fn manhattan(a: &(i16, i16), b: &(i16, i16)) -> i16 {
    return (a.0 - b.0).abs() + (a.1 - b.1).abs();
}
