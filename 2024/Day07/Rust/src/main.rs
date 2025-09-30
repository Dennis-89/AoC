use itertools::Itertools;
use std::error::Error;
use std::fs::read_to_string;
use std::iter::repeat_n;
use std::time::Instant;

type Operations = [fn(&u64, &u64) -> u64; 2];

fn add(a: &u64, b: &u64) -> u64 {
    a + b
}

fn multiply(a: &u64, b: &u64) -> u64 {
    a * b
}

fn parse_lines<'a>(
    lines: impl Iterator<Item = &'a str>,
) -> Result<Vec<(u64, Vec<u64>)>, Box<dyn Error>> {
    lines
        .map(|line| {
            let (target, operands) = line.split_once(": ").ok_or("No colon in line")?;
            let operands = operands
                .split(' ')
                .map(|operand| operand.parse())
                .collect::<Result<Vec<_>, _>>()?;
            Ok((target.parse()?, operands))
        })
        .collect()
}

fn check_calibration(target: &u64, values: &[u64], operations: &Operations) -> bool {
    for operations in repeat_n(operations, values.len() - 1).multi_cartesian_product() {
        let mut values = values.iter();
        let mut result: u64 = *values.next().unwrap();
        for (operation, value) in operations.iter().zip_eq(values) {
            let result_: u64 = operation(&result, value);
            result = result_;
            if result > *target {
                break;
            }
        }
        if result == *target {
            return true;
        }
    }
    false
}

fn sum_solvable_calibrations(calibrations: &Vec<(u64, Vec<u64>)>, operations: &Operations) -> u64 {
    let mut solvable: Vec<u64> = Vec::new();
    for (target, values) in calibrations {
        if check_calibration(target, values, operations) {
            solvable.push(*target);
        };
    }
    solvable.iter().sum()
}

fn main() {
    let input =
        read_to_string("/home/dennis/PycharmProjects/AdventofCode/2024/Day07/input07.txt").unwrap();
    let calibrations_result = parse_lines(input.lines());
    let calibrations = match calibrations_result {
        Ok(values) => values,
        Err(error) => panic!("Error: {error:?}"),
    };
    let operations: Operations = [add, multiply];
    let start = Instant::now();
    let sum_ = sum_solvable_calibrations(&calibrations, &operations);
    println!("{:?}", sum_);
    println!("{:.5?} runtime", start.elapsed());
}
