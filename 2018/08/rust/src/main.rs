use std::fs::read_to_string;

fn main() {
    let file = read_to_string("input.txt").unwrap();
    let inpt: Vec<u32> =
        file.trim().split(" ").map(|s| s.parse().unwrap()).collect();

    // Part 1
    println!("{}", metadata_sum(&inpt));

    // Part 2
    println!("{}", value(&inpt));
}

fn metadata_sum(tree: &Vec<u32>) -> u32 {
    fn metadata_sum_helper(tree: &[u32]) -> (u32, usize) {
        let (n_children, n_entries) = (tree[0], tree[1] as usize);
        let (mut index, mut sum) = (2, 0);
        for _ in 0..n_children {
            let (child_sum, child_index) = metadata_sum_helper(&tree[index..]);
            sum += child_sum;
            index += child_index;
        }
        sum += tree[index..index + n_entries].iter().sum::<u32>();
        return (sum, index + n_entries);
    }

    return metadata_sum_helper(tree).0;
}

fn value(tree: &Vec<u32>) -> u32 {
    fn value_helper(tree: &[u32]) -> (u32, usize) {
        let (n_children, n_entries) = (tree[0], tree[1] as usize);
        let mut index = 2;
        let mut child_sums = Vec::new();
        for _ in 0..n_children {
            let (child_sum, child_index) = value_helper(&tree[index..]);
            child_sums.push(child_sum);
            index += child_index;
        }
        let sum = match n_children {
            0 => tree[index..index + n_entries].iter().sum(),
            _ => tree[index..index + n_entries]
                .iter()
                .filter(|&&i| i < n_children + 1)
                .map(|&i| child_sums[i as usize - 1])
                .sum(),
        };
        return (sum, index + n_entries);
    }

    return value_helper(tree).0;
}
