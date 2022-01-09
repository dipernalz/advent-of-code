use regex::Regex;
use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let inpt: Vec<&str> = file.trim().split("\n").collect();

    let re = Regex::new(r".+([A-Z]).+([A-Z])").unwrap();
    let mut graph = HashMap::new();
    let mut prereq_start = HashMap::new();
    let mut available_start: HashSet<char> =
        HashSet::from_iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ".chars());
    for i in inpt.iter() {
        let capture = re.captures(i).unwrap();
        let (a, b) = (
            capture[1].chars().next().unwrap(),
            capture[2].chars().next().unwrap(),
        );
        graph.entry(a).or_insert(HashSet::new()).insert(b);
        prereq_start.entry(b).or_insert(HashSet::new()).insert(a);
        available_start.remove(&b);
    }
    let available_start =
        BinaryHeap::from_iter(available_start.iter().map(Reverse));

    // Part 1
    let mut available = available_start.clone();
    let mut prereq = prereq_start.clone();
    let mut result = String::from("");
    while !available.is_empty() {
        let Reverse(next) = available.pop().unwrap();
        result.push(*next);
        match graph.get(next) {
            Some(s) => {
                for c in s.iter() {
                    let p = prereq.get_mut(c).unwrap();
                    p.remove(next);
                    if p.is_empty() {
                        available.push(Reverse(c));
                    }
                }
            }
            None => {}
        }
    }
    println!("{}", result);

    // Part 2
    let mut workers = [Worker::new(0, '\0'); 5];
    available = available_start.clone();
    prereq = prereq_start.clone();
    let (mut i, mut working) = (0, 0);
    while !available.is_empty() || working > 0 {
        for w in workers.iter_mut() {
            if !w.is_working() {
                continue;
            }
            let next = w.work();
            if next == '\0' {
                continue;
            }
            working -= 1;
            match graph.get(&next) {
                Some(s) => {
                    for c in s.iter() {
                        let p = prereq.get_mut(c).unwrap();
                        p.remove(&next);
                        if p.is_empty() {
                            available.push(Reverse(c));
                        }
                    }
                }
                None => {}
            }
        }
        for w in workers.iter_mut() {
            if w.is_working() {
                continue;
            }
            match available.pop() {
                Some(Reverse(&c)) => {
                    w.give_job(c);
                    working += 1;
                }
                None => {
                    break;
                }
            }
        }
        if working > 0 {
            i += 1;
        }
    }
    println!("{}", i);
}

#[derive(Copy, Clone)]
struct Worker {
    time: u8,
    task: char,
}

impl Worker {
    fn new(time: u8, task: char) -> Worker {
        Worker {
            time: time,
            task: task,
        }
    }

    fn give_job(&mut self, task: char) {
        self.time = task as u8 - 'A' as u8 + 61;
        self.task = task;
    }

    fn is_working(&self) -> bool {
        return self.task != '\0';
    }

    fn work(&mut self) -> char {
        self.time -= 1;
        if self.time == 0 {
            let temp = self.task;
            self.task = '\0';
            return temp;
        }
        return '\0';
    }
}
