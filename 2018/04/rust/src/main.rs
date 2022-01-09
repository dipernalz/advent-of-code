use regex::Regex;
use std::collections::HashMap;
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let mut inpt: Vec<&str> = file.trim().split("\n").collect();
    inpt.sort();

    let (mut mins_asleep, mut mins_tracker) = (HashMap::new(), HashMap::new());
    let re = Regex::new(r"(\d\d):(\d\d).+(#\d+|wakes|falls)").unwrap();
    let (mut guard, mut prev_min, mut prev_hr) = (0, 0, 0);
    for s in inpt {
        let capture = re.captures(s).unwrap();
        let hr = capture[1].parse().unwrap();
        let min = capture[2].parse().unwrap();
        let action = &capture[3];
        match action {
            "wakes" => {
                *mins_asleep.entry(guard).or_insert(0) +=
                    (hr - prev_hr) * 60 + min - prev_min;
                for i in prev_min..min {
                    *mins_tracker
                        .entry(guard)
                        .or_insert(HashMap::new())
                        .entry(i)
                        .or_insert(0) += 1;
                }
            }
            "falls" => {}
            _ => {
                guard = action[1..].parse().unwrap();
            }
        }
        prev_min = min;
        prev_hr = hr;
    }

    // Part 1
    let max_guard = mins_asleep
        .iter()
        .max_by(|a, b| a.1.cmp(&b.1))
        .map(|(k, _v)| k)
        .unwrap();
    let max_min = mins_tracker[max_guard]
        .iter()
        .max_by(|a, b| a.1.cmp(&b.1))
        .map(|(k, _v)| k)
        .unwrap();
    println!("{}", max_guard * max_min);

    // Part 2
    let mut most_frequent = HashMap::new();
    for (g, freqs) in mins_tracker.iter() {
        most_frequent
            .insert(g, freqs.iter().max_by(|a, b| a.1.cmp(&b.1)).unwrap());
    }
    println!(
        "{}",
        most_frequent
            .iter()
            .max_by(|a, b| (a.1).1.cmp((&b.1).1))
            .map(|(k, v)| *k * v.0)
            .unwrap()
    );
}
