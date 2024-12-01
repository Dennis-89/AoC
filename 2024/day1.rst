use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
    iter::zip
};
extern crate itertools;
use itertools::Itertools;

fn read_lines(filepath: impl AsRef<Path>) -> Vec<String> {
    let file_content = File::open(filepath).expect("File not found");
    let buffer = BufReader::new(file_content);
    buffer.lines()
        .map(|l| l.expect("Can't read"))
        .collect()
}

fn format_input(lines: Vec<String>) -> (Vec<i32>, Vec<i32>) {
    let mut destinations: Vec<Vec<String>> = Vec::new();
    for line in lines {
        let line: Vec<String> = line.split_whitespace().map(str::to_string).collect();
        destinations.push(line);
    };

    let mut left_values: Vec<i32> = Vec::new();
    let mut right_values: Vec<i32> = Vec::new();
    for pair in destinations {
        let left:i32 = pair[0].parse::<i32>().unwrap();
        left_values.push(left);
        let right:i32 = pair[1].parse::<i32>().unwrap();
        right_values.push(right);
    };
    left_values.sort();
    right_values.sort();
    (left_values, right_values)
}

fn part_1(left_values: Vec<i32>, right_values: Vec<i32>) -> i32 {
    let mut calculated_values: Vec<i32> = Vec::new();
    for (left, right) in zip(left_values, right_values) {
        let result:i32 = left - right;
        calculated_values.push(result.abs());
    };
    let result: i32 = calculated_values.iter().sum();
    result
}

fn part_2(left_values: Vec<i32>, right_values: Vec<i32>) -> i32 {
    let counts = right_values.into_iter().counts();
    let mut calcualted_values: Vec<i32> = Vec::new();
    for value in left_values {
        if counts.contains_key(&value) {
            let result = value * counts[&value] as i32;
            calcualted_values.push(result);
        }
    };
    let result: i32 = calcualted_values.iter().sum();
    result
}

fn main() {
    let lines = read_lines("/home/dennis/PycharmProjects/AdventofCode/2024/puzzel_input.txt");
    let (left_values, right_values)  = format_input(lines);
    println!("{:?}", part_1(left_values.clone(), right_values.clone()));
    println!("{:?}", part_2(left_values, right_values));
}